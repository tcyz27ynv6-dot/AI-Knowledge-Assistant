import streamlit as st
import requests

st.title("AI Knowledge Assistant")

question = st.text_input("Ask a question")

if st.button("Ask"):

    if not question:
        st.warning("Please enter a question.")
        st.stop()

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"question": question}
    )

    result = response.json()

    st.success("Answer Generated")

    st.subheader("Answer")

    st.write(
        result["answer"]
    )

    st.subheader("Sources")

    for source in result["sources"]:
        st.markdown(
            f"📄 {source['source']}"
        )