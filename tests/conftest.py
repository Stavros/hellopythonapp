import pytest
import sys
sys.path.append( '.' )
import myapp

@pytest.fixture(scope="module")
def client():
    myapp.app.testing = True
    client = myapp.app.test_client()
    return client