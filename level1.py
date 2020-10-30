def readFile(file):
    file1 = open(file + ".in", 'r')
    lines = file1.readlines()
    file1.close()
    return [line.replace("\n", "").replace("\t", "") for line in lines]


def getMinutes(minutes):
    return [(key, value,) for key, value in enumerate(readFile(f"inputs/{file}")[1:], 0)]


def writeOutput(lines, file):
    with open(f"outputs/{file}.out", 'w') as out_file:
        for line in lines:
            out_file.write(f"{line}\n")


def getSortedMinutes(file):
    return sorted(getMinutes(file), key=lambda tup: tup[1])


def level1(file):
    minutes = getSortedMinutes(file)
    first = [minutes[0][0]]
    writeOutput(first, file)


if __name__ == '__main__':
    level1("level1_example")
    level1("level1_1")
    level1("level1_2")
    level1("level1_3")
    level1("level1_4")
    level1("level1_5")
