from typing import List

from fastapi import APIRouter

from app.dto.feedback_request import FeedbackRequest
from app.dto.feedback_response import FeedbackResponse
from app.facade import feedbacks_facade

router = APIRouter(
    prefix="/admin/feedback",
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=List[FeedbackResponse])
def create_feedback(request: FeedbackRequest):
    # Can put a log here
    return feedbacks_facade.create_feedback(request)
