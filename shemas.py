from pydantic import BaseModel, Field
from datetime import date


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=1, max_length=20)
    last_name: str = Field(min_length=2, max_length=20)
    email: str = Field(min_length=10, max_length=50)
    telephon_number: str = Field(min_length=7, max_length=12)
    birthday: date = Field()
    description: str = Field(max_length=250)


class ContactResponse(BaseModel):
    contact_id: int
    first_name: str
    last_name: str
    email: str
    telephon_number: str
    birthday: date
    description: str

    class Config:
        from_attributes = True
