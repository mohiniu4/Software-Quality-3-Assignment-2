"""
this module implements a Flask server that processes images and predicts labels 
"""
from flask import Flask, render_template, request
from keras.preprocessing.image import img_to_array  # pylint: disable=E0401
from keras.models import load_model  # pylint: disable=E0401
import cv2  # pylint: disable=E1101
import numpy as np
from flask_cors import CORS

# list of possible flowers
names = ["daisy", "dandelon", "roses", "sunflowers", "tulips"]

def process_img(img_path):
    """
    Processes the input image and predicts the flower label

    Parameters:
        Path to the input image - img_path(string)

    Returns:
        Predicted flower label - string
    """
    # Read image
    model = load_model("flower.model")
    # Read & preprocess image
    image = cv2.imread(img_path) # pylint: disable=E1101
    image = cv2.resize(image, (199, 199)) # pylint: disable=E1101
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    #Predict and print the flower label
    res = model.predict(image)
    label = np.argmax(res)
    print("Label", label)
    label_name = names[label]
    print("Label name:", label_name)
    return label_name


# Initializing flask application
app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def main_page():
    """
    Main page route

    Returns:
        Confirmation message - string 
    """
    return "Application is working"

# About page with render 
@app.route("/about")
def about_page():
    """
    About page route

    Returns:
        Rendered about page  - string
    """
    return render_template("about.html")

# Process images
@app.route("/process", methods=["POST"])
def process_req():
    """
    Process the incoming image and return the predicted label

    Returns:
        Predicted flower label - string
    """
    data = request.files["img"]
    data.save("img.jpg")

    # process saved image
    resp = process_img("img.jpg")


    return resp


if __name__ == "__main__":
    app.run(debug=True)
