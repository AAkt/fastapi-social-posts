"""'add_phone_number'

Revision ID: d8a53678ef9d
Revises: 38c5f52e5018
Create Date: 2024-06-25 22:36:12.708145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8a53678ef9d'
down_revision: Union[str, None] = '38c5f52e5018'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts2', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts2', 'phone_number')
    # ### end Alembic commands ###