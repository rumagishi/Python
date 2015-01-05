#import pandas as pd
#
#df = pd.read_csv('sample_9_csv.log', index_col='time')
#print df

import csv

with open('sample_9_csv.log', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        if row[3]=='0':
            value = int(row[1])
            if value<0: 
                value = value + 256
            else:
                pass
            value = value / 2 - 121
            row[1] = str(value)

            value = int(row[2])
            if value<0: 
                value = value + 256
            else:
                pass
            value = value / 2 - 121
            row[2] = str(value)
        else:
            pass
        print(','.join(row))
