import csv
from fetchtime import *
from toten import *

if __name__ == "__main__":
    low=0
    high=10
    _ave1=0
    ave1=0
    _ave2=0
    ave2=0
    counter=0
    sec=0
    
    with open('sample_9_csv.log', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
    
        for row in reader:
            if row[3] == '0':
                row[1] = modify_level(row[1])
                row[2] = modify_level(row[2])
    
                sec = fetchtime(row[0])
                if low<=sec<high:
                    _ave1 += float(row[1])
                    _ave2 += float(row[2])
                    counter += 1
                elif high<=sec:
                    ave1 = _ave1 / counter
                    ave2 = _ave2 / counter
                    _ave1 = float(row[1])
                    _ave2 = float(row[2])
                    counter = 1
                    low += 10
                    high += 10
                    print(str(low) + "," + str(ave1) + "," + str(ave2))
            else:
                pass

def modify_level(_row):
    value = int(_row)
    if value<0: 
        value += 256
    else:
        pass
    value = value / 2 - 121
    return str(value)
