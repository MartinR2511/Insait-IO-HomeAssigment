"""create questions table

Revision ID: 9de9a5556a9e
Revises: 
Create Date: 2024-07-02 15:22:52.282501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9de9a5556a9e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA homeassigment")
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("question", sa.String(4096), nullable=False), 
        sa.Column("answer", sa.String(4096), nullable=False),   
        sa.Column("timestamp", sa.DateTime, nullable=True),
        schema="homeassigment"
    )


def downgrade() -> None:
    op.execute("DROP SCHEMA homeassigment")
    op.drop_table("questions", schema="homeassigment")
