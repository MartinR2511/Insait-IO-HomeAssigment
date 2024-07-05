"""create ipaddress column in question table

Revision ID: 6e3eb0df0f07
Revises: 9de9a5556a9e
Create Date: 2024-07-05 15:01:45.057185

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e3eb0df0f07'
down_revision: Union[str, None] = '9de9a5556a9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('questions', sa.Column('ipaddress', sa.String(15), nullable=True), schema='homeassigment')

def downgrade() -> None:
    op.drop_column('questions', 'ipaddress', schema='homeassigment')
