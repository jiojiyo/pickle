"""empty message

Revision ID: a17099c97778
Revises: 9bdadd784645
Create Date: 2021-09-27 16:42:17.972838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a17099c97778'
down_revision = '9bdadd784645'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_info',
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
        batch_op.create_foreign_key(None, 'movieinfo', ['mno'], ['mno'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'user_info', ['uno'], ['uno'], ondelete='CASCADE')

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
        batch_op.create_foreign_key(None, 'movieinfo', ['mno'], ['mno'])
        batch_op.create_foreign_key(None, 'userInfo', ['uno'], ['uno'])

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
    op.drop_table('user_info')
    # ### end Alembic commands ###