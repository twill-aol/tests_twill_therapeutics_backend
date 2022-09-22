import datetime as dt
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


TIME_START = str(dt.datetime.now().strftime("%Y%m%d%H%M%S"))


class MainCase(BaseCase):
    @classmethod
    def signup(self, email=None):
        dynamic_part = f'oleynik+{TIME_START}'
        domain = 'alarstudios.com'
        if email is None:
            email = f"{dynamic_part}@{domain}"
        signup_data = {
                "username": f"Bot{TIME_START}",
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
        return response

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
