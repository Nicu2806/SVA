import streamlit as st
import streamlit.components.v1 as components
import os

def main():
    st.set_page_config(
        page_title="Recunoașterea Statistică a Formelor",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Read the HTML file
    html_file_path = os.path.join(os.path.dirname(__file__), 'test.html')
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Inject the HTML into Streamlit
    components.html(html_content, height=2000, scrolling=False)

if __name__ == "__main__":
    main()
