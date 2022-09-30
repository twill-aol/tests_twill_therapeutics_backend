import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Today] Home Page")
class TestHomePage(BaseCase):
    '''Tests Home Page'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("track", "search", "authorization", "smoke")
    @allure.description("This test checks /api/kabinet-homepage/")
    def test_home_page(self):
        '''Get search tracks'''
        response = MyRequests.get(
            "/api/kabinet-homepage/",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys(
            response,
            [
                "user",
                "track",
                "medals",
                "stats",
            ]
        )
