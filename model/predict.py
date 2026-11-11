
import pickle
import pandas as pd

# Load trained model
with open('model/model_1.pkl', 'rb') as f:
    model = pickle.load(f)

# Get class labels
class_labels = model.classes_.tolist()


def predict_output(user_input: dict):

    # Convert user input into DataFrame
    input_df = pd.DataFrame([user_input])

    # Prediction
    output = model.predict(input_df)[0]

    # Prediction probabilities
    probabilities = model.predict_proba(input_df)[0]

    # Confidence of predicted class
    confidence = float(max(probabilities)*100)

    # Probability of each class
    class_proba = {
        str(label): round(float(probability)*100, 4)
        for label, probability in zip(class_labels, probabilities)
    }

    return {
        "predicted_number": int(output),
        "confidence": round(confidence, 4),
        "class_probability": class_proba
    }
