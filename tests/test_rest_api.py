"""
This module contains a basic REST API tests using requests.
Its purpose is to show how to use pytest framework by example.
"""

# -----------------------------
# Imports
# -----------------------------

import pytest
import requests


# -----------------------------
# Tests
# -----------------------------
@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_anwser_api():

    # Arrange
    url = 'https://api.duckduckgo.com/?q=Python+programming&format=json'

    # Act
    response = requests.get(url)
    # To parse into python dictionary object
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']


