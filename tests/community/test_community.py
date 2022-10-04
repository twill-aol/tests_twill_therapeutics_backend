import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Community] posts")
class TestCommunity(BaseCase):
    '''Tests Community posts'''

    user_id, email, cookies = MainCase.signup_router()
    post_id = ""
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
            TestCommunity.post_id = response_as_dict[0]["id"]
            TestCommunity.offender_user_id = response_as_dict[0]["user_id"]

    @allure.label("community", "post", "popular", "authorization")
    @allure.description("This test checks /api/report_abuse/ api")
    def test_report_post(self):
        '''Report post'''
        if self.post_id != "":
            data = {
                "abuse_type": "post",
                "about_item_id": self.post_id,
                "offender_user_id": self.offender_user_id
            }
            response = MyRequests.post(
                "/api/report_abuse/",
                json=data,
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
            self.post_id,
            f"Field `about_item_id` != {self.post_id}"
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

    @allure.label("community", "post", "track", "authorization")
    @allure.description("This test checks \
    /api/activity/?page=1&page_size=12&feed_filter=trackGroup")
    def test_community_track_posts(self):
        '''Get track posts in Community'''
        response = MyRequests.get(
            "/api/activity/?page=1&page_size=12&feed_filter=trackGroup",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        response_as_dict = BaseCase.response_to_json(response)
        if len(response_as_dict) > 0:
            assert ("id" and "user_id") in response_as_dict[0]

    @allure.label("community", "post", "followers", "authorization")
    @allure.description("This test checks \
    /api/activity/?page=1&page_size=12&feed_filter=followers")
    def test_community_followers_posts(self):
        '''Get followers posts in Community'''
        response = MyRequests.get(
            "/api/activity/?page=1&page_size=12&feed_filter=followers",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        response_as_dict = BaseCase.response_to_json(response)
        if len(response_as_dict) > 0:
            assert ("id" and "user_id") in response_as_dict[0]

    @allure.label("community", "post", "comment", "authorization")
    @allure.description("This test checks \
    /api/activity_statuses/52650445/comments/")
    def test_send_comment_to_post(self):
        '''Send comment to post in Community'''
        text = MainCase.good_phrases()
        data = {
            "text": text
        }
        response = MyRequests.post(
            f"/api/activity_statuses/{self.post_id}/comments",
            json=data,
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_value_by_name(
            response,
            "text",
            text,
            f"Comment is no {text}"
        )

# /api/activity_statuses/52651040/like/
# /api/comments/433197/like/
# post and delete empty data