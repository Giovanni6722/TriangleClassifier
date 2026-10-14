import math

def is_valid_triangle(a,b,c) -> bool:

    if(a <= 0 or b <= 0 or c <= 0): return False
    
    base, leg, hypotenuse = sorted(a,b,c)

    if(hypotenuse > base + leg or math.isclose(base + leg, hypotenuse)): return False
    
    return True

def classify_triangle(a,b,c) -> str:

    if not is_valid_triangle(a,b,c): return "Invalid"
    
    base, leg, hypotenuse = sorted(a,b,c)

    type_of_triangle = "Scaline"

    if(x == y == z): type_of_triangle = "Equalateral"
    elif(x == y or y == z): type_of_triangle = "Isocelese"

    #pythag check
    if math.isclose(base * base + leg * leg, hypotenuse * hypotenuse):
        return "Right" + type_of_triangle
    
    return type_of_triangle

    