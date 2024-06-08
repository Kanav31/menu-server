Certainly! Here's an improved and more detailed README content for your project:

---

# Menu Image Scraper and OCR Processor

This project is designed to scrape food menu images from Zomato for specific restaurants in Mumbai, process these images using OCR (Optical Character Recognition) with `pytesseract`, and store the extracted content in a Django SQL database.

## Features

- Scrapes menu images from Zomato for specified restaurants in Mumbai.
- Uses `pytesseract` to perform OCR on the menu images.
- Stores the extracted menu content in a Django SQL database.

## Assumptions

1. **Full Restaurant Name**: 
    - When providing a restaurant name, ensure you provide the complete name as it appears on Zomato.
    - For example, for the restaurant "Epitome The Lower Parel" in Mumbai, you must provide the full name. Simply entering "Epitome" will not work and will cause the application to crash.
    - Another example: "The Global Adda Dadar Shivaji Park".

2. **Mumbai Restaurants**:
    - The API endpoint currently targets restaurants in Mumbai. If you need to scrape menus from restaurants in a different city, you will need to modify the API endpoint accordingly.

## How to Use

1. **Check the Restaurant Name on Zomato**:
    - Before using the application, verify the restaurant's name by searching for it on Zomato.
    - Make sure to enter the complete name as it appears in the Zomato URL.

2. **API Endpoint for Mumbai**:
    - The current API endpoint for scraping menu images in Mumbai:
    ```
    https://www.zomato.com/webroutes/getPage?page_url=/mumbai/{restaurant_name.lower().replace(' ', '-')}/menu&location=&isMobile=0
    ```

3. **Changing the Location**:
    - If you need to scrape menus for restaurants in a different city, modify the API endpoint to reflect the new location. For example, for restaurants in NCR, use:
    ```
    https://www.zomato.com/webroutes/getPage?page_url=/ncr/{restaurant_name.lower().replace(' ', '-')}/menu&location=&isMobile=0
    ```

    - Make sure to provide the full restaurant name as per the Zomato URL, like:
    ```
    ncr/cé-la-vie-kitchen-bar-connaught-place-new-delhi
    ```

## Steps to Run the Project

1. **Setup Django Project**:
    - Ensure you have Django installed in your environment.
    - Set up your Django project and create a Django app for managing the restaurant menus.

2. **Scrape Menu Images**:
    - Use the provided API endpoint to scrape the menu images from Zomato for the specified restaurant.
    - Store these images in the `menu_images` folder inside the `restaurant` app.

3. **Perform OCR on Menu Images**:
    - Use `pytesseract` to extract text from the scraped menu images.
    - Ensure `pytesseract` is installed and configured properly in your environment.

4. **Store Extracted Content in the Database**:
    - Process the OCR results and store the extracted menu content in your Django SQL database.

## Example Usage

Here's a basic example of how to scrape and process a menu for a specific restaurant:

```python
import requests
import pytesseract
from PIL import Image
from io import BytesIO
from django.conf import settings
from myapp.models import MenuItem

# Function to fetch menu image from Zomato
def fetch_menu_image(restaurant_name):
    restaurant_url = f"https://www.zomato.com/webroutes/getPage?page_url=/mumbai/{restaurant_name.lower().replace(' ', '-')}/menu&location=&isMobile=0"
    response = requests.get(restaurant_url)
    # Process response to get image URLs
    # Assume image_url is extracted
    return image_url

# Function to perform OCR on the image
def process_menu_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    text = pytesseract.image_to_string(img)
    return text

# Function to save OCR result to database
def save_menu_to_db(restaurant_name, menu_text):
    for item in menu_text.split('\n'):
        MenuItem.objects.create(restaurant_name=restaurant_name, item_name=item)

# Main function to scrape and process menu
def scrape_and_process_menu(restaurant_name):
    image_url = fetch_menu_image(restaurant_name)
    menu_text = process_menu_image(image_url)
    save_menu_to_db(restaurant_name, menu_text)

# Example usage
scrape_and_process_menu('Epitome The Lower Parel')
```

## Requirements

- Django
- Requests
- Pillow
- Pytesseract

## Installation

1. Install Django:
    ```
    pip install django
    ```

2. Install Requests:
    ```
    pip install requests
    ```

3. Install Pillow:
    ```
    pip install pillow
    ```

4. Install Pytesseract:
    ```
    pip install pytesseract
    ```

5. Ensure Tesseract-OCR is installed on your system:
    - On Ubuntu:
        ```
        sudo apt-get install tesseract-ocr
        ```
    - On macOS using Homebrew:
        ```
        brew install tesseract
        ```

## Conclusion

By following the above steps, you will be able to scrape menu images from Zomato, perform OCR to extract menu content, and store the extracted data in a Django SQL database. Make sure to provide the full and correct restaurant name as per Zomato to avoid any issues.

---
SQL DB Image
![image](https://github.com/Kanav31/menu-server/assets/90086445/a7a4392a-0f35-4682-b70f-711e2b33809b)

Feel free to adapt this README further to fit any additional requirements or details specific to your project.
