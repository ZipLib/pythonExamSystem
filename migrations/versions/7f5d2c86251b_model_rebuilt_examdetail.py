"""model rebuilt ExamDetail

Revision ID: 7f5d2c86251b
Revises: 
Create Date: 2017-03-17 11:18:09.753180

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7f5d2c86251b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('examPaperCorrected',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('corrected_content', sa.String(length=64), nullable=True),
    sa.Column('corrected_score', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('corrector_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['corrector_id'], ['correctors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questionMakers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('id_card', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('sex', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('login_times', sa.Integer(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questionMakers_account'), 'questionMakers', ['account'], unique=True)
    op.create_index(op.f('ix_questionMakers_id_card'), 'questionMakers', ['id_card'], unique=True)
    op.create_table('answerQuestions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('difficulty', sa.String(length=6), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('answer', sa.String(length=64), nullable=True),
    sa.Column('answer_describe', sa.Text(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('is_examinee', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('question_maker_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], ),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionMakers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('examPapers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exam_paper_name', sa.String(length=64), nullable=True),
    sa.Column('total_score', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('is_examinees', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('answer_time_set', sa.String(length=64), nullable=True),
    sa.Column('question_maker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionMakers.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_examPapers_exam_paper_name'), 'examPapers', ['exam_paper_name'], unique=True)
    op.create_table('fillQuestions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('difficulty', sa.String(length=6), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('fill1', sa.String(length=64), nullable=True),
    sa.Column('fill2', sa.String(length=64), nullable=True),
    sa.Column('fill3', sa.String(length=64), nullable=True),
    sa.Column('fill4', sa.String(length=64), nullable=True),
    sa.Column('fill5', sa.String(length=64), nullable=True),
    sa.Column('fill6', sa.String(length=64), nullable=True),
    sa.Column('answer', sa.String(length=64), nullable=True),
    sa.Column('answer_describe', sa.Text(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('is_examinee', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('question_maker_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], ),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionMakers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('judgeQuestions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('difficulty', sa.String(length=6), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('option1', sa.String(length=64), nullable=True),
    sa.Column('option2', sa.String(length=64), nullable=True),
    sa.Column('answer', sa.String(length=64), nullable=True),
    sa.Column('answer_describe', sa.Text(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('is_examinee', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('question_maker_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], ),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionMakers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('multiQuestions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('difficulty', sa.String(length=6), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('option1', sa.String(length=64), nullable=True),
    sa.Column('option2', sa.String(length=64), nullable=True),
    sa.Column('option3', sa.String(length=64), nullable=True),
    sa.Column('option4', sa.String(length=64), nullable=True),
    sa.Column('option5', sa.String(length=64), nullable=True),
    sa.Column('option6', sa.String(length=64), nullable=True),
    sa.Column('answer', sa.String(length=64), nullable=True),
    sa.Column('answer_describe', sa.Text(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('is_examinee', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('question_maker_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], ),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionMakers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('singleQuestions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('difficulty', sa.String(length=6), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('option1', sa.String(length=64), nullable=True),
    sa.Column('option2', sa.String(length=64), nullable=True),
    sa.Column('option3', sa.String(length=64), nullable=True),
    sa.Column('option4', sa.String(length=64), nullable=True),
    sa.Column('answer', sa.String(length=64), nullable=True),
    sa.Column('answer_describe', sa.Text(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('is_examinee', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('question_maker_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionMakers.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('examPaperDetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('examinee_id', sa.Integer(), nullable=True),
    sa.Column('exam_paper_id', sa.Integer(), nullable=True),
    sa.Column('single_question_id', sa.Integer(), nullable=True),
    sa.Column('multi_question_id', sa.Integer(), nullable=True),
    sa.Column('judge_question_id', sa.Integer(), nullable=True),
    sa.Column('fill_question_id', sa.Integer(), nullable=True),
    sa.Column('answer_question_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['answer_question_id'], ['answerQuestions.id'], ),
    sa.ForeignKeyConstraint(['exam_paper_id'], ['examPapers.id'], ),
    sa.ForeignKeyConstraint(['examinee_id'], ['examinees.id'], ),
    sa.ForeignKeyConstraint(['fill_question_id'], ['fillQuestions.id'], ),
    sa.ForeignKeyConstraint(['judge_question_id'], ['judgeQuestions.id'], ),
    sa.ForeignKeyConstraint(['multi_question_id'], ['multiQuestions.id'], ),
    sa.ForeignKeyConstraint(['single_question_id'], ['singleQuestions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('examPaperFinished',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answered_content', sa.String(length=64), nullable=True),
    sa.Column('per_score', sa.Integer(), nullable=True),
    sa.Column('question_type', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('examinee_id', sa.Integer(), nullable=True),
    sa.Column('exam_paper_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['exam_paper_id'], ['examPapers.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['examinee_id'], ['examinees.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('exampaperdetails')
    op.drop_table('fillquestions')
    op.drop_table('answerquestions')
    op.drop_table('exampapers')
    op.drop_table('judgequestions')
    op.drop_table('multiquestions')
    op.drop_table('questionmakers')
    op.drop_table('singlequestions')
    op.drop_table('exampapercorrected')
    op.drop_table('exampaperfinished')
    op.drop_constraint('notice_ibfk_2', 'notice', type_='foreignkey')
    op.create_foreign_key(None, 'notice', 'questionMakers', ['question_maker_id'], ['id'])
    op.drop_constraint('scores_ibfk_2', 'scores', type_='foreignkey')
    op.create_foreign_key(None, 'scores', 'examPaperFinished', ['exam_paper_finish_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'scores', type_='foreignkey')
    op.create_foreign_key('scores_ibfk_2', 'scores', 'exampaperfinished', ['exam_paper_finish_id'], ['id'])
    op.drop_constraint(None, 'notice', type_='foreignkey')
    op.create_foreign_key('notice_ibfk_2', 'notice', 'questionmakers', ['question_maker_id'], ['id'])
    op.create_table('exampaperfinished',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('answered_content', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('per_score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('question_type', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('question_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('examinee_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('exam_paper_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['exam_paper_id'], ['exampapers.id'], name='exampaperfinished_ibfk_2', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['examinee_id'], ['examinees.id'], name='exampaperfinished_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('exampapercorrected',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('corrected_content', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('corrected_score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('start_time', mysql.DATETIME(), nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.Column('corrector_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['corrector_id'], ['correctors.id'], name='exampapercorrected_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('singlequestions',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('question', mysql.TEXT(), nullable=True),
    sa.Column('difficulty', mysql.VARCHAR(length=6), nullable=True),
    sa.Column('score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('option1', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('option2', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('option3', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('option4', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('answer', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('answer_describe', mysql.TEXT(), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_examinee', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.Column('question_maker_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('chapter_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], name='singlequestions_ibfk_2', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionmakers.id'], name='singlequestions_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('questionmakers',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('account', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('id_card', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('sex', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('phone', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('address', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('login_times', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('last_login', mysql.DATETIME(), nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.Column('department_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], name='questionmakers_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('multiquestions',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('question', mysql.TEXT(), nullable=True),
    sa.Column('difficulty', mysql.VARCHAR(length=6), nullable=True),
    sa.Column('score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('option1', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('option2', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('option3', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('option4', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('option5', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('option6', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('answer', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('answer_describe', mysql.TEXT(), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_examinee', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.Column('question_maker_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('chapter_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], name='multiquestions_ibfk_2'),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionmakers.id'], name='multiquestions_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('judgequestions',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('question', mysql.TEXT(), nullable=True),
    sa.Column('difficulty', mysql.VARCHAR(length=6), nullable=True),
    sa.Column('score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('option1', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('option2', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('answer', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('answer_describe', mysql.TEXT(), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_examinee', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.Column('question_maker_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('chapter_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], name='judgequestions_ibfk_2'),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionmakers.id'], name='judgequestions_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('exampapers',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('exam_paper_name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('total_score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_examinees', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.Column('start_time', mysql.DATETIME(), nullable=True),
    sa.Column('end_time', mysql.DATETIME(), nullable=True),
    sa.Column('answer_time_set', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('question_maker_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionmakers.id'], name='exampapers_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('answerquestions',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('question', mysql.TEXT(), nullable=True),
    sa.Column('difficulty', mysql.VARCHAR(length=6), nullable=True),
    sa.Column('score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('answer', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('answer_describe', mysql.TEXT(), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_examinee', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.Column('question_maker_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('chapter_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], name='answerquestions_ibfk_2'),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionmakers.id'], name='answerquestions_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('fillquestions',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('question', mysql.TEXT(), nullable=True),
    sa.Column('difficulty', mysql.VARCHAR(length=6), nullable=True),
    sa.Column('score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('fill1', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('fill2', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('fill3', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('fill4', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('fill5', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('fill6', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('answer', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('answer_describe', mysql.TEXT(), nullable=True),
    sa.Column('status', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('is_examinee', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('timestamp', mysql.DATETIME(), nullable=True),
    sa.Column('question_maker_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('chapter_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], name='fillquestions_ibfk_2'),
    sa.ForeignKeyConstraint(['question_maker_id'], ['questionmakers.id'], name='fillquestions_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('exampaperdetails',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('examinee_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('exam_paper_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('single_question_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('multi_question_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('judge_question_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('fill_question_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('answer_question_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['answer_question_id'], ['answerquestions.id'], name='exampaperdetails_ibfk_7'),
    sa.ForeignKeyConstraint(['exam_paper_id'], ['exampapers.id'], name='exampaperdetails_ibfk_2'),
    sa.ForeignKeyConstraint(['examinee_id'], ['examinees.id'], name='exampaperdetails_ibfk_1'),
    sa.ForeignKeyConstraint(['fill_question_id'], ['fillquestions.id'], name='exampaperdetails_ibfk_6'),
    sa.ForeignKeyConstraint(['judge_question_id'], ['judgequestions.id'], name='exampaperdetails_ibfk_5'),
    sa.ForeignKeyConstraint(['multi_question_id'], ['multiquestions.id'], name='exampaperdetails_ibfk_4'),
    sa.ForeignKeyConstraint(['single_question_id'], ['singlequestions.id'], name='exampaperdetails_ibfk_3'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('examPaperFinished')
    op.drop_table('examPaperDetails')
    op.drop_table('singleQuestions')
    op.drop_table('multiQuestions')
    op.drop_table('judgeQuestions')
    op.drop_table('fillQuestions')
    op.drop_index(op.f('ix_examPapers_exam_paper_name'), table_name='examPapers')
    op.drop_table('examPapers')
    op.drop_table('answerQuestions')
    op.drop_index(op.f('ix_questionMakers_id_card'), table_name='questionMakers')
    op.drop_index(op.f('ix_questionMakers_account'), table_name='questionMakers')
    op.drop_table('questionMakers')
    op.drop_table('examPaperCorrected')
    # ### end Alembic commands ###
