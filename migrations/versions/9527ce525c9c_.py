"""empty message

Revision ID: 9527ce525c9c
Revises: 5ae1ebdcf3fd
Create Date: 2021-09-24 10:43:04.867895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9527ce525c9c'
down_revision = '5ae1ebdcf3fd'
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
    op.drop_table('userInfo')
    with op.batch_alter_table('movieinfo', schema=None) as batch_op:
        batch_op.alter_column('mno',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)

    with op.batch_alter_table('preferMovie', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'userinfo', ['uno'], ['uno'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'movieinfo', ['mno'], ['mno'], ondelete='CASCADE')

    with op.batch_alter_table('sqlite_sequence', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sqlite_sequence', schema=None) as batch_op:
        batch_op.drop_column('id')

    with op.batch_alter_table('preferMovie', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'userInfo', ['uno'], ['uno'])
        batch_op.create_foreign_key(None, 'movieinfo', ['mno'], ['mno'])

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
    op.drop_table('userinfo')
    # ### end Alembic commands ###
