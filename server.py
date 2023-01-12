import json
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    return redirect(url_for('login'))


@app.route('/showSummary', methods=['GET', 'POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        flash("email incorrect")
        return render_template('login.html')

    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    number_places_required = int(request.form['places'])
    number_places_max = 12
    number_places_available = int(competition['numberOfPlaces'])
    number_places_club = int(club['points'])

    if number_places_required > number_places_max:
        flash("Impossible to buy more than 12 places")
        return render_template('booking.html', club=club, competition=competition)

    elif number_places_required > number_places_available:
        flash("Impossible to buy more places than available")
        return render_template('booking.html', club=club, competition=competition)

    else:
        flash('Great-booking complete!')
        club['points'] = str(number_places_club - number_places_required)
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - number_places_required
        return render_template('welcome.html', club=club, competitions=competitions)

# TODO: Add route for points display
