# OLX Car Cover Scraper (Selenium Version)

This project automates the process of searching **Car Covers** on OLX using **Python + Selenium**.  
The script extracts listing details (title, price, location, and link) and saves them into a JSON file.  

If OLX blocks automated scraping (due to SSL/bot protection), the script **falls back to sample data** so you can still demonstrate file-saving functionality.

---

## 🚀 Features
- Scrapes car cover listings from OLX  
- Extracts:
  - Title  
  - Price  
  - Location  
  - Link  
  - Search timestamp  
- Saves results to `car_cover_search_results.json`  
- Pretty prints listings in the console  
- Falls back to **sample listings** if scraping fails  
- Bypasses SSL warnings and some bot detection techniques  

---

## 📦 Requirements
Install dependencies before running:

```bash```
pip install selenium webdriver-manager

Run the scraper with:
python main.py
