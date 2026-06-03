import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .hero {
        padding: 50px;
        border-radius: 20px;
        background: linear-gradient(
        135deg,
        #111827,
        #7c3aed
        );
        color:white;
        text-align:center;
    }

    .product-card {
        background:white;
        border-radius:15px;
        padding:20px;
        box-shadow:0 5px 15px rgba(0,0,0,0.1);
    }

    </style>
    """,
    unsafe_allow_html=True)
