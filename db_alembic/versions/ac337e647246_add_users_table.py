"""add users table

Revision ID: ac337e647246
Revises: 6afa699f83b4
Create Date: 2023-05-30 14:15:50.512737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac337e647246'
down_revision = '6afa699f83b4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
