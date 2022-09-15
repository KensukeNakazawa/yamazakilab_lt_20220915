from pydantic import BaseModel, Field

class SimpleInformationForTax(BaseModel):
    annual_income: int = Field(...)
    annual_medical_fee: int = Field(...)
