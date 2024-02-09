
# 第1引数:データをタプルで, 第2引数:名称のリスト, 第3引数: データの個数

def tukey_hsd( lst, ind, n ):
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    import numpy as np
    import pandas as pd
    data_arr = np.hstack( lst )
    ind_arr = np.repeat(ind, n)
    result = pairwise_tukeyhsd(data_arr,ind_arr)
    #print(result)
    df = pd.DataFrame(data=result._results_table.data[1:], columns=result._results_table.data[0])
    return df