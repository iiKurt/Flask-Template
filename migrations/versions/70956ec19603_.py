"""empty message

Revision ID: 70956ec19603
Revises: e109d3d4b96e
Create Date: 2022-04-18 21:45:59.873282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70956ec19603'
down_revision = 'e109d3d4b96e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    # ### end Alembic commands ###
