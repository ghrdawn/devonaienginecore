import streamlit as st
import time
import requests


def main():
    st.set_page_config(  # Alternate names: setup_page, page, layout
        # Can be "centered" or "wide". In the future also "dashboard", etc.
        layout="wide",
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        # String or None. Strings get appended with "• Streamlit".
        page_title="Devon AI Engine Core",
        page_icon=None,  # String, anything supported by st.image, or None.
    )
    st.title("Devon AI Engine Core")
    """This app enables you to develop faster!"""

    inp = st.text_area(
        "Ask me for help:", placeholder="Type here", max_chars=2000, height=150
    )

    response = None
    with st.form(key="inputs"):
        submit_button = st.form_submit_button(label="Generate!")

        if submit_button:

            payload = {
                "inputs": inp + ". Answer:",
                "parameters": {
                    "max_length": 500,
                    "stop_sequences": ["\n\n"],
                    "skip_special_tokens": True,
                    "return_full_text": False,
                    "repetition_penalty": 1.1,
                    "top_p": 0.7,
                    "top_k": 40,
                    "temperature": 0.3
                }
            }
            API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-j-6B"
            headers = {
                "Authorization": "Bearer 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"}

            query = requests.post(API_URL, headers=headers, json=payload, verify=False)
            response = query.json()
            response = response[0]

            st.text(response["generated_text"])

    if False:
        col1, col2, *rest = st.beta_columns([1, 1, 10, 10])

        def on_click_good():
            response["rate"] = "good"
            print(response)

        def on_click_bad():
            response["rate"] = "bad"
            print(response)

        col1.form_submit_button("👍", on_click=on_click_good)
        col2.form_submit_button("👎", on_click=on_click_bad)

    st.text("Copyright @Devon")


if __name__ == "__main__":
    main()
