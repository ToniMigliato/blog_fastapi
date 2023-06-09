"""add foreign key to posts table

Revision ID: 5da00f2418c2
Revises: ac337e647246
Create Date: 2023-05-30 14:34:00.288699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5da00f2418c2'
down_revision = 'ac337e647246'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass

def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
