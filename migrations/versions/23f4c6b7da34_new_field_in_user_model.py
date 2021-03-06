"""new field in user model

Revision ID: 23f4c6b7da34
Revises: ea3a17d5d7a3
Create Date: 2021-09-01 23:03:38.523870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23f4c6b7da34'
down_revision = 'ea3a17d5d7a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
