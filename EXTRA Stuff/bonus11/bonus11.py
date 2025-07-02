def read_file():
    
    with open("files/data.txt", "r") as f:
        read = f.readlines()
    
    return read


def number():
    
    list = []

    for temp in read_file():
        temp = temp.strip()
    
        if temp.isdigit():
            list.append(temp)
    
    return list


def average():
    
    list = number()
    total = 0

    for item in list:
        total = total + float(item)
    
    average = total / len(list)
    return average


print(average())
