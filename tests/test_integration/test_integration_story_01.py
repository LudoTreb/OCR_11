import server


def test_buy_places_by_specific_club(client):
    # Chargement de la db
    clubs = server.load_clubs()
    competitions = server.load_competitions()

    # 1 Un club s'authentifie via son email.
    response_login = client.post('/showSummary',
                                 data={
                                     'email': "john@simplylift.co"
                                 })
    assert response_login.status_code == 200

    # Il choisit un évènement.
    club = server.clubs[0]  # Simply Lift
    competition = server.competitions[0]  # Spring Festival

    # Il achète 6 places
    club_initial_point = club["points"]
    competition_initial_place = competition["numberOfPlaces"]
    message_buy_places_succed = "Great-booking complete!"
    number_place = 6
    response_buy_places = client.post("/purchasePlaces",
                                      data={
                                          "club": club["name"],
                                          "competition": competition["name"],
                                          "places": number_place,
                                      })

    assert message_buy_places_succed in response_buy_places.data.decode()
    assert response_buy_places.status_code == 200
    assert club["points"] != club_initial_point
    assert competition["numberOfPlaces"] != competition_initial_place

    # Il consulte la liste des points des autres clubs
    response_check_point_other_clubs = client.get('/clubs')
    assert response_check_point_other_clubs.status_code == 200

    # Il se déconnecte
    response_logout = client.get('/logout')
    assert response_logout.status_code == 302
