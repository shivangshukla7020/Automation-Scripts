# Import the required libraried (OS) and (shutil)
import os
import shutil

# Check for custom path input or to use downloads

n = input("Enter 1 for specific directory / 2 for downloads : ")

while(n != '1' and n != '2'):
  print("Invalid Input")
  n = input("Enter 1 for specific directory / 2 for downloads : ")

n = int(n)

if n == 1:
  dir = input("Enter the directory : ")
else:
  # Get the home directory of the current user  
  home_dir = os.path.expanduser("~")  

  # Construct the path to the Downloads directory  
  dir = os.path.join(home_dir, "Downloads") 

# Get all the files of the directory
files = os.listdir(dir)

# Some common extensions for better organization of media files and programs
extensions = {'Images' : ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'svg', 'heif', 'heic', 'ico', 'raw'], 'Audio' : ['mp3', 'wav', 'wma', 'aac', 'flac', 'ogg', 'm4a', 'aif', 'aiff', 'opus', 'cda'], 'Videos' : ['mp4', 'avi', 'mkv','mov', 'wmv', 'flv', 'm4v', 'webm', 'mpg', 'wmv', '3gp', 'ts'], 'Programs' : ['py', 'js', 'java', 'c', 'cpp', 'cc', 'cxx', 'h', 'hpp', 'hxx', 'cs', 'rb', 'php', 'go', 'swift', 'kt', 'kts', 'rs', 'ts', 'tsx', 'html', 'htm', 'css', 'sql', 'sh', 'bash', 'pl', 'hs', 'scala', 'lua', 'm', 'h', 'vb', 'R', 'r', 'm', 'dart', 'jl', 'elm', 'cr', 'asm', 'asmx', 'as', 'cfm', 'groovy', 'tcl', 'vb', 'frm', 'sas', 'fs', 'fsx','ipynb']}

# Run a loop for each file 
for file in files:
  filename,extension = os.path.splitext(file)

  # Get the extension of the particular file
  extension = extension[1:]

  # Check if the file extension lies in any media type
  if extension in extensions['Images']:
    extended = 'Images'
  elif extension in extensions['Audio']:
    extended = 'Audio'
  elif extension in extensions['Videos']:
    extended = 'Video'
  elif extension in extensions['Programs']:
    extended = 'Programming Files'
  else:
     extended = ''

  # Check if the required directory exits or not (If not then make the directory)
  if not os.path.exists(dir + '/' + extended + '/' + extension):
    os.makedirs(dir + '/' + extended + '/' + extension)

  # Move the file 
  shutil.move(dir + '/' + file,dir + '/' + extended + '/' + extension + '/' + file)

