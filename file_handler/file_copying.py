import shutil
import os
try:
    source_file = ['text3.txt', 'text1.txt']
    destination_dir = 'destination1'
    checking=os.path.isdir(destination_dir)
    while checking:
        for i in source_file:
            if os.path.exists(i):
                print("file exists")
            else:
                shutil.copy(i, "destination_dir")
                print("file copied successfully")
        break
    else:
        print("The directory not found")
except FileNotFoundError as e:
    print(f"File does not exist: {e}" )