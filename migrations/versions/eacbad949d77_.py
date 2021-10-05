"""empty message

Revision ID: eacbad949d77
Revises: 57593227fbeb
Create Date: 2021-09-11 21:26:13.050749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eacbad949d77'
down_revision = '57593227fbeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.add_column(sa.Column('movie_nation', sa.String(length=150), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.drop_column('movie_nation')

    # ### end Alembic commands ###
