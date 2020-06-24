from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_direct_usage():
    driver = webdriver.Chrome()
    driver.get("https://google.co.id")
    driver.implicitly_wait(10)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('Fachrul Choliluddin'+ Keys.ENTER)
    assert 'Fachrul Choliluddin' in driver.title
    driver.quit()


#  Using pytest
def test_searching():
    # Given I open google
    # When I search "Fachrul Choliluddin"
    # Then I should see search result contain "Celotehan si FachrulCH"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://google.co.id')
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('fachrul choliluddin'+ Keys.ENTER)
    results_title = driver.find_elements_by_css_selector('h3')
    results = [title.text for title in results_title]
    print(results)
    expected_link = "Celotehan si FachrulCH"
    matches = [text for text in results if expected_link.lower() in text.lower()]
    print(matches)
    assert len(matches) > 0
    driver.quit()