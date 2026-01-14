import os
import glob

folder = r'C:\Users\musta\Documents\Paradox Interactive\Hearts of Iron IV\mod\esicolor\common\national_focus\\'
dict = dict()
for filename in glob.glob(os.path.join(folder, 'generic*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        content = f.read()

        id_index = 0
        cost_index = 0
        while content.find("	id = ", id_index) != -1:
            id_index = content.find("id = ", id_index) + 5
            if content[id_index - 6:id_index - 5] != "	":
                continue

            id = content[id_index:content.find("\n", id_index)]

            cost_index = content.find("cost = ", id_index) + 7
            cost = content[cost_index:content.find("\n", cost_index)]

            has_key = False
            for x in dict.keys():
                if x == cost:
                    has_key = True

            if has_key:
                dict[cost].append(id)
            else:
                dict[cost] = [ id ]

print(dict)

with open("focus_list_by_cost.txt", "w") as f:
    for x, y in dict.items():
        f.write(x + ": ")
        for z in y:
            f.write(z + " ")
        f.write("\n\n")
