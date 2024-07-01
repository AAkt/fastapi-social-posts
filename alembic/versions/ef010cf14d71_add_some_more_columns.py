"""add_some_more_columns

Revision ID: ef010cf14d71
Revises: 6d8e7805d0c9
Create Date: 2024-06-25 22:15:14.594456

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef010cf14d71'
down_revision: Union[str, None] = '6d8e7805d0c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts2',sa.Column('published',sa.Boolean,server_default='TRUE',nullable=False))
    op.add_column('posts2',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('posts2','published')
    op.drop_column('posts2','created_at')
    pass
