import streamlit
import streamlit as st
import requests
st.title('Big Bag courier')
st.write("Hello, welcome to Big Bag!")

API_URL = "http://127.0.0.1:8000/docs"  # Assuming FastAPI is running locally
def register_user():
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        response = requests.post(f"{API_URL}/register/", json={"name": name, "email": email, "password": password})
        st.write(response.json())

def create_order():
    user_id = st.number_input("User ID", min_value=1)
    country_id = st.number_input("Country ID", min_value=1)
    parcel_size = st.number_input("Parcel Size (cm³)", min_value=1)
    parcel_weight = st.number_input("Parcel Weight (kg)", min_value=1)

    if st.button("Create Order"):
        order_data = {
            "user_id": user_id,
            "country_id": country_id,
            "parcel_size": parcel_size,
            "parcel_weight": parcel_weight
        }
        response = requests.post(f"{API_URL}/create_order/", json=order_data)
        st.write(response.json())

st.title("Shipping System")
page = st.sidebar.selectbox("Choose a page", ["Register", "Create Order"])

if page == "Register":
    register_user()
elif page == "Create Order":
    create_order()

#streamlit run C:\Users\Admin\PycharmProjects\newStreamlit\streamlt.py