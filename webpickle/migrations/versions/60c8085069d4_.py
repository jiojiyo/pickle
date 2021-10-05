"""empty message

Revision ID: 60c8085069d4
Revises: 49eda277d789
Create Date: 2021-09-16 13:46:26.280894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60c8085069d4'
down_revision = '49eda277d789'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movieinfo',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('mno', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('director', sa.Text(), nullable=True),
    sa.Column('actor', sa.Text(), nullable=True),
    sa.Column('country', sa.Text(), nullable=True),
    sa.Column('release', sa.Text(), nullable=True),
    sa.Column('runtime', sa.Text(), nullable=True),
    sa.Column('overview', sa.Text(), nullable=True),
    sa.Column('keywords', sa.Text(), nullable=True),
    sa.Column('genres', sa.Text(), nullable=True),
    sa.Column('img1', sa.Text(), nullable=True),
    sa.Column('img2', sa.Text(), nullable=True),
    sa.Column('video', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('mno')
    )
    op.create_table('sqllite_sequence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('seq', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userinfo',
    sa.Column('uno', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(length=120), nullable=False),
    sa.Column('pw', sa.String(length=200), nullable=False),
    sa.Column('n_name', sa.String(length=150), nullable=False),
    sa.Column('uimg', sa.Text(), nullable=True),
    sa.Column('number', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('uno'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_table('prefer_movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uno', sa.Integer(), nullable=False),
    sa.Column('mno', sa.Integer(), nullable=False),
    sa.Column('mpref', sa.Integer(), nullable=True),
    sa.Column('mwish', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mno'], ['movieinfo.mno'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['uno'], ['userinfo.uno'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prefer_movie')
    op.drop_table('userinfo')
    op.drop_table('sqllite_sequence')
    op.drop_table('movieinfo')
    # ### end Alembic commands ###
