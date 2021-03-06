"""empty message

Revision ID: 57593227fbeb
Revises: 318eeb754153
Create Date: 2021-09-11 21:19:35.101093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57593227fbeb'
down_revision = '318eeb754153'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.add_column(sa.Column('movie_video', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.drop_column('movie_video')

    # ### end Alembic commands ###
