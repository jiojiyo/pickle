"""empty message

Revision ID: f4c8d6215ce5
Revises: 54965954b719
Create Date: 2021-10-04 20:31:52.083497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4c8d6215ce5'
down_revision = '54965954b719'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_movieinfo')
    op.drop_table('sqlite_sequence')
    with op.batch_alter_table('movieinfo', schema=None) as batch_op:
        batch_op.alter_column('mno',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)

    with op.batch_alter_table('preferMovie', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'movieinfo', ['mno'], ['mno'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'userInfo', ['uno'], ['uno'], ondelete='CASCADE')

    with op.batch_alter_table('userInfo', schema=None) as batch_op:
        batch_op.alter_column('uno',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('id',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('pw',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('n_name',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('number',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_unique_constraint(None, ['id'])
        batch_op.create_unique_constraint(None, ['number'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('userInfo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('number',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('n_name',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('pw',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('uno',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

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

    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.create_table('_alembic_tmp_movieinfo',
    sa.Column('mno', sa.INTEGER(), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('title', sa.TEXT(), nullable=True),
    sa.Column('director', sa.TEXT(), nullable=True),
    sa.Column('actor', sa.TEXT(), nullable=True),
    sa.Column('country', sa.TEXT(), nullable=True),
    sa.Column('release', sa.TEXT(), nullable=True),
    sa.Column('runtime', sa.TEXT(), nullable=True),
    sa.Column('overview', sa.TEXT(), nullable=True),
    sa.Column('keywords', sa.TEXT(), nullable=True),
    sa.Column('genres', sa.TEXT(), nullable=True),
    sa.Column('img1', sa.TEXT(), nullable=True),
    sa.Column('img2', sa.TEXT(), nullable=True),
    sa.Column('video', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('mno')
    )
    # ### end Alembic commands ###
