def alive_person(size, step):
    persons = []
    for index_loop in range(1, size + 1):
        persons.append(index_loop)
    index = 0
    counter = 0
    while (len(persons) > 1):
        counter = counter + 1
        if counter % step == 0:
            persons.pop(index)
            continue#index = index - 1
        index = index + 1
        if index > len(persons) - 1:
            index = 0
    return persons


size = int(input())
step = int(input())
print(alive_person(size, step))
