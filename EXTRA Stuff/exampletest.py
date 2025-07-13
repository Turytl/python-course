greetlist = ['james', 'donald', 'robert', 'scott']

def greet(name):
    greeting = 'Hello ' + name
    return greeting

for greeting in greetlist:
    print(greet(greeting))
