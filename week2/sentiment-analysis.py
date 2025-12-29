import tensorflow as tf
import numpy as np
import pickle

with open('sentiment_set.pickle', 'rb') as f:
    train_x, train_y, test_x, test_y = pickle.load(f)
    
    
# print(f"{len(train_x)} , {len(train_y)} , {len(test_x)} , {len(test_y)}") 
# print(train_x[12], train_y[12]) #Uncomment to see a sample feature and label

nodes_hl1 = 256
nodes_hl2 = 128
#nodes_hl3 = 500

n_classes = 2
batch_size = 100
n_features = len(train_x[0])

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(n_features,)),
    tf.keras.layers.Dense(nodes_hl1, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(nodes_hl2, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    #tf.keras.layers.Dense(nodes_hl3, activation='relu'),
    tf.keras.layers.Dense(n_classes)
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(),      
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

train_x = np.asarray(train_x, dtype=np.float32)
train_y = np.asarray(train_y, dtype=np.float32)
test_x = np.asarray(test_x, dtype=np.float32)
test_y = np.asarray(test_y, dtype=np.float32)

val_x_len = int(len(train_x) * 0.2)
val_x = train_x[:val_x_len]
val_y = train_y[:val_x_len]

train_x = train_x[val_x_len:]
train_y = train_y[val_x_len:]

cb = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=2, restore_best_weights=True)

history = model.fit(
    train_x, train_y,
    epochs=10,
    batch_size=batch_size,
    validation_data=(val_x, val_y),
    verbose=1,
    callbacks=[cb]
)

model.save('sentiment_model.h5')


loss, acc = model.evaluate(test_x, test_y, verbose=0)
print("Accuracy:", acc)

    
    