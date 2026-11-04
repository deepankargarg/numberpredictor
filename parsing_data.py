from installing_dataset import get_dataset
from PIL import Image
import numpy as np

def parse_data() -> tuple:
    train_dataset, test_dataset = get_dataset()
    train_data = []
    test_data = []

    for i in range(len(train_dataset)):
        image = train_dataset[i]['image']
        label = train_dataset[i]['label']
        # Convert the image to a NumPy array
        train_data.append((np.array(image), label))

    for i in range(len(test_dataset)):
        image = test_dataset[i]['image']
        label = test_dataset[i]['label']
        # Convert the image to a NumPy array
        test_data.append((np.array(image), label))

    return train_data, test_data

if __name__ == "__main__":
    train_data, test_data = parse_data()
    print(train_data[0])
    print(test_data[0])
    print("Data parsing completed successfully.")