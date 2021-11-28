import tensorflow as tf 
from tensorflow import keras 

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])]) 

model.compile(optimizer='sgd', loss='mean_squared_error') 


xs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
ys=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 

model.fit(xs, ys, epochs=100) 

inputnumber = float(input("Which number do you want to get predicted?: "))

print(model.predict([inputnumber])) 
