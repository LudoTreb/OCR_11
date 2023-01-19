import server


# def test_competition_place_update(client):
#     club = server.clubs[1]
#     competition = server.competitions[0]
#     initial_places = competition['numberOfPlaces']
#     response = client.post('/purchasePlaces',
#                            data={
#                                'club': club['name'],
#                                'competition': competition['name'],
#                                'places': 3
#                            })
#     assert response.status_code == 200
#     assert initial_places != competition['numberOfPlaces']
