"""empty message

Revision ID: 26bceb54a791
Revises: 
Create Date: 2021-04-29 20:38:26.564556

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '26bceb54a791'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companyprofile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=191), server_default=sa.text('NULL'), nullable=True),
    sa.Column('city', sa.String(length=191), server_default=sa.text('NULL'), nullable=True),
    sa.Column('state', sa.String(length=2), server_default=sa.text('NULL'), nullable=True),
    sa.Column('website', sa.String(length=191), server_default=sa.text('NULL'), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['useraccount.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('company_id')
    )
    op.create_table('seekerprofile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seeker_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=191), nullable=False),
    sa.Column('last_name', sa.String(length=191), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('city', sa.String(length=191), server_default=sa.text('NULL'), nullable=True),
    sa.Column('state', sa.String(length=2), server_default=sa.text('NULL'), nullable=True),
    sa.ForeignKeyConstraint(['seeker_id'], ['useraccount.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('seeker_id')
    )
    op.drop_table('useractivity')
    op.add_column('useraccount', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('useraccount', sa.Column('join_date', postgresql.TIMESTAMP(precision=0), server_default=sa.text('now()'), nullable=False))
    op.add_column('useraccount', sa.Column('last_login', postgresql.TIMESTAMP(precision=0), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('useraccount', 'last_login')
    op.drop_column('useraccount', 'join_date')
    op.drop_column('useraccount', 'is_active')
    op.create_table('useractivity',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(precision=0), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False),
    sa.Column('join_date', postgresql.TIMESTAMP(precision=0), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['useraccount.id'], name='useractivity_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='useractivity_pkey'),
    sa.UniqueConstraint('user_id', name='useractivity_user_id_key')
    )
    op.drop_table('seekerprofile')
    op.drop_table('companyprofile')
    # ### end Alembic commands ###