import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Menu] Resources")
class TestResourcesPage(BaseCase):
    '''Tests resources page'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("menu", "page", "resources")
    @allure.description("This test checks \
    /api/get_member_resources_template/ api")
    def test_resource_page(self):
        '''Get resources page'''
        response = MyRequests.get(
            "/api/get_member_resources_template/",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(
            response,
            "member_resources"
        )
