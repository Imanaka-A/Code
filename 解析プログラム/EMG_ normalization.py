#2022/05/23 更新
#筋電正規化プログラム
#原らの論文を基に，歩行車を使わずに歩いた相ごとの平均値を100%とし正規化する
#相ごとにフォルダに入れる．(file_miove_new.pyを利用) 

import pandas as pd
import numpy as np
import glob
import os
from tqdm import trange, tqdm

os.makedirs('Normalization_phase1/', exist_ok = True)
os.makedirs('Normalization_phase2/', exist_ok = True)
os.makedirs('Normalization_phase3_1/', exist_ok = True)
os.makedirs('Normalization_phase3_2/', exist_ok = True)
os.makedirs('Normalization_phase3_3/', exist_ok = True)
os.makedirs('Normalization_phase3_4/', exist_ok = True)

n = 4 #試行数（ファイルの数）

#変数初期化
L_Bic = 0
R_Bic = 0
L_Tri = 0
R_Tri = 0
L_Vlo = 0
R_Vlo = 0
L_Rec = 0
R_Rec = 0
L_Tib = 0
R_Tib = 0
L_Gas = 0
R_Gas = 0

files = glob.glob("phase1/*.csv")

for file in files:
    df = pd.read_csv(file)
    df = df.abs() #絶対値

    #試行数で割った平均を足していく
    L_Bic = L_Bic + df["L.Biceps Br.(uV):"].mean() / n
    R_Bic = R_Bic + df["R.Biceps Br.(uV):"].mean() / n
    L_Tri = L_Tri + df["L.Med. Triceps(uV):"].mean() / n
    R_Tri = R_Tri + df["R.Med. Triceps(uV):"].mean() / n
    L_Vlo = L_Vlo + df["L.Vlo(uV):"].mean() / n
    R_Vlo = R_Vlo + df["R.Vlo(uV):"].mean() / n
    L_Rec = L_Rec + df["L.Rectus Fem.(uV):"].mean() / n
    R_Rec = R_Rec + df["R.Rectus Fem.(uV):"].mean() / n
    L_Tib = L_Tib + df["L.Tib.Ant.(uV):"].mean() / n
    R_Tib = R_Tib + df["R.Tib.Ant.(uV):"].mean() / n
    L_Gas = L_Gas + df["L.Med. Gastro(uV):"].mean() / n
    R_Gas = R_Gas + df["R.Med. Gastro(uV):"].mean() / n

print("第1相処理中...")

files = glob.glob("phase1_nom/*.csv")

for file in tqdm(files):
    df = pd.read_csv(file)
    df = df.abs()

    df["L.Biceps Br.(uV):"]=df["L.Biceps Br.(uV):"]*100/L_Bic
    df["R.Biceps Br.(uV):"]=df["R.Biceps Br.(uV):"]*100/R_Bic
    df["L.Med. Triceps(uV):"]=df["L.Med. Triceps(uV):"]*100/L_Tri
    df["R.Med. Triceps(uV):"]=df["R.Med. Triceps(uV):"]*100/R_Tri
    df["L.Vlo(uV):"]=df["L.Vlo(uV):"]*100/L_Vlo
    df["R.Vlo(uV):"]=df["R.Vlo(uV):"]*100/R_Vlo
    df["L.Rectus Fem.(uV):"]=df["L.Rectus Fem.(uV):"]*100/L_Rec
    df["R.Rectus Fem.(uV):"]=df["R.Rectus Fem.(uV):"]*100/R_Rec
    df["L.Tib.Ant.(uV):"]=df["L.Tib.Ant.(uV):"]*100/L_Tib
    df["R.Tib.Ant.(uV):"]=df["R.Tib.Ant.(uV):"]*100/R_Tib
    df["L.Med. Gastro(uV):"]=df["L.Med. Gastro(uV):"]*100/L_Gas
    df["R.Med. Gastro(uV):"]=df["R.Med. Gastro(uV):"]*100/R_Gas
    
    new_file = 'Normalization_phase1/' + file.replace('phase1_nom\\', '')
    df.to_csv(new_file, index = None) 

