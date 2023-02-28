# That theorem used:
# https://en.wikipedia.org/wiki/Rational_root_theorem
# See also:
# https://en.wikipedia.org/wiki/Ruffini%27s_rule

import math
from fractions import Fraction

superscript_map = str.maketrans({
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹"
})
subscript_map = str.maketrans({
    "0": "₀",
    "1": "₁",
    "2": "₂",
    "3": "₃",
    "4": "₄",
    "5": "₅",
    "6": "₆",
    "7": "₇",
    "8": "₈",
    "9": "₉"
})


def toSuper(num):
    num = str(num)
    result = num.translate(superscript_map)
    return result


def toSub(num):
    num = str(num)
    result = num.translate(subscript_map)
    return result


# A fast and easy method to divide a polynomial P(x) by (x-a)
def ruffiniRule(a, polynomial):
    # WARNING: this function does not return a remainder because I imply that 'a' is a root of the polynomial
    result = []
    result.append(polynomial[0])
    # if you devide (x-b) by (x-a), you will get only a constant (and maybe a remainder)
    for i in range(1, len(polynomial) - 1):
        result.append(result[i - 1] * a + polynomial[i])
    return result


def getSupposedRoots(hightestDegreeCoefficient, freeTerm):
    freeTermFactors = []
    # an array of factors of the coefficient before the highest degree of x
    degreeFactors = []
    for i in range(1, math.ceil(abs(freeTerm) / 2) + 1):
        if (freeTerm % i == 0):
            freeTermFactors.append(i)
            freeTermFactors.append(-i)
    for i in range(1, math.ceil(abs(hightestDegreeCoefficient) / 2) + 1):
        if (hightestDegreeCoefficient % i == 0):
            degreeFactors.append(i)
    freeTermFactors.append(freeTerm)
    freeTermFactors.append(-freeTerm)  # remember about negative roots also
    degreeFactors.append(hightestDegreeCoefficient)
    supposedRoots = set()
    for i in range(len(freeTermFactors)):
        for j in range(len(degreeFactors)):
            supposedRoots.add(Fraction(freeTermFactors[i], degreeFactors[j]))
    supposedRoots = list(supposedRoots)
    return supposedRoots


def checkRoots(supposedRoots, coefficients):
    roots = []
    while (True):
        rootFound = False
        for i in range(len(supposedRoots)):
            sum = Fraction(0)
            for j in range(len(coefficients) - 1, -1, -1):
                sum += Fraction(coefficients[j]) * supposedRoots[i]**(
                    len(coefficients) - 1 - j)
            if (sum == 0):
                # this algorithm divides polynomial until it becomes a constant
                # (when a polynomial becomes a non-zero constant, it has no roots so loop stops)
                rootFound = True
                coefficients = ruffiniRule(supposedRoots[i], coefficients)
                roots.append(supposedRoots[i])
                break
        if not (rootFound):
            break
    # if only  a constant remains, return empty polynomial (all foots found)
    return roots, (getPolynomial(list(map(int, coefficients)))
                   if len(coefficients) >= 2 else "")


def getPolynomial(coefficients):  # convert array of coeffs to a cute string
    polynomial = ""
    # the last coeffecient can't be 0 probably
    for i in range(0, len(coefficients) - 1):
        deg = len(coefficients) - 1 - i
        if (coefficients[i] == 0):
            continue
        else:
            polynomial += (("" if len(polynomial) == 0 else
                            ("+" if coefficients[i] == 1 else
                             ("-" if coefficients[i] == -1 else "{0:+}".format(
                                 coefficients[i])))) +
                           "x{}".format("" if deg == 1 else toSuper(deg)))
    # add the free term
    polynomial += "" if coefficients[len(coefficients) -
                                     1] == 0 else ("{0:+}".format(
                                         coefficients[len(coefficients) - 1]))
    return polynomial


coefficients = []

degree = int(input("Enter the highest degree of a polynomial: "))
for i in range(degree, 0, -1):
    a = int(input("Enter a coefficient before x{}: ".format(toSuper(i) if i!=1 else "")))
    coefficients.append(a)
coefficients.append(int(input("Enter the free term (Non-zero): ")))
supposedRoots = getSupposedRoots(coefficients[0],
                                 coefficients[len(coefficients) - 1])
# "polynomial" is an indecomposable polynomial (over rational numbers)
roots, polynomial = checkRoots(supposedRoots, coefficients)
if(len(roots)!=0):
    print("Founded rational roots (with multiplicities):")
    for i in range(len(roots)):
        print("x" + toSub(i + 1), "=", roots[i])
    print("======================")
    print("Factorized polynomial:")
    for i in range(len(roots)):
        if (roots[i] > 0):
            print("(x-" + str(roots[i]) + ")", end="")
        else:
            print("(x+" + str(abs(roots[i])) + ")", end="")
    if (len(polynomial) != 0):
        print("({})".format(polynomial))
else:
    print("No rational roots found.")
