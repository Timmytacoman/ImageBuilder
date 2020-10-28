def solve(a, b, c, d, e, f):
    x = (b * f) - (e * c)
    y = -(a * f) + (d * c)
    z = (a * e) - (d * b)
    return x, y, z


def main():
    first_vector = input("Enter first vector in the form a,b,c: ").split(',')
    a, b, c = first_vector
    a = int(a)
    b = int(b)
    c = int(c)
    second_vector = input("Enter second vector in the form d,e,f: ").split(',')
    d, e, f = second_vector
    d = int(d)
    e = int(e)
    f = int(f)
    x, y, z = solve(a, b, c, d, e, f)
    print(f"<{a},{b},{c}> x <{d},{e},{f}> = <{x},{y},{z}>")


main()
