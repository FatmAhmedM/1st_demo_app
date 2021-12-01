from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd
df = pd.read_csv("homeprices.csv")
df.bedrooms.fillna(df.bedrooms.mean(),inplace = True)

features = df.drop('price',axis = 'columns')
target = df['price']

model = LinearRegression()
model.fit(features,target)
print(model.predict([[2000,4,50]]))


joblib.dump(model,'demo_RegModel')