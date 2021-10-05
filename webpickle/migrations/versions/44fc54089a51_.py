"""empty message

Revision ID: 44fc54089a51
Revises: eacbad949d77
Create Date: 2021-09-11 21:29:48.490250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44fc54089a51'
down_revision = 'eacbad949d77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.drop_column('movie_nation')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.add_column(sa.Column('movie_nation', sa.VARCHAR(length=150), nullable=True))

    # ### end Alembic commands ###
