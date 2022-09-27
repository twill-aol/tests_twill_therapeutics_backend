import allure
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Activities] by Skill")
class TestActivitiesSkill(BaseCase):
    '''Tests with autorization'''

    response = MainCase.signup()
    user_id = BaseCase.response_to_json(response)["user_id"]
    email = BaseCase.response_to_json(response)["user"]["email"]
    cookies = MainCase.cookies_marty_construction(response)

    @allure.label("Activities", "login", "skills")
    @allure.description("This test checks /api/activities \
    and api/v3/activity_status api")
    def test_activities_skill(self):
        '''New activity initializes and get its id'''
        with allure.step(f"Complete S-02 activity"):
            response = MyRequests.get("/api/activities/S-02/activity_status/", cookies=self.cookies)
            activity_id = BaseCase.response_to_json(response)["id"]
            data = {"is_complete": True}
            response = MyRequests.post(f"/api/v3/activity_status/{activity_id}/", json=data, cookies=self.cookies)
            Assertions.assert_code_status(response, 200)
            Assertions.assert_json_has_keys(
                response,
                [
                    "scores_old",
                    "image",
                    "show_levelup_modal",
                    "scores_current",
                    "is_first_activity",
                    "is_earned",
                ]
            )
        with allure.step(f"Check skill points in user's stats"):
            response = MyRequests.get(f"/api/users/{self.user_id}/scores/", cookies=self.cookies)
            Assertions.assert_code_status(response, 200)
            points = self.response_to_json(response)["skills"]["SA"]['points']
            assert points == 21, f"Current points does not = 21"