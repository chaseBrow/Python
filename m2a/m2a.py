import sys
import dinodata
import mapmaker
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-z', dest='zipcode',type=str, required=True, help='zipcode to center search')
parser.add_argument('-d', dest='distance',type=float, required=True, help='length of longitude and latitude to extend search')
parser.add_argument('-f', dest='file',type=str, required=True, help='name of file to save image to')

args = parser.parse_args()

dinos = dinodata.dinodata()

dinos.readDinos()
dinos.findDinos(args.zipcode, args.distance)

# dinos.found = list(str) -> str = age\tlong\tlat
map = mapmaker.map(dinos.found, args.zipcode)
map.generate(args.file)
