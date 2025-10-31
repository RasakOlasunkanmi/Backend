"""alter users table

Revision ID: 33664d7e5f23
Revises: 9cffbd51d676
Create Date: 2025-10-27 11:27:06.680941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33664d7e5f23'
down_revision: Union[str, Sequence[str], None] = '9cffbd51d676'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
               ALTER TABLE users
               ADD COLUMN gender varchar(100) DEFAULT 'female'
""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
               ALTER TABLE users
               DROP COLUMN gender
""")
    pass
