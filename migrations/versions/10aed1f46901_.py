"""empty message

Revision ID: 10aed1f46901
Revises: 6ee654fc7ac3
Create Date: 2022-11-08 22:14:09.485310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10aed1f46901'
down_revision = '6ee654fc7ac3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('goal_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goal')
    # ### end Alembic commands ###