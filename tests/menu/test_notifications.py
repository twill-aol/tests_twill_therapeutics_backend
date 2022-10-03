import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Menu] Notifications")
class TestNotifications(BaseCase):
    '''Tests notifications'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("menu", "smoke", "notifications", "authorization")
    @allure.description("This test checks /api/notifications/ api")
    def test_get_all_notifications(self):
        '''Get all notifications'''
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

    @allure.label("menu", "smoke", "notifications", "authorization")
    @allure.description("This test checks /api/alerts/new/count/")
    def test_new_notifications(self):
        '''Get new notifications'''
        response = MyRequests.get(
            "/api/alerts/new/count/",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "count")
        count_new_notifications = self.response_to_json(response)["count"]
        assert count_new_notifications >= 0, "Count of new notifications < 0"