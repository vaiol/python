from asyncio.subprocess import PIPE
import subprocess
import shutil
import glob
import os
import json

# open files

# f = open('text.txt', 'rt')
# print(f.read())
# print(f)
# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line)

# f.close()


# get multiple files
# for file in glob.glob(r'*.txt'):
#     print(file)


    
# check if file exist
# print(os.path.exists('text.txt'))


# # remove file
# os.remove('test')


# # remove folder recursively
# shutil.rmtree('test')


# # create empty file
open('t1.txt', 'w').close()
# with open('t1.txt', 'w') as outfil:
    # outfil.write('123')

# # run sub process
# bashCommand = f'touch file.txt'
# process = subprocess.Popen(bashCommand.split(), stdout=PIPE, stderr=PIPE)
# _, error = process.communicate()

# # create dir
# os.mkdir('test')

# # write to files
dictionary = {
    "name": "Alex",
    "age": 27,
}
 
# # Serializing json
# json_object = json.dumps(dictionary, indent=2)

 
# # # Writing to sample.json
# with open("t3.json", "w") as outfile:
#     outfile.write(json_object)

# import pathlib
# print(pathlib.Path().resolve())
# print(pathlib.Path(__file__).parent.resolve())