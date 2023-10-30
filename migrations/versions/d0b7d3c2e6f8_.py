"""empty message

Revision ID: d0b7d3c2e6f8
Revises: 
Create Date: 2023-10-30 13:02:50.488782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0b7d3c2e6f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), nullable=False))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
        batch_op.alter_column('id',
               existing_type=sa.UUID(),
               type_=sa.String(length=50),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('id',
               existing_type=sa.String(length=50),
               type_=sa.UUID(),
               existing_nullable=False,
               existing_server_default=sa.text('uuid_generate_v4()'))
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