#変数初期化
L_Bic = 0
R_Bic = 0
L_Tri = 0
R_Tri = 0
L_Vlo = 0
R_Vlo = 0
L_Rec = 0
R_Rec = 0
L_Tib = 0
R_Tib = 0
L_Gas = 0
R_Gas = 0

files = glob.glob("phase2/*.csv")

for file in files:
    df = pd.read_csv(file)
    df = df.abs()
    #試行数で割った平均を足していく
    L_Bic = L_Bic + df["L.Biceps Br.(uV):"].mean()/n
    R_Bic = R_Bic + df["R.Biceps Br.(uV):"].mean()/n
    L_Tri = L_Tri + df["L.Med. Triceps(uV):"].mean()/n
    R_Tri = R_Tri + df["R.Med. Triceps(uV):"].mean()/n
    L_Vlo = L_Vlo + df["L.Vlo(uV):"].mean()/n
    R_Vlo = R_Vlo + df["R.Vlo(uV):"].mean()/n
    L_Rec = L_Rec + df["L.Rectus Fem.(uV):"].mean()/n
    R_Rec = R_Rec + df["R.Rectus Fem.(uV):"].mean()/n
    L_Tib = L_Tib + df["L.Tib.Ant.(uV):"].mean()/n
    R_Tib = R_Tib + df["R.Tib.Ant.(uV):"].mean()/n
    L_Gas = L_Gas + df["L.Med. Gastro(uV):"].mean()/n
    R_Gas = R_Gas + df["R.Med. Gastro(uV):"].mean()/n

print("第2相処理中...")
files = glob.glob("phase2_nom/*.csv")

for file in tqdm(files):
    df = pd.read_csv(file)
    df = df.abs()

    df["L.Biceps Br.(uV):"]=df["L.Biceps Br.(uV):"]*100/L_Bic
    df["R.Biceps Br.(uV):"]=df["R.Biceps Br.(uV):"]*100/R_Bic
    df["L.Med. Triceps(uV):"]=df["L.Med. Triceps(uV):"]*100/L_Tri
    df["R.Med. Triceps(uV):"]=df["R.Med. Triceps(uV):"]*100/R_Tri
    df["L.Vlo(uV):"]=df["L.Vlo(uV):"]*100/L_Vlo
    df["R.Vlo(uV):"]=df["R.Vlo(uV):"]*100/R_Vlo
    df["L.Rectus Fem.(uV):"]=df["L.Rectus Fem.(uV):"]*100/L_Rec
    df["R.Rectus Fem.(uV):"]=df["R.Rectus Fem.(uV):"]*100/R_Rec
    df["L.Tib.Ant.(uV):"]=df["L.Tib.Ant.(uV):"]*100/L_Tib
    df["R.Tib.Ant.(uV):"]=df["R.Tib.Ant.(uV):"]*100/R_Tib
    df["L.Med. Gastro(uV):"]=df["L.Med. Gastro(uV):"]*100/L_Gas
    df["R.Med. Gastro(uV):"]=df["R.Med. Gastro(uV):"]*100/R_Gas
    
    new_file = 'Normalization_phase2/' + file.replace('phase2_nom\\', '')
    df.to_csv(new_file, index = None) 

#変数初期化
L_Bic = 0
R_Bic = 0
L_Tri = 0
R_Tri = 0
L_Vlo = 0
R_Vlo = 0
L_Rec = 0
R_Rec = 0
L_Tib = 0
R_Tib = 0
L_Gas = 0
R_Gas = 0

files = glob.glob("phase3_1/*.csv")

