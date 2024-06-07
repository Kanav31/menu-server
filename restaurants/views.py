# restaurant/views.py
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, HttpResponseRedirect
from .forms import RestaurantForm
from .models import MenuItem
from .scraper import scrape_menu_images
from selenium import webdriver
from .utils import process_menu_images 

def restaurant_menu(request, url=None):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            url = f"https://www.zomato.com/webroutes/getPage?page_url=/mumbai/{restaurant_name.lower().replace(' ', '-')}/menu&location=&isMobile=0"
            print(f"URL: {url}")
            # return HttpResponseRedirect(url)
    else:
        form = RestaurantForm()
    
    if url:
        # Scraping menu images
        menu_images_url = scrape_menu_images(url)
        print("Menu Images:", menu_images_url)
        # Perform OCR on menu images
        directory = 'restaurants/menu_images'
        process_menu_images (directory, restaurant_name)
        
    return render(request, 'menu.html', {'form': form})
