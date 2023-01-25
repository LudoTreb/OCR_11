import server


def test_purchase_places_more_than_12(client):
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    number_place = 15
    expected_value = 200

    response = client.post('/purchasePlaces',
                           data={
                               'club': club,
                               'competition': competition['name'],
                               'numberOfPlaces': competition['numberOfPlaces'],
                               'places': number_place,
                           })

    assert response.status_code == expected_value
