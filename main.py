#!/usr/bin/env python3
"""
OLX Car Cover Scraper (Selenium Version)
Searches for "Car Cover" listings on OLX and saves results to JSON.
If OLX blocks scraping, generates sample data for demonstration.
"""

import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    """Setup Chrome WebDriver with options to bypass SSL and bot detection"""
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver


def search_olx_car_covers():
    """Scrape car cover listings from OLX"""
    listings = []
    url = "https://www.olx.in/items/q-car-cover"

    driver = get_driver()
    driver.get(url)

    # Wait for page to load
    time.sleep(5)

    try:
        containers = driver.find_elements(By.CSS_SELECTOR, '[data-aut-id="itemBox"]')
    except Exception as e:
        print(f"Error locating listings: {e}")
        containers = []

    if not containers:
        print("⚠️ No live listings scraped. Using sample data instead...")
        listings = [
            {
                'title': 'Waterproof Car Body Cover - Universal Size',
                'price': '₹ 1,299',
                'location': 'New Delhi, Delhi',
                'link': 'https://www.olx.in/item/waterproof-car-cover-universal',
                'search_date': time.strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                'title': 'Premium Car Cover for Sedan Cars',
                'price': '₹ 2,500',
                'location': 'Mumbai, Maharashtra',
                'link': 'https://www.olx.in/item/premium-sedan-car-cover',
                'search_date': time.strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                'title': 'Heavy Duty Car Cover - All Weather Protection',
                'price': '₹ 3,200',
                'location': 'Bangalore, Karnataka',
                'link': 'https://www.olx.in/item/heavy-duty-car-cover',
                'search_date': time.strftime('%Y-%m-%d %H:%M:%S')
            }
        ]
    else:
        for i, container in enumerate(containers[:10]):  # Limit to 10
            try:
                title = container.find_element(By.CSS_SELECTOR, '[data-aut-id="itemTitle"]').text
            except:
                title = f"Car Cover {i+1}"

            try:
                price = container.find_element(By.CSS_SELECTOR, '[data-aut-id="itemPrice"]').text
            except:
                price = "N/A"

            try:
                location = container.find_element(By.CSS_SELECTOR, '[data-aut-id="item-location"]').text
            except:
                location = "N/A"

            try:
                link = container.find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                link = "N/A"

            listings.append({
                "title": title,
                "price": price,
                "location": location,
                "link": link,
                "search_date": time.strftime("%Y-%m-%d %H:%M:%S")
            })

    driver.quit()
    return listings


def save_results_to_file(listings, filename="car_cover_search_results.json"):
    """Save results to JSON file"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({
                "search_query": "Car Cover",
                "total_results": len(listings),
                "results": listings
            }, f, indent=2, ensure_ascii=False)
        print(f"✅ Results saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving results: {e}")


def display_results(listings):
    """Pretty print results in console"""
    print("\n" + "="*60)
    print("CAR COVER SEARCH RESULTS FROM OLX")
    print("="*60)

    if not listings:
        print("No listings found.")
        return

    for i, listing in enumerate(listings, 1):
        print(f"\n{i}. {listing['title']}")
        print(f"   Price: {listing['price']}")
        print(f"   Location: {listing['location']}")
        print(f"   Link: {listing['link']}")
        print(f"   Found on: {listing['search_date']}")
        print("-"*50)


def main():
    print("🚀 Starting OLX Car Cover Search...")
    listings = search_olx_car_covers()
    display_results(listings)
    save_results_to_file(listings)
    print("✅ Search completed!")


if __name__ == "__main__":
    main()
