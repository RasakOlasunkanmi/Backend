"""alter user table

Revision ID: ee7a6339d5b5
Revises: 
Create Date: 2025-10-23 11:19:27.326705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee7a6339d5b5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
            ALTER TABLE users
            ADD COLUMN userType varchar(100) DEFAULT 'student'
""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
            ALTER TABLE users
            DROP COLUMN userType
""")
    pass
