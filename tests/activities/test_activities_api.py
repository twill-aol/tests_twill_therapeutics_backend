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
        response = MyRequests.get("/api/activities/S-02/activity_status/", cookies=self.cookies)
        activity_id = BaseCase.response_to_json(response)["id"]
        # print(activity_id)
        data = {
            "is_complete": True,
            "is_doing": False,
            "selected_tip_id": "S-02-OVERVIEW",
            "happy_face":"1",
            "image":{
                "id":"875584",
                "source":"happify",
                "is_processed": True,
                "small":{
                    "url":"https://hpf-happify-b2c-eu-qa-03-user-uploads.happify.com/user_uploads/images/9cc2/a51f/9cc2a51f4cc9db5c87ba35efaa08e56e215b67d5_180.jpeg",
                    "width":"180",
                    "height":"120"
                },
                "medium":{
                    "url":"https://hpf-happify-b2c-eu-qa-03-user-uploads.happify.com/user_uploads/images/9cc2/a51f/9cc2a51f4cc9db5c87ba35efaa08e56e215b67d5_370.jpeg",
                    "width":"370",
                    "height":"247"
                },
                "large":{
                    "url":"https://hpf-happify-b2c-eu-qa-03-user-uploads.happify.com/user_uploads/images/9cc2/a51f/9cc2a51f4cc9db5c87ba35efaa08e56e215b67d5_600.jpeg",
                    "width":"600",
                    "height":"400"
                },
                "thumbnail":{
                    "url":"https://hpf-happify-b2c-eu-qa-03-user-uploads.happify.com/user_uploads/images/9cc2/a51f/9cc2a51f4cc9db5c87ba35efaa08e56e215b67d5_72.jpeg",
                    "width":"72",
                    "height":"48"
                },
                "image_picker":{
                    "url":"https://hpf-happify-b2c-eu-qa-03-user-uploads.happify.com/user_uploads/images/9cc2/a51f/9cc2a51f4cc9db5c87ba35efaa08e56e215b67d5_110.jpeg",
                    "width":"110",
                    "height":"73"
                },
                "profile_post":{
                    "url":"https://hpf-happify-b2c-eu-qa-03-user-uploads.happify.com/user_uploads/images/9cc2/a51f/9cc2a51f4cc9db5c87ba35efaa08e56e215b67d5_222.jpeg",
                    "width":"222",
                    "height":"148"
                },
                "aspect_ratio":"1.5",
                "description":"Flags and lamps"
            },
            "image_id":"875584",
            "permission":"FOLLOWERS",
            "long_text":"2022"
        }
        response = MyRequests.post(f"/api/v3/activity_status/{activity_id}/", data=data, cookies=self.cookies)
        print(BaseCase.response_to_json(response))
