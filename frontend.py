
import streamlit as st
import requests

API_URL = "http://16.171.255.195:8001/predict"

st.title("Fraud Transaction Prediction")
st.markdown("Enter your transaction details below.")

# User inputs
amount = st.number_input("Transaction Amount", min_value=0.0)
your_balance_before_transaction = st.number_input(
    "Your Bank Balance Before Transaction", min_value=0.0
)
your_balance_after_transaction = st.number_input(
    "Your Bank Balance After Transaction", min_value=0.0
)
receiver_balance_before_transaction = st.number_input(
    "Receiver Balance Before Transaction", min_value=0.0
)
receiver_balance_after_transaction = st.number_input(
    "Receiver Balance After Transaction", min_value=0.0
)

if st.button("Predict Transaction"):

    input_data = {
        "amount": amount,
        "your_balance_before_transaction": your_balance_before_transaction,
        "your_balance_after_transaction": your_balance_after_transaction,
        "receiver_balance_before_transaction": receiver_balance_before_transaction,
        "receiver_balance_after_transaction": receiver_balance_after_transaction
    }

    try:
        response = requests.post(
            API_URL,
            json=input_data,
            timeout=30
        )

        if response.status_code == 200:

            result = response.json()

            # Extract values directly from API response
            prediction = result["predicted_number"]
            confidence = result["confidence"]
            probabilities = result["class_probability"]

            st.subheader("Prediction Result")

            # Assuming 0 = Non-Fraud and 1 = Fraud
            if prediction == 1:
                st.error("Warning! This transaction is predicted as FRAUD.")
            elif prediction == 0:
                st.success("This transaction is predicted as NON-FRAUD.")

            st.metric("Prediction Confidence", f"{confidence}%")

            st.subheader("Class Probabilities")

            st.write(f"Non-Fraud: {probabilities['0']}%")
            st.progress(float(probabilities["0"]) / 100)

            st.write(f"Fraud: {probabilities['1']}%")
            st.progress(float(probabilities["1"]) / 100)

        else:
            st.error(
                f"API Error: {response.status_code} - {response.text}"
            )

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server.")

    except requests.exceptions.Timeout:
        st.error("The API request timed out.")

    except (KeyError, ValueError, requests.exceptions.JSONDecodeError) as e:
        st.error(f"Invalid API response: {e}")

