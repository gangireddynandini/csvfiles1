import csv
try:
    with open('heyu.csv','r')as fp:
        gh=fp.read()
        print(gh)
except FileExistsError:
    print('fil alredy exists')