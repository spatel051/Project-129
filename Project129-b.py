import csv

dataset_1 = []
dataset_2 = []

with open('Project129.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

with open('Project127.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

header_1 = dataset_1[0]
star_data_1 = dataset_1[1:]

header_2 = dataset_2[0]
star_data_2 = dataset_2[1:]

headers = header_1 + header_2
star_data = []

for index, data_row in enumerate(star_data_2):
    star_data.append(star_data_2[index] + star_data_1[index])

with open('final.csv', 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)