import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Menu] Blocked users")
class TestResourcesPage(BaseCase):
    '''Tests disclaimer page'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("menu", "page", "blocked users", "authorization")
    @allure.description("This test checks \
    /api/v2/user/blocking/get-my/ api")
    def test_blocked_users_page(self):
        '''Get Blocked users page'''
        response = MyRequests.get(
            "/api/v2/user/blocking/get-my/",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
