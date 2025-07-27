feedback = ["The food was very good.", "The water was just alright.", "The waiter was very hot."]
file = ["food.txt", "water.txt", "waiter.txt"]

i = 0
for name in file:
    store = open("files/" + name, "w")
    store.write(feedback[i])
    i = i + 1
    store.close()
    
print("Completed!")
