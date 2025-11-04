from unittest.mock import Mock


def fetch_data(api_url):
    response = requests.get(api_url)
    return response.json()


def test_fetch_data():
    mock_response = Mock()
    mock_response.json.return_value = {"key": "value"}

    requests.get = Mock(return_value=mock_response)
    data = fetch_data("https://example.com")

    assert data == {"key": "value"}