import csv

que = input("Enter a city: ")

with open('weather.csv', 'r') as csvfile:
    reader = list(csv.reader(csvfile))

city_names = [row[0] for row in reader]
temperatures = [row[1] for row in reader]

for city_name in city_names:
    if city_name == que:
        index = city_names.index(city_name)
        print(city_name, temperatures[index])
