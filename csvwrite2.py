import csv
row=['4','hansi','btech']
filename='heyu.csv'
try:
    with open(filename,'a')as fp:
        fg=csv.writer(fp)
        fg.writerow(row)
    print()
except FileNotFoundError:
    print('file alread exists')
