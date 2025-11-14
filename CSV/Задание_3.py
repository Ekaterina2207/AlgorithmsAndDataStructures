import csv

def filter_goods(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)
        writer.writerow(header)
        for row in reader:
            amount = int(row[2])
            if amount > 1000:
                writer.writerow(row)
filter_goods('goods.csv', 'new_goods.csv')