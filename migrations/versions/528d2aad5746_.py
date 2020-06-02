"""empty message

Revision ID: 528d2aad5746
Revises: e21872c3d68d
Create Date: 2020-05-30 21:46:12.032402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '528d2aad5746'
down_revision = 'e21872c3d68d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('seeking_artist', sa.Boolean(), nullable=True))
    op.add_column('venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'seeking_description')
    op.drop_column('venue', 'seeking_artist')
    # ### end Alembic commands ###
