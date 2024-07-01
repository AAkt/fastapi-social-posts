"""'add_content_table'

Revision ID: 4b9de52afde2
Revises: aa961b460ee3
Create Date: 2024-06-25 20:21:04.879260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b9de52afde2'
down_revision: Union[str, None] = 'aa961b460ee3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts2',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts2','content')
    pass
