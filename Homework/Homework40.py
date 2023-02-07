import csv

with open('C:/Python228/data2.csv', 'r') as fc:
    file_read = csv.reader(fc, delimiter=";")
    for i in file_read:
        print(i)
