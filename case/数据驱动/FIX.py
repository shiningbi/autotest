import pytest
@pytest.fixture(scope='module',autouse=True)
def createzhanngsan():
    print('\n创建')
    yield
    print('\n销毁')
def test_001():
    print('\n0001')
def test_002():
    print('\n0002')