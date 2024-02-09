#筋電のtukeyのために使用する
#file_move_newおよびEMG_normalizationの後に使用すること！

import pandas as pd
from tqdm import trange, tqdm
import glob
import os
from natsort import natsorted

os.makedirs("condition2/phase/phase1", exist_ok = True)
os.makedirs("condition2/phase/phase2", exist_ok = True)
os.makedirs("condition2/phase/phase3_1", exist_ok = True)
os.makedirs("condition2/phase/phase3_2", exist_ok = True)
os.makedirs("condition2/phase/phase3_3", exist_ok = True)
os.makedirs("condition2/phase/phase3_4", exist_ok = True)

os.makedirs("condition3/phase/phase1", exist_ok = True)
os.makedirs("condition3/phase/phase2", exist_ok = True)
os.makedirs("condition3/phase/phase3_1", exist_ok = True)
os.makedirs("condition3/phase/phase3_2", exist_ok = True)
os.makedirs("condition3/phase/phase3_3", exist_ok = True)
os.makedirs("condition3/phase/phase3_4", exist_ok = True)

os.makedirs("condition4/phase/phase1", exist_ok = True)
os.makedirs("condition4/phase/phase2", exist_ok = True)
os.makedirs("condition4/phase/phase3_1", exist_ok = True)
os.makedirs("condition4/phase/phase3_2", exist_ok = True)
os.makedirs("condition4/phase/phase3_3", exist_ok = True)
os.makedirs("condition4/phase/phase3_4", exist_ok = True)

os.makedirs("condition5/phase/phase1", exist_ok = True)
os.makedirs("condition5/phase/phase2", exist_ok = True)
os.makedirs("condition5/phase/phase3_1", exist_ok = True)
os.makedirs("condition5/phase/phase3_2", exist_ok = True)
os.makedirs("condition5/phase/phase3_3", exist_ok = True)
os.makedirs("condition5/phase/phase3_4", exist_ok = True)

os.makedirs("condition6/phase/phase1", exist_ok = True)
os.makedirs("condition6/phase/phase2", exist_ok = True)
os.makedirs("condition6/phase/phase3_1", exist_ok = True)
os.makedirs("condition6/phase/phase3_2", exist_ok = True)
os.makedirs("condition6/phase/phase3_3", exist_ok = True)
os.makedirs("condition6/phase/phase3_4", exist_ok = True)

os.makedirs("condition7/phase/phase1", exist_ok = True)
os.makedirs("condition7/phase/phase2", exist_ok = True)
os.makedirs("condition7/phase/phase3_1", exist_ok = True)
os.makedirs("condition7/phase/phase3_2", exist_ok = True)
os.makedirs("condition7/phase/phase3_3", exist_ok = True)
os.makedirs("condition7/phase/phase3_4", exist_ok = True)

os.makedirs("condition8/phase/phase1", exist_ok = True)
os.makedirs("condition8/phase/phase2", exist_ok = True)
os.makedirs("condition8/phase/phase3_1", exist_ok = True)
os.makedirs("condition8/phase/phase3_2", exist_ok = True)
os.makedirs("condition8/phase/phase3_3", exist_ok = True)
os.makedirs("condition8/phase/phase3_4", exist_ok = True)

os.makedirs("condition9/phase/phase1", exist_ok = True)
os.makedirs("condition9/phase/phase2", exist_ok = True)
os.makedirs("condition9/phase/phase3_1", exist_ok = True)
os.makedirs("condition9/phase/phase3_2", exist_ok = True)
os.makedirs("condition9/phase/phase3_3", exist_ok = True)
os.makedirs("condition9/phase/phase3_4", exist_ok = True)

os.makedirs("condition10/phase/phase1", exist_ok = True)
os.makedirs("condition10/phase/phase2", exist_ok = True)
os.makedirs("condition10/phase/phase3_1", exist_ok = True)
os.makedirs("condition10/phase/phase3_2", exist_ok = True)
os.makedirs("condition10/phase/phase3_3", exist_ok = True)
os.makedirs("condition10/phase/phase3_4", exist_ok = True)

files = glob.glob("Normalization_phase1/*.csv")

