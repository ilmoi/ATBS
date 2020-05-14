import json
import csv
with open('automate_online-materials/example.csv', 'r') as f:
    csv_reader = csv.reader(f)

    # simplest way to work with a csv is to convert it to a list
    data = list(csv_reader)
    print(data)

    # then you can access its parts as [row][col]
    print(data[0][1])


# for larger csv files you'll want to use a for loop to avoid loading the entire thing into memory at once
with open('automate_online-materials/example.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        print('row # is '+str(csv_reader.line_num) + str(row))


# now lets write
# need to pass newline='' to fix a bug on Windows where if we don't the output is double spaced
with open('output.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])  # the first row becomes the title row!
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])


print("-------------------- DELIM --------------------")
# if we wanted to use a different delimiter and terminator (char that comes at the END of each row)
# NOTE we're using a different extension (tsv) for tab separated values
with open('output2.tsv', 'w', newline='') as f:
    csv_writer = csv.writer(f, delimiter='\t', lineterminator='\n\n')
    csv_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])  # the first row becomes the title row!
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])
    csv_writer.writerow(['z', 'zz', 'zzz', 'zzzzzzzzzz'])


print("-------------------- DICT --------------------")
# when we have a file with headers it's more convenient to use a dict-reader/writer - allows us to target columns more precisely
with open('output.csv', 'r') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        print(row['ham'])

# if your csv did not have a header row, you could supply one of your own
with open('output.csv', 'r') as f:
    csv_reader = csv.DictReader(f, ['this', 'is', 'a fake', 'header row'])

    for row in csv_reader:
        print(row['this'])


# when writing, if we want to supply a header row, we'd do this:
with open('new_output.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, ['name', 'phone', 'email'])
    csv_writer.writeheader()  # you can also skip this and write without a header
    csv_writer.writerow({
        'name': 'ilja',
        'phone': '9999',
        'email': 'gofuck@yourself.now'
    })


print("-------------------- JSON! --------------------")
# JSON can't sore every type of value.
# YES: strings, integers, floats, Bools, lists, dictionaries, NoneTypes
# NO: file objects, csv reader objects, regex objects, selenium objects

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

# json -> str
js = json.loads(stringOfJsonData)  # load from string
print(js['name'])  # access as dictionary

# str -> json
newJson = json.dumps(js)
print(newJson)
