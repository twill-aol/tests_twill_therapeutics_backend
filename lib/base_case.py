import json.decoder
from datetime import datetime
from requests import Response
import datetime as dt


TIME_START = str(dt.datetime.now().strftime("%Y%m%d%H%M%S"))

class BaseCase:
    @classmethod
    def response_to_json(cls, response: Response):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert (
                False
            ), f"Response is not in JSON format. \
                Response text is {response.text}"
        return response_as_dict

    def get_cookie(self, response: Response, cookie_name):
        assert (
            cookie_name in response.cookies
        ), f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert (
            headers_name in response.headers
        ), f"Cannot find header with the name {headers_name} \
            in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert (
                False
            ), f"Response is not in JSON-format. \
                Response text is '{response.text}'"

        assert name in response_as_dict, \
            "Response JSON does not have key '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self, email=None):
        dynamic_part = f'oleynik+{TIME_START}'
        domain = 'alarstudios.com'
        if email is None:
            email = f"{dynamic_part}@{domain}"
        signup_data = {
                "username": f"Bot{TIME_START}",
                "email": email,
                "password": 'Password+1',
                "agreement":"on",
                "first_name": f"Bot{TIME_START}",
                "last_name": f"AQABot{TIME_START}",
            }
        return signup_data