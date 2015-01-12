import csv
import sys
from fetchtime import *

class toten():

    def modify_level(_row):
        value = int(_row)
        if value<0: 
            value += 256
        else:
            pass
        value = value / 2 - 121
        return str(value)

    if __name__ == "__main__":
        low=0
        high=10
        total1=0
        total2=0
        counter=0

        argvs = sys.argv

        f = open(argvs[1], 'r')

        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if len(row)!=4:
                total1 += total1 / counter
                total2 += total2 / counter
            elif row[3] == '0':
                row[1] = modify_level(row[1])
                row[2] = modify_level(row[2])

                sec = fetchtime(row[0])
                if low<=sec<high:
                    total1 += float(row[1])
                    total2 += float(row[2])
                    counter += 1
                elif high<=sec:
                    ave1 = total1 / counter
                    ave2 = total2 / counter
                    total1 = float(row[1])
                    total2 = float(row[2])
                    counter = 1
                    low += 10
                    high += 10
                    print(str(low) + "," + str(ave1) + "," + str(ave2) + "," + str(row[3]))
            else:
                pass

        f.close()

