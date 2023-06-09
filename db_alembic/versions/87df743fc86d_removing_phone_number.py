"""removing phone_number

Revision ID: 87df743fc86d
Revises: 04feed1f8616
Create Date: 2023-05-31 10:41:53.310050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87df743fc86d'
down_revision = '04feed1f8616'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_phone_number_key', 'users', type_='unique')
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_phone_number_key', 'users', ['phone_number'])
    # ### end Alembic commands ###
