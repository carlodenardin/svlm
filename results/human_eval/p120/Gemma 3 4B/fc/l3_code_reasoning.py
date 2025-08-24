import math

def calculate_transformation(Kc):
    sqrt_Kc = math.sqrt(Kc)
    squared_sqrt_Kc = sqrt_Kc * sqrt_Kc
    abs_squared_sqrt_Kc = abs(squared_sqrt_Kc)
    return abs_squared_sqrt_Kc