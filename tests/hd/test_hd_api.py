import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[HD] No Authorization cases")
class TestHDUnlogin(BaseCase):
    @allure.label("HD", "unlogin")
    @allure.description("This test checks /daily api")
    def test_hd_get_last_article_unlogin(self, cookies=None):
        response = MyRequests.get("/api/happifiers/daily/", cookies=cookies)
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
    def test_hd_get_topics_unlogin(self, cookies=None):
        response = MyRequests.get("/api/happifiers/topics/", cookies=cookies)

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
    def test_hd_get_article_unlogin(self, human_url="", cookies=None):
        def hd_get_article_asserts(response, uri_type, uri):
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

        if human_url == "" or human_url is None:
            for article_id in range(1, 450, 32):
                response = MyRequests.get(
                    f"/api/happifiers/{article_id}/",
                    cookies=cookies
                )
                if response.status_code != 200:
                    continue
                elif response.status_code == 200:
                    hd_get_article_asserts(response, "article_id", article_id)
                    h_url = self.response_to_json(response)['human_url']
                    if human_url == "":
                        self.test_hd_get_article_unlogin(h_url)
                    return h_url
                else:
                    assert 0, "None of the articles opened"
        else:
            response = MyRequests.get(
                f"/api/happifiers/{human_url}/",
                cookies=cookies
            )
            hd_get_article_asserts(response, "human_url", human_url)

    @allure.label("HD", "unlogin")
    @allure.description("This test checks /happifiers+params api")
    def test_hd_get_count_of_topics_unlogin(self, cookies=None):
        count_of_articles_param = 5
        response = MyRequests.get(
            f"/api/happifiers/?page=1&page_size={count_of_articles_param}",
            cookies=cookies
        )

        Assertions.assert_code_status(response, 200)
        Assertions.assert_length_of_json(
            response,
            count_of_articles_param,
            f"Response does not contain {count_of_articles_param} keys",
        )


@allure.epic("[HD] Authorization cases")
class TestHDLogin(BaseCase):

    response = MainCase.signup()
    cookies = MainCase.cookies_marty_construction(response)

    @allure.label("HD", "Authorization")
    @allure.description("This test checks /happifiers+params api")
    def test_hd_get_last_article_login(self):
        TestHDUnlogin.test_hd_get_last_article_unlogin(
            self,
            cookies=self.cookies
        )

    @allure.label("HD", "Authorization")
    @allure.description("This test checks /api/happifiers/topics/ api")
    def test_hd_get_topics_login(self):
        TestHDUnlogin.test_hd_get_topics_unlogin(self, cookies=self.cookies)

    @allure.label("HD", "Authorization")
    @allure.description("This test checks /happifiers/[id] api")
    def test_hd_get_article_login(self, human_url=""):
        TestHDUnlogin.test_hd_get_article_unlogin(
            self,
            human_url=None,
            cookies=self.cookies
        ) # check getting article only by id

    @allure.label("HD", "unlogin")
    @allure.description("This test checks /happifiers+params api")
    def test_hd_get_count_of_topics_unlogin(self):
        TestHDUnlogin.test_hd_get_count_of_topics_unlogin(
            self,
            cookies=self.cookies
        )
