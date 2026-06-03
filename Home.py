import streamlit as st
from utils.styles import load_css

load_css()

st.markdown("""
<div class="hero">
<h1>MonaFit</h1>
<h3>Fashion That Fits You</h3>
</div>
""",
unsafe_allow_html=True)

st.write("")

col1,col2,col3 = st.columns(3)

with col1:
    st.image(
        "https://picsum.photos/300",
        use_container_width=True
    )
    st.write("Women's Collection")

with col2:
    st.image(
        "https://picsum.photos/301",
        use_container_width=True
    )
    st.write("Men's Collection")

with col3:
    st.image(
        "https://picsum.photos/302",
        use_container_width=True
    )
    st.write("Accessories")
