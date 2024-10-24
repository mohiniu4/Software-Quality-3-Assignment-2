"""
this module tests the process_img function to ensure it functions as its supposed to 
"""
import pytest
from main import process_img

def valid_test_process_test():
    res = process_img("img.jpg")
    assert res in ["daisy", "dandelon", "roses", "sunflowers", "tulips"]
    
def invalid_test_process_test():
    res = process_img("car.jpg")
    assert res in ["daisy", "dandelon", "roses", "sunflowers", "tulips"]
 