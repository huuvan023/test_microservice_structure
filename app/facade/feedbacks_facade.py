from app.dto.feedback_request import FeedbackRequest
from service import feedback_service, download_service


def validate_data() -> bool:
    return True

def upload_image_to_s3():
    pass

def create_feedback(request: FeedbackRequest):
    # Add log here
    # Step 1: validate data
    validate_data()
    # Step 2: Upload image to s3
    upload_image_to_s3()
    # Step 3: Save to download
    download_service.save_download()
    # Step 4: Save data
    return feedback_service.save_feedback(feedback=request, None)
