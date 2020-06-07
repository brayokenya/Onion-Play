"""Third  Migration

Revision ID: 778b3a359851
Revises: 160f10bc4307
Create Date: 2020-06-04 11:35:53.959338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '778b3a359851'
down_revision = '160f10bc4307'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###