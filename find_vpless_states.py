import os
import glob

folder = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\\'
for filename in glob.glob(os.path.join(folder, '*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        content = f.read()
        if content.find("victory_point") == -1:
            print("state = " + filename[len(folder) - 1:filename.find("-")])
