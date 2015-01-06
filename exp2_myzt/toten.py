import csv
from fetchtime import fetchtime

low=0
high=10
_ave=0
ave=0
counter=0
sec=0

with open('sample_9_csv.log', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        if row[3] == '0':
            value = int(row[1])
            if value<0: 
                value += 256
            else:
                pass
            value = value / 2 - 121
            row[1] = str(value)

            value = int(row[2])
            if value<0: 
                value += 256
            else:
                pass
            value = value / 2 - 121
            row[2] = str(value)

            sec = fetchtime(row[0])
            if low<=sec<high:
                _ave += float(row[1])
                counter += 1
            elif high<=sec:
                ave = _ave / counter
                _ave = float(row[1])
                counter = 1
                low += 10
                high += 10
            #if sec%10 == 0 and sec != 0:
                print(str(low) + "," + str(ave))
        else:
            pass
        #print(','.join(row))
        #if time%10 == 0:
        #    _ave = 0 
        #    low += 10
        #    high += 10
        #else:
        #    pass
