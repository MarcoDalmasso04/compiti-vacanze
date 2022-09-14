def equilateral(sides: list) -> bool:
    
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b >= c and b + c >= a and a + c >= b:
        if a == b == c and a * b * c != 0:
            return True
        else:
            return False
    else:
        return False
def isosceles(sides: list) -> bool:
    
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b >= c and b + c >= a and a + c >= b:
        if a == b or a == c or b == c and a * b * c != 0:
            return True
        else:
            return False
    else:
        return False
def scalene(sides: list) -> bool:
    
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b >= c and b + c >= a and a + c >= b:
        if a != b and a != c and b != c and a * b * c != 0:
            return True
        else:
            return False
    else:
        return False
