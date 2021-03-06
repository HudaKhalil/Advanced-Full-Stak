"""empty message

Revision ID: d0c15253a512
Revises: 2bd083ea3f51
Create Date: 2020-11-19 21:11:42.470449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0c15253a512'
down_revision = '2bd083ea3f51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
