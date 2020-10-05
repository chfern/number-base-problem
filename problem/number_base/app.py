def mod(num, denominator):
    return num - (denominator * int(num/denominator))


# Reference: https://mathbits.com/MathBits/CompSci/Introduction/tobase10.htm
def to_base10(num, base):
    result = 0
    power = 0

    while num != 0:
        result += (mod(num, 10)) * pow(base, power)
        num -= (mod(num, 10))
        num = int(num / 10)
        power += 1

    return result


# Reference: https://mathbits.com/MathBits/CompSci/Introduction/frombase10.htm
def to_base(num, from_base, to_base):
    num_to_divide = to_base10(num, from_base)

    power = 0
    result = 0
    while num_to_divide != 0:
        remainder = mod(num_to_divide, to_base)
        result += remainder * pow(10, power)
        power += 1
        num_to_divide = int(num_to_divide / to_base)

    return result


