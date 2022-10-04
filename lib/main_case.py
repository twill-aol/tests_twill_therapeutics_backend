import datetime as dt
import random
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


TIME_START = str(dt.datetime.now().strftime("%Y%m%d%H%M%S"))


class MainCase(BaseCase):

    # response = MainCase.signup()
    user_id = ""
    email = ""
    cookies = ""

    @classmethod
    def cookies_marty_construction(self, response):
        marty_session_id = self.get_cookie(self, response, "marty_session_id")
        marty_session_id_hash = self.get_cookie(
            self,
            response,
            "marty_session_id_hash"
        )
        cookies = {
            "marty_session_id": marty_session_id,
            "marty_session_id_hash": marty_session_id_hash
        }
        return cookies

    @classmethod
    def generate_names(self):
        names = (
            "Ethan",
            "Kevin",
            "Justin",
            "Matthew",
            "William",
            "Christopher", 
            "Anthony",
            "Ryan",
            "Nicholas",
            "David",
            "Alex",
            "James",
            "Josh",
            "Dillon",
            "Brandon",
            "Philip",
            "Fred",
            "Tyler",
            "Caleb",
            "Thomas",
            "Aaron",
            "Brad",
            "Emilу",
            "Hannah",
            "Natalie",
            "Sophia",
            "Ella",
            "Madison",
            "Sydney",
            "Anna",
            "Taylor",
            "Isabella",
            "Kayla",
            "Victoria",
            "Elizabeth",
            "Ashley",
            "Rachel",
            "Alexis",
            "Julia",
            "Samantha",
            "Haley",
            "Olivia",
            "Sarah",
            "Jessica",
            "Ava",
            "Kaitlyn",
            "Katherine"
        )
        surnames = (
            "Johnson",
            "Brown",
            "Walker",
            "Hall",
            "White",
            "Wilson",
            "Thompson",
            "Moore",
            "Taylor",
            "Anderson",
            "Smith",
            "Jackson",
            "Harris",
            "Martin",
            "Young",
            "Hernandez",
            "Garcia",
            "Davis",
            "Miller",
            "Martinez",
            "Robinson",
            "Clark",
            "Rodrigues",
            "Lewis",
            "Lee",
            "Allen",
            "King"
        )
        names = f"{random.choice(names)} {random.choice(surnames)}"
        return names

    @classmethod
    def signup(self, email=None):
        dynamic_part = f'oleynik+{TIME_START}'
        domain = 'alarstudios.com'
        if email is None:
            email = f"{dynamic_part}@{domain}"
        signup_data = {
                "username": MainCase.generate_names(),
                "email": email,
                "password": 'Password+1',
                "agreement": "on",
                "first_name": f"Bot{TIME_START}",
                "last_name": f"AQABot{TIME_START}",
            }

        response = MyRequests.post("/auth/signup/", json=signup_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys(
            response,
            [
                "user_id",
                "user",
                "is_redirected",
                "original_url",
                "origin_referral_id",
                "env",
                "access_token",
            ],
        )
        self.user_id = BaseCase.response_to_json(response)["user_id"]
        self.email = BaseCase.response_to_json(response)["user"]["email"]
        self.cookies = MainCase.cookies_marty_construction(response)
        return self.user_id, self.email, self.cookies

    @classmethod
    def signup_router(self, email=None):
        if self.cookies != "":
            return self.user_id, self.email, self.cookies
        else:
            return MainCase.signup(email)

    @classmethod
    def finder_text(self, content, flag, board):
        find_id_position = content.find(flag) + len(flag)
        text = ""
        for symbol in content[find_id_position:]:
            if symbol != board:
                text += symbol
            else:
                break
        return text

    @classmethod
    def good_phrases(self):
        phrases = (
            "Be happy",
            "Everything will be alright",
            "Let's make this world a kinder place",
            "Nothing is impossible",
            "Believe in the dream",
            "You can do more",
            "Just do it",
            "Smile and everything will work out",
            "Focus on your breath",
            "Feel the fluidity",
            "We are all connected",
            "Happiness comes from within",
            "Our heart is full",
            "Focus on your breath",
            "Concentrate the mind on the present moment",
            "Humility, infinity, integrity, liberty, majesty, synergy",
            "Don't give up",
            "Be an example",
            "Stand on the side of the light",
            "God is everywhere",
        )
        phrase = random.choice(phrases)
        return phrase
