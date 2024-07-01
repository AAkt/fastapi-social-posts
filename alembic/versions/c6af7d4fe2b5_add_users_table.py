"""'add_users_table'

Revision ID: c6af7d4fe2b5
Revises: 4b9de52afde2
Create Date: 2024-06-25 20:36:26.555396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6af7d4fe2b5'
down_revision: Union[str, None] = '4b9de52afde2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users1',sa.Column('id',sa.Integer,nullable=False,primary_key=True),sa.Column('email',sa.String,nullable=False,unique=True),sa.Column('password',sa.String,nullable=False),sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False))

    
    pass


def downgrade():
    op.drop_table('users1')
    pass
