import dinodata

# function: dinodata initiation
# Description: creates all the data present in the dinodata class
# Data: found = list()
#       data = list()
# arguments: ()
dinos = dinodata.dinodata()


# function: readDinos
# Description: takes all complete lines from dinosaur.dat and adds them to a list
# arguments: ()
# data updated:
#       data = list(str) -> str = age\tlongitude\tlatitude
dinos.readDinos()

# function: findDinos
# Description:  takes all dinosaur entries that are within a certain range of a zipcodes
#               and saves them to the self.found list
# arguments: (zip, dist)
# data:
#       zip = str -> 46545
#       dist = float -> 20
# data updated:
#       found = list(str) -> str = age\tlongitude\tlatitude
dinos.findDinos('23456', 5)

# function: printFound
# Description:  takes all dinosaur entries that are within a certain range of a zipcodes
#               and saves them to the self.found list
# arguments: (zip, dist)
dinos.printFound()
