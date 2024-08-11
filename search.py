import csv

class search():
    library = []
    with open('info.csv') as csv_file:
        records = csv_file.readlines()
        csv_reader = csv.reader(csv_file, delimiter=',')
        for record in records:
            fields = record.strip().split(',')
            LibraryItem = {}
            LibraryItem['id'] = fields[0]
            LibraryItem['name'] = fields[1]
            LibraryItem['director'] = fields[2]
            LibraryItem['rating'] = fields[3]
            LibraryItem['play_count'] = fields[4]

            library.append(LibraryItem)

    # search

    term = input('Enter a search term: ').lower()
    result_list = []

    for LibraryItem in library:
        for val in LibraryItem.values():
            if isinstance(val, str) and term in val.lower(): # checks if val is a string before attempting to use the "in" operator. 
                result_list.append(LibraryItem)
                break 

    # print 

    for LibraryItem in result_list:
        print(LibraryItem['id'], ':', LibraryItem['name'], ',', LibraryItem['director'],  ',',LibraryItem['rating'],  ',',LibraryItem['play_count'])