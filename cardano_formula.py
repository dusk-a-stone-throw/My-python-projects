from fractions import Fraction
# WARNING: roots found with this program are approximate (but close to the truth).

# Let ax³ + bx ² + cx+ d = 0, where a != 0
# Divide all sides by a
# Let y = x + b/3a
# You get: y³ + px + q, where p = (3ac - b²) / 3a², q = (27a²d + 2b³ - 9abc) / 27a³
# Let y = r + g
# You get: r³ + g³+ (r + g)(3rg + p) + q = 0
# so r³ + g³ = -q and
# (r + g)(3rg + p) = 0 (In general r + g != 0 so you need 3rg + p = 0)
# 3rg + p = 0 => r³g³ = -p3 / 27
# Finally, you get the system:
# { r³g³= -p³ / 27
# { r³ + g³=-q
# As you can see, it's just vieta formulas for quadratic equation =>
# r³ = (-q + sqrt(q² + (4p³) / 27)) / 2
# g³ = (-q - sqrt(q² + (4p³) / 27)) / 2
# remember that y = r + g, you get:
# y = cbrt(r) + cbrt(g)
# And x = y - b/3a
# You should pick other complex values for cube roots according that statement: r³+g³=-p³ / 27
# Other roots: y₂ = -(r + g) / 2 + cbrt(3) * i(r - g) / 2
# Other roots: y₃ = -(r + g) / 2 - cbrt(3) * i(r - g) / 2
def cube_root(x):
    if not (type(x) is complex):
        if (x == 0):
            return 0
        if (x > 0):
            return x**(1 / 3)
        else:
            return -abs(x**(1 / 3))
    return x**(1 / 3)


a = int(input("Enter the coefficient before x³: "))
b = int(input("Enter the coefficient before x²: "))
c = int(input("Enter the coefficient before x: "))
d = int(input("Enter the free term: "))
p = Fraction((3 * a * c - b**2) / (3 * a**2))
q = Fraction((2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3))
Q = (q**2 + ((4 * p**3) / 27))
alpha = cube_root((-q + Q**0.5) / 2)
beta = cube_root((-q - Q**0.5) / 2)
y1 = alpha + beta
y2 = -(alpha + beta) / 2 + 1j * 3**0.5 * (alpha - beta) / 2
y3 = -(alpha + beta) / 2 - 1j * 3**0.5 * (alpha - beta) / 2
x1 = y1 - (b / (3 * a))
x2 = y2 - (b / (3 * a))
x3 = y3 - (b / (3 * a))
print("Roots found:")
print("x₁ =", x1.real if x1.imag == 0j else x1)
print("x₂ =", x2.real if x2.imag == 0j else x2)
print("x₃ =", x3.real if x3.imag == 0j else x3)
