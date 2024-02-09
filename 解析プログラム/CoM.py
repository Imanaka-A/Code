#重心位置算出プログラム(winter)

import pandas as pd
import numpy as np
import glob
from matplotlib import pyplot
from tqdm import trange, tqdm
import os
#import Butterworth_filter as fc

os.makedirs("CoM/", exist_ok = True)

#ファイル読みこみ
files = glob.glob("position/*.csv")

weight = 64 #[kg]


for file in tqdm(files):
    df = pd.read_csv(file)

    front_head_x = df["Body_FrontHead_Position_X"]
    front_head_y = df["Body_FrontHead_Position_Y"]
    front_head_z = df["Body_FrontHead_Position_Z"]
    rear_head_x = df["Body_RearHead_Position_X"]
    rear_head_y = df["Body_RearHead_Position_Y"]
    rear_head_z = df["Body_RearHead_Position_Z"]
    head_x = (front_head_x + rear_head_x)/2
    head_y = (front_head_y + rear_head_y)/2
    head_z = (front_head_z + rear_head_z)/2
    R_hand_x = df["Body_RHand_Position_X"]
    R_hand_y = df["Body_RHand_Position_Y"]
    R_hand_z = df["Body_RHand_Position_Z"]
    L_hand_x = df["Body_LHand_Position_X"]
    L_hand_y = df["Body_LHand_Position_Y"]
    L_hand_z = df["Body_LHand_Position_Z"]
    R_Radius_x = df["Body_RRadius_Position_X"]
    R_Radius_y = df["Body_RRadius_Position_Y"]
    R_Radius_z = df["Body_RRadius_Position_Z"]
    L_Radius_x = df["Body_LRadius_Position_X"]
    L_Radius_y = df["Body_LRadius_Position_Y"]
    L_Radius_z = df["Body_LRadius_Position_Z"]
    R_Ulna_x = df["Body_RUlna_Position_X"]
    R_Ulna_y = df["Body_RUlna_Position_Y"]
    R_Ulna_z = df["Body_RUlna_Position_Z"]
    L_Ulna_x = df["Body_LUlna_Position_X"]
    L_Ulna_y = df["Body_LUlna_Position_Y"]
    L_Ulna_z = df["Body_LUlna_Position_Z"]
    R_wrist_x = (R_Radius_x + R_Ulna_x)/2
    R_wrist_y = (R_Radius_y + R_Ulna_y)/2
    R_wrist_z = (R_Radius_z + R_Ulna_z)/2
    L_wrist_x = (L_Radius_x + L_Ulna_x)/2
    L_wrist_y = (L_Radius_y + L_Ulna_y)/2
    L_wrist_z = (L_Radius_z + L_Ulna_z)/2
    R_Elbow_x = (df["Body_RElbowMedial_Position_X"] + df["Body_RElbow_Position_X"])/2
    R_Elbow_y = (df["Body_RElbowMedial_Position_Y"] + df["Body_RElbow_Position_Y"])/2
    R_Elbow_z = (df["Body_RElbowMedial_Position_Z"] + df["Body_RElbow_Position_Z"])/2
    L_Elbow_x = (df["Body_LElbowMedial_Position_X"] + df["Body_LElbow_Position_X"])/2
    L_Elbow_y = (df["Body_LElbowMedial_Position_Y"] + df["Body_LElbow_Position_Y"])/2
    L_Elbow_z = (df["Body_LElbowMedial_Position_Z"] + df["Body_LElbow_Position_Z"])/2
    R_Shoulder_x = df["Body_RShoulder_Position_X"]
    R_Shoulder_y = df["Body_RShoulder_Position_Y"]
    R_Shoulder_z = df["Body_RShoulder_Position_Z"]
    L_Shoulder_x = df["Body_LShoulder_Position_X"]
    L_Shoulder_y = df["Body_LShoulder_Position_Y"]
    L_Shoulder_z = df["Body_LShoulder_Position_Z"]
    chest_x = (R_Shoulder_x + L_Shoulder_x)/2
    chest_y = (R_Shoulder_y + L_Shoulder_y)/2
    chest_z = (R_Shoulder_z + L_Shoulder_z)/2
    R_asis_x = df["Body_RASIS_Position_X"]
    R_asis_y = df["Body_RASIS_Position_Y"]
    R_asis_z = df["Body_RASIS_Position_Z"]
    L_asis_x = df["Body_LASIS_Position_X"]
    L_asis_y = df["Body_LASIS_Position_Y"]
    L_asis_z = df["Body_LASIS_Position_Z"]
    sacral_x = df["Body_VSacral_Position_X"]
    sacral_y = df["Body_VSacral_Position_Y"]
    sacral_z = df["Body_VSacral_Position_Z"]
    Pelvis_x = (R_asis_x + L_asis_x + sacral_x)/3
    Pelvis_y = (R_asis_y + L_asis_y + sacral_y)/3
    Pelvis_z = (R_asis_z + L_asis_z + sacral_z)/3
    R_GTOF_x = df["Body_RTrochanter_Position_X"]
    R_GTOF_y = df["Body_RTrochanter_Position_Y"]
    R_GTOF_z = df["Body_RTrochanter_Position_Z"]
    L_GTOF_x = df["Body_LTrochanter_Position_X"]
    L_GTOF_y = df["Body_LTrochanter_Position_Y"]
    L_GTOF_z = df["Body_LTrochanter_Position_Z"]
    R_knee_x = (df["Body_RKneeMedial_Position_X"] + df["Body_RKnee_Position_X"])/2
    R_knee_y = (df["Body_RKneeMedial_Position_Y"] + df["Body_RKnee_Position_Y"])/2
    R_knee_z = (df["Body_RKneeMedial_Position_Z"] + df["Body_RKnee_Position_Z"])/2
    L_knee_x = (df["Body_LKneeMedial_Position_X"] + df["Body_LKnee_Position_X"])/2
    L_knee_y = (df["Body_LKneeMedial_Position_Y"] + df["Body_LKnee_Position_Y"])/2
    L_knee_z = (df["Body_LKneeMedial_Position_Z"] + df["Body_LKnee_Position_Z"])/2
    R_ankle_x = (df["Body_RAnkleMedial_Position_X"] + df["Body_RAnkle_Position_X"])/2
    R_ankle_y = (df["Body_RAnkleMedial_Position_Y"] + df["Body_RAnkle_Position_Y"])/2
    R_ankle_z = (df["Body_RAnkleMedial_Position_Z"] + df["Body_RAnkle_Position_Z"])/2
    L_ankle_x = (df["Body_LAnkleMedial_Position_X"] + df["Body_LAnkle_Position_X"])/2
    L_ankle_y = (df["Body_LAnkleMedial_Position_Y"] + df["Body_LAnkle_Position_Y"])/2
    L_ankle_z = (df["Body_LAnkleMedial_Position_Z"] + df["Body_LAnkle_Position_Z"])/2
    R_toe_x = df["Body_RToe_Position_X"]
    R_toe_y = df["Body_RToe_Position_Y"]
    R_toe_z = df["Body_RToe_Position_Z"]
    L_toe_x = df["Body_LToe_Position_X"]
    L_toe_y = df["Body_LToe_Position_Y"]
    L_toe_z = df["Body_LToe_Position_Z"]

    #各節重心位置
    Rhand_x = 0.506*R_hand_x + 0.494*R_wrist_x
    Rhand_y = 0.506*R_hand_y + 0.494*R_wrist_y
    Rhand_z = 0.506*R_hand_z + 0.494*R_wrist_z
    Lhand_x = 0.506*L_hand_x + 0.494*L_wrist_x
    Lhand_y = 0.506*L_hand_y + 0.494*L_wrist_y
    Lhand_z = 0.506*L_hand_z + 0.494*L_wrist_z

    Rfarm_x = 0.430*R_wrist_x + 0.570*R_Elbow_x
    Rfarm_y = 0.430*R_wrist_y + 0.570*R_Elbow_y
    Rfarm_z = 0.430*R_wrist_z + 0.570*R_Elbow_z
    Lfarm_x = 0.430*L_wrist_x + 0.570*L_Elbow_x
    Lfarm_y = 0.430*L_wrist_y + 0.570*L_Elbow_y
    Lfarm_z = 0.430*L_wrist_z + 0.570*L_Elbow_z

    Ruarm_x = 0.436*R_Elbow_x + 0.564*R_Shoulder_x
    Ruarm_y = 0.436*R_Elbow_y + 0.564*R_Shoulder_y
    Ruarm_z = 0.436*R_Elbow_z + 0.564*R_Shoulder_z
    Luarm_x = 0.436*L_Elbow_x + 0.564*L_Shoulder_x
    Luarm_y = 0.436*L_Elbow_y + 0.564*L_Shoulder_y
    Luarm_z = 0.436*L_Elbow_z + 0.564*L_Shoulder_z

    Rfoot_x = 0.500*R_toe_x + 0.500*R_ankle_x
    Rfoot_y = 0.500*R_toe_y + 0.500*R_ankle_y
    Rfoot_z = 0.500*R_toe_z + 0.500*R_ankle_z
    Lfoot_x = 0.500*L_toe_x + 0.500*L_ankle_x
    Lfoot_y = 0.500*L_toe_y + 0.500*L_ankle_y
    Lfoot_z = 0.500*L_toe_z + 0.500*L_ankle_z

    Rtibia_x = 0.433*R_ankle_x + 0.567*R_knee_x
    Rtibia_y = 0.433*R_ankle_y + 0.567*R_knee_y
    Rtibia_z = 0.433*R_ankle_z + 0.567*R_knee_z
    Ltibia_x = 0.433*L_ankle_x + 0.567*L_knee_x
    Ltibia_y = 0.433*L_ankle_y + 0.567*L_knee_y
    Ltibia_z = 0.433*L_ankle_z + 0.567*L_knee_z

    Rfemur_x = 0.433*R_knee_x + 0.567*R_GTOF_x
    Rfemur_y = 0.433*R_knee_y + 0.567*R_GTOF_y
    Rfemur_z = 0.433*R_knee_z + 0.567*R_GTOF_z
    Lfemur_x = 0.433*L_knee_x + 0.567*L_GTOF_x
    Lfemur_y = 0.433*L_knee_y + 0.567*L_GTOF_y
    Lfemur_z = 0.433*L_knee_z + 0.567*L_GTOF_z

    Chest_x = chest_x/2 + Pelvis_x/2
    Chest_y = chest_y/2 + Pelvis_y/2
    Chest_z = chest_z/2 + Pelvis_z/2

    #各節の重さ
    M_Rhand = 0.006*weight
    M_Lhand = 0.006*weight
    M_Rfarm = 0.016*weight
    M_Lfarm = 0.016*weight
    M_Ruarm = 0.028*weight
    M_Luarm = 0.028*weight

    M_Rfoot = 0.0145*weight
    M_Lfoot = 0.0145*weight
    M_Rtibia = 0.0465*weight
    M_Ltibia = 0.0465*weight
    M_Rfemur = 0.1*weight
    M_Lfemur = 0.1*weight

    M_head = 0.081*weight
    M_chest = 0.355*weight
    M_pelvis = 0.142*weight

    #重心位置（加重平均）
    CoM_x = (M_Rhand*Rhand_x + M_Rfarm*Rfarm_x + M_Ruarm*Ruarm_x +
    M_Lhand*Lhand_x + M_Lfarm*Lfarm_x + M_Luarm*Luarm_x +
    M_Rfoot*Rfoot_x + M_Rtibia*Rtibia_x + M_Rfemur*Rfemur_x +
    M_Lfoot*Lfoot_x + M_Ltibia*Ltibia_x + M_Lfemur*Lfemur_x +
    M_head*head_x + M_chest*Chest_x + M_pelvis*Pelvis_x)/(M_Rhand +
    M_Lhand + M_Rfarm + M_Lfarm + M_Ruarm + M_Luarm +
    M_Rfoot + M_Rtibia + M_Rfemur + M_Lfoot + M_Ltibia + M_Lfemur +
    M_head + M_chest + M_pelvis)

    CoM_y = (M_Rhand*Rhand_y + M_Rfarm*Rfarm_y + M_Ruarm*Ruarm_y +
    M_Lhand*Lhand_y + M_Lfarm*Lfarm_y + M_Luarm*Luarm_y +
    M_Rfoot*Rfoot_y + M_Rtibia*Rtibia_y + M_Rfemur*Rfemur_y +
    M_Lfoot*Lfoot_y + M_Ltibia*Ltibia_y + M_Lfemur*Lfemur_y +
    M_head*head_y + M_chest*Chest_y + M_pelvis*Pelvis_y)/(M_Rhand +
    M_Lhand + M_Rfarm + M_Lfarm + M_Ruarm + M_Luarm +
    M_Rfoot + M_Rtibia + M_Rfemur + M_Lfoot + M_Ltibia + M_Lfemur +
    M_head + M_chest + M_pelvis)

    CoM_z = (M_Rhand*Rhand_z + M_Rfarm*Rfarm_z + M_Ruarm*Ruarm_z +
    M_Lhand*Lhand_z + M_Lfarm*Lfarm_z + M_Luarm*Luarm_z +
    M_Rfoot*Rfoot_z + M_Rtibia*Rtibia_z + M_Rfemur*Rfemur_z +
    M_Lfoot*Lfoot_z + M_Ltibia*Ltibia_z + M_Lfemur*Lfemur_z +
    M_head*head_z + M_chest*Chest_z + M_pelvis*Pelvis_z)/(M_Rhand +
    M_Lhand + M_Rfarm + M_Lfarm + M_Ruarm + M_Luarm +
    M_Rfoot + M_Rtibia + M_Rfemur + M_Lfoot + M_Ltibia + M_Lfemur +
    M_head + M_chest + M_pelvis)



    CoM = pd.DataFrame({"Time":df["Time"],
                    "CoM_x":CoM_x,
                    "CoM_y":CoM_y,
                    "CoM_z":CoM_z})

    new_file = "CoM/" + file.replace("position\\", "")
    CoM.to_csv(new_file, index = None)
    print("終了")
    #print(CoM)

    #print(CoM.mean())