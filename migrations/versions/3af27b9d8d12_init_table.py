"""init table

Revision ID: 3af27b9d8d12
Revises: 
Create Date: 2022-08-28 22:46:15.423195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3af27b9d8d12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model_users',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=230), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_model_users_email'), 'model_users', ['email'], unique=True)
    op.create_table('model_absensi',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('type', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['model_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model_activity',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('activity_name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['model_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_model_activity_created_at'), 'model_activity', ['created_at'], unique=False)
    op.create_index(op.f('ix_model_activity_updated_at'), 'model_activity', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_model_activity_updated_at'), table_name='model_activity')
    op.drop_index(op.f('ix_model_activity_created_at'), table_name='model_activity')
    op.drop_table('model_activity')
    op.drop_table('model_absensi')
    op.drop_index(op.f('ix_model_users_email'), table_name='model_users')
    op.drop_table('model_users')
    # ### end Alembic commands ###
