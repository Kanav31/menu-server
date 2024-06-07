import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_menu_images(url):
    headers = {
        'Cookie': '_gcar_id=0696b46733edeac962b24561ce67970199ee8668',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        sections = data.get('page_data', {}).get('sections', {})
        menu_items = sections.get('SECTION_IMAGE_MENU', {}).get('menuItems', [])

        image_urls = []
        for item in menu_items:
            pages = item.get('pages', [])
            for page in pages:
                image_url = page.get('url')
                if image_url:
                    image_urls.append(image_url)

        # Define the directory to save images
        directory = 'restaurants/menu_images'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Setup Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        for image_url in image_urls:
            driver.get(image_url)
            image_data = driver.get_screenshot_as_png()
            filename = os.path.basename(image_url)
            filepath = os.path.join(directory, filename)
            with open(filepath, 'wb') as f:
                f.write(image_data)

        driver.quit()

        return image_urls
    else:
        print("Error:", response.status_code)
        return []
