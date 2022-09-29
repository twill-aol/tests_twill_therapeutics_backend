import allure
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Track] Search")
class TestTracksSearch(BaseCase):
    '''Tests Track Search'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("track", "search", "authorization", "smoke")
    @allure.description("This test checks api/v2/tracks/search/?query=love")
    def test_topics_of_track(self):
        '''Get search tracks'''
        response = MyRequests.get(
            "/api/v2/tracks/search/?query=love",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys(
            response,
            [
                "creators",
                "tracks"
            ]
        )
