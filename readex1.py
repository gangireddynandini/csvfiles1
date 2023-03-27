import csv
try:
    with open('heyu.csv','r')as fp:
        gh=csv.reader(fp)
        for val in gh:
            print(val)
except FileExistsError:
    print('fil alredy exists')