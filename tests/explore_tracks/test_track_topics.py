import allure
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Track] Topics")
class TestTracksTopics(BaseCase):
    '''Tests Track Topics'''
    exclude_params_subscribe = [
        # ("FK", ("CARE", "EN", "PT", "PYK")),
        # ("LI", ("DM", "BD", "FC")),
        # ("MF", ("CF", "COMP", "SA", "SD")),
        ("PG", ("FMC", "GU", "OT", "SCA")),
        # ("SW", ("DA", "HLF", "SR", "CC")),
        ("WC", ("CS", "FWB", "WLB", "MP"))
    ]

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("track", "topics", "authorization", "smoke")
    @allure.description("This test checks /api/v2/tracks/life-domains/ \
    and /api/v2/tracks/life-domains/[topic]/ api")
    @pytest.mark.parametrize("topic", exclude_params_subscribe)
    def test_topics_of_track(self, topic):
        f'''Get {topic[0]} topic data and individually'''
        response = MyRequests.get(
            "/api/v2/tracks/life-domains/",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        # content = str(response.content)
        # assert topic[0] in content,\
        #     f"Topic {topic[0]} doesn't meet expectations"

    @allure.label("topics", "subtopics", "authorization", "smoke")
    @allure.description("This test checks /api/v2/tracks/life-domains/ \
    and /api/v2/tracks/life-domains/[topic]/ api")
    @pytest.mark.parametrize("topic", exclude_params_subscribe)
    def test_subtopics_of_topics(self, topic):
        response = MyRequests.get(
            f"/api/v2/tracks/life-domains/{topic[0]}/life-conditions/tracks/",
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        # content = str(response.content)
        # for suptopic in topic[1]:
        #     assert suptopic in content,\
        #         f"Subtopic {suptopic} doesn't meet expectations"
