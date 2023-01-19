import server


def test_club_point_update(client):
    club = server.clubs[1]
    initial_points = club['points']
    competition = server.competitions[0]['name']
    response = client.post('/purchasePlaces',
                           data={
                               'club': club['name'],
                               'competition': competition,
                               'places': 3
                           })
    assert response.status_code == 200
    assert initial_points != club['points']



