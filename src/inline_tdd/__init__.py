from .inline import itestdd, Group

import sys as _sys

_REWRITE_ACTIVE = False


def _rewrite_and_exec():
    """When running under plain `python` (not pytest), re-execute the
    caller's __main__ module with all itestdd() expression-statements
    removed so that TDD-mode references to not-yet-assigned variables
    do not cause UnboundLocalError."""
    global _REWRITE_ACTIVE
    if _REWRITE_ACTIVE:
        return
    if "pytest" in _sys.modules or "_pytest" in _sys.modules:
        return

    import ast as _ast

    # Walk up the frame chain to find the __main__ module
    frame = _sys._getframe(1)
    while frame is not None:
        if frame.f_globals.get("__name__") == "__main__":
            break
        frame = frame.f_back
    if frame is None:
        return
    caller_file = frame.f_globals.get("__file__")
    if not caller_file:
        return

    class _ItestddRemover(_ast.NodeTransformer):
        """Remove bare itestdd() expression-statements."""
        def _is_itestdd_chain(self, node):
            if isinstance(node, _ast.Call):
                if isinstance(node.func, _ast.Name) and node.func.id == "itestdd":
                    return True
                if isinstance(node.func, _ast.Attribute) and isinstance(node.func.value, _ast.Call):
                    return self._is_itestdd_chain(node.func.value)
            return False

        def visit_Expr(self, node):
            if isinstance(node.value, _ast.Call) and self._is_itestdd_chain(node.value):
                return None
            return self.generic_visit(node)

    try:
        source = open(caller_file, "r").read()
        tree = _ast.parse(source, filename=caller_file)
        tree = _ItestddRemover().visit(tree)
        _ast.fix_missing_locations(tree)
        code = compile(tree, caller_file, "exec")

        _REWRITE_ACTIVE = True
        globs = {"__name__": "__main__", "__file__": caller_file,
                 "__builtins__": __builtins__}
        exec(code, globs)
        _sys.exit(0)
    except SystemExit:
        raise
    except Exception:
        pass


_rewrite_and_exec()
