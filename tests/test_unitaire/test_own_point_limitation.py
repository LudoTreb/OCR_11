import server


def test_buy_more_places_than_their_own_points(client):
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    response = client.post('/purchasePlaces',
                           data={
                               'club': club,
                               'competition': competition['name'],
                               'numberOfPlaces': competition['numberOfPlaces'],
                               'places': 42,
                           })

    assert response.status_code == 200
