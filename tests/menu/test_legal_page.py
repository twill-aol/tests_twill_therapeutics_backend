import allure
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.main_case import MainCase
from lib.my_requests import MyRequests


@allure.epic("[Menu] Legal")
class TestResourcesPage(BaseCase):
    '''Tests legal page'''
    @allure.label("menu", "page", "legal", "unlogin", "public")
    @allure.description("This test checks \
    /public/legal/")
    def test_resource_page(self):
        '''Get legal page'''
        response = MyRequests.get("/public/legal/")
        Assertions.assert_code_status(response, 200)
        flag_article_id = "Twill Therapeutics  |  "
        part_of_text = MainCase.finder_text(
            str(response.content),
            flag_article_id,
            "</title>"
        )
        assert "Legal" in part_of_text, 'Answer does not have "Legal"'
