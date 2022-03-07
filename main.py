import csv
from csv import reader


with open('example_input.csv', 'r') as read_obj: #Note : Ganti example_input.csv ke nama file yg mau diubah formatnya, dan pastikan 1 directory dengan main.py
    # Inisialisasi Header CSV
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Iterasi setiap kolom
    if header != None:
        for row in csv_reader:
            with open('output.txt', 'a') as the_file:
                the_file.write('Host ' + row[0] + ' {'+ '\n')
                the_file.write('Hardware ethernet ' + row[1] + ';'+ '\n')
                the_file.write('fixed-address ' + row[2] + ';' + '\n')
                the_file.write('}\n')
