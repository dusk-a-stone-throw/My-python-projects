import math

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


def toSuper(num):
    num = str(num)
    result = num.translate(superscript_map)
    return result


def newtonBinomial(n):
    polynomial = ""
    polynomial += "a{}+".format(toSuper(n))
    for k in range(1, n):
        polynomial += (str(math.comb(n, k)) +
                       "a{}b{}+".format("" if n - k == 1 else toSuper(n - k),
                                        "" if k == 1 else toSuper(k)))
    polynomial += "b{}".format(toSuper(n))
    return polynomial


n = int(input("Please enter n for (a+b)ⁿ: "))
print("(a+b)" + toSuper(n)+"="+ newtonBinomial(n))
