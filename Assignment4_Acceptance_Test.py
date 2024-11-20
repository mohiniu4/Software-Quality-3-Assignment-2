import pytest
from main import app
from unittest.mock import patch, MagicMock
import io

@pytest.fixture
def client():
    """
    Flask test client fixture for acceptance tests.
    """
    app.testing = True
    client = app.test_client()
    yield client

#Acceptance Test 1: Process endpoint with a valid image
@patch("main.load_model")
def test_process_endpoint_with_valid_image(mock_load_model, client):
    """
    Acceptance Test 1: Verify the `/process` endpoint works with a valid image.
    GIVEN a valid image file
    WHEN the file is sent to the `/process` endpoint
    THEN the response should contain the correct flower label ('daisy').
    """
    # Mock the model's predict function
    mock_model = MagicMock()
    mock_load_model.return_value = mock_model
    mock_model.predict.return_value = [[1, 0, 0, 0, 0]]  # Simulating "daisy" prediction

    # Simulate uploading a valid image file


    with open("img.jpg", "rb") as valid_image:
        response = client.post(
            "/process", data={"img": (valid_image, "img.jpg")}
        )
    
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "daisy"

#Acceptance Test 2: Process endpoint with an invalid file
@patch("main.load_model")
def test_process_endpoint_with_invalid_file(mock_load_model, client):
    """
    Acceptance Test 2: Verify the `/process` endpoint handles invalid files gracefully.
    GIVEN a non-image file
    WHEN the file is sent to the `/process` endpoint
    THEN the response should fail gracefully with a 500 error or appropriate error message.
    """
    # Mock the model's predict function to simulate an error
    mock_model = mock_load_model.return_value
    mock_model.predict.side_effect = RuntimeError("Invalid file")

    # Simulate uploading a non-image file
    non_image = io.BytesIO(b"This is not an image")
    response = client.post(
        "/process", data={"img": (non_image, "non_image.txt")}
    )

    assert response.status_code == 500  
