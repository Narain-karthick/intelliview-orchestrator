"""merge heads

Revision ID: a9c4c63a79be
Revises: 003_add_candidate_features, 850f7086ffdd
Create Date: 2026-08-28 22:35:13.855443

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a9c4c63a79be"
down_revision: Union[str, Sequence[str], None] = (
    "003_add_candidate_features",
    "850f7086ffdd",
)
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
