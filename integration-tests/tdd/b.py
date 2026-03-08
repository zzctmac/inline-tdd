from inline_tdd import itestdd

def calculate_discount(price, rate):
    itestdd().given(price, 100).given(rate, 0.2).check_eq(discount, 20.0)
    discount = price * rate
    
    itestdd().given(price, 100).given(discount, 20.0).check_eq(final, 80.0)
    final = price - discount
    
    return final