import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile

def get_lenght(file_path):
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        print(reader_list)
        return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ['id', 'name', 'email']
    next_id = get_lenght(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'id': next_id,
            'name': name,
            'email': email,
        })


#append_data('data.csv', 'Kirill', 'sag33rus@gmail.com')


filename = 'data.csv'
temp_file = NamedTemporaryFile(delete=False)

with open(filename, 'r') as csvfile, open(temp_file.name, 'w', newline='') as temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames = fieldnames)
        writer.writeheader()
        for row in reader:
                print(row)
                writer.writerow({
                        'id': row['id'],
                        'name': row['name'],
                        'email': row['email'],
                        'amount': 13.1313,
                        'sent': '',
                        'date': datetime.datetime.now()
                })
        temp_file.close()
        shutil.move(temp_file.name, filename)
