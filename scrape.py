#!/usr/bin/env python3
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

# --- Scrape website ---
def scrape_website(url):
    """Scrape website HTML content. Use requests first; Selenium only if JS-heavy"""
    try:
        # Try simple requests first (faster)
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except:
        # Fallback: Selenium for JS-rendered pages
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(service=Service(), options=options)
        try:
            driver.get(url)
            return driver.page_source
        finally:
            driver.quit()

# --- Extract body content ---
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

# --- Clean text content ---
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()
    cleaned = "\n".join(line.strip() for line in soup.get_text(separator="\n").splitlines() if line.strip())
    return cleaned

# --- Optional: Split for large text ---
def split_dom_content(dom_content, max_length=5000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]
