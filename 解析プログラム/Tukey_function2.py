#データ数違うときに使用
# 第1引数:データをタプルで, 第2引数:名称のリスト

def tukey_hsd( ind, args ):
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    import numpy as np
    import pandas as pd
    data_arr = np.hstack( args )
    ind_arr = np.array([])
    for x in range(len(args)):
      ind_arr = np.append(ind_arr, np.repeat(ind[x], len(args[x])))

    result = pairwise_tukeyhsd(data_arr,ind_arr)
    df = pd.DataFrame(data = result._results_table.data[1:], columns=result._results_table.data[0])
    return df