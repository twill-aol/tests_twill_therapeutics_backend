import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Menu] Notifications")
class TestResourcesPage(BaseCase):
    '''Tests notifications page'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("menu", "page", "notifications", "authorization")
    @allure.description("This test checks /api/notifications/ api")
    def test_disclaimer_page(self):
        '''Get notifications page'''
        response = MyRequests.get(
            "/api/notifications/",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys(
            response,
            [
                "total_count",
                "next_page",
                "notifications"
            ]
        )
