from selenium import webdriver

def test_ThoughtcodersLoading():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://thoughtcoders.com/")
    title =driver.title
    print(title)
    driver.close
    assert title =='ThoughtCoders | QA Services, Application Development and Training Solutions - Thoughtcoders'