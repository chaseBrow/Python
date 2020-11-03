class dinodata:
    def __init__(self):
        self.found = list()
        self.data = list()

    def readDinos(self):
        file = open('dinosaur.dat', 'r')
        headers = file.readline().split('\t')
        for line in file:
            cols = line.split('\t')
            if (len(cols) == len(headers)):
                avg = (float(cols[15]) + float(cols[16])) / 2
                self.data.append(str(avg) + "\t" + cols[18] + "\t" + cols[19])
        file.close()

# 3 = long 4 = lat 0 = zip
    def findDinos(self, zip, dist):
        file = open('zipcodes.dat', 'r')
        for line in file:
            cols = line.split(';')
            if(zip == cols[0]):
                for x in self.data:
                    x = x.split('\t')
                    if(float(x[2]) >= float(cols[3]) - dist and float(x[2]) <= float(cols[3]) + dist) :
                        if(float(x[1]) >= float(cols[4]) - dist and float(x[1]) <= float(cols[4]) + dist) :
                            self.found.append(x)

    def printFound(self):
        for dino in self.found:
            print(dino)
