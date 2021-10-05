"""empty message

Revision ID: c598b9a529c5
Revises: fc99b80e79f2
Create Date: 2021-09-27 18:33:53.455482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c598b9a529c5'
down_revision = 'fc99b80e79f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_movieinfo')
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

    with op.batch_alter_table('sqlite_sequence', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))

    with op.batch_alter_table('userInfo', schema=None) as batch_op:
        batch_op.alter_column('uno',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('number',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_unique_constraint(None, ['number'])
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('userInfo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('number',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('uno',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

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