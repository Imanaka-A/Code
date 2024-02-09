# ファイルを10分割してphaseを10 %毎に分けるプログラム
# files = でフォルダの名前を指定する

import pandas as pd
import glob
import os
from tqdm import trange, tqdm
import math

name = "GRF" #処理したい項目

#フォルダ作成
for i in range(1,11):
    #条件1
    os.makedirs("condition1/phase1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition1/phase2/" + name + "/" + str(i*10), exist_ok = True)
    os.makedirs("condition1/phase3_1/" + name + "/" + str(i*10), exist_ok = True)
    os.makedirs("condition1/phase3_2/" + name + "/" + str(i*10), exist_ok = True)
    os.makedirs("condition1/phase3_3/" + name + "/" + str(i*10), exist_ok = True)
    os.makedirs("condition1/phase3_4/" + name + "/" + str(i*10), exist_ok = True)
    #条件2
    os.makedirs("condition2/phase1/" + name + "/" + str(i*10), exist_ok = True)
    os.makedirs("condition2/phase2/" + name + "/" + str(i*10), exist_ok = True)
    os.makedirs("condition2/phase3_1/" + name + "/" + str(i*10), exist_ok = True)
    os.makedirs("condition2/phase3_2/" + name + "/" + str(i*10), exist_ok = True)
    os.makedirs("condition2/phase3_3/" + name + "/" + str(i*10), exist_ok = True)
    os.makedirs("condition2/phase3_4/" + name + "/" + str(i*10), exist_ok = True)
    #条件3
    os.makedirs("condition3/phase1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition3/phase2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition3/phase3_1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition3/phase3_2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition3/phase3_3/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition3/phase3_4/" + name + "/" + str(i*10) , exist_ok = True)
    #条件4
    os.makedirs("condition4/phase1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition4/phase2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition4/phase3_1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition4/phase3_2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition4/phase3_3/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition4/phase3_4/" + name + "/" + str(i*10) , exist_ok = True)
    #条件5
    os.makedirs("condition5/phase1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition5/phase2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition5/phase3_1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition5/phase3_2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition5/phase3_3/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition5/phase3_4/" + name + "/" + str(i*10) , exist_ok = True)
    #条件6
    os.makedirs("condition6/phase1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition6/phase2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition6/phase3_1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition6/phase3_2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition6/phase3_3/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition6/phase3_4/" + name + "/" + str(i*10) , exist_ok = True)
    #条件7
    os.makedirs("condition7/phase1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition7/phase2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition7/phase3_1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition7/phase3_2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition7/phase3_3/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition7/phase3_4/" + name + "/" + str(i*10) , exist_ok = True)
    #条件8
    os.makedirs("condition8/phase1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition8/phase2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition8/phase3_1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition8/phase3_2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition8/phase3_3/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition8/phase3_4/" + name + "/" + str(i*10) , exist_ok = True)
    #条件9
    os.makedirs("condition9/phase1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition9/phase2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition9/phase3_1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition9/phase3_2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition9/phase3_3/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition9/phase3_4/" + name + "/" + str(i*10) , exist_ok = True)
    #条件10
    os.makedirs("condition10/phase1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition10/phase2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition10/phase3_1/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition10/phase3_2/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition10/phase3_3/" + name + "/" + str(i*10) , exist_ok = True)
    os.makedirs("condition10/phase3_4/" + name + "/" + str(i*10) , exist_ok = True)

#処理したいファイルを入力
##要変更
files = glob.glob("GRF/*.csv")

print("処理開始．．．")

#処理開始
for file in tqdm(files):
    df = pd.read_csv(file)
    split_len = len(df) /10
    split_name = file.split("_", 3)

    for i in range(1,11):
        a = i
        df_Split = df.iloc[round((a - 1)*split_len) : round(a*split_len), :] #10％ずつで切り取り
        df_Split = df_Split.reset_index(drop = True) #インデックス削除
        
        if split_name[1] == "1":
            if split_name[3] == "phase1.csv":
                new_file = "condition1/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition1/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition1/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition1/phase3_2/" + name + "/"+ str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition1/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition1/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
                 
        if split_name[1] == "2":
            if split_name[3] == "phase1.csv":
                new_file = "condition2/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition2/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition2/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition2/phase3_2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition2/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition2/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None)  
                 
        if split_name[1] == "3":
            if split_name[3] == "phase1.csv":
                new_file = "condition3/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition3/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition3/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition3/phase3_2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition3/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition3/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None)  

        if split_name[1] == "4":
            if split_name[3] == "phase1.csv":
                new_file = "condition4/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition4/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition4/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition4/phase3_2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition4/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition4/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None)  
 
        if split_name[1] == "5":
            if split_name[3] == "phase1.csv":
                new_file = "condition5/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition5/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition5/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition5/phase3_2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition5/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition5/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None)  

        if split_name[1] == "6":
            if split_name[3] == "phase1.csv":
                new_file = "condition6/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition6/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition6/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition6/phase3_2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition6/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition6/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None)  

        if split_name[1] == "7":
            if split_name[3] == "phase1.csv":
                new_file = "condition7/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition7/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition7/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition7/phase3_2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition7/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition7/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None)  

        if split_name[1] == "8":
            if split_name[3] == "phase1.csv":
                new_file = "condition8/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition8/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition8/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition8/phase3_2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition8/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition8/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 

        if split_name[1] == "9":
            if split_name[3] == "phase1.csv":
                new_file = "condition9/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition9/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition9/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition9/phase3_2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition9/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition9/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None)  

        if split_name[1] == "10":
            if split_name[3] == "phase1.csv":
                new_file = "condition10/phase1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase2.csv":
                new_file = "condition10/phase2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_1.csv":
                new_file = "condition10/phase3_1/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_2.csv":
                new_file = "condition10/phase3_2/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_3.csv":
                new_file = "condition10/phase3_3/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None) 
            if split_name[3] == "phase3_4.csv":
                new_file = "condition10/phase3_4/" + name + "/" + str(a*10) + "/" + file.replace("GRF\\", "").replace(".csv", "") +"_" + str(a*10) + ".csv"
                df_Split.to_csv(new_file, index = None)          