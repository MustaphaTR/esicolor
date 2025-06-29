import os
import glob

folder = r'C:\Users\musta\Documents\Paradox Inte*ractive\Hearts of Iron IV\mod\esicolor\history\units\\'
result = ""
for filename in glob.glob(os.path.join(folder, '*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        content = f.read()
        state = filename[len(folder) - 2:filename.find("_")]
        while state.startswith("0"):
            state = state[1:len(state)]
        location_index = content.find("location = ") + 11
        location = content[location_index:content.find("\n", location_index, location_index+6)]
        text = """
    else_if = {
        limit = { state = """+state+""" }
        add_victory_points = {
            province = """+location+"""
            value = 2
        }
    }"""
        result = result + text

with open("upgrade_main_city.txt", "w") as f:
  f.write(result)
