"""
this module tests the process_img function to ensure it functions as its supposed to 
"""

import pytest
from main import process_img

def test_valid_process_img_image():
    res = process_img("img.jpg")
    assert res in ["daisy", "dandelon", "roses", "sunflowers", "tulips"]
    
def test_invalid_process_img_image():
    res = process_img("car.jpg")
    assert res not in ["daisy", "dandelon", "roses", "sunflowers", "tulips"]
 
def test_invalid_process_img_file():
    with pytest.raises(FileNotFoundError):
        process_img("nofile.jpg")
     
def test_process_img_png_format():
    res = process_img("rose.png")
    assert res in ["daisy", "dandelon", "roses", "sunflowers", "tulips"] 

