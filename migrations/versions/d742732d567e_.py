"""empty message

Revision ID: d742732d567e
Revises: 29b6a13268f1
Create Date: 2021-09-19 19:20:34.164146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd742732d567e'
down_revision = '29b6a13268f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    op.create_table('prefer',
    sa.Column('uno', sa.Integer(), nullable=False),
    sa.Column('mno', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['mno'], ['movieinfo.mno'], ),
    sa.ForeignKeyConstraint(['uno'], ['userinfo.uno'], ),
    sa.PrimaryKeyConstraint('uno', 'mno')
    )
    op.drop_table('preferMovie')
    op.drop_table('userInfo')
    with op.batch_alter_table('movieinfo', schema=None) as batch_op:
        batch_op.alter_column('mno',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)

    with op.batch_alter_table('sqlite_sequence', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sqlite_sequence', schema=None) as batch_op:
        batch_op.drop_column('id')

    with op.batch_alter_table('movieinfo', schema=None) as batch_op:
        batch_op.alter_column('mno',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    op.create_table('userInfo',
    sa.Column('uno', sa.INTEGER(), nullable=True),
    sa.Column('id', sa.TEXT(), nullable=False),
    sa.Column('pw', sa.TEXT(), nullable=False),
    sa.Column('n_name', sa.TEXT(), nullable=False),
    sa.Column('uimg', sa.BLOB(), nullable=True),
    sa.Column('number', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('uno')
    )
    op.create_table('preferMovie',
    sa.Column('uno', sa.INTEGER(), nullable=False),
    sa.Column('mno', sa.INTEGER(), nullable=False),
    sa.Column('mpref', sa.INTEGER(), nullable=True),
    sa.Column('mwish', sa.INTEGER(), server_default=sa.text('0'), nullable=True),
    sa.ForeignKeyConstraint(['mno'], ['movieinfo.mno'], ),
    sa.ForeignKeyConstraint(['uno'], ['userInfo.uno'], )
    )
    op.drop_table('prefer')
    op.drop_table('userinfo')
    # ### end Alembic commands ###
