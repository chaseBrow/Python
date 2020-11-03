from staticmap import StaticMap, CircleMarker

class map:
    def __init__(self, entries, center):
        self.entries = list(entries)
        self.center = center
        self.map = StaticMap(512, 512)

    def generate(self, filename):
        file = open('zipcodes.dat', 'r')
        long = 0
        lat = 0
        for line in file:
            line = line.split(';')
            if(line[0] == self.center):
                long = float(line[3])
                lat = float(line[4])
                break
        cir = CircleMarker((lat, long), 'black', 20)
        self.map.add_marker(cir)
        for x in self.entries:
            if(float(x[0]) < 50):
                color = "red"
            elif(float(x[0]) > 50 and float(x[0]) < 100):
                color = "orange"
            elif(float(x[0]) > 100 and float(x[0]) < 150):
                color = "yellow"
            elif(float(x[0]) > 150 and float(x[0]) < 200):
                color = "green"
            elif(float(x[0]) > 200 and float(x[0]) < 250):
                color = "blue"
            elif(float(x[0]) > 250 and float(x[0]) < 300):
                color = "purple"
            else :
                color = "white"
            cir = CircleMarker((float(x[1]), float(x[2])), color, 10)
            self.map.add_marker(cir)
        image = self.map.render()
        image.save(filename)
