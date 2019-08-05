import math

# решение линейного уравнения
def linear_equation(a,b):
    if a == 0 and b == 0:
        return 'Решений бесконечно много'
    elif a == 0 and b != 0:
        return 'Нет решений'
    else:
        return round(b/a, 2)

# решение квадратного уравнения
def quadratic_equation(a,b,c):
    D=b**2-4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        return round(x1, 2), round(x2, 2)
    elif D == 0:
        x = -b/(2*a)
        return round(x, 2)
    else:
        x1 = complex(-b/2*a, math.sqrt(abs(D))/(2*a) )
        x2 = complex(-b/2*a, -math.sqrt(abs(D))/(2*a) )
        return x1 , x2

# решение кубического уравнения
def cubic_equation(a,b,c,d):
    p = ((b/a)**2-3*c/a)/9
    q = (2*(b/a)**3-9*b*c/a**2+27*d/a)/54
    if p**3 - q**2 > 0:
        t = math.acos(q/math.sqrt(p**3))/3
        x1 = -2*math.sqrt(p)*math.cos(t) - b/3
        x2 = -2*math.sqrt(p)*math.cos(t + (2*math.pi/3)) - b/3
        x3 = -2*math.sqrt(p)*math.cos(t - (2*math.pi/3)) - b/3
        return x1, x2, x3
    else:
        f = - math.pow(q + math.sqrt(q**2 - p**3),1/3)
        if f == 0:
            x1 = -b/(3*a)
            return x1
        else:
            g = p/f
            if g == f:
                x1 = (f+g)-b/(3*a)
                x2 = -(f+g)/2 - b/(3*a)
                return x1, x2
            else:
                x1 = (f+g)-b/(3*a)
                x2 = complex(-(f+g)/2 - b/(3*a), math.sqrt(3)*(f-g)/2)
                x3 = complex(-(f+g)/2 - b/(3*a), -math.sqrt(3)*(f-g)/2)
                return x1, x2, x3

# решение уравнения 4-ой степени

