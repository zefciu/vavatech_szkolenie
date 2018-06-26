import csv

with open('MOCK_DATA.csv') as f:
    reader = csv.reader(f)
    for id, first_name, last_name, email, ip_address in reader:
        print(last_name)

with open('new_data', 'w') as f:
    writer = csv.writer(f)
    writer.writerows([(i, i) for i in range(10)])
