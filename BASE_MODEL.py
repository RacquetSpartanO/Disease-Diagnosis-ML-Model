import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np

file = pd.read_csv(r"D:\DP project\IV SEM\refined\NewDSetfile.csv")

X = file.drop('Diagnosis', axis='columns')
Y = file.Diagnosis

column_trans = make_column_transformer((OneHotEncoder(),['Sex', 'Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4']), remainder=StandardScaler())
logreg = LogisticRegression(solver='lbfgs')

pipe = make_pipeline(column_trans, logreg)

acc = cross_val_score(pipe, X, Y, cv=5, scoring='accuracy').mean()

pipe.fit(X,Y)

Testset = pd.read_csv(r"D:\DP project\IV SEM\refined\test_dataset.csv")
Test_X = Testset.drop('Diagnosis', axis='columns')
Test_Y = Testset.Diagnosis

age = int(input("Enter your age: "))
sex = input("Enter [M] or [F]: ")
temp = float(input("Enter temperature in farenheit: "))
bp = input("Enter BP(SSS/DD): ")
bpl = bp.split("/")
sbp = int(bpl[0])
dbp = int(bpl[1])
sym = []
for i in range(4):
    a = input(f"Enter Symptom {i+1}: ")
    sym.append(a)

user_data = pd.DataFrame({
        'Age': [age],
        'Sex': [sex],
        'Temperature': [temp],
        'Systolic_BP': [sbp],
        'Diastolic_BP': [dbp],
        'Symptom_1': [sym[0]],
        'Symptom_2': [sym[1]],
        'Symptom_3': [sym[2]],
        'Symptom_4': [sym[3]]
    })

pred = pipe.predict(user_data)

print(pred)


