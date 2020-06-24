import pytest
from pages.google_home_page import GoogleHomePage
from pages.google_result_page import GoogleResultPage


@pytest.mark.parametrize('something', ['golife', 'goclean', 'gojek'])
class TestGooglingPom():
    def test_search_golife(self, browser, something):
        search_page = GoogleHomePage(browser)
        result_page = GoogleResultPage(browser)
        search_page.load()
        search_page.search_for(something)
        inputed = result_page.get_search_input()
        print(inputed)
        assert inputed == something
        assert something in result_page.title()
