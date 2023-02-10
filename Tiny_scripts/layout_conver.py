from sys import argv

argv.pop(0)
rus = ".юбьтимсчяэждлорпавыфъхзщшгнекуцйё,"
eng = "/.,mnbvcxz\';lkjhgfdsa][poiuytrewq`?"
for i in argv:
    tmp = ""
    for j in i:
        if j.lower() in eng:
            if j.isupper():
                tmp += rus[eng.index(j.lower())].upper()
            else:
                tmp += rus[eng.index(j.lower())]
        else:
            tmp += j
    print(tmp, end="", sep=" ")
