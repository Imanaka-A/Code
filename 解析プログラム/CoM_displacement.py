#相毎の重心の変位を算出

import pandas as pd
from tqdm import trange, tqdm
import os
import glob

os.makedirs("CoM_displacement/", exist_ok = True)

files = glob.glob("phase/CoM/*.csv")

for file in tqdm(files):
    print("処理中・・・", file)

    df = pd.read_csv(file)
    #はじめの値を基準
    #読み込みセルは変更可能性あり
    std_comx = df.iloc[0, 3]
    std_comy = df.iloc[0, 4]
    std_comz = df.iloc[0, 5]

    df["CoM_x"] = df["CoM_x"] - std_comx
    df["CoM_y"] = df["CoM_y"] - std_comy
    df["CoM_z"] = df["CoM_z"] - std_comz

    file_name = file.replace("phase/CoM\\", "").replace(".csv","")
    new_file_name = "CoM_displacement/" + file_name  + ".csv"
    df.to_csv(new_file_name, index = None)