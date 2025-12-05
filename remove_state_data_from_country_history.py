import os
import glob

folder = r'C:\Users\musta\Documents\Paradox Interactive\Hearts of Iron IV\mod\esicolor\history\countries\\'
for filename in glob.glob(os.path.join(folder, '*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        content = f.read()
        if content.find("capital") != -1:
            content = content[content.find("capital"):]
            print(content)

    with open(os.path.join(os.getcwd(), filename), 'w') as f:
        f.write(content)
