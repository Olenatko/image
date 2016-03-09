import matplotlib.pyplot as plt
import math
from  collections import Counter


def obraz():
    data_1 = ([10.28,  6.27,  10.47,  3.71,  9.09,  5.96,  9.58,  4.97,  10.78,  6.10,  9.84,  6.74,  10.09,  3.48,  10.22,  5.31,  9.08,  3.36,  10.70,
        6.39,  10.70,  5.76,  9.14,  4.37,  9.58, 5.59, 10.00, 5.18, 9.96, 4.78, 10.12, 5.64, 9.75, 4.16, 9.64, 6.52, 10.46, 5.61,
        9.21,  3.53])
    data_2 = [5.28, 10.42, 5.47, 9.57, 4.09, 10.32, 4.58, 9.99, 5.78, 10.37, 4.84, 10.58, 5.09, 9.49, 5.22, 10.10,4.08, 9.45, 5.70,
        10.46, 5.70, 10.25, 4.14, 9.79, 4.58, 10.20, 5.00, 10.06, 4.96, 9.93, 5.12, 10.21, 4.75, 9.72, 4.64, 10.51, 5.46, 10.20,
        4.21,  9.51]
    kvadrat1 = 0
    kvadrat2 = 0
    seredneA = 0
    seredneB = 0
    for i in range(0, len(data_1)):
        kvadrat1 += math.pow(data_1[i], 2)
        kvadrat2 += math.pow(data_2[i], 2)
        seredneA += data_1[i]
        seredneB += data_2[i]
    dyspA = kvadrat1/len(data_1) - (seredneA/len(data_1)) ** 2
    dyspB = kvadrat2/len(data_2) - (seredneB/len(data_2)) ** 2
    medA = len(data_1)/2
    medB = len(data_2)/2
    if len(data_1) % 2 == 0:
        medA = (data_1[int(len(data_1)/2)] + data_1[int(len(data_1)/2-1)])/2
    if len(data_2) % 2 == 0:
        medB = (data_2[int(len(data_2)/2)] + data_2[int(len(data_2)/2-1)])/2

    print('Дисперсія А: ', dyspA)
    print('Дисперсія B: ', dyspB)
    print('Ознаки центру: ')
    print('Мода A: ', Counter(data_1).most_common(1))
    print('Мода B: ', Counter(data_2).most_common(1))
    print('Медіана A: ', medA)
    print('Медіана B: ', medB)
    plt.plot(data_1, data_2, 'go')
    plt.show()


obraz()

def solver():
        obr_1 = ([10.28,  6.27,  10.47,  3.71,  9.09,  5.96,  9.58,  4.97,  10.78,  6.10,  9.84,  6.74,  10.09,  3.48,  10.22,  5.31,  9.08,  3.36,  10.70,
        6.39,  10.70,  5.76,  9.14,  4.37,  9.58, 5.59, 10.00, 5.18, 9.96, 4.78, 10.12, 5.64, 9.75, 4.16, 9.64, 6.52, 10.46, 5.61,
        9.21,  3.53])
        obr_2 = [5.28, 10.42, 5.47, 9.57, 4.09, 10.32, 4.58, 9.99, 5.78, 10.37, 4.84, 10.58, 5.09, 9.49, 5.22, 10.10,4.08, 9.45, 5.70,
        10.46, 5.70, 10.25, 4.14, 9.79, 4.58, 10.20, 5.00, 10.06, 4.96, 9.93, 5.12, 10.21, 4.75, 9.72, 4.64, 10.51, 5.46, 10.20,
        4.21,  9.51]

        classA = []
        classB = []
        for i in range(0, len(obr_1)):
            for j in range(0, len(obr_2)):
                d1 = -5 * obr_1[i] + 4 * obr_2[j] + 1
                d2 = -obr_1[i] - 3 * obr_2[j]
                if d1 > 0:
                    classA.append(d1)

                    #print('lol', d1)
                elif d2 < 0:
                    classB.append(d2)
        plt.plot(classA[:len(classB)], classB[:len(classA)], 'go')
        plt.xlabel('1')
        plt.ylabel('2')
        plt.show()
print(solver())

