
from inline_tdd import itestdd

def _inline_tdd__schema_tests():
    class _ITestSchema():
        def v(self, value):
            pass
    itestdd().given(schema, _ITestSchema()).check_true(True)
    schema = _ITestSchema()
    schema.v("test")
    