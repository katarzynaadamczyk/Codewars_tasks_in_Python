''' exercise all your base '''
        
def check_base(base, text):
    if base < 2:
        raise ValueError(text + " base must be >= 2")
    return True

def rebase(input_base, digits, output_base):
    check_base(input_base, "input")
    check_base(output_base, "output")
    decimal_value, ret_val = 0, []
    for index, value in enumerate(digits[::-1]):
        if not (0 <= value < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal_value += value * input_base ** index            
    if decimal_value == 0:
        return [0]
    while decimal_value > 0:
        ret_val.insert(0, decimal_value % output_base)
        decimal_value //= output_base 
    return ret_val
