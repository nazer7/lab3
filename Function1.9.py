import math
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3  
r = float(input("r of sphere: "))
print("sphere volume:", sphere_volume(r))