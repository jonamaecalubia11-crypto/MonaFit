import streamlit as st

def initialize_cart():

    if "cart" not in st.session_state:
        st.session_state.cart = []

def add_to_cart(product):

    st.session_state.cart.append(product)

def remove_from_cart(index):

    st.session_state.cart.pop(index)
