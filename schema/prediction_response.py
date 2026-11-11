from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):

    predicted_number: int = Field(
        description="Predicted class: 0 = Legitimate, 1 = Fraud",
        examples=[0]
    )

    confidence: float = Field(
        description="Confidence of the prediction in percentage",
        examples=[85.7]
    )

    class_probability: dict[str, float] = Field(
        description="Probability percentage for each class",
        examples=[{"0": 85.7, "1": 14.3}]
    )
