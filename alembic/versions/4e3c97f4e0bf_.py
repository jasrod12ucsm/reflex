"""empty message

Revision ID: 4e3c97f4e0bf
Revises: 6de436f68676
Create Date: 2024-10-31 06:14:14.816778

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '4e3c97f4e0bf'
down_revision: Union[str, None] = '6de436f68676'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('autor', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('categoria', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('locacion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('idioma', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
