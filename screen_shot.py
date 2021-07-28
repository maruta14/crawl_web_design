import os
import sys
from selenium import webdriver
import time

def main():
    # File Name
    FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/screen2.png")

    # Chrome のオプションを設定する
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Selenium Server に接続する
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=options.to_capabilities(),
        options=options,
    )

    # Selenium 経由でブラウザを操作する
    url = 'https://www.playstation.com/ja-jp/'
    driver.get(url)

    # get width and height of the page
    # w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")

    # set window size
    driver.set_window_size(1500, h)

    time.sleep(3)
    # Get Screen Shot
    driver.save_screenshot(FILENAME)

    # ブラウザを終了する
    driver.quit()

if __name__=="__main__":
    main()