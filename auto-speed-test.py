from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class wait_for_testing_complete(object):

    def __init__(self):
        pass

    def __call__(self, driver):
        """
        I feel I should explain the horror here.
        In order to detect when the speed test has completed, a change needs to be detected on the page.
        Since the test results are shown in a flash window (why, BT, why FLASH?), there's no way to detect that,
        Instead, we look for the correct HTML for the navigation banner at the top of the page.
        The "Results" tab changes colour to green when complete. Each tab is actually just an image, so
        look for the correct img tags in the innerHTML of the headtry element.

        I'm so very, very sorry.
        """
        expected_inner_html = "<img src=\"images/home_grey.JPG\" alt=\"\" width=\"78\" height=\"25\" border=\"0\"><img src=\"images/testing_test.JPG\" alt=\"\" width=\"78\" height=\"25\" border=\"0\"><img src=\"images/results_gr.JPG\" alt=\"\" width=\"78\" height=\"25\" border=\"0\">"
        actual_inner_html = driver.find_element_by_id("headtry").get_attribute("innerHTML")
        return actual_inner_html == expected_inner_html

def run_test():
    driver = webdriver.Chrome()
    
    driver.get("http://speedtest.btwholesale.com/")

    driver.switch_to.frame("f2")

    driver.find_element_by_id("Yes").click()

    driver.find_element_by_xpath("//input[@name='fttpbeta']").click()

    WebDriverWait(driver, 60).until(wait_for_testing_complete())

    driver.switch_to.default_content();
    driver.switch_to.frame("f2")
    
    download_speed = float(driver.find_element_by_xpath("//input[@id='downloadSpeed']").get_attribute("value"))/1000
    upload_speed = float(driver.find_element_by_xpath("//input[@id='uploadSpeed']").get_attribute("value"))/1000
    
    driver.close()

    return download_speed, upload_speed

if __name__ == "__main__":
    download_speed, upload_speed = run_test()
    
    print("Download {} Mbps".format(download_speed))
    print("Upload {} Mbps".format(upload_speed))