for file in files:
    df = pd.read_csv(file)
    df = df.abs()
    #試行数で割った平均を足していく
    L_Bic = L_Bic + df["L.Biceps Br.(uV):"].mean()/n
    R_Bic = R_Bic + df["R.Biceps Br.(uV):"].mean()/n
    L_Tri = L_Tri + df["L.Med. Triceps(uV):"].mean()/n
    R_Tri = R_Tri + df["R.Med. Triceps(uV):"].mean()/n
    L_Vlo = L_Vlo + df["L.Vlo(uV):"].mean()/n
    R_Vlo = R_Vlo + df["R.Vlo(uV):"].mean()/n
    L_Rec = L_Rec + df["L.Rectus Fem.(uV):"].mean()/n
    R_Rec = R_Rec + df["R.Rectus Fem.(uV):"].mean()/n
    L_Tib = L_Tib + df["L.Tib.Ant.(uV):"].mean()/n
    R_Tib = R_Tib + df["R.Tib.Ant.(uV):"].mean()/n
    L_Gas = L_Gas + df["L.Med. Gastro(uV):"].mean()/n
    R_Gas = R_Gas + df["R.Med. Gastro(uV):"].mean()/n

print("第3_1相処理中...")
files = glob.glob("phase3_1_nom/*.csv")

for file in tqdm(files):
    df = pd.read_csv(file)
    df = df.abs()

    df["L.Biceps Br.(uV):"]=df["L.Biceps Br.(uV):"]*100/L_Bic
    df["R.Biceps Br.(uV):"]=df["R.Biceps Br.(uV):"]*100/R_Bic
    df["L.Med. Triceps(uV):"]=df["L.Med. Triceps(uV):"]*100/L_Tri
    df["R.Med. Triceps(uV):"]=df["R.Med. Triceps(uV):"]*100/R_Tri
    df["L.Vlo(uV):"]=df["L.Vlo(uV):"]*100/L_Vlo
    df["R.Vlo(uV):"]=df["R.Vlo(uV):"]*100/R_Vlo
    df["L.Rectus Fem.(uV):"]=df["L.Rectus Fem.(uV):"]*100/L_Rec
    df["R.Rectus Fem.(uV):"]=df["R.Rectus Fem.(uV):"]*100/R_Rec
    df["L.Tib.Ant.(uV):"]=df["L.Tib.Ant.(uV):"]*100/L_Tib
    df["R.Tib.Ant.(uV):"]=df["R.Tib.Ant.(uV):"]*100/R_Tib
    df["L.Med. Gastro(uV):"]=df["L.Med. Gastro(uV):"]*100/L_Gas
    df["R.Med. Gastro(uV):"]=df["R.Med. Gastro(uV):"]*100/R_Gas
    
    new_file = 'Normalization_phase3_1/' + file.replace('phase3_1_nom\\', '')
    df.to_csv(new_file, index = None) 

#変数初期化
L_Bic = 0
R_Bic = 0
L_Tri = 0
R_Tri = 0
L_Vlo = 0
R_Vlo = 0
L_Rec = 0
R_Rec = 0
L_Tib = 0
R_Tib = 0
L_Gas = 0
R_Gas = 0

files = glob.glob("phase3_2/*.csv")

for file in files:
    df = pd.read_csv(file)
    df = df.abs()
    #試行数で割った平均を足していく
    L_Bic = L_Bic + df["L.Biceps Br.(uV):"].mean()/n
    R_Bic = R_Bic + df["R.Biceps Br.(uV):"].mean()/n
    L_Tri = L_Tri + df["L.Med. Triceps(uV):"].mean()/n
    R_Tri = R_Tri + df["R.Med. Triceps(uV):"].mean()/n
    L_Vlo = L_Vlo + df["L.Vlo(uV):"].mean()/n
    R_Vlo = R_Vlo + df["R.Vlo(uV):"].mean()/n
    L_Rec = L_Rec + df["L.Rectus Fem.(uV):"].mean()/n
    R_Rec = R_Rec + df["R.Rectus Fem.(uV):"].mean()/n
    L_Tib = L_Tib + df["L.Tib.Ant.(uV):"].mean()/n
    R_Tib = R_Tib + df["R.Tib.Ant.(uV):"].mean()/n
    L_Gas = L_Gas + df["L.Med. Gastro(uV):"].mean()/n
    R_Gas = R_Gas + df["R.Med. Gastro(uV):"].mean()/n

print("第3_2相処理中...")
files = glob.glob("phase3_2_nom/*.csv")

