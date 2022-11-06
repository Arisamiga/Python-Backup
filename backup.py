from datetime import datetime
from distutils.dir_util import copy_tree, remove_tree
from distutils.file_util import copy_file
import os
import sys
import time
from tqdm import tqdm

# Paths of things you want to backup
backup_dir = [
    r"C:\Users\"",
]

# bytes pretty-printing
UNITS_MAPPING = [
    (1 << 50, ' PB'),
    (1 << 40, ' TB'),
    (1 << 30, ' GB'),
    (1 << 20, ' MB'),
    (1 << 10, ' KB'),
    (1, (' byte', ' bytes')),
]


def get_unit(bytes):
    units=UNITS_MAPPING
    for factor, suffix in units:
        if bytes >= factor:
            break
    amount = int(bytes / factor)

    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix


def backup():
    combined_size = 0
    for i in backup_dir:
        i = i.replace('"', '')
        size = 0
        if os.path.exists(i):
            if os.path.isdir(i):
                for ele in os.scandir(i):
                    size += os.path.getsize(ele)
            elif os.path.isfile(i):
                size += os.path.getsize(i)
            combined_size = combined_size + size
        else:
            sys.stdout.write("\033[1;31m")
            print("Folder does not exist and wont be included in the backup: " + i)
            sys.stdout.write("\033[0;0m")
    sys.stdout.write("\033[1;30m")
    print(" * Combined size is: ", str(combined_size),
          "bytes", " Or: ", get_unit(combined_size))
    sys.stdout.write("\033[0;0m")
    choice = input(" | Do you want to continue? (y/n): ")
    if choice == "y":
        sys.stdout.write("\033[1;30m")
        print(" * Starting backup...")
        sys.stdout.write("\033[0;0m")
        inputpath = input(" | Enter the path of the backup folder: ")
        if not os.path.exists(inputpath):
            sys.stdout.write("\033[1;31m")
            print(" ! Path does not exist")
            sys.stdout.write("\033[0;0m")
        else:
            sys.stdout.write("\033[1;30m")
            print(" * Creating backup folder...")
            sys.stdout.write("\033[0;0m")
            inputpath = inputpath + "/Backup-" + \
                str(datetime.now().strftime("%Y-%m-%d"))
            if os.path.exists(inputpath):
                sys.stdout.write("\033[1;31m")
                print(" ! '/Backup-" + str(datetime.now().strftime("%Y-%m-%d")
                                           ) + "' Backup folder already exists")
                sys.stdout.write("\033[0;0m")
                choice = input(
                    " | Do you want it to be erased? and replaced with a new one? (y/n): ")
            if choice == "y" or not os.path.exists(inputpath):
                timeStart = time.perf_counter()
                if os.path.exists(inputpath):
                    remove_tree(inputpath)
                os.mkdir(inputpath)
                sys.stdout.write("\033[1;30m")
                print(" * Copying files...")
                sys.stdout.write("\033[0;0m")
                progressBar = tqdm(backup_dir)
                for i in progressBar:
                    i = i.replace('"', '')
                    if os.path.exists(i) and os.path.isdir(i):
                        progressBar.set_description(" Copying: " + str(i))
                        copy_tree(i, inputpath + i[2:])
                    elif os.path.exists(i) and os.path.isfile(i):
                        progressBar.set_description(" Copying: " + str(i))
                        copy_file(i, inputpath + i[2:])
                timeEnd = time.perf_counter()
                sys.stdout.write("\033[0;32m")
                print(
                    f" ! Backup completed in: {timeEnd - timeStart:0.4f} seconds")
            else:
                sys.stdout.write("\033[1;31m")
                print(" ! Backup aborted!")
    else:
        sys.stdout.write("\033[1;31m")
        print(" ! Backup aborted!")


# - Main -
sys.stdout.write("\033[1;36m")
print("# Backup System - By Arisamiga")
sys.stdout.write("\033[0;0m")
choice = input("1: Backup, 2: Check Paths, 3: Exit: ")

if choice != "1" and choice != "2" and choice != "3":
    sys.stdout.write("\033[1;31m")
    print(" | Invalid choice!")
else:
    if choice == "1":
        backup()
    elif choice == "2":
        combined_size = 0
        files = 0
        path_Exists = 0
        for i in backup_dir:
            i = i.replace('"', '')
            size = 0
            if os.path.exists(i):
                path_Exists += 1
                if os.path.isdir(i):
                    for ele in os.scandir(i):
                        size += os.path.getsize(ele)
                        files += 1
                else:
                    size += os.path.getsize(i)
                    files += 1
                combined_size = combined_size + size
                sys.stdout.write("\033[0;32m")
                print(f"Checking: {i} | " + str(size) + " bytes", " Or: ", get_unit(size),
                      " Exists: " + str(os.path.exists(i)))
                sys.stdout.write("\033[0;0m")
            else:
                sys.stdout.write("\033[1;31m")
                print(f"Checking: {i} | " + str(size) + " bytes", " Or: ", get_unit(size),
                      " Exists: " + str(os.path.exists(i)))
                sys.stdout.write("\033[0;0m")
        print("------------------------")
        sys.stdout.write("\033[1;36m")
        print("* Backup Information")
        print(" | Combined size is: ", str(combined_size), "bytes", "\n | Or: ", get_unit(
            combined_size), "\n | Files: " + str(files) + "\n | Paths: " + str(len(backup_dir)) + 
            "\n | Paths Exist: " + str(path_Exists) + "/" + str(len(backup_dir)))

    elif choice == "3":
        print("Exited..")
        exit()
