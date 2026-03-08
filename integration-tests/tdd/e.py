from inline_tdd import itestdd
class Calculator:
    def add(self, a, b):
        itestdd().given(a, 2).given(b, 3).check_eq(result, 5)
        result = a + b
        return result