from pydantic import BaseModel, Field

from domain.schema.Feedback import Feedback


def build_image_url(file_id:str):
    return f"http://c-diam/com/images/{file_id}"

class FeedbackResponse(Feedback):
    fileUrl: str = Field()

    @classmethod
    def from_orm(cls, feedback: Feedback):
        feedback_read = super().from_orm(feedback)
        feedback_read.mediaUrl = build_image_url(feedback.file_id)
        return feedback_read