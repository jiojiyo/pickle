"""empty message

Revision ID: 6d8cfbb2e304
Revises: 896425606cf9
Create Date: 2021-09-09 16:07:25.415697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d8cfbb2e304'
down_revision = '896425606cf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq_user_email'), 'user', ['email'])
    op.create_unique_constraint(op.f('uq_user_user_phone'), 'user', ['user_phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_user_user_phone'), 'user', type_='unique')
    op.drop_constraint(op.f('uq_user_email'), 'user', type_='unique')
    # ### end Alembic commands ###
