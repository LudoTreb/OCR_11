import server
from tests.conftest import client


def test_purchase_places_more_than_12(client):
    # Mettre en place le test
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    number_place = 15
    expected_value = 200

    # Executer la fonction importée
    response = client.post('/purchasePlaces',
                           data={
                               'club': club,
                               'competition': competition['name'],
                               'numberOfPlaces': competition['numberOfPlaces'],
                               'places': number_place,
                           })

    # Vérification
    assert response.status_code == expected_value
