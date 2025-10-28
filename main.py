import streamlit as st
from scrape import scrape_website, clean_body_content, extract_body_content
from parse import parse_with_ollama

st.title("🌐 AI Web Scraper & Parser")

# --- Input URL ---
url = st.text_input("Enter a website URL:")

# --- Scrape Site ---
if st.button("Scrape Site"):
    if url.strip() == "":
        st.warning("Please enter a valid URL")
    else:
        st.info("Scraping website... ⏳")
        try:
            html_content = scrape_website(url)
            visible_text = clean_body_content(extract_body_content(html_content))
            st.session_state.visible_text = visible_text
            st.text_area("Website Text Content", visible_text, height=300)
            st.success("Scraping complete!")
        except Exception as e:
            st.error(f"Error scraping website: {e}")

# --- Parse Section ---
if "visible_text" in st.session_state:
    parse_description = st.text_area("What information do you want to extract?")
    if st.button("Parse Content"):
        if parse_description.strip() == "":
            st.warning("Please enter a valid parse description")
        else:
            st.info("Parsing content... ⏳")
            result = parse_with_ollama(st.session_state.visible_text, parse_description)
            st.subheader("🧠 Parsed Output")
            st.write("Result", result, height=300)
