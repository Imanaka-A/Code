# 関節角度

import pandas as pd
import numpy as np
import glob
from matplotlib import pyplot
import os
from tqdm import trange, tqdm

os.makedirs("angle/", exist_ok=True)

files = glob.glob("phase/position/*.csv")

for file in tqdm(files):
    df = pd.read_csv(file)

    R_asis_x = df["Body_RASIS_Position_X"]
    R_asis_y = df["Body_RASIS_Position_Y"]
    R_asis_z = df["Body_RASIS_Position_Z"]
    L_asis_x = df["Body_LASIS_Position_X"]
    L_asis_y = df["Body_LASIS_Position_Y"]
    L_asis_z = df["Body_LASIS_Position_Z"]
    sacral_x = df["Body_VSacral_Position_X"]
    sacral_y = df["Body_VSacral_Position_Y"]
    sacral_z = df["Body_VSacral_Position_Z"]
    R_GTOF_x = df["Body_RTrochanter_Position_X"]
    R_GTOF_y = df["Body_RTrochanter_Position_Y"]
    R_GTOF_z = df["Body_RTrochanter_Position_Z"]
    L_GTOF_x = df["Body_LTrochanter_Position_X"]
    L_GTOF_y = df["Body_LTrochanter_Position_Y"]
    L_GTOF_z = df["Body_LTrochanter_Position_Z"]
    R_knee_x = (df["Body_RKnee_Position_X"] + df["Body_RKneeMedial_Position_X"])/2
    R_knee_y = (df["Body_RKnee_Position_Y"] + df["Body_RKneeMedial_Position_Y"])/2
    R_knee_z = (df["Body_RKnee_Position_Z"] + df["Body_RKneeMedial_Position_Z"])/2
    L_knee_x = (df["Body_LKnee_Position_X"] + df["Body_LKneeMedial_Position_X"])/2
    L_knee_y = (df["Body_LKnee_Position_Y"] + df["Body_LKneeMedial_Position_Y"])/2
    L_knee_z = (df["Body_LKnee_Position_Z"] + df["Body_LKneeMedial_Position_Z"])/2
    R_ankle_x = (df["Body_RAnkle_Position_X"] + df["Body_RAnkleMedial_Position_X"])/2
    R_ankle_y = (df["Body_RAnkle_Position_Y"] + df["Body_RAnkleMedial_Position_Y"])/2
    R_ankle_z = (df["Body_RAnkle_Position_Z"] + df["Body_RAnkleMedial_Position_Z"])/2
    L_ankle_x = (df["Body_LAnkle_Position_X"] + df["Body_LAnkleMedial_Position_X"])/2
    L_ankle_y = (df["Body_LAnkle_Position_Y"] + df["Body_LAnkleMedial_Position_Y"])/2
    L_ankle_z = (df["Body_LAnkle_Position_Z"] + df["Body_LAnkleMedial_Position_Z"])/2
    R_toe_x = df["Body_RToe_Position_X"]
    R_toe_y = df["Body_RToe_Position_Y"]
    R_toe_z = df["Body_RToe_Position_Z"]
    L_toe_x = df["Body_LToe_Position_X"]
    L_toe_y = df["Body_LToe_Position_Y"]
    L_toe_z = df["Body_LToe_Position_Z"]

    #股関節
    #右
    #x-y
    crotch_innerproduct_xy = (sacral_x - R_GTOF_x)*(R_knee_x - R_GTOF_x) + (sacral_y - R_GTOF_y)*(R_knee_y - R_GTOF_y)
    crotch_size_xy = np.sqrt((sacral_x - R_GTOF_x)**2+(sacral_y - R_GTOF_y)**2)*np.sqrt((R_knee_x - R_GTOF_x)**2+(R_knee_y - R_GTOF_y)**2)

    crotch_theta_xy = np.arccos(crotch_innerproduct_xy/crotch_size_xy)
    crotch_degree_xy = crotch_theta_xy*180/np.pi

    #y-z
    crotch_innerproduct_yz = (sacral_y - R_GTOF_y)*(R_knee_y - R_GTOF_y) + (sacral_z - R_GTOF_z)*(R_knee_z - R_GTOF_z)
    crotch_size_yz = np.sqrt((sacral_z - R_GTOF_z)**2 + (sacral_y - R_GTOF_y)**2)*np.sqrt((R_knee_z - R_GTOF_z)**2 + (R_knee_y-R_GTOF_y)**2)

    crotch_theta_yz = np.arccos(crotch_innerproduct_yz/crotch_size_yz)
    crotch_degree_yz = crotch_theta_yz *180/np.pi

    #z-x
    crotch_innerproduct_zx = (sacral_x - R_GTOF_x)*(R_knee_x - R_GTOF_x) + (sacral_z - R_GTOF_z)*(R_knee_z - R_GTOF_z)
    crotch_size_zx = np.sqrt((sacral_z - R_GTOF_z)**2 + (sacral_x - R_GTOF_x)**2)*np.sqrt((R_knee_z - R_GTOF_z)**2 + (R_knee_x - R_GTOF_x)**2)

    crotch_theta_zx = np.arccos(crotch_innerproduct_zx/crotch_size_zx)
    crotch_degree_zx = crotch_theta_zx *180/np.pi

    #左
    #x-y
    L_crotch_innerproduct_xy = (sacral_x - L_GTOF_x)*(L_knee_x - L_GTOF_x) + (sacral_y - L_GTOF_y)*(L_knee_y - L_GTOF_y)
    L_crotch_size_xy =np.sqrt((sacral_x - L_GTOF_x)**2 + (sacral_y - L_GTOF_y)**2)*np.sqrt((L_knee_x - L_GTOF_x)**2 + (L_knee_y - L_GTOF_y)**2)

    L_crotch_theta_xy = np.arccos(L_crotch_innerproduct_xy/L_crotch_size_xy)
    L_crotch_degree_xy = L_crotch_theta_xy*180/np.pi

    #y-z
    L_crotch_innerproduct_yz = (sacral_y-L_GTOF_y)*(L_knee_y-L_GTOF_y) + (sacral_z-L_GTOF_z)*(L_knee_z-L_GTOF_z)
    L_crotch_size_yz =np.sqrt((sacral_z-L_GTOF_z)**2+(sacral_y-L_GTOF_y)**2)*np.sqrt((L_knee_z-L_GTOF_z)**2+(L_knee_y-L_GTOF_y)**2)

    L_crotch_theta_yz = np.arccos(L_crotch_innerproduct_yz/L_crotch_size_yz)
    L_crotch_degree_yz = L_crotch_theta_yz *180/np.pi
    
    #z-x
    L_crotch_innerproduct_zx = (sacral_x-L_GTOF_x)*(L_knee_x-L_GTOF_x) + (sacral_z-L_GTOF_z)*(L_knee_z-L_GTOF_z)
    L_crotch_size_zx =np.sqrt((sacral_z-L_GTOF_z)**2+(sacral_x-L_GTOF_x)**2)*np.sqrt((L_knee_z-L_GTOF_z)**2+(L_knee_x-L_GTOF_x)**2)

    L_crotch_theta_zx = np.arccos(L_crotch_innerproduct_zx/L_crotch_size_zx)
    L_crotch_degree_zx = L_crotch_theta_zx *180/np.pi

    #膝関節
    #右
    #x-y
    knee_innerproduct_xy = (R_GTOF_x-R_knee_x)*(R_ankle_x-R_knee_x) + (R_GTOF_y-R_knee_y)*(R_ankle_y-R_knee_y) 
    knee_size_xy =np.sqrt((R_GTOF_x-R_knee_x)**2+(R_GTOF_y-R_knee_y)**2)*np.sqrt((R_ankle_x-R_knee_x)**2+(R_ankle_y-R_knee_y)**2)

    knee_theta_xy = np.arccos(knee_innerproduct_xy/knee_size_xy)
    knee_degree_xy = knee_theta_xy*180/np.pi

    #y-z
    knee_innerproduct_yz = (R_GTOF_y-R_knee_y)*(R_ankle_y-R_knee_y) + (R_GTOF_z-R_knee_z)*(R_ankle_z-R_knee_z) 
    knee_size_yz =np.sqrt((R_GTOF_y-R_knee_y)**2+(R_GTOF_z-R_knee_z)**2)*np.sqrt((R_ankle_y-R_knee_y)**2+(R_ankle_z-R_knee_z)**2)

    knee_theta_yz = np.arccos(knee_innerproduct_yz/knee_size_yz)
    knee_degree_yz = knee_theta_yz*180/np.pi

    #z-x
    knee_innerproduct_zx = (R_GTOF_x-R_knee_x)*(R_ankle_x-R_knee_x) + (R_GTOF_z-R_knee_z)*(R_ankle_z-R_knee_z) 
    knee_size_zx =np.sqrt((R_GTOF_x-R_knee_x)**2+(R_GTOF_z-R_knee_z)**2)*np.sqrt((R_ankle_x-R_knee_x)**2+(R_ankle_z-R_knee_z)**2)

    knee_theta_zx = np.arccos(knee_innerproduct_zx/knee_size_zx)
    knee_degree_zx = knee_theta_zx*180/np.pi

    #左
    #x-y
    L_knee_innerproduct_xy = (L_GTOF_x-L_knee_x)*(L_ankle_x-L_knee_x) + (L_GTOF_y-L_knee_y)*(L_ankle_y-L_knee_y) 
    L_knee_size_xy =np.sqrt((L_GTOF_x-L_knee_x)**2+(L_GTOF_y-L_knee_y)**2)*np.sqrt((L_ankle_x-L_knee_x)**2+(L_ankle_y-L_knee_y)**2)

    L_knee_theta_xy = np.arccos(L_knee_innerproduct_xy/L_knee_size_xy)
    L_knee_degree_xy = L_knee_theta_xy*180/np.pi

    #y-z
    L_knee_innerproduct_yz = (L_GTOF_y-L_knee_y)*(L_ankle_y-L_knee_y) + (L_GTOF_z-L_knee_z)*(L_ankle_z-L_knee_z) 
    L_knee_size_yz =np.sqrt((L_GTOF_y-L_knee_y)**2+(L_GTOF_z-L_knee_z)**2)*np.sqrt((L_ankle_y-L_knee_y)**2+(L_ankle_z-L_knee_z)**2)

    L_knee_theta_yz = np.arccos(L_knee_innerproduct_yz/L_knee_size_yz)
    L_knee_degree_yz = L_knee_theta_yz*180/np.pi

    #z-x
    L_knee_innerproduct_zx = (L_GTOF_x-L_knee_x)*(L_ankle_x-L_knee_x) + (L_GTOF_z-L_knee_z)*(L_ankle_z-L_knee_z) 
    L_knee_size_zx =np.sqrt((L_GTOF_x-L_knee_x)**2+(L_GTOF_z-L_knee_z)**2)*np.sqrt((L_ankle_x-L_knee_x)**2+(L_ankle_z-L_knee_z)**2)

    L_knee_theta_zx = np.arccos(L_knee_innerproduct_zx/L_knee_size_zx)
    L_knee_degree_zx = L_knee_theta_zx*180/np.pi

    #足関節
    #右
    #x-y
    ankle_innerproduct_xy = (R_toe_x-R_ankle_x)*(R_knee_x-R_ankle_x) + (R_toe_y-R_ankle_y)*(R_knee_y-R_ankle_y) 
    ankle_size_xy =np.sqrt((R_toe_x-R_ankle_x)**2+(R_toe_y-R_ankle_y)**2)*np.sqrt((R_knee_x-R_ankle_x)**2+(R_knee_y-R_ankle_y)**2)

    ankle_theta_xy = np.arccos(ankle_innerproduct_xy/ankle_size_xy)
    ankle_degree_xy = ankle_theta_xy*180/np.pi

    #y-z
    ankle_innerproduct_yz = (R_toe_z-R_ankle_z)*(R_knee_z-R_ankle_z) + (R_toe_y-R_ankle_y)*(R_knee_y-R_ankle_y) 
    ankle_size_yz =np.sqrt((R_toe_z-R_ankle_z)**2+(R_toe_y-R_ankle_y)**2)*np.sqrt((R_knee_z-R_ankle_z)**2+(R_knee_y-R_ankle_y)**2)

    ankle_theta_yz = np.arccos(ankle_innerproduct_yz/ankle_size_yz)
    ankle_degree_yz = ankle_theta_yz*180/np.pi

    #z-x
    ankle_innerproduct_zx = (R_toe_z-R_ankle_z)*(R_knee_z-R_ankle_z) + (R_toe_x-R_ankle_x)*(R_knee_x-R_ankle_x) 
    ankle_size_zx =np.sqrt((R_toe_z-R_ankle_z)**2+(R_toe_x-R_ankle_x)**2)*np.sqrt((R_knee_z-R_ankle_z)**2+(R_knee_x-R_ankle_x)**2)

    ankle_theta_zx = np.arccos(ankle_innerproduct_zx/ankle_size_zx)
    ankle_degree_zx = ankle_theta_zx*180/np.pi

    #左
    #x-y
    L_ankle_innerproduct_xy = (L_toe_x-L_ankle_x)*(L_knee_x-L_ankle_x) + (L_toe_y-L_ankle_y)*(L_knee_y-L_ankle_y) 
    L_ankle_size_xy =np.sqrt((L_toe_x-L_ankle_x)**2+(L_toe_y-L_ankle_y)**2)*np.sqrt((L_knee_x-L_ankle_x)**2+(L_knee_y-L_ankle_y)**2)

    L_ankle_theta_xy = np.arccos(L_ankle_innerproduct_xy/L_ankle_size_xy)
    L_ankle_degree_xy = L_ankle_theta_xy*180/np.pi

    #y-z
    L_ankle_innerproduct_yz = (L_toe_z-L_ankle_z)*(L_knee_z-L_ankle_z) + (L_toe_y-L_ankle_y)*(L_knee_y-L_ankle_y) 
    L_ankle_size_yz =np.sqrt((L_toe_z-L_ankle_z)**2+(L_toe_y-L_ankle_y)**2)*np.sqrt((L_knee_z-L_ankle_z)**2+(L_knee_y-L_ankle_y)**2)

    L_ankle_theta_yz = np.arccos(L_ankle_innerproduct_yz/L_ankle_size_yz)
    L_ankle_degree_yz = L_ankle_theta_yz*180/np.pi

    #z-x
    L_ankle_innerproduct_zx = (L_toe_z-L_ankle_z)*(L_knee_z-L_ankle_z) + (L_toe_x-L_ankle_x)*(L_knee_x-L_ankle_x) 
    L_ankle_size_zx =np.sqrt((L_toe_z-L_ankle_z)**2+(L_toe_x-L_ankle_x)**2)*np.sqrt((L_knee_z-L_ankle_z)**2+(L_knee_x-L_ankle_x)**2)

    L_ankle_theta_zx = np.arccos(L_ankle_innerproduct_zx/L_ankle_size_zx)
    L_ankle_degree_zx = L_ankle_theta_zx*180/np.pi
    """
    fig1 = pyplot.figure()
    pyplot.plot(df.Time,180-knee_degree_yz)
    pyplot.xlim(0,7)
    axis_array = np.arange(0,7,step=1)
    pyplot.xticks(axis_array)
    img1 = fig1.savefig("tmp_tem/tmp1.png")
    """

    df1 = pd.DataFrame({"Time":df["Time"],
                        "R_crotch_degree_xy":crotch_degree_xy,
                        "R_crotch_degree_yz":crotch_degree_yz,
                        "R_crotch_degree_zx":crotch_degree_zx,
                        "L_crotch_degree_xy":L_crotch_degree_xy,
                        "L_crotch_degree_yz":L_crotch_degree_yz,
                        "L_crotch_degree_zx":L_crotch_degree_zx,
                        "R_knee_degree_xy":knee_degree_xy,
                        "R_knee_degree_yz":knee_degree_yz,
                        "R_knee_degree_zx":knee_degree_zx,
                        "L_knee_degree_xy":L_knee_degree_xy,
                        "L_knee_degree_yz":L_knee_degree_yz,
                        "L_knee_degree_zx":L_knee_degree_zx,
                        "R_ankle_degree_xy":ankle_degree_xy,
                        "R_ankle_degree_yz":ankle_degree_yz,
                        "R_ankle_degree_zx":ankle_degree_zx,
                        "L_ankle_degree_xy":L_ankle_degree_xy,
                        "L_ankle_degree_yz":L_ankle_degree_yz,
                        "L_ankle_degree_zx":L_ankle_degree_zx})

    time = df["Time"]
    """
    #ラジアン表記に変換
    df1 = df1*np.pi/180
    df1["Time"] = df1["Time"]*180/np.pi
    df1.Time = df1.Time.round(2)"""
    
    file_name = file.replace("phase/position\\", "")
    new_file = "angle/" + file_name
    df1.to_csv(new_file, index = None)