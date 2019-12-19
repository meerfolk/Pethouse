import pytest
from src.app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


def test_config(file_conf):
    response = file_conf.get('/api/config')
    assert response.status_code == 200
