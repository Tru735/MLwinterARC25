import tensorflow as tf
import numpy as np
import pickle

with open('sentiment_set.pickle', 'rb') as f:
    train_x, train_y, test_x, test_y = pickle.load(f)
    
    
# print(f"{len(train_x)} , {len(train_y)} , {len(test_x)} , {len(test_y)}") 
print(train_x[12], train_y[12]) #Uncomment to see a sample feature and label

