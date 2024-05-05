"""empty message

Revision ID: 04b522119698
Revises: 1640302c7211
Create Date: 2024-05-05 14:44:50.500502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04b522119698'
down_revision: Union[str, None] = '1640302c7211'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('topic_content_id_fkey', 'topic', type_='foreignkey')
    op.drop_column('topic', 'content_id')
    op.add_column('topic_content', sa.Column('topic_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'topic_content', 'topic', ['topic_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'topic_content', type_='foreignkey')
    op.drop_column('topic_content', 'topic_id')
    op.add_column('topic', sa.Column('content_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('topic_content_id_fkey', 'topic', 'topic_content', ['content_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
