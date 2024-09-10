import csv

file = open("names.csv")
reader = csv.DictReader(file)
for line in reader:
    print(line["姓"] + line["名"] + "さん");
