from unittest.mock import call

from pytest_mock import mocker


def test_email_in_db(client):
    expected_value = 200

    response = client.post('/showSummary',
                           data={'email': 'john@simplylift.co'},
                           )
    assert response.status_code == expected_value


def test_email_not_in_db(mocker, client):
    expected_value = 401
    mock_server_flash = mocker.patch('server.flash')

    response = client.post('/showSummary',
                           data={'email': 'lulu@gmail.com'},
                           )

    assert mock_server_flash.call_args == call('email incorrect', )
    assert mock_server_flash.call_count == 1  # call_out permet de savoir combien de fois le response_message a été appelé
    # assert response.status_code == expected_value


def test_email_not_in_db_template_error(client):
    expected_value = 200

    response = client.post('/showSummary',
                           data={'email': 'lulu@gmail.com'},
                           )
    assert b'email incorrect' in response.data  # b pour convertir en byte
    assert response.status_code == expected_value
