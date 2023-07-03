import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd
import h5py
from tensorflow import keras


data_path = "D:/cyclone/TCIR-ATLN_EPAC_WPAC.h5"
data_info = pd.read_hdf(data_path, key="info", mode='r')
with h5py.File(data_path, 'r') as hf:
    data_matrix = hf['matrix'][:1000]

print(data_matrix.shape)

## keep only IR and PMW
X_irpmw = data_matrix[:,:,:,0::3]
y = data_info['Vmax'].values[:1000]

X_irpmw[np.isnan(X_irpmw)] = 0
X_irpmw[X_irpmw > 1000] = 0


#Test Train Split
X_train, X_test, y_train, y_test = train_test_split(X_irpmw, y, test_size=0.1, random_state=42)
# Define the input shape
input_shape = (201, 201, 2)

model = keras.models.load_model('D:/cyclone/model_0_AEW.h5')
model.summary()

y_pred=y_test
y_true=model.predict(X_test)

plt.scatter(y_true, y_pred)
plt.xlabel("Neutral Fraction (Predicted)")
plt.ylabel("Neutral Fraction (Actual)")
# plt.savefig("./models/3DCNN/y_test_y_pred_scatter.jpg")
plt.show()
