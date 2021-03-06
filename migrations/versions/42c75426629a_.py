"""empty message

Revision ID: 42c75426629a
Revises: bcaff8b7a4eb
Create Date: 2022-04-02 14:00:56.616012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42c75426629a'
down_revision = 'bcaff8b7a4eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('image_url', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'image_url')
    # ### end Alembic commands ###
