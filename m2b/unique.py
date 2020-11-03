import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', action='store_true', dest='count', default=False, required=False, help='Prefix lines by the number of occurrences')
parser.add_argument('-d', action='store_true', dest='dupe', default=False, required=False, help='Only print duplicate lines')
parser.add_argument('-i', action='store_true', dest='lower', default=False, required=False, help='Ignore differences in case when comparing, prints out full line in lowercase')
parser.add_argument('-u', action='store_true', dest='uniq', default=False, required=False, help='Only print unique lines')
args = parser.parse_args()

input = sys.stdin

data = list()
for line in input:
    data.append(line.rstrip())

if(args.lower):
    temp = list(data)
    data = list()
    for x in temp:
        data.append(x.lower())

count = dict()
if(args.count):
    for x in data:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1

if(args.dupe):
    duplicate = dict()
    for x in data:
        if x in duplicate:
            duplicate[x] += 1
        else:
            duplicate[x] = 1
    for x in duplicate:
        if duplicate[x] > 1:
            if(args.count):
                print(count[x], x)
            else:
                print(x)


elif(args.uniq):
    unique = dict()
    for x in data:
        if x in unique:
            unique[x] += 1
        else:
            unique[x] = 1
    for x in unique:
        if unique[x] == 1:
            if(args.count):
                print(count[x], x)
            else:
                print(x)

elif(args.count):
    for x in count:
        print(count[x], x)

else:
    temp = dict()
    for x in data:
        if(x in temp):
            x = x
        else:
            temp[x] = x
    for x in temp:
        print(temp[x])
