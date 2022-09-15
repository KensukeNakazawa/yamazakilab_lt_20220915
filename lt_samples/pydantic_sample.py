from pydantic import BaseModel, Field, conint


class BoundixBox(BaseModel):
    x1: conint(gt=0) = Field(
        ...,
        description='hogehoge'
    )
    
class RGB(BaseModel):
    r: conint(ge=0, le=255) = Field(
        ...,
        description=''
    )
    g: conint(ge=0, le=255) = Field(
        ...,
        description=''
    )
    b: conint(ge=0, le=255) = Field(
        ...,
        description=''
    )

    @property
    def rgb(self):
        return (self.r, self.g, self.b)
