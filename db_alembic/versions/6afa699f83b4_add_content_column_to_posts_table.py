"""add content column to posts table

Revision ID: 6afa699f83b4
Revises: bc4a478cb716
Create Date: 2023-05-30 14:06:13.629925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6afa699f83b4'
down_revision = 'bc4a478cb716'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', 
        sa.Column('content', sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
