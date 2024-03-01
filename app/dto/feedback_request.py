from pydantic import BaseModel, Field

from domain.schema.Feedback import Feedback


def build_image_url(file_id:str):
    return f"http://c-diam/com/images/{file_id}"

class FeedbackRequest(Feedback):
    current_path: str = Field()