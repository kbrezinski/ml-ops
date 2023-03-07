# API model schemas

from typing import List
from fastapi import Query
from pydantic import BaseModel, validator

# Base class for a text object of size 1
class Text(BaseModel):
    text: str = Query(None, min_length=1)

# List of text objects, each one defaults to None and has a min size of 1 char
class PredictPayload(BaseModel):
    texts: List[Text]
    
    # custom decorator to validate the list of texts
    @validator("texts")
    def list_must_not_be_empty(cls, value):
        if not len(value):
            raise ValueError("List of texts to classify cannot be empty.")
        return value
    
    # default example for the API docs for what PredictPayload should look like
    class Config:
        schema_extra = {
            "example": {
                "texts": [
                    {"text": "Transfer learning with transformers for text classification."},
                    {"text": "Generative adversarial networks in both PyTorch and TensorFlow."},
                ]
            }
        }