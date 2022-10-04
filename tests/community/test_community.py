import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Community] posts")
class TestCommunity(BaseCase):
    '''Tests Community posts'''

    user_id, email, cookies = MainCase.signup_router()
    about_item_id = ""
    offender_user_id = ""

    @allure.label("community", "post", "popular", "authorization")
    @allure.description("This test checks \
    api/activity/?page=1&page_size=12&feed_filter=popular")
    def test_community_popular_posts(self):
        '''Get popular posts in Community'''
        response = MyRequests.get(
            "/api/activity/?page=1&page_size=12&feed_filter=popular",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        response_as_dict = BaseCase.response_to_json(response)
        if len(response_as_dict) > 0:
            TestCommunity.about_item_id = response_as_dict[0]["id"]
            TestCommunity.offender_user_id = response_as_dict[0]["user_id"]

    @allure.label("community", "post", "popular", "authorization")
    @allure.description("This test checks /api/report_abuse/ api")
    def test_report_post(self):
        '''Report post'''
        if self.about_item_id != "":
            params = {
                "abuse_type": "post",
                "about_item_id": self.about_item_id,
                "offender_user_id": self.offender_user_id
            }
            response = MyRequests.post(
                "/api/report_abuse/",
                json=params,
                cookies=self.cookies
            )
            Assertions.assert_code_status(response, 200)
            Assertions.assert_json_has_keys(
                response,
                [
                    "id",
                    "text",
                    "about_item_id",
                    "reporter_user_id",
                    "offenderer_user_id",
                    "abuse_type",
                    "created_at"
                ]
            )
        
        Assertions.assert_json_value_by_name(
            response,
            "about_item_id",
            self.about_item_id,
            f"Field `about_item_id` != {self.about_item_id}"
        )
        Assertions.assert_json_value_by_name(
            response,
            "reporter_user_id",
            self.user_id,
            f"Field `reporter_user_id` != {self.user_id}"
        )
        Assertions.assert_json_value_by_name(
            response,
            "offenderer_user_id",
            self.offender_user_id,
            f"Field `offenderer_user_id` != {self.offender_user_id}"
        )
