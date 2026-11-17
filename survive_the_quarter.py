import csv

with open ("scenarios_A.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

scenarios = []
