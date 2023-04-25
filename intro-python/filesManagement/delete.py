import os

path = './intro-python/filesManagement/'

if os.path.exists(path + 'file.txt'):
    os.remove(path + 'file.txt')
    print('file deleted successfully!')
else:
    print('Could not find file')

os.rmdir(path + 'dir')