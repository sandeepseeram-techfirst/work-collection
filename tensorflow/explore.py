import tensorflow as tf

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(3, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

loss_fn = tf.keras.losses.MeanSquaredError()

# compile the model 
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

import pandas as pd 

data = pd.read_csv("https://tinyurl.com/y2qmhfsr")

# Extract the input columns, scale down by 255
X = (data.iloc[:, 0:3].values / 255.0)
Y = data.iloc[:, -1].values

# fit the model
model.fit(X,Y,epochs=100,batch_size=32)
