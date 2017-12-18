"""added response_time

Revision ID: 320731fcb869
Revises: 
Create Date: 2017-12-18 21:15:22.421958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '320731fcb869'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proxies', sa.Column('response_time', sa.SmallInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proxies', 'response_time')
    # ### end Alembic commands ###