"""empty message

Revision ID: ed457526b6f6
Revises: 00eaaa02def3
Create Date: 2019-11-05 14:51:04.916973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed457526b6f6'
down_revision = '00eaaa02def3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logger',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logger')
    # ### end Alembic commands ###
