import allure
import random
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


# @allure.epic("[Assessment] HA")
# class TestHA(BaseCase):
#     '''Tests HA'''

#     user_id, email, cookies = MainCase.signup_router()

#     @allure.label("ha", "assessment", "profile", "authorization")
#     @allure.description("This test checks \
#     /api/happiness_assessment/result/")
#     def test_ha_result(self):
#         '''Get HA status in Community'''
#         response = MyRequests.get(
#             "/api/happiness_assessment/result/",
#             cookies=self.cookies
#         )
#         Assertions.assert_code_status(response, 200)
