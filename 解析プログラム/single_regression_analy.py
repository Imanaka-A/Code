#マーカー欠損時の回帰分析
#回帰分析で補えるかは検討してから使用


import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("n_2_2.csv")

x = df[["Body_RHand_Position_X"]]
y = df[["Body_RRadius_Position_X"]]

model = LinearRegression()
model.fit(x,y)


print('a = ', model.coef_)
print('b = ', model.intercept_)


x = df[["Body_RHand_Position_Y"]]
y = df[["Body_RRadius_Position_Y"]]

model = LinearRegression()
model.fit(x,y)


print('a = ', model.coef_)
print('b = ', model.intercept_)

x = df[["Body_RHand_Position_Z"]]
y = df[["Body_RRadius_Position_Z"]]

model = LinearRegression()
model.fit(x,y)


print('a = ', model.coef_)
print('b = ', model.intercept_)