from asyncio.subprocess import PIPE
from distutils import file_util
import subprocess
import shutil
import glob
import os
import json

# open files

f = open('text.txt', 'rt')
# print(f.read())
# print()
# print(f.readline())

for line in f:
    print(line)

f.close()


# get multiple files
for file in glob.glob(rf'*.txt'):
    print(file)


    
# check if file exist
# os.path.exists('file.txt')


# remove file
# os.remove('file.txt')


# remove folder recursively
# shutil.rmtree(destination_path)


# create empty file
# open(file, 'a').close()

# run sub process
# bashCommand = f'touch file.txt'
# process = subprocess.Popen(bashCommand.split(), stdout=PIPE, stderr=PIPE)
# _, error = process.communicate()

# create dir
# os.mkdir('test')

# write to files
dictionary = {
    "name": "Alex",
    "age": 27,
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=2)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)