for file in tqdm(files):
    df = pd.read_csv(file)
    df = df.abs()

    df["L.Biceps Br.(uV):"]=df["L.Biceps Br.(uV):"]*100/L_Bic
    df["R.Biceps Br.(uV):"]=df["R.Biceps Br.(uV):"]*100/R_Bic
    df["L.Med. Triceps(uV):"]=df["L.Med. Triceps(uV):"]*100/L_Tri
    df["R.Med. Triceps(uV):"]=df["R.Med. Triceps(uV):"]*100/R_Tri
    df["L.Vlo(uV):"]=df["L.Vlo(uV):"]*100/L_Vlo
    df["R.Vlo(uV):"]=df["R.Vlo(uV):"]*100/R_Vlo
    df["L.Rectus Fem.(uV):"]=df["L.Rectus Fem.(uV):"]*100/L_Rec
    df["R.Rectus Fem.(uV):"]=df["R.Rectus Fem.(uV):"]*100/R_Rec
    df["L.Tib.Ant.(uV):"]=df["L.Tib.Ant.(uV):"]*100/L_Tib
    df["R.Tib.Ant.(uV):"]=df["R.Tib.Ant.(uV):"]*100/R_Tib
    df["L.Med. Gastro(uV):"]=df["L.Med. Gastro(uV):"]*100/L_Gas
    df["R.Med. Gastro(uV):"]=df["R.Med. Gastro(uV):"]*100/R_Gas
    
    new_file = 'Normalization_phase3_2/' + file.replace('phase3_2_nom\\', '')
    df.to_csv(new_file, index = None) 

#変数初期化
L_Bic = 0
R_Bic = 0
L_Tri = 0
R_Tri = 0
L_Vlo = 0
R_Vlo = 0
L_Rec = 0
R_Rec = 0
L_Tib = 0
R_Tib = 0
L_Gas = 0
R_Gas = 0

files = glob.glob("phase3_3/*.csv")

for file in files:
    df = pd.read_csv(file)
    df = df.abs()
    #試行数で割った平均を足していく
    L_Bic = L_Bic + df["L.Biceps Br.(uV):"].mean()/n
    R_Bic = R_Bic + df["R.Biceps Br.(uV):"].mean()/n
    L_Tri = L_Tri + df["L.Med. Triceps(uV):"].mean()/n
    R_Tri = R_Tri + df["R.Med. Triceps(uV):"].mean()/n
    L_Vlo = L_Vlo + df["L.Vlo(uV):"].mean()/n
    R_Vlo = R_Vlo + df["R.Vlo(uV):"].mean()/n
    L_Rec = L_Rec + df["L.Rectus Fem.(uV):"].mean()/n
    R_Rec = R_Rec + df["R.Rectus Fem.(uV):"].mean()/n
    L_Tib = L_Tib + df["L.Tib.Ant.(uV):"].mean()/n
    R_Tib = R_Tib + df["R.Tib.Ant.(uV):"].mean()/n
    L_Gas = L_Gas + df["L.Med. Gastro(uV):"].mean()/n
    R_Gas = R_Gas + df["R.Med. Gastro(uV):"].mean()/n

print("第3_3相処理中...")
files = glob.glob("phase3_3_nom/*.csv")

