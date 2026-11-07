from datasets import load_dataset

global mnist

def main():
    # Download MNIST, or reuse it if it is already cached.
    mnist = load_dataset("ylecun/mnist")

    print("MNIST is ready!")
    print(mnist)

    return mnist

def get_dataset():
    x = main()
    print("Dataset is ready!")
    return x["train"], x["test"]

if __name__ == "__main__":
    main()