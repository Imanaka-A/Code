
#速度，加速度
#中心差分法

import pandas as pd
import glob
from matplotlib import pyplot
from tqdm import trange, tqdm
import os

os.makedirs("CoM_velocity", exist_ok = True)
os.makedirs("CoM_acceleration", exist_ok = True)

#処理したいフォルダの名前
filename = "CoM"

SAMPLING_RATE = 200 #[Hz]
dt = 1 / SAMPLING_RATE

files = glob.glob(filename + "/*.csv")

for file in tqdm(files):
    data = pd.read_csv(file)

    ####################### 速度 ####################################
    cdiff = (data.shift(-1) - data.shift(1)) / 2 / dt
    
    #print(cdiff)

    #時間オフセット用
    offset_times = []
    for step in range(len(data)):
        offset_times.append(step/SAMPLING_RATE)
    #オフセット時間をデータフレームに追加
    cdiff.insert(0, "Time", offset_times, True)

    new_file = "CoM_velocity/" + file.replace("CoM\\", "")
    cdiff.to_csv(new_file, index = None)

    ####################### 加速度 ###################################
    cdiff_a = (cdiff.shift(-1) - cdiff.shift(1)) / 2 / dt

    #print(cdiff_a)

    #オフセット時間をデータフレームに追加
    cdiff_a.insert(0, "Time", offset_times, True)    

    new_file = "CoM_acceleration/" + file.replace("CoM\\", "")
    cdiff_a.to_csv(new_file, index = None)  

    """
    fig1 = pyplot.figure()
    pyplot.plot(data.Time,cdiff.CoM_z)
    pyplot.xlim(0,7)
    #pyplot.ylim(0.8,0.9)
    pyplot.xlabel("Time(s)")
    pyplot.ylabel("Angular velocity(rad/s)")
    pyplot.rcParams["font.family"] = "Times New Romen"
    axis_array = np.arange(0,7,step=1)
    pyplot.xticks(axis_array)
    img1 = fig1.savefig("tmp_tem/tmp2.png")
    """
