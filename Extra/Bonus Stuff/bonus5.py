waiting_list = ["sigma", "alpha", "delta"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    format = f"{index + 1}. {item.capitalize()}"
    print(format)
