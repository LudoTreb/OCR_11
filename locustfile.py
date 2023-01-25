from locust import HttpUser, task, between

import server


class TestUser(HttpUser):
    wait_time = between(1, 2)
    competitions = server.load_competitions()[0]["name"]
    club = server.load_clubs()[0]

    @task
    def login(self):
        """"""
        self.client.get("/login")

    @task
    def connexion(self):
        self.client.post("/showSummary", data={"email": self.club["email"]}, name="showSummary")

    @task
    def purchase_places(self):
        self.client.post("/purchasePlaces", data={
            "club": self.club["name"],
            "competition": self.competitions,
            "places": 2,
        }, name="purchasePlaces")

    @task
    def get_place(self):
        self.client.get("/book/" + self.competitions
                        + "/" + self.club, name="book")

    @task
    def logout(self):
        """"""
        self.client.get("/logout")
