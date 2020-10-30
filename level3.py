def readFile(file):
    file1 = open("inputs/" + file + ".in", 'r')
    lines = file1.readlines()
    file1.close()
    return [line.replace("\n", "").replace("\t", "") for line in lines]


def getMinutes(minutes):
    return [(key, int(value),) for key, value in enumerate(minutes, 0)]


def getTasks(tasks):
    return [(int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]), int(line.split(" ")[3]),) for line in tasks]


def writeOutput(lines, file):
    with open(f"outputs/{file}.out", 'w') as out_file:
        for line in lines:
            out_file.write(f"{line}\n")


def getSortedMinutes(minutes):
    return sorted(getMinutes(minutes), key=lambda tup: tup[1])


def getCheapest(minutes, task):
    interval = minutes[task[2]: task[3]+1]
    minimum = min(interval, key=lambda tup: tup[1])
    return f"{task[0]} {minimum[0]} {task[1]}"


def level3(file):
    content = readFile(file)
    minutes_count = int(content[0])
    minutes = content[1:minutes_count + 1]
    minutes = getMinutes(minutes)
    tasks_count = content[minutes_count + 1]
    tasks = content[minutes_count + 2:]
    tasks = getTasks(tasks)

    lines = [len(tasks)]
    for task in tasks:
        line = getCheapest(minutes, task)
        lines.append(line)

    writeOutput(lines, file)


if __name__ == '__main__':
    level3("level3_example")
    level3("level3_1")
    level3("level3_2")
    level3("level3_3")
    level3("level3_4")
    level3("level3_5")
