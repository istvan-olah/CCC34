import math

totalBill = 0


def readFile(file):
    file1 = open("inputs/" + file + ".in", 'r')
    lines = file1.readlines()
    file1.close()
    return [line.replace("\n", "").replace("\t", "") for line in lines]


def getMinutes(minutes):
    return [[key, int(value), int(value), 0] for key, value in enumerate(minutes, 0)]


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


def getNewPrice(basePrice, powerConsumed, maxPower):
    return math.ceil(basePrice * (1 + (powerConsumed / maxPower)))


def getCheapest(minutes, task, timeline, max_power):
    global totalBill
    interval = minutes[task[2]: task[3] + 1]
    sorted_interval = sorted(interval, key=lambda tup: tup[1])
    power_needed = task[1]
    index = 0
    while power_needed > 0 and index < len(sorted_interval):
        minute = sorted_interval[index]
        remained_on_time = timeline[minute[0]][0]
        remained_nr = timeline[minute[0]][1]
        power_consumed = 0
        if remained_on_time > 0 and remained_nr > 0:
            if remained_on_time > power_needed:
                timeline[minute[0]][0] = remained_on_time - power_needed
                task[1] = 0
                power_consumed = power_needed
                task[4].append(f"{minute[0]} {power_needed}")
            else:
                if index + 1 < len(sorted_interval) and remained_on_time > 1:
                    taken = math.floor(remained_on_time / 2)
                    task[1] = power_needed - taken
                    timeline[minute[0]][0] = remained_on_time - taken
                    power_consumed += taken
                    task[4].append(f"{minute[0]} {taken}")
                else:
                    task[1] = power_needed - remained_on_time
                    timeline[minute[0]][0] = 0
                    power_consumed = remained_on_time
                    task[4].append(f"{minute[0]} {remained_on_time}")
            timeline[minute[0]][1] -= 1
            power_consumed += minute[3]
            minute[3] = power_consumed
            minute[1] = getNewPrice(minute[2], power_consumed, max_power)
            totalBill += minute[1] * power_consumed
        index += 1
        power_needed = task[1]
    if power_needed > 0:
        raise Exception(f"Error mate at task {task[0]}")
    return f"{task[0]} " + " ".join(task[4])


def level7(file):
    content = readFile(file)
    max_power = int(content[0])
    max_bill = int(content[1])
    threshold = int(content[2])
    minutes_count = int(content[3])
    minutes = content[4:minutes_count + 4]
    minutes = getMinutes(minutes)
    house_count = int(content[minutes_count + 4])
    house_start = minutes_count + 5
    lines = [house_count]
    house_number = 1

    for house_index in range(house_count):
        tasks_count = int(content[house_start])
        tasks = content[house_start + 1: house_start + tasks_count + 1]
        house_start = house_start + tasks_count + 1
        tasks = getTasks(tasks)
        sorted_tasks = sorted(tasks, key=lambda task: task[3] - task[2])
        lines.append(house_number)
        house_number += 1
        lines.append(len(tasks))
        timeline = []
        for i in range(minutes_count):
            timeline.append([max_power, threshold])

        for task in sorted_tasks:
            line = getCheapest(minutes, task, timeline, max_power)
            lines.append(line)

    writeOutput(lines, file)


if __name__ == '__main__':
    level7("level7_example")
    level7("level7_1")
    level7("level7_2")
    level7("level7_3")
    level7("level7_4")
    level7("level7_5")
    print(totalBill)
