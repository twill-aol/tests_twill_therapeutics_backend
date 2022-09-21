import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


@allure.epic("[HD] No Authorization cases")
class TestHDUnlogin(BaseCase):
    @allure.label("HD", "unlogin")
    @allure.description("This test checks /daily api")
    def test_hd_get_last_article(self):
        response = MyRequests.get("/api/happifiers/daily/")

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys(
            response,
            [
                "id",
                "human_url",
                "happifier_type",
                "og_title",
                "og_description",
                "meta_title",
                "meta_description",
                "image_click_url",
                "image",
                "right_rail_image",
                "og_image",
                "title",
                "is_sponsored",
                "sponsor",
                "experts",
                "authors",
                "tags",
                "publish_at_app",
                "rid",
                "author_image",
                "author_info",
                "author",
                "publisher_id",
                "publisher_image",
                "publisher_info",
                "publisher_name",
                "image_alt",
                "audio_duration",
                "publish_at",
                "audio_url",
                "video_url",
            ],
        )

    @allure.label("HD", "unlogin")
    @allure.description("This test checks /topics api")
    def test_hd_get_topics(self):
        response = MyRequests.get("/api/happifiers/topics/")

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys(
            response,
            [
                "id",
                "human_url",
                "parent_id",
                "sequence",
                "name",
                "description",
                "parent_name",
                "type",
            ],
            0,
        )

    @allure.label("HD", "unlogin")
    @allure.description("This test checks /happifiers/[id] api")
    def test_hd_get_article(self, human_url=""):
        def asserts(response, uri_type, uri):
            with allure.step(f"Get article by {uri_type}: '{uri}'"):
                Assertions.assert_code_status(response, 200),
                Assertions.assert_json_has_keys(
                    response,
                    [
                        "id",
                        "ad_position",
                        "human_url",
                        "happifier_type",
                        "content_type",
                        "og_title",
                        "og_description",
                        "meta_title",
                        "meta_description",
                        "image_click_url",
                        "image",
                        "right_rail_image",
                        "og_image",
                        "title",
                        "subtitle",
                        "body",
                        "credits",
                        "video",
                        "audio",
                        "is_sponsored",
                        "sponsor",
                        "experts",
                        "authors",
                        "tags",
                        "created_at",
                        "modified_at",
                        "publish_at_app",
                        "rid",
                        "author_image",
                        "author_info",
                        "author",
                        "publisher_id",
                        "publisher_image",
                        "publisher_info",
                        "publisher_name",
                        "image_alt",
                        "audio_duration",
                        "publish_at",
                        "audio_url",
                        "video_url",
                    ],
                )

        if human_url == "":
            for article_id in range(1, 450, 32):
                response = MyRequests.get(f"/api/happifiers/{article_id}/")
                if response.status_code != 200:
                    continue
                elif response.status_code == 200:
                    asserts(response, "article_id", article_id)
                    h_url = self.response_to_json(response)['human_url']
                    self.test_hd_get_article(h_url)
                    break
                else:
                    assert 0, "None of the articles opened"
        else:
            response = MyRequests.get(f"/api/happifiers/{human_url}/")
            asserts(response, "human_url", human_url)

    @allure.label("HD", "unlogin")
    @allure.description("This test checks /happifiers+params api")
    def test_hd_get_count_of_topics(self):
        count_of_articles_param = 5
        response = MyRequests.get(
            f"/api/happifiers/?page=1&page_size={count_of_articles_param}"
        )

        Assertions.assert_code_status(response, 200)
        Assertions.assert_length_of_json(
            response,
            count_of_articles_param,
            f"Response does not contain {count_of_articles_param} keys",
        )


@allure.epic("[HD] Authorization cases")
class TestHDLogin(BaseCase):

    @allure.label("HD", "Authorization")
    @allure.description("This test checks /happifiers+params api")
    def test_hd_get_count_of_topics(self):
        signup_data = self.prepare_registration_data()
        response = MyRequests.post("/auth/signup/", json=signup_data)
        user_id = self.response_to_json(response)["user_id"]

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "user_id")

# response = MyRequests.post("/auth/signup/", json=signup_data)
# response_as_dict = BaseCase.response_to_json(response)
# print("user_id" in response_as_dict.keys())