import os
import shutil

folder = r'C:\Users\musta\Documents\Paradox Interactive\Hearts of Iron IV\mod\esicolor\localisation\english\\'
languages = [ "braz_por", "french", "german", "japanese", "korean", "polish", "russian", "simp_chinese", "spanish" ] # Excluding "english", that's the source language.

for language in languages:
    new_folder = "localisation\\" + language + "\\"
    shutil.copytree(folder, new_folder, dirs_exist_ok=True)

    for file_name in os.listdir(new_folder):
        old_name = new_folder + file_name
        file_name = file_name.replace("english", language)
        new_name = new_folder + file_name

        if not os.path.isfile(new_name):
            os.rename(old_name, new_name)

            with open(os.path.join(os.getcwd(), new_name), 'r') as f:
                content = f.read()
                content = content.replace("l_english:", "l_"+language+":")
            with open(os.path.join(os.getcwd(), new_name), 'w') as f2:
                f2.write(content)
        else:
            os.remove(old_name)
