def my_func(x1, x2, x3):
    if not isinstance(x1, float) or not isinstance(x2, float) or not isinstance(x3, float):
        print("Error: parameters should be float")
        return None
    if x1+x2+x3 == 0:
        print("Not a number - denominator equals zero")
        return None
    t = ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
    return t


def convert(hours, minutes):
    if hours < 0 or minutes < 0:
        print("Input error!")
        return None
    return (hours*60 + minutes)*60
