import streamlit as st
import pandas as pd

products = pd.DataFrame({

    "Name":[
        "Oversized Shirt",
        "Denim Jacket",
        "Graphic Tee"
    ],

    "Price":[
        799,
        1499,
        699
    ]
})

st.title("🛍 Shop")

search = st.text_input(
    "Search Product"
)

filtered = products[
    products["Name"]
    .str.contains(search,
    case=False)
]

for i,row in filtered.iterrows():

    col1,col2 = st.columns([1,2])

    with col1:
        st.image(
            "https://picsum.photos/200"
        )

    with col2:
        st.subheader(row["Name"])
        st.write(
            f"₱{row['Price']}"
        )

        if st.button(
            "Add to Cart",
            key=i
        ):
            st.session_state.cart.append(
                row.to_dict()
            )
