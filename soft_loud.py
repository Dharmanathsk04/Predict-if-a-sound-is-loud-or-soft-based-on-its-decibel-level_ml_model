

from sklearn.linear_model import LogisticRegression

import numpy as np


X = np.array([[10], [20], [30], [40], [50], [60], [70], [80], [90]])

y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1])  

model = LogisticRegression()

model.fit(X, y)


db = float(input("Enter sound level in decibels (dB): "))



prediction = model.predict([[db]])[0]



if prediction == 0:
    print(f"{db} dB → Soft sound 🔉")
else:
    print(f"{db} dB → Loud sound 🔊")
