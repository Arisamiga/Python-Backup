# Python-Backup
A Script made in Python to Backup Folders and its files.

### Works Using the following Libraries

+ [datetime](https://pypi.org/project/DateTime/)

+ [tqdm](https://pypi.org/project/tqdm/)

+ distutils ( Comes Installed with Python )

+ os ( Comes Installed with Python )

+ sys ( Comes Installed with Python )

+ time ( Comes Installed with Python )

## Installation
```
You have to install Python and Git
Create a folder.
Open Command Promt.
Type in: cd The path to your new folder. (Example: C:\Users\User\Desktop\New folder)
Press enter.
After that type in: git clone https://github.com/Arisamiga/Python-Backup.git
Press enter.
When you see all Github files in your folder you installed the bot files succesfully.
After that you would want to edit the backup.py script
```

Add the paths you want to backup in backup_dir
```python
backup_dir = [
    r"C:\Users\User\Desktop"",
    r"C:\Users\User\Music"",
    r"C:\Users\User\Documents"",
    r"C:\Users\User\Pictures"",
]
```

## Running the Script

Run the Script by using `python backup.py`

When you run the script you should see this

![image](https://user-images.githubusercontent.com/64918822/200147374-430015ab-b9b1-4dc2-b47a-f73e8cecce44.png)

**1**: Is to start the backup sequence 

**2**: Is to check that your paths are correct and that they exist.

**3**: Is to exit the script.

## Starting the Backup

After you Press **"1"** You will be shown the approximate size of your backup if you want to continue press `y`.

You will be asked to give a path of the backup Folder. **A Backup Folder will be created with the date within the Path you have given**

Eg. `ThePathGiven/Backup-2022-11-05/`

After You have provided a path a folder will be created and the backup will start!

