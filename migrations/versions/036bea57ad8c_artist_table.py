"""artist table

Revision ID: 036bea57ad8c
Revises: 
Create Date: 2021-02-05 13:20:00.415661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '036bea57ad8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_artist_name'), 'artist', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_artist_name'), table_name='artist')
    op.drop_table('artist')
    # ### end Alembic commands ###