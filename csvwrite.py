import csv
rec=[['1','nandu','eee'],
    ['2','madhu','cse'],
    ['3','pallu','mech']]
colna=['rol no','name','group']
filename='heyu.csv'
with open(filename,'w')as fp:
    cf=csv.writer(fp)
    cf.writerow(colna)
    cf.writerows(rec)
print('tbx')



