import csv

def read_csv(file_name):
    f = open(file_name, 'rb')
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
    f.close()
    return data

def filter_by_column(data, index, value):
    filtered = []
    for row in data:
        if row[index] == value:
            filtered.append(row)
    return filtered

def main():
    data = read_csv('sales.csv')
    filtered = filter_by_column(data, 2, 'Books')
    print "Filtered Data:"
    for row in filtered:
        print row

main()
