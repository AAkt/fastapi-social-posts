"""'add_foreign_key'

Revision ID: 6d8e7805d0c9
Revises: c6af7d4fe2b5
Create Date: 2024-06-25 22:01:16.841085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d8e7805d0c9'
down_revision: Union[str, None] = 'c6af7d4fe2b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.add_column('posts2',sa.Column('owner_id',sa.Integer,nullable=False))
    op.create_foreign_key('posts_users_fk',source_table='posts2',referent_table='users1',local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fk','posts2')
    op.drop_column('posts2','owner_id')
    pass
