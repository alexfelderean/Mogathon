import cv2
import numpy as np

def preprocess_image(image):
    # Resize image to the input size expected by the model
    resized_image = cv2.resize(image, (100, 100))
    # Normalize pixel values to be in the range [0, 1]
    normalized_image = resized_image / 255.0
    # Expand dimensions to match the input shape expected by the model
    processed_image = np.expand_dims(normalized_image, axis=0)
    return processed_image

def classify_ripeness(image):
    # Preprocess the input image
    processed_image = preprocess_image(image)
    # Make prediction using the loaded model
    prediction = model.predict(processed_image)
    # Convert prediction to human-readable class (ripe or unripe)
    if prediction < 0.5:
        return "Unripe"
    else:
        return "Ripe"

def main():
    # Load the image
    image_path = 'amogus'
    image = cv2.imread(image_path)
    
    # Apply any necessary preprocessing to the image
    # (e.g., image segmentation to isolate the banana)
    
    # Classify the ripeness of the banana
    ripeness = classify_ripeness(image)
    
    # Display the result
    print("The banana is:", ripeness)

if __name__ == "__main__":
    main()
