from typing import Literal
from typing import List
from pydantic import BaseModel, Field
from app.dto.model.question_type import QuestionType

class Question(BaseModel):
    questionType: QuestionType = Field(
        description="Type of the question: SINGLE_CHOICE, MULTIPLE_CHOICE, TEXT_RESPONSE"
    )
    title: str = Field(
        description="Content of the question"
    )
    isRequired: bool = Field(
        description="Indicates whether answering the question is mandatory"
    )
    choices: List[str] = Field(
        description="Options for multiple-choice questions"
    )
    isAllowOther: bool = Field(       
        description="Indicates whether to allow an 'Other' response for multiple-choice questions"
    )