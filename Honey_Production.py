import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")

prod_per_year = df.groupby("year").totalprod.mean().reset_index()
#print(prod_per_year)

x = prod_per_year["year"]
x = x.values.reshape(-1, 1)
#print(x)

y = prod_per_year["totalprod"]
#print(y)

plt.scatter(x,y)
#plt.show()

regr = linear_model.LinearRegression()
regr.fit(x,y)

#print(regr.coef_)
#print(regr.intercept_)

y_predict = regr.predict(x)

plt.plot(x, y_predict)
#plt.show()

X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)
#print(X_future)

future_predict = regr.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()