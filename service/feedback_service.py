from domain.schema.Feedback import Feedback


def save_feedback(feedback: Feedback, db: Session):
    db.save(feedback)

# Ngoài ra ở đay có th xử lý nhiều function liên quan tới db phức tạp khác
