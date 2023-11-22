from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class wait_for_testing_complete(object):

    def __init__(self):
        pass

    def __call__(self, driver):
        return driver.find_element(By.CSS_SELECTOR, "div.card-body div.successTest")

def run_test():
    driver = webdriver.Chrome()
    
    driver.get("https://speedtest.btwholesale.com/details")

    WebDriverWait(driver, 60).until(wait_for_testing_complete())

    ping = int(driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/h3').text)
    download_speed = float(driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/h3').text)
    upload_speed = float(driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/div/div/div[2]/div/h3').text)
    
    driver.close()

    return ping, download_speed, upload_speed

if __name__ == "__main__":
    ping, download_speed, upload_speed = run_test()

    print("%d ms - \u2193 %f Mbps \u2191 %f Mbps" % (ping, download_speed, upload_speed))
