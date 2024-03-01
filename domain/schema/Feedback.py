from pydantic import Field
from sqlalchemy import Integer, Column


class Feedback(SQLModel):
    id: int = Field(
        nullable=False,
        sa_column=Column(Integer,
                         nullable=False,
                         autoincrement=True,
                         primary_key=True)
    )
