import allure


class TestCheckOfTestingByMachine:

    @allure.description("This test checks works the test \
        system by not using network")
    def test_logic(self):
        assert 1, "Test Machine does not work"
