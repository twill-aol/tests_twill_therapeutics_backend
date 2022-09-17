import Assertions
import BaseCase
import MyRequests


class TestHDUnlogin(BaseCase):
    def test_hd_get_last_article(self):
        response = MyRequests.get("/happifiers/daily/")

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


    def test_hd_get_topics(self):
        response = MyRequests.get("/happifiers/topics/")

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
                "type"
            ],
            0
            )


    def test_hd_get_last_articles(self):
        for article_id in range(1, 11, 2):
            response = MyRequests.get(f"/happifiers/{article_id}/")
            if response.status_code == 200:
                Assertions.assert_code_status(response, 200)
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
                        "video_url"
                    ],
                    )
                break