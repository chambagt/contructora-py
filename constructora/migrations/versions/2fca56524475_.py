"""empty message

Revision ID: 2fca56524475
Revises: 9db6dcd2630a
Create Date: 2025-02-25 21:02:59.228025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fca56524475'
down_revision = '9db6dcd2630a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exc_zanja', schema=None) as batch_op:
        batch_op.add_column(sa.Column('materiales', sa.Float(precision=3), nullable=True))
        batch_op.add_column(sa.Column('mano_obra', sa.Float(precision=3), nullable=True))
        batch_op.alter_column('cantidad',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
        batch_op.drop_column('mat')
        batch_op.drop_column('mo')

    with op.batch_alter_table('exc_zanja_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('grupo', sa.String(), nullable=True))
        batch_op.alter_column('rendimiento_hora',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
        batch_op.alter_column('dist',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
        batch_op.alter_column('dist_hora',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
        batch_op.alter_column('valor_hora',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
        batch_op.alter_column('valor_galon',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
        batch_op.alter_column('valor_dist',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)
        batch_op.alter_column('factor',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)

    with op.batch_alter_table('exc_zanja_plantilla', schema=None) as batch_op:
        batch_op.alter_column('cantidad',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=3),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exc_zanja_plantilla', schema=None) as batch_op:
        batch_op.alter_column('cantidad',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)

    with op.batch_alter_table('exc_zanja_item', schema=None) as batch_op:
        batch_op.alter_column('factor',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('valor_dist',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('valor_galon',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('valor_hora',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('dist_hora',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('dist',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('rendimiento_hora',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.drop_column('grupo')

    with op.batch_alter_table('exc_zanja', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mo', sa.REAL(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('mat', sa.REAL(), autoincrement=False, nullable=True))
        batch_op.alter_column('cantidad',
               existing_type=sa.Float(precision=3),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.drop_column('mano_obra')
        batch_op.drop_column('materiales')

    # ### end Alembic commands ###
