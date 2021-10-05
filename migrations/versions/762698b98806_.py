"""empty message

Revision ID: 762698b98806
Revises: 6d8cfbb2e304
Create Date: 2021-09-09 16:08:26.184871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '762698b98806'
down_revision = '6d8cfbb2e304'
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
