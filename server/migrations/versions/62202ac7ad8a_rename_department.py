"""rename department

Revision ID: 62202ac7ad8a
Revises: e6bd889f1ee0
Create Date: 2025-06-25 20:40:26.198374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62202ac7ad8a'
down_revision = 'e6bd889f1ee0'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('department', 'departments')

def downgrade():
    op.rename_table('departments', 'department')
