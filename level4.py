def readFile(file):
    file1 = open("inputs/" + file + ".in", 'r')
    lines = file1.readlines()
    file1.close()
    return [line.replace("\n", "").replace("\t", "") for line in lines]


def getMinutes(minutes):
    return [(key, int(value),) for key, value in enumerate(minutes, 0)]


def getTasks(tasks):
    return [[int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]), int(line.split(" ")[3]), []]
            for
            line in tasks]


def writeOutput(lines, file):
    with open(f"outputs/{file}.out", 'w') as out_file:
        for line in lines:
            out_file.write(f"{line}\n")


def getSortedMinutes(minutes):
    return sorted(getMinutes(minutes), key=lambda tup: tup[1])


def getCheapest(minutes, task, timeline):
    interval = minutes[task[2]: task[3] + 1]
    sorted_interval = sorted(interval, key=lambda tup: tup[1])
    power_needed = task[1]
    index = 0
    while power_needed > 0 and index < len(sorted_interval):
        minute = sorted_interval[index]
        remained_on_time = timeline[minute[0]]
        if remained_on_time > 0:
            if remained_on_time > power_needed:
                timeline[minute[0]] = remained_on_time - power_needed
                task[1] = 0
                task[4].append(f"{minute[0]} {power_needed}")
            else:
                task[1] = power_needed - remained_on_time
                timeline[minute[0]] = 0
                task[4].append(f"{minute[0]} {remained_on_time}")
        index += 1
        power_needed = task[1]
    if power_needed > 0:
        raise Exception(f"Error mate at task {task[0]}")
    return f"{task[0]} " + " ".join(task[4])


def level4(file):
    content = readFile(file)
    max_power = int(content[0])
    max_bill = int(content[1])
    minutes_count = int(content[2])
    timeline = [max_power] * minutes_count
    minutes = content[3:minutes_count + 1]
    minutes = getMinutes(minutes)
    tasks_count = content[minutes_count + 1]
    tasks = content[minutes_count + 4:]
    tasks = getTasks(tasks)
    sorted_tasks = sorted(tasks, key=lambda task: task[3]-task[2])
    lines = [len(tasks)]
    for task in sorted_tasks:
        line = getCheapest(minutes, task, timeline)
        lines.append(line)

    writeOutput(lines, file)


if __name__ == '__main__':
    level4("level4_example")
    level4("level4_1")
    level4("level4_2")
    level4("level4_3")
    level4("level4_4")
    level4("level4_5")
