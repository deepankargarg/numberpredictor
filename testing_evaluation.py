

def test_model():
    test_loss, test_accuracy = model.evaluate(X_test_flattened, y_test)
    print("Test loss:", test_loss)
    print("Test accuracy:", test_accuracy)