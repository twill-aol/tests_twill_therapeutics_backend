import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Menu] Disclaimer")
class TestResourcesPage(BaseCase):
    '''Tests disclaimer page'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("menu", "page", "disclaimer", "authorization")
    @allure.description("This test checks /api/disclaimer/ api")
    def test_disclaimer_page(self):
        '''Get disclaimer page'''
        response = MyRequests.get(
            "/api/disclaimer/",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys(
            response,
            [
                "disclaimer",
                "footer"
            ]
        )
