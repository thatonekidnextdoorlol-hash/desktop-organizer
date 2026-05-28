import os
import time
import shutil

print("Finding user Desktop...")
DesktopPath = os.path.join(os.path.expanduser("~"), "Desktop")
if not os.path.exists(DesktopPath):
    DesktopPath = input('\033[31m' + "ERROR: Could not locate Desktop in user root. Please input the name of the folder you would like to organize: " + '\033[0m')
print('\033[32m' + "User Desktop Found! " + DesktopPath + '\033[0m')

extensions = set()
DesktopOriginalFiles = os.listdir(DesktopPath)
for i, v in enumerate(DesktopOriginalFiles):
    if os.path.isfile(os.path.join(DesktopPath, v)):
        print('\033[33m' + str(v) + " >>> File" + '\033[0m')
        extensions.add(os.path.splitext(v)[1])
    else:
        print('\033[34m' + str(v) + " >>> Folder" + '\033[0m')
print("\033[38;5;206m" + "Found Extensions: " + str(extensions) + '\033[0m')

ExtensionList = sorted(extensions)
print(str(ExtensionList))

time.sleep(3)

os.system('cls' if os.name == 'nt' else 'clear')

print('\033[33m' + "Organizer found " + str(len(ExtensionList)) + " unique extensions in " + DesktopPath + '\033[0m')
for i, v in enumerate(ExtensionList):
    print("(" + str(i+1) + ") : " + str(v) + " >>> " + str(sum(1 for f in DesktopOriginalFiles if os.path.splitext(f)[1] == v)) + " Instance(s)")

excludeselection = input('\033[32m' + "These extensions will be sorted. Would you like to exclude some extensions from the sort? (Y/n):" + '\033[0m')

if str.upper(excludeselection) == "Y":
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, v in enumerate(ExtensionList):
        print("(" + str(i+1) + ") : " + str(v) + " >>> " + str(sum(1 for f in DesktopOriginalFiles if os.path.splitext(f)[1] == v)) + " Instance(s)")
    exclude = input('\033[32m' + "Please enter the number(s) of the extensions you would like to remove from this sort:" + '\033[0m')
    exclusionnumbers = [int(x) for x in exclude.split()]
    selectedextensions = [v for i, v in enumerate(ExtensionList) if i+1 not in exclusionnumbers]
else:
    selectedextensions = ExtensionList
os.system('cls' if os.name == 'nt' else 'clear')

tree = {}
for i, v in enumerate(selectedextensions):
    foldername = v.replace(".", "").upper()
    tree[foldername] = []
    for f in DesktopOriginalFiles:
        if os.path.splitext(f)[1] == v:
            tree[foldername].append(f)

print(DesktopPath)
for i, (folder, files) in enumerate(tree.items()):
    if i == len(tree) -1:
        print("└── " + folder)
        prefix = "    "
    else:  
        print("├── " + folder)
        prefix = "│   "
    for j, file in enumerate(files):
        if j == len(files) - 1:
            print(prefix + "└── " + file)
        else:
            print(prefix + "├── " + file)
while True:
    print('\033[32m' + "These files will be created upon confirmation." + '\033[0m')
    print('\033[32m' + "(X) - Exit without saving changes." + '\033[0m')
    print('\033[32m' + "(D) - Delete all files within a specific folder." + '\033[0m')
    print('\033[32m' + "(Y) - Change Folder Name" + '\033[0m')
    print('\033[32m' + "(N) - New Folder" + '\033[0m')
    # print('\033[32m' + "(U) - Ungroup Folder" + '\033[0m')
    # print('\033[32m' + "(B) - Change Folder Parent" + '\033[0m')
    print('\033[32m' + "(S) - Save & Continue." + '\033[0m')
    selection = input()
    if selection.upper() == "X":
        break
    elif selection.upper() == "S":
        for i, (folder, files) in enumerate(tree.items()):
            os.makedirs(os.path.join(DesktopPath, folder), exist_ok=True)
            for ind,file in enumerate(files):
                shutil.move(os.path.join(DesktopPath, file), os.path.join(DesktopPath, folder, file))
        break
    elif selection.upper() == "N":
        newfoldername = input('\033[32m' + "New Folder Name: " + '\033[0m')
        pass
    elif selection.upper() == "D":
        delete = input('\033[31m' + "Path to folder from root (" + DesktopPath + "...) to remove all contents: " + '\033[0m')
        
        if delete.upper() in tree:
            del tree[delete.upper()]
        else:
            while delete.upper() not in tree:
                delete = input('\033[31m' + "Path to folder from root (" + DesktopPath + "...) to remove all contents: " + '\033[0m')
            del tree[delete.upper()]
    elif selection.upper() == "Y":
        foldertorename = input('\033[31m' + "Path to folder from root (" + DesktopPath + "...) to rename: " + '\033[0m')

        if foldertorename.upper() in tree:
            newfoldername = input('\033[31m' + "Input New Folder Name: " + '\033[0m')
            tree[newfoldername] = tree[foldertorename.upper()]
            del tree[foldertorename.upper()]
        else:
            while foldertorename.upper() not in tree:
                foldertorename = input('\033[31m' + "Path to folder from root (" + DesktopPath + "...) to rename: " + '\033[0m')
            newfoldername = input('\033[31m' + "Input New Folder Name: " + '\033[0m')
            tree[newfoldername] = tree[foldertorename.upper()]
            del tree[foldertorename.upper()]