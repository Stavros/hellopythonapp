import pytest
import sys
sys.path.append( '.' )
import mypythonapp

@pytest.fixture(scope="module")
def client():
    mypythonapp.app.testing = True
    client = mypythonapp.app.test_client()
    return client