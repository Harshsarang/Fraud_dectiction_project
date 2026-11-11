from pydantic import BaseModel, computed_field, Field
from typing import Literal, Annotated


class UserInput(BaseModel):

    amount: Annotated[float, Field(..., description= 'Enter your transaction amount')]
    your_balance_before_transaction: Annotated[float, Field(..., description= 'Enter your bank amount before transaction')]
    your_balance_after_transaction: Annotated[float, Field(..., description= 'Enter your bank amount after transaction')]
    receiver_balance_before_transaction: Annotated[float, Field(..., description= 'Enter receiver bank amount before transaction')]
    receiver_balance_after_transaction: Annotated[float, Field(..., description= 'Enter receiver bank amount after transaction')]

    @computed_field
    @property
    def balance_difference(self) -> float:
        return self.your_balance_before_transaction - self.your_balance_after_transaction
