import allure
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Track] Featured")
class TestTracksFeatured(BaseCase):
    '''Tests Track Featured'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("track", "featured", "authorization", "smoke")
    @allure.description("This test checks /api/v2/tracks/featured/ api")
    def test_featured_track(self):
        '''Get featured tracks'''
        response = MyRequests.get(
            "/api/v2/tracks/featured/",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        assert len(response.content) > 0, "No featured tracks"
