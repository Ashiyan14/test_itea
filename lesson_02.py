import re


def readMass(fileName):
    with open(fileName) as file:
        mass = []
        N = 0

        for row in file:
            z = []

            rowStr = row.strip('\n')
            rowStr = re.split(' +', rowStr)

            for i in rowStr:
                z.append(int(i))

            mass.append(z)
            N += 1

    return mass, N


# Function print 2d array to screen
def printMass(mass, N):
    for i in range(N):
        for j in range(N):
            print("%-4d" % mass[i][j], end='')

        print()


# Function write 2d array to file
def writeMass(mass, N, fileName):
    with open(fileName, 'w') as file:
        for i in range(N):
            for j in range(N):
                file.write("%-4d" % mass[i][j])
            file.write('\n')


# i + j = n - 1
# j = n - 1 - i
def exchange(mass, N):
    for i in range(N):
        for j in range(N):
            if i == j:
                mass[i][j], mass[i][N - 1 - i] = mass[i][N - 1 - i], mass[i][j]


if __name__ == '__main__':
    arr, count = readMass(r'doc1\test_1\input.txt')

    printMass(arr, count)

    print()

    exchange(arr, count)

    printMass(arr, count)
    writeMass(arr, count, r'doc1\test_1\output.txt')
