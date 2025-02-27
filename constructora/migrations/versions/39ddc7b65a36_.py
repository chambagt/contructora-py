"""empty message

Revision ID: 39ddc7b65a36
Revises: d1d2212ff982
Create Date: 2025-02-25 12:18:04.512276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39ddc7b65a36'
down_revision = 'd1d2212ff982'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exc_zanja',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('familia', sa.String(length=15), nullable=True),
    sa.Column('descripcion', sa.String(), nullable=True),
    sa.Column('unidad_metrica', sa.String(length=5), nullable=True),
    sa.Column('cantidad', sa.Float(precision=3), nullable=True),
    sa.Column('mat', sa.Float(precision=3), nullable=True),
    sa.Column('mo', sa.Float(precision=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exc_zanja_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exc_zanja_id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=15), nullable=True),
    sa.Column('nombre', sa.String(length=15), nullable=True),
    sa.Column('descripcion', sa.String(), nullable=True),
    sa.Column('rendimiento_hora', sa.Float(precision=3), nullable=True),
    sa.Column('dist', sa.Float(precision=3), nullable=True),
    sa.Column('dist_hora', sa.Float(precision=3), nullable=True),
    sa.Column('valor_hora', sa.Float(precision=3), nullable=True),
    sa.Column('valor_galon', sa.Float(precision=3), nullable=True),
    sa.Column('valor_dist', sa.Float(precision=3), nullable=True),
    sa.Column('factor', sa.Float(precision=3), nullable=True),
    sa.ForeignKeyConstraint(['exc_zanja_id'], ['exc_zanja.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exc_zanja_item')
    op.drop_table('exc_zanja')
    # ### end Alembic commands ###
