import numpy as np
from tensorflow import keras
from parsing_data import parse_data


# Load the data using your existing function
train_data, test_data = parse_data()

# Separate each (image, label) pair into arrays
X_train = np.array([image for image, label in train_data], dtype=np.float32)
y_train = np.array([label for image, label in train_data], dtype=np.int64)

X_test = np.array([image for image, label in test_data], dtype=np.float32)
y_test = np.array([label for image, label in test_data], dtype=np.int64)

# Create the model
model = keras.Sequential([
    keras.layers.Input(shape=(784,)),
    keras.layers.Dense(10, activation="softmax")
])

# Configure training
model.compile( 
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train and evaluate
model.fit(X_train, y_train, epochs=5)
model.evaluate(X_test, y_test)