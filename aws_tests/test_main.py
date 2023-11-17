from aws_data.load_data import get_data

def test_check_dynamo_resource():
    assert get_data is not None