print("phase1")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "condition2/phase/phase1/" + file.replace("Normalization_phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "condition3/phase/phase1/" + file.replace("Normalization_phase1\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[2] =="4":
        new_file = "condition4/phase/phase1/" + file.replace("Normalization_phase1\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[2] =="5":
        new_file = "condition5/phase/phase1/" + file.replace("Normalization_phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "condition6/phase/phase1/" + file.replace("Normalization_phase1\\", "")
        df.to_csv(new_file, index = None)
       
    if split_name[2] =="7":
        new_file = "condition7/phase/phase1/" + file.replace("Normalization_phase1\\", "")
        df.to_csv(new_file, index = None)
    
    if split_name[2] =="8":
        new_file = "condition8/phase/phase1/" + file.replace("Normalization_phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "condition9/phase/phase1/" + file.replace("Normalization_phase1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "condition10/phase/phase1/" + file.replace("Normalization_phase1\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("Normalization_phase2/*.csv")
print("phase2")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[2] =="2":
        new_file = "condition2/phase/phase2/" + file.replace("Normalization_phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="3":
        new_file = "condition3/phase/phase2/" + file.replace("Normalization_phase2\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[2] =="4":
        new_file = "condition4/phase/phase2/" + file.replace("Normalization_phase2\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[2] =="5":
        new_file = "condition5/phase/phase2/" + file.replace("Normalization_phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="6":
        new_file = "condition6/phase/phase2/" + file.replace("Normalization_phase2\\", "")
        df.to_csv(new_file, index = None)
       
    if split_name[2] =="7":
        new_file = "condition7/phase/phase2/" + file.replace("Normalization_phase2\\", "")
        df.to_csv(new_file, index = None)
    
    if split_name[2] =="8":
        new_file = "condition8/phase/phase2/" + file.replace("Normalization_phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="9":
        new_file = "condition9/phase/phase2/" + file.replace("Normalization_phase2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[2] =="10":
        new_file = "condition10/phase/phase2/" + file.replace("Normalization_phase2\\", "")
        df.to_csv(new_file, index = None)   

files = glob.glob("Normalization_phase3_1/*.csv")
print("phase3_1")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[3] =="2":
        new_file = "condition2/phase/phase3_1/" + file.replace("Normalization_phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="3":
        new_file = "condition3/phase/phase3_1/" + file.replace("Normalization_phase3_1\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[3] =="4":
        new_file = "condition4/phase/phase3_1/" + file.replace("Normalization_phase3_1\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[3] =="5":
        new_file = "condition5/phase/phase3_1/" + file.replace("Normalization_phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="6":
        new_file = "condition6/phase/phase3_1/" + file.replace("Normalization_phase3_1\\", "")
        df.to_csv(new_file, index = None)
       
    if split_name[3] =="7":
        new_file = "condition7/phase/phase3_1/" + file.replace("Normalization_phase3_1\\", "")
        df.to_csv(new_file, index = None)
    
    if split_name[3] =="8":
        new_file = "condition8/phase/phase3_1/" + file.replace("Normalization_phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="9":
        new_file = "condition9/phase/phase3_1/" + file.replace("Normalization_phase3_1\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="10":
        new_file = "condition10/phase/phase3_1/" + file.replace("Normalization_phase3_1\\", "")
        df.to_csv(new_file, index = None)   

files = glob.glob("Normalization_phase3_2/*.csv")
print("phase3_2")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[3] =="2":
        new_file = "condition2/phase/phase3_2/" + file.replace("Normalization_phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="3":
        new_file = "condition3/phase/phase3_2/" + file.replace("Normalization_phase3_2\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[3] =="4":
        new_file = "condition4/phase/phase3_2/" + file.replace("Normalization_phase3_2\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[3] =="5":
        new_file = "condition5/phase/phase3_2/" + file.replace("Normalization_phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="6":
        new_file = "condition6/phase/phase3_2/" + file.replace("Normalization_phase3_2\\", "")
        df.to_csv(new_file, index = None)
       
    if split_name[3] =="7":
        new_file = "condition7/phase/phase3_2/" + file.replace("Normalization_phase3_2\\", "")
        df.to_csv(new_file, index = None)
    
    if split_name[3] =="8":
        new_file = "condition8/phase/phase3_2/" + file.replace("Normalization_phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="9":
        new_file = "condition9/phase/phase3_2/" + file.replace("Normalization_phase3_2\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="10":
        new_file = "condition10/phase/phase3_2/" + file.replace("Normalization_phase3_2\\", "")
        df.to_csv(new_file, index = None)   

files = glob.glob("Normalization_phase3_3/*.csv")
print("phase3_3")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[3] =="2":
        new_file = "condition2/phase/phase3_3/" + file.replace("Normalization_phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="3":
        new_file = "condition3/phase/phase3_3/" + file.replace("Normalization_phase3_3\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[3] =="4":
        new_file = "condition4/phase/phase3_3/" + file.replace("Normalization_phase3_3\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[3] =="5":
        new_file = "condition5/phase/phase3_3/" + file.replace("Normalization_phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="6":
        new_file = "condition6/phase/phase3_3/" + file.replace("Normalization_phase3_3\\", "")
        df.to_csv(new_file, index = None)
       
    if split_name[3] =="7":
        new_file = "condition7/phase/phase3_3/" + file.replace("Normalization_phase3_3\\", "")
        df.to_csv(new_file, index = None)
    
    if split_name[3] =="8":
        new_file = "condition8/phase/phase3_3/" + file.replace("Normalization_phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="9":
        new_file = "condition9/phase/phase3_3/" + file.replace("Normalization_phase3_3\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="10":
        new_file = "condition10/phase/phase3_3/" + file.replace("Normalization_phase3_3\\", "")
        df.to_csv(new_file, index = None)

files = glob.glob("Normalization_phase3_4/*.csv")
print("phase3_4")
for file in tqdm(natsorted(files)):

    df = pd.read_csv(file)
    split_name = file.split("_", 4)

    if split_name[3] =="2":
        new_file = "condition2/phase/phase3_4/" + file.replace("Normalization_phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="3":
        new_file = "condition3/phase/phase3_4/" + file.replace("Normalization_phase3_4\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[3] =="4":
        new_file = "condition4/phase/phase3_4/" + file.replace("Normalization_phase3_4\\", "")
        df.to_csv(new_file, index = None)
   
    if split_name[3] =="5":
        new_file = "condition5/phase/phase3_4/" + file.replace("Normalization_phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="6":
        new_file = "condition6/phase/phase3_4/" + file.replace("Normalization_phase3_4\\", "")
        df.to_csv(new_file, index = None)
       
    if split_name[3] =="7":
        new_file = "condition7/phase/phase3_4/" + file.replace("Normalization_phase3_4\\", "")
        df.to_csv(new_file, index = None)
    
    if split_name[3] =="8":
        new_file = "condition8/phase/phase3_4/" + file.replace("Normalization_phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="9":
        new_file = "condition9/phase/phase3_4/" + file.replace("Normalization_phase3_4\\", "")
        df.to_csv(new_file, index = None)

    if split_name[3] =="10":
        new_file = "condition10/phase/phase3_4/" + file.replace("Normalization_phase3_4\\", "")
        df.to_csv(new_file, index = None)
print("END")