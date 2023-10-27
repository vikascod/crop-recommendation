from pydantic import BaseModel


class CropInput(BaseModel):
    N = float
    P = float
    K = float
    temperature = float
    humidity = float
    pH = float
    rainfall = float
    class Config:
        schema_extra = {
            "example":{
                "N":113,
                "P":38,
                "K":20,
                "temperature":22.10718988,
                "humidity":78.58320116,
                "pH":25,
                "rainfall":60
            }
        }