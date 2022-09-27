import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Activities] Kindness Chain")
class TestKindnessChain(BaseCase):
    '''Tests Kindness Chain activity'''

    response = MainCase.signup()
    user_id = BaseCase.response_to_json(response)["user_id"]
    email = BaseCase.response_to_json(response)["user"]["email"]
    cookies = MainCase.cookies_marty_construction(response)

    @allure.label("Activities", "login", "Kindness Chain", "KC")
    @allure.description("This test checks /api/activities \
    and api/v3/activity_status api")
    def test_activities_skill(self):
        '''New activity initializes and get its id'''
        params = {
            "text": "You Make Me Laugh",
            "from_email": "aqa@bot.com",
            "from_name": "bot",
            "to_email": "reciver@test.com"
        }
        response = MyRequests.post(
            "/api/kindness_chain/create/",
            json=params,
            cookies=self.cookies
        )
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys(
            response,
            [
                "compliment_id",
                "chain_id"
            ]
        )
