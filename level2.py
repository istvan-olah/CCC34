def readFile(file):
    file1 = open("inputs/" + file + ".in", 'r')
    lines = file1.readlines()
    file1.close()
    return [line.replace("\n", "").replace("\t", "") for line in lines]


def getMinutes(minutes):
    return [(key, int(value),) for key, value in enumerate(minutes, 0)]


def getTasks(tasks):
    return [(int(line.split(" ")[0]), int(line.split(" ")[1]),) for line in tasks]


def writeOutput(lines, file):
    with open(f"outputs/{file}.out", 'w') as out_file:
        for line in lines:
            out_file.write(f"{line}\n")


def getSortedMinutes(minutes):
    return sorted(getMinutes(minutes), key=lambda tup: tup[1])


def getCheapest(minutes, length):
    minimum_pos = 0
    minimum_sum = 746128794612897461829642186417829647891624871412987461827946421407120471204721094091274091278409217
    for i in range(len(minutes) - length + 1):
        s = 0
        for j in range(i, i + length):
            s += minutes[j][1]
        if s < minimum_sum:
            minimum_sum = s
            minimum_pos = i
    return minimum_pos


def level2(file):
    content = readFile(file)
    minutes_count = int(content[0])
    minutes = content[1:minutes_count + 1]
    minutes = getMinutes(minutes)
    tasks_count = content[minutes_count + 1]
    tasks = content[minutes_count + 2:]
    tasks = getTasks(tasks)

    lines = [len(tasks)]
    for task in tasks:
        print(task)
        position = getCheapest(minutes, task[1])
        lines.append(f"{task[0]} {position}")

    writeOutput(lines, file)


if __name__ == '__main__':
    level2("level2_example")
    level2("level2_1")
    level2("level2_2")
    level2("level2_3")
    level2("level2_4")
    level2("level2_5")
