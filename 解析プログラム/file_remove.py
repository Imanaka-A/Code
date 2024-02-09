#解析用csvのために不要な試行数を削除する

import os
import glob
from natsort import natsorted
from tqdm import trange, tqdm

#被験者名
name = "i"

#不要な試行
del_1 = str(2)
del_2 = str(4)
del_3 = str(4)
del_4 = str(3)
del_5 = str(5)
del_6 = str(1)
del_7 = str(3)
del_8 = str(2)
del_9 = str(5)
del_10 =str(3)

file_position = glob.glob("position/*.csv")
file_grf = glob.glob("grf/*.csv")
file_emg = glob.glob("emg/*.csv")
file_Robot = glob.glob("Robot/*.csv")

print("開始")
print("position")
for file in natsorted(file_position):
    try:
        os.remove("position/" + name + "_" + "1" + "_" + del_1 + ".csv" )
        os.remove("position/" + name + "_" + "2" + "_" + del_2 + ".csv" )
        os.remove("position/" + name + "_" + "3" + "_" + del_3 + ".csv" )
        os.remove("position/" + name + "_" + "4" + "_" + del_4 + ".csv" )
        os.remove("position/" + name + "_" + "5" + "_" + del_5 + ".csv" )
        os.remove("position/" + name + "_" + "6" + "_" + del_6 + ".csv" )
        os.remove("position/" + name + "_" + "7" + "_" + del_7 + ".csv" )
        os.remove("position/" + name + "_" + "8" + "_" + del_8 + ".csv" )
        os.remove("position/" + name + "_" + "9" + "_" + del_9 + ".csv" )
        os.remove("position/" + name + "_" + "10" + "_" + del_10 + ".csv" )
    except:
        pass

print("grf")
for file in natsorted(file_grf):
    try:
        os.remove("grf/" + name + "_" + "1" + "_" + del_1 + ".csv" )
        os.remove("grf/" + name + "_" + "2" + "_" + del_2 + ".csv" )
        os.remove("grf/" + name + "_" + "3" + "_" + del_3 + ".csv" )
        os.remove("grf/" + name + "_" + "4" + "_" + del_4 + ".csv" )
        os.remove("grf/" + name + "_" + "5" + "_" + del_5 + ".csv" )
        os.remove("grf/" + name + "_" + "6" + "_" + del_6 + ".csv" )
        os.remove("grf/" + name + "_" + "7" + "_" + del_7 + ".csv" )
        os.remove("grf/" + name + "_" + "8" + "_" + del_8 + ".csv" )
        os.remove("grf/" + name + "_" + "9" + "_" + del_9 + ".csv" )
        os.remove("grf/" + name + "_" + "10" + "_" + del_10 + ".csv" )
    except:
        pass

print("emg")
for file in natsorted(file_emg):
    try:
        os.remove("emg/" + name + "_" + "1" + "_" + del_1 + ".csv" )
        os.remove("emg/" + name + "_" + "2" + "_" + del_2 + ".csv" )
        os.remove("emg/" + name + "_" + "3" + "_" + del_3 + ".csv" )
        os.remove("emg/" + name + "_" + "4" + "_" + del_4 + ".csv" )
        os.remove("emg/" + name + "_" + "5" + "_" + del_5 + ".csv" )
        os.remove("emg/" + name + "_" + "6" + "_" + del_6 + ".csv" )
        os.remove("emg/" + name + "_" + "7" + "_" + del_7 + ".csv" )
        os.remove("emg/" + name + "_" + "8" + "_" + del_8 + ".csv" )
        os.remove("emg/" + name + "_" + "9" + "_" + del_9 + ".csv" )
        os.remove("emg/" + name + "_" + "10" + "_" + del_10 + ".csv" )
    except:
        pass

print("Robot")
for file in natsorted(file_Robot):
    try:
        os.remove("Robot/" + name + "_" + "1" + "_" + del_1 + ".csv" )
        os.remove("Robot/" + name + "_" + "2" + "_" + del_2 + ".csv" )
        os.remove("Robot/" + name + "_" + "3" + "_" + del_3 + ".csv" )
        os.remove("Robot/" + name + "_" + "4" + "_" + del_4 + ".csv" )
        os.remove("Robot/" + name + "_" + "5" + "_" + del_5 + ".csv" )
        os.remove("Robot/" + name + "_" + "6" + "_" + del_6 + ".csv" )
        os.remove("Robot/" + name + "_" + "7" + "_" + del_7 + ".csv" )
        os.remove("Robot/" + name + "_" + "8" + "_" + del_8 + ".csv" )
        os.remove("Robot/" + name + "_" + "9" + "_" + del_9 + ".csv" )
        os.remove("Robot/" + name + "_" + "10" + "_" + del_10 + ".csv" )
    except:
        pass

print("終了")