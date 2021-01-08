#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
import os
import shutil
import subprocess
from zipfile import ZipFile 

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
 
  # value= os.getcwd()
  # print(value,"current directory")
  file_paths=[]
  filenames = os.listdir(dir)
  print(filenames)
  for filename in filenames:
    # print (filename,"filename")  
    # print (os.path.join(dir, filename),"joined path")
    reqpath=os.path.abspath(os.path.join(dir, filename))
    file_paths.append(reqpath) 
    print (reqpath,"abspath") 
  return file_paths

def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
    print( os.walk(directory))
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        print (files)
        for filename in files: 
            print(filename,'filename')
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths         

def copy_to(paths, dir):
 print(dir)
 source = dir
 target = paths  ## path to target file
 print(os.path.isabs(source),"abspath")
#  assert not os.path.isabs(source)
#  target = os.path.join(target, os.path.dirname(source))

 try:
    shutil.copy(source, target)
 except IOError as e:
    print("Unable to copy file. %s" % e)
 except:
    print("Unexpected error:", sys.exc_info())
#  os.makedirs(target)
 return 

def zip_to(file_paths, zippath):
  print('Following files will be zipped:') 
  for file_name in file_paths: 
      print(file_name) 
  
  if os.path.exists('my_python_files.zip'):
    print("file exists already change the file name")
  else:  
   with ZipFile('my_python_files.zip','w') as zip: 
      for file in file_paths:
            print(file,"--file") 
            zip.write(file) 
  
   print('All files zipped successfully!')   
  return


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  # get_special_paths("F:\idealistic\lets_python-master\exercises\copyspecial")
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(0)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    dir= sys.argv[2]
    print(dir, "--dir" )
    paths= sys.argv[3]
    print(paths, "--paths")
  
    copy_to(paths, dir)
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    directory= sys.argv[2]
    path=get_special_paths(directory)
    # path=get_all_file_paths(directory)
    print ()
    zippath= sys.argv[3]
    print(zippath, "--zippath")

    zip_to(path, zippath)

    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(0)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
