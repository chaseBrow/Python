import mapmaker

# I am kind of confused how you want us to test the map maker...
# I made a the range in the sample list can be changed and it will generate a map with sample data

# function: map initiation
# Description: takes all of the entries and adds them to a list
# arguments: (entries, center)
# Data: entries = list()
#       center = int -> **zip code**

# creating a sample list
test = list()
for x in range(30, 80):
    temp = list()
    temp.append(x)
    temp.append(60 + x)
    temp.append(30 + x)
    test.append(temp)

map = mapmaker.map(test, 23456)

# function: generate
# Description: takes all of the entries and plots them to a map
# arguments: (filename)
# data:
#        filename = str -> test.png
map.generate('test.png')

# I ran these commands to generate 4 maps and compared them to yours...
# mine are named the same, just appended with _test
# $ python3 m2a.py -z 23456 -d 5 -f 23456_5_test.png
# (see 23456_5.png)
#
# $ python3 m2a.py -z 66208 -d 20 -f 66208_20_test.png
# (see 66208_20.png)
#
# $ python3 m2a.py -z 91210 -d 1 -f 91210_1_test.png
# (see 91210_1.png)
#
# $ python3 m2a.py -z 62681 -d 2 -f 62681_2_test.png
# (see 62681_2.png)
