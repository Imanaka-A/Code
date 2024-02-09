#Tukey-Kramer検定
#GRFの平均を検定

import os
import openpyxl
import pandas as pd
import numpy as np
import glob 
from tqdm import trange, tqdm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#項目，相，条件入力
phase = "phase1"
condition_A = "condition4"
condition_B = "condition7"
condition_C = "condition10"

os.makedirs("analysis/tukey/GRF/" + phase + "/", exist_ok = True)

file_A = glob.glob("GRF/" + phase + "/" + condition_A + "/*.csv")
file_B = glob.glob("GRF/" + phase + "/" + condition_B + "/*.csv")
file_C = glob.glob("GRF/" + phase + "/" + condition_C + "/*.csv")

list_A =[]
list_B =[]
list_C =[]

wbname = "average" + "_" + condition_A + condition_B + condition_C + ".xlsx"
wb = openpyxl.Workbook()
wb.save("analysis/tukey/GRF/" + phase + "/" + wbname)

#print("比較..", condition_A + condition_B + condition_C)

for file in tqdm(file_A):
    df = pd.read_csv(file)
    list = df["L_Sum"] + df["R_Sum"]

    list_A.extend(list)

for file in tqdm(file_B):
    df = pd.read_csv(file)
    list = df["L_Sum"] + df["R_Sum"]

    list_B.extend(list)

for file in tqdm(file_C):
    df = pd.read_csv(file)
    list = df["L_Sum"] + df["R_Sum"]

    list_C.extend(list)

list_A = np.array(list_A)    
list_B = np.array(list_B)
list_C = np.array(list_C)

count_A = np.repeat([condition_A], len(list_A))
count_B = np.repeat([condition_B], len(list_B))
count_C = np.repeat([condition_C], len(list_C))

value = np.hstack((list_A, list_B, list_C))
count = np.hstack((count_A, count_B, count_C))

tukey = pairwise_tukeyhsd(value, count)

tukey = pd.DataFrame(data = tukey._results_table.data[1:], columns = tukey._results_table.data[0])

with pd.ExcelWriter("analysis/tukey/GRF/" + phase + "/" + wbname, mode = "a") as writer:
    tukey.to_excel(writer)