for file in tqdm(files):
    df = pd.read_csv(file)
    df = df.abs()

    df["L.Biceps Br.(uV):"]=df["L.Biceps Br.(uV):"]*100/L_Bic
    df["R.Biceps Br.(uV):"]=df["R.Biceps Br.(uV):"]*100/R_Bic
    df["L.Med. Triceps(uV):"]=df["L.Med. Triceps(uV):"]*100/L_Tri
    df["R.Med. Triceps(uV):"]=df["R.Med. Triceps(uV):"]*100/R_Tri
    df["L.Vlo(uV):"]=df["L.Vlo(uV):"]*100/L_Vlo
    df["R.Vlo(uV):"]=df["R.Vlo(uV):"]*100/R_Vlo
    df["L.Rectus Fem.(uV):"]=df["L.Rectus Fem.(uV):"]*100/L_Rec
    df["R.Rectus Fem.(uV):"]=df["R.Rectus Fem.(uV):"]*100/R_Rec
    df["L.Tib.Ant.(uV):"]=df["L.Tib.Ant.(uV):"]*100/L_Tib
    df["R.Tib.Ant.(uV):"]=df["R.Tib.Ant.(uV):"]*100/R_Tib
    df["L.Med. Gastro(uV):"]=df["L.Med. Gastro(uV):"]*100/L_Gas
    df["R.Med. Gastro(uV):"]=df["R.Med. Gastro(uV):"]*100/R_Gas
    
    new_file = 'Normalization_phase3_3/' + file.replace('phase3_3_nom\\', '')
    df.to_csv(new_file, index = None) 

#変数初期化
L_Bic = 0
R_Bic = 0
L_Tri = 0
R_Tri = 0
L_Vlo = 0
R_Vlo = 0
L_Rec = 0
R_Rec = 0
L_Tib = 0
R_Tib = 0
L_Gas = 0
R_Gas = 0

files = glob.glob("phase3_4/*.csv")

for file in files:
    df = pd.read_csv(file)
    df = df.abs()
    #試行数で割った平均を足していく
    L_Bic = L_Bic + df["L.Biceps Br.(uV):"].mean()/n
    R_Bic = R_Bic + df["R.Biceps Br.(uV):"].mean()/n
    L_Tri = L_Tri + df["L.Med. Triceps(uV):"].mean()/n
    R_Tri = R_Tri + df["R.Med. Triceps(uV):"].mean()/n
    L_Vlo = L_Vlo + df["L.Vlo(uV):"].mean()/n
    R_Vlo = R_Vlo + df["R.Vlo(uV):"].mean()/n
    L_Rec = L_Rec + df["L.Rectus Fem.(uV):"].mean()/n
    R_Rec = R_Rec + df["R.Rectus Fem.(uV):"].mean()/n
    L_Tib = L_Tib + df["L.Tib.Ant.(uV):"].mean()/n
    R_Tib = R_Tib + df["R.Tib.Ant.(uV):"].mean()/n
    L_Gas = L_Gas + df["L.Med. Gastro(uV):"].mean()/n
    R_Gas = R_Gas + df["R.Med. Gastro(uV):"].mean()/n

print("第3_4相処理中...")
files = glob.glob("phase3_4_nom/*.csv")

for file in tqdm(files):
    df = pd.read_csv(file)
    df = df.abs()

    df["L.Biceps Br.(uV):"]=df["L.Biceps Br.(uV):"]*100/L_Bic
    df["R.Biceps Br.(uV):"]=df["R.Biceps Br.(uV):"]*100/R_Bic
    df["L.Med. Triceps(uV):"]=df["L.Med. Triceps(uV):"]*100/L_Tri
    df["R.Med. Triceps(uV):"]=df["R.Med. Triceps(uV):"]*100/R_Tri
    df["L.Vlo(uV):"]=df["L.Vlo(uV):"]*100/L_Vlo
    df["R.Vlo(uV):"]=df["R.Vlo(uV):"]*100/R_Vlo
    df["L.Rectus Fem.(uV):"]=df["L.Rectus Fem.(uV):"]*100/L_Rec
    df["R.Rectus Fem.(uV):"]=df["R.Rectus Fem.(uV):"]*100/R_Rec
    df["L.Tib.Ant.(uV):"]=df["L.Tib.Ant.(uV):"]*100/L_Tib
    df["R.Tib.Ant.(uV):"]=df["R.Tib.Ant.(uV):"]*100/R_Tib
    df["L.Med. Gastro(uV):"]=df["L.Med. Gastro(uV):"]*100/L_Gas
    df["R.Med. Gastro(uV):"]=df["R.Med. Gastro(uV):"]*100/R_Gas

    new_file = 'Normalization_phase3_4/' + file.replace('phase3_4_nom\\', '')
    df.to_csv(new_file, index = None) 
print("終了")    