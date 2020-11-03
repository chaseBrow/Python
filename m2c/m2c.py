#!/usr/bin/env python3

import ray
import exrex
import argparse
import sys
import time
import hashlib

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument('-r', dest='regex', type=str, help='This is a regular expression to generate all possible passwords')
group.add_argument('-f', dest='filename', type=str, help='this is a filename to read encrypted passwords from')
group.add_argument('-e', dest='encrypted', type=str, help='this is a single encrypted password to crack')
group.add_argument('-p', dest='cleartext', type=str, help='this is for entering a cleartext password for debugging')
parser.add_argument('-t', dest='numThreads', type=int, default=1, help='This is the number of threads to use for cracking the password')
args = parser.parse_args()

ray.init(num_cpus=args.numThreads)
m = hashlib.md5()

possible  = list(exrex.generate(args.regex));

global find
find = list()
if(args.filename):
    file = open(args.filename, 'r')
    for line in file:
        find.append(line.rstrip())
    print(find)

elif(args.encrypted):
    find.append(args.encrypted)
    print(find)

elif(args.cleartext):
    temp = args.cleartext.encode('utf-8')
    m.update(temp)
    find.append(m.hexdigest())
    print(find)

@ray.remote
def match(x):
    global find
    m = hashlib.md5()
    x = x.encode('utf-8')
    m.update(x)
    if(m.hexdigest() in find):
        return True
    return None

password = ""
start = time.time()
for x in possible :
    if(ray.get(match.remote(x))) :
        password = x
        break

print(password, " is the password");
print("in: ", time.time() - start)
