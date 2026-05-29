"""merge branches

Revision ID: 2c78db4abe16
Revises: 7160b9935ca0, f70225c8830d
Create Date: 2026-05-19 12:09:28.274816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c78db4abe16'
down_revision: Union[str, Sequence[str], None] = ('7160b9935ca0', 'f70225c8830d')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
