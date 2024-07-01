"""empty message

Revision ID: d0cd67f83bd7
Revises: d8a53678ef9d
Create Date: 2024-06-25 22:39:46.843633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0cd67f83bd7'
down_revision: Union[str, None] = 'd8a53678ef9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts2', 'phone_number')
    op.add_column('users1', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users1', 'phone_number')
    op.add_column('posts2', sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###