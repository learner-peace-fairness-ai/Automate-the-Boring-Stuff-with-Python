import os

for foldername, subfolders, filenames in os.walk('delicious'):
    print(f'The current folder is {foldername}')

    for subfolder in subfolders:
        print(f'SUBFOLDER OF {foldername}: {subfolder}')
    
    for filename in filenames:
        print(f'FILE INSIDE {foldername}: {filename}')
    
    print('')