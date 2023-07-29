import os

folder = '/Users/linuss/Desktop/'
folder_original = os.path.join(folder, 'original_folder')
os.mkdir(folder_original)
folder_destination = os.path.join(folder, 'destination_folder')
os.mkdir(folder_destination)

entries = os.scandir(folder)
for entry in entries:
  location_original = os.path.join(folder, entry.name)
  location_destination = os.path.join(folder_destination, entry.name)

  if os.path.isfile(location_original):
    print('File: %s' % entry.name)
    os.rename(location_original, location_destination)
  elif os.path.isdir(entry):
    print('Directory: %s' % entry.name)

os.listdir(location_destination)

