"""empty message

Revision ID: 254f650b2a22
Revises: d3855c994820
Create Date: 2020-11-20 21:21:04.825599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '254f650b2a22'
down_revision = 'd3855c994820'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'past_shows_count')
    op.drop_column('artist', 'upcoming_shows_count')
    op.drop_column('venue', 'past_shows_count')
    op.drop_column('venue', 'upcoming_shows_count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('upcoming_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('venue', sa.Column('past_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('artist', sa.Column('upcoming_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('artist', sa.Column('past_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###