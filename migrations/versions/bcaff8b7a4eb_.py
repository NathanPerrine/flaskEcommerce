"""empty message

Revision ID: bcaff8b7a4eb
Revises: 5a4f58fd6e51
Create Date: 2022-04-02 13:30:39.121113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcaff8b7a4eb'
down_revision = '5a4f58fd6e51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('book_list_seller_id_fkey', 'book_list', type_='foreignkey')
    op.create_foreign_key(None, 'book_list', 'user', ['seller_id'], ['id'])
    op.drop_table('seller')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book_list', type_='foreignkey')
    op.create_foreign_key('book_list_seller_id_fkey', 'book_list', 'seller', ['seller_id'], ['id'])
    op.create_table('seller',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('c_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['c_id'], ['user.id'], name='seller_c_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='seller_pkey')
    )
    # ### end Alembic commands ###