def test(): # test
    time = "0:01:10"
    print(fetchtime(time)) # >>> 70

def fetchtime(string):
    hms = string.split(':')
    seconds = int(hms[0])*3600 + int(hms[1])*60 + int(hms[2])
    return seconds
