from app.dto.model.section import Section
from pydantic import BaseModel


class EditSectionWithChatRequest(BaseModel):
    session_id: str
    survey_data: Section
    user_prompt: str
