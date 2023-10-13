"""usertable added

Revision ID: eaf4a86dd4e9
Revises:
Create Date: 2023-10-13 21:36:01.479264

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "eaf4a86dd4e9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("phone_number", sa.Integer(), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=True),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("modified_on", sa.DateTime(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("is_admin", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("phone_number"),
    )
    op.create_table(
        "otp",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.Integer(), nullable=True),
        sa.Column("otp", sa.Integer(), nullable=True),
        sa.Column("modified_on", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["email"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("otp")
    op.drop_table("users")
    # ### end Alembic commands ###