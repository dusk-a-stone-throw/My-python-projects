divs = 0
maxDivs = 0
numWithMaxDivs = 0
for i in range(568023, 569231):
    for j in range(1, i // 2):
        if (i % j == 0):
            divs += 1
    if (divs > maxDivs):
        maxDivs = divs
        numWithMaxDivs = i
        divs = 0
    else:
        pass
print(maxDivs, numWithMaxDivs)
