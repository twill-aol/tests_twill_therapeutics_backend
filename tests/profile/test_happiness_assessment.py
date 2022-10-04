import allure
import random
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Assessment] HA")
class TestHA(BaseCase):
    '''Tests HA'''

    user_id, email, cookies = MainCase.signup_router()

    @allure.label("ha", "assessment", "profile", "authorization")
    @allure.description("This test checks \
    /api/happiness_assessment/result/")
    def test_ha_complete(self):
        '''Get HA status'''
        def test_ha_result(self):
            response = MyRequests.get(
                "/api/happiness_assessment/result/",
                cookies=self.cookies
            )
            Assertions.assert_code_status(response, 200)
            return response
        response = test_ha_result(self)
        len_ha_res = len(BaseCase.response_to_json(response)["result"])
        assert len_ha_res == 0, "New user has HA-result"
        ha_id = BaseCase.response_to_json(response)["dialog"]["dialog_id"]
        type_question = "single_obj"
        data = {"client_input": str(random.randint(1, 4))}
        while type_question != "end":
            response = MyRequests.post(
                f"/api/assessment/v1/dialogs/{ha_id}/conversation/",
                json=data,
                cookies=self.cookies
            )
            Assertions.assert_code_status(response, 200)
            Assertions.assert_json_has_keys(
                response,
                [
                    "conversation_id",
                    "turn_number"
                ]
            )
            conversation_id = \
                BaseCase.response_to_json(response)["conversation_id"]
            data = {
                "client_input": str(random.randint(1, 4)),
                "conversation_id": conversation_id
            }
            type_question = BaseCase.response_to_json(response)["data"]["type"]
        response = test_ha_result(self)
        len_ha_res = len(BaseCase.response_to_json(response)["result"])
        assert len_ha_res > 0, "User doesn't have HA-result"
