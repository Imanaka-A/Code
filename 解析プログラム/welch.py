#welchのt検定

import pandas as pd
import numpy as np
import scipy.stats as st

#適宜選択
part = "R_ankle"
phase = "phase1"
condition_A = "condition7"
condition_B = "condition10"

file_A =pd.read_excel("analysis/angle/ankle/" + phase + "/" + part + "_" + phase + "_" + condition_A + ".xlsx")
file_B = pd.read_excel("analysis/angle/ankle/" + phase + "/" + part + "_" + phase + "_" + condition_B + ".xlsx")

print("比較..", condition_A + condition_B)
for i in range(0, 10):
    value_A = file_A.iloc[2:,i] #読込は変更
    value_A = value_A.dropna(how = "any", axis = 0)
    value_A = value_A.to_list()
    
    value_B = file_B.iloc[2:,i] #読込は変更
    value_B = value_B.dropna(how = "any", axis = 0)
    value_B = value_B.to_list()
    
    p_value_welch =st.ttest_ind(value_A, value_B, equal_var = False)

    print("結果...", str((i + 1) * 10), "%", p_value_welch)