# restaurants/ocr_utils.py
import os
import cv2
import pytesseract
from pytesseract import Output
import csv
from .models import MenuItem

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = "C:/Users/Kanav College/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

def extract_menu_items(image_path, restaurant_name):
    # Load the image using OpenCV
    img = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply OCR on the image
    d = pytesseract.image_to_data(gray, output_type=Output.DICT)

    current_item = {}

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:  # Only consider texts with confidence > 60
            text = d['text'][i].strip()
            if text:
                # Heuristic to determine if text is an item name or a price
                if text.replace('.', '', 1).isdigit():
                    # Current text is a price
                    current_item['price'] = text
                    if 'name' in current_item:
                        # Save to database
                        MenuItem.objects.create(
                            restaurant_name=restaurant_name,
                            item_name=current_item['name'],
                            price=current_item['price']
                        )
                        current_item = {}
                else:
                    # Current text is an item name
                    current_item['name'] = text

def extract_menu_items(image_path, restaurant_name):
    # Load the image using OpenCV
    img = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply OCR on the image
    d = pytesseract.image_to_data(gray, output_type=Output.DICT)

    current_item = {}
    prev_text = ""

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:  # Only consider texts with confidence > 60
            text = d['text'][i].strip()
            if text:
                # Heuristic to determine if text is an item name or a price
                if text.replace('.', '', 1).isdigit():
                    # Current text is a price
                    if 'name' in current_item:
                        current_item['price'] = text
                        # Validate if price is a decimal number
                        if current_item['price'].replace('.', '', 1).isdigit():
                            # Save to database
                            MenuItem.objects.create(
                                restaurant_name=restaurant_name,
                                item_name=current_item['name'],
                                price=current_item['price']
                            )
                        current_item = {}
                else:
                    # Check if previous text and current text together form an item name
                    combined_text = prev_text + " " + text
                    if combined_text.replace('.', '', 1).isdigit():
                        # Previous text and current text together form an item name
                        current_item['name'] = combined_text
                    else:
                        # Previous text and current text are separate items
                        if 'name' in current_item:
                            # Validate if price is a decimal number
                            if current_item.get('price', '').replace('.', '', 1).isdigit():
                                # Save to database
                                MenuItem.objects.create(
                                    restaurant_name=restaurant_name,
                                    item_name=current_item['name'],
                                    price=current_item['price']
                                )
                        # Current text is an item name
                        current_item['name'] = text

                # Store the current text for the next iteration
                prev_text = text



def process_menu_images(directory, restaurant_name):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(directory, filename)
            extract_menu_items(image_path, restaurant_name)

