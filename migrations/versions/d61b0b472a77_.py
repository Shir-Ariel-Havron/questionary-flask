"""empty message

Revision ID: d61b0b472a77
Revises: ddca244e5fde
Create Date: 2020-07-13 14:55:49.566080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd61b0b472a77'
down_revision = 'ddca244e5fde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relationships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slave', sa.Integer(), nullable=False),
    sa.Column('master', sa.Integer(), nullable=False),
    sa.Column('slave_description', sa.String(length=120), nullable=False),
    sa.Column('master_description', sa.String(length=120), nullable=False),
    sa.Column('relationship_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['master'], ['user.id'], ),
    sa.ForeignKeyConstraint(['slave'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'slave', 'master')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('relationships')
    # ### end Alembic commands ###