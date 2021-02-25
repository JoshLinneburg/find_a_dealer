"""Initial migration

Revision ID: a84f65f3bb93
Revises: 
Create Date: 2021-02-21 18:41:21.564934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a84f65f3bb93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dealer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=128), nullable=True),
    sa.Column('internal_id', sa.String(length=100), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('street_address', sa.String(length=250), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=50), nullable=True),
    sa.Column('postal_code', sa.Integer(), nullable=True),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('phone', sa.String(length=25), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('website', sa.String(length=50), nullable=True),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('modified_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=128), nullable=True),
    sa.Column('service_name', sa.String(length=250), nullable=False),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('modified_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('dealer_hours',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=128), nullable=True),
    sa.Column('dealer_id', sa.Integer(), nullable=False),
    sa.Column('day_of_week', sa.String(length=25), nullable=False),
    sa.Column('open_time', sa.Time(), nullable=True),
    sa.Column('close_time', sa.Time(), nullable=True),
    sa.Column('schedule_type', sa.String(length=25), nullable=False),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('modified_datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dealer_id'], ['dealer.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('dealer_service',
    sa.Column('dealer_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('modified_datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dealer_id'], ['dealer.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('dealer_id', 'service_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dealer_service')
    op.drop_table('dealer_hours')
    op.drop_table('service')
    op.drop_table('dealer')
    # ### end Alembic commands ###