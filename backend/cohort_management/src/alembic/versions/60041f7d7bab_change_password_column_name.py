"""Change password column name

Revision ID: 60041f7d7bab
Revises: f7a32c1a0b17
Create Date: 2024-12-16 16:02:51.590253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60041f7d7bab'
down_revision: Union[str, None] = 'f7a32c1a0b17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'users',  # nazwa tabeli
        'password_hash',  # stara nazwa kolumny
        new_column_name='hashed_password',  # nowa nazwa kolumny
        schema='cohort_management'
    )

def downgrade() -> None:
    op.alter_column(
        'users',
        'hashed_password',
        new_column_name='password_hash',
        schema='cohort_management'
    )
