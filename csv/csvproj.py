import csv

filename = "records.csv"
fields = ['First Name', 'Last Name', 'Roll Number', 'Section', 'Phone Number']


def insert_data():
    with open(filename, 'a', newline='') as csvfile:
        writecsv = csv.writer(csvfile, delimiter=',')
        readcsv = csv.reader(csvfile, delimiter=',')
        for i in readcsv:
            if i[0] == 'First Name':
                pass
            else:
                writecsv.writerow(fields)
        ch = 'y'
        while (ch == 'y'):
            data = list(map(str, input('Enter data row : ').split()))
            writecsv.writerow(data)
            ch = input('Want to Enter nore data (Y/n): ')


if __name__ == "__main__":
    insert_data()
