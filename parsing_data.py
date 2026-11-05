from installing_dataset import get_dataset
import converting_to_1Darray
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
        image = np.array(image)
        image = converting_to_1Darray.to_1D_array(image)
        train_data.append((image, label))

    for i in range(len(test_dataset)):
        image = test_dataset[i]['image']
        label = test_dataset[i]['label']
        # Convert the image to a NumPy array
        image = np.array(image)
        image = converting_to_1Darray.to_1D_array(image)
        test_data.append((image, label))

    return train_data, test_data

if __name__ == "__main__":
    train_data, test_data = parse_data()
    print("Data parsing completed successfully.")
    print(train_data[0])
    print(test_data[0])