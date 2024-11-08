"""
    this module tests the process_img function to ensure it functions as its 
    supposed to using happy and sad path testing while using test doubles
"""

#suppresses the tensorflow logs
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import pytest
from main import process_img
from unittest.mock import patch, MagicMock


"""
    happy path testing
"""
#test that it works as it should
@patch("main.load_model")
def test_happy_path_process_img(mock_load_model):
    mock_model = MagicMock()
    mock_load_model.return_value = mock_model
    mock_model.predict.return_value = [[1, 0, 0, 0, 0]]  #simulates prediction for daisy, 1 at index 0 as daisy is first in the names array
    result = process_img("img.jpg")
    assert result == "daisy"

#test that it works with a png
@patch("main.load_model")
def test_happy_path_process_img_with_png(mock_load_model):
    mock_model = MagicMock()
    mock_load_model.return_value = mock_model
    mock_model.predict.return_value = [[0, 0, 1, 0, 0]]  #simulates prediction for roses, 1 at index 2 as roses is third in the names array
    result = process_img("rose.png")
    assert result == "roses"
    

"""
    sad path testing
"""
#test for missing model file
#simulate file not found
@patch("main.load_model", side_effect=FileNotFoundError("File not found"))
def test_sad_path_process_img_model(mock_load_model):
   with pytest.raises(FileNotFoundError, match="File not found"):
       process_img("img.jpg")


#test for any runtime errors during the prediction process
@patch("main.load_model")
def test_sad_path_process_img_prediction(mock_load_model):
   mock_model = MagicMock()
   mock_model.predict.side_effect = RuntimeError("unable to make a prediction")
   mock_load_model.return_value = mock_model
   with pytest.raises(RuntimeError, match="unable to make a prediction"):
       process_img("img.jpg")


#test for any unacceptable images
@patch("main.load_model")
@patch("main.cv2.resize", side_effect=ValueError("Unsupported image resize"))
def test_sad_path_process_img_resize (mock_resize, mock_load_model):
    mock_load_model.return_value = MagicMock()
    with pytest.raises(ValueError, match="Unsupported image resize"):
       process_img("img.jpg")
