# 2022/05/24 更新版
# 筋電の正規化のためにファイルを移動させる。
# ファイル名は　stw_条件_試行数 とする。
# 条件1（歩行車を用いない起立歩行動作）だけを別に入れる(nomがつかないフォルダ)
# その他の条件はnomフォルダに格納


import pandas as pd
from tqdm import trange, tqdm
import glob
import os

#処理したいフォルダ
foldername = "EMG"
#被験者
name = "stw"

#フォルダ作成
os.makedirs("phase1/", exist_ok = True)
os.makedirs("phase1_nom/", exist_ok = True)
os.makedirs("phase2/", exist_ok = True)
os.makedirs("phase2_nom/", exist_ok = True)
os.makedirs("phase3_1/", exist_ok = True)
os.makedirs("phase3_1_nom/", exist_ok = True)
os.makedirs("phase3_2/", exist_ok = True)
os.makedirs("phase3_2_nom/", exist_ok = True)
os.makedirs("phase3_3/", exist_ok = True)
os.makedirs("phase3_3_nom/", exist_ok = True)
os.makedirs("phase3_4/", exist_ok = True)
os.makedirs("phase3_4_nom/", exist_ok = True)

print("処理開始")

#相分け後のEGMデータ読み込み
files = glob.glob("phase/" + foldername + "\*.csv")

#条件1だけ別フォルダに格納
for file in tqdm(files):

    df = pd.read_csv(file)
    split_name = file.split("_",3) #ファイル名を"_"で分割　#phase/EMG\stw #1 #1 #ad

    if split_name[1] == "1": #条件1の時

            if split_name[3] == "phase1.csv":
                new_file = "phase1/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase2.csv":
                new_file = "phase2/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase3_1.csv":
                new_file = "phase3_1/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase3_2.csv":
                new_file = "phase3_2/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase3_3.csv":
                new_file = "phase3_3/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase3_4.csv":
                new_file = "phase3_4/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            else:
                pass

    else: #他の条件の時

            if split_name[3] == "phase1.csv":
                new_file = "phase1_nom/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase2.csv":
                new_file = "phase2_nom/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase3_1.csv":
                new_file = "phase3_1_nom/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase3_2.csv":
                new_file = "phase3_2_nom/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase3_3.csv":
                new_file = "phase3_3_nom/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            elif split_name[3] == "phase3_4.csv":
                new_file = "phase3_4_nom/" + file.replace("phase/" + foldername + "\\", "")
                df.to_csv(new_file, index = None)
            else:
                pass

print("処理終了")