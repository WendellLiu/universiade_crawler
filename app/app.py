import csv

from script import schedule

data = schedule.main()
keys = data[0].keys()
with open('output/schedule.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)
