import csv
import os

# first lets create a bunch of files with bogus headers
# for i in range(10):
#     with open(f'csv_file_{i}.csv', 'w') as f:
#         csv_writer = csv.writer(f)
#         csv_writer.writerow(['name', 'phone', 'address'])
#         csv_writer.writerow(['ilja', 123456789, '1 hacker street, Riga'])
#         csv_writer.writerow(['ilja', 123456789, '1 hacker street, Riga'])
#         csv_writer.writerow(['ilja', 123456789, '1 hacker street, Riga'])
#         csv_writer.writerow(['ilja', 123456789, '1 hacker street, Riga'])
#         csv_writer.writerow(['ilja', 123456789, '1 hacker street, Riga'])
#         csv_writer.writerow(['ilja', 123456789, '1 hacker street, Riga'])

# next lets combine the files into one skipping the header on each
os.chdir('csv_bs')
files = os.listdir()

total_csv = open('total_csv.csv', 'w')
total_csv_writer = csv.writer(total_csv)

for file in files:
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the header - nicest way possible
        for row in reader:
            total_csv_writer.writerow(row)

total_csv.close()

# alternatively using the dict method, but doesn't feel very efficient!
with open('csv_file_0_no_head.csv', 'w') as wf:
    csv_writer = csv.DictWriter(wf, ['name', 'phone', 'address'])
    with open('csv_file_0.csv', 'r') as rf:
        csv_reader = csv.DictReader(rf)
        for row in csv_reader:
            csv_writer.writerow({
                'name': row['name'],
                'phone': row['phone'],
                'address': row['address']
            })
