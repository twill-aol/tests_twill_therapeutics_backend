import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Today] Current Track")
class TestCurrentTrack(BaseCase):
    '''Tests Current Track'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("track", "сurrent", "authorization", "smoke")
    @allure.description("This test checks /api/kabinet-homepage/")
    def test_home_page(self):
        '''Get search tracks'''
        response = MyRequests.get(
            "/api/kabinet-homepage/",
            cookies=self.cookies
        )
        track_id = self.response_to_json(response)["track"]["id"]
        response = MyRequests.get(
            f"/api/tracks/{track_id}/",
            cookies=self.cookies
        )

        # response_as_dict = self.response_to_json(response)
        Assertions.assert_code_status(response, 200)
        # # if track started
        # Assertions.assert_json_has_keys(
        #     response,
        #     [
        #         "id",
        #         "name",
        #         "description_html",
        #         "small_square_image",
        #     ]
        # )
