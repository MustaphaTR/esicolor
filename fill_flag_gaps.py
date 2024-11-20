import os
import shutil

ooo_flag = r'C:\Users\musta\Documents\Paradox Interactive\Hearts of Iron IV\mod\esicolor\gfx\flags\OOO.tga'
folder = r'C:\Users\musta\Documents\Paradox Interactive\Hearts of Iron IV\mod\esicolor\gfx\flags\\'
i = 1
while i < 981:
    name = str(i)
    if i < 10:
        name = "00" + name
    elif i > 9 and i < 100:
        name = "0" + name

    name = name.replace("0", "O")
    name = name.replace("1", "I")
    name = name.replace("2", "Z")
    name = name.replace("3", "E")
    name = name.replace("4", "A")
    name = name.replace("5", "S")
    name = name.replace("6", "L")
    name = name.replace("7", "F")
    name = name.replace("8", "B")
    name = name.replace("9", "Y")

    if name.endswith("IAS"): name = name.replace("IAS", "JBT")
    if name.endswith("ELS"): name = name.replace("ELS", "FMT")
    if name.endswith("AOI"): name = name.replace("AOI", "BPJ")
    if name.endswith("ALB"): name = name.replace("ALB", "BMC")
    if name.endswith("AFA"): name = name.replace("AFA", "BGB")
    if name.endswith("SOL"): name = name.replace("SOL", "TPM")
    if name.endswith("SIE"): name = name.replace("SIE", "TJF")
    if name.endswith("SIA"): name = name.replace("SIA", "TJB")
    if name.endswith("SIL"): name = name.replace("SIL", "TJM")
    if name.endswith("SAF"): name = name.replace("SAF", "TBG")
    if name.endswith("SLO"): name = name.replace("SLO", "TMP")
    if name.endswith("LIB"): name = name.replace("LIB", "MJC")
    if name.endswith("LEB"): name = name.replace("LEB", "MFC")
    if name.endswith("LAO"): name = name.replace("LAO", "MBP")
    if name.endswith("LBA"): name = name.replace("LBA", "MCB")
    if name.endswith("BOS"): name = name.replace("BOS", "CPT")
    if name.endswith("BOL"): name = name.replace("BOL", "CPM")
    if name.endswith("BIA"): name = name.replace("BIA", "CJB")
    if name.endswith("BEL"): name = name.replace("BEL", "CFM")
    if name.endswith("BAS"): name = name.replace("BAS", "CBT")
    if name.endswith("BAY"): name = name.replace("BAY", "CBZ")
    if name.endswith("BLZ"): name = name.replace("BLZ", "CMA")
    if name.endswith("BYA"): name = name.replace("BYA", "CZB")
    if name.endswith("YES"): name = name.replace("YES", "ZFT")

    new_name = folder + name
    new_name_dot_tga = new_name + ".tga"
    new_name_communism = new_name + "_communism.tga"
    new_name_democratic = new_name + "_democratic.tga"
    new_name_fascism = new_name + "_fascism.tga"
    new_name_neutrality = new_name + "_neutrality.tga"
    if not os.path.isfile(new_name_dot_tga):
        if not os.path.isfile(new_name_communism) or not os.path.isfile(new_name_democratic) or not os.path.isfile(new_name_fascism) or not os.path.isfile(new_name_neutrality):
            shutil.copyfile(ooo_flag, new_name_dot_tga)

            print(new_name_dot_tga)

    i += 1
