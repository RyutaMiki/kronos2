
from datetime import datetime
from sqlalchemy import (
    Column, String, Text, Integer, Float, Boolean, Date, TIMESTAMP, DECIMAL,
    Index, UniqueConstraint, ForeignKey, ForeignKeyConstraint,
    PrimaryKeyConstraint, CheckConstraint, text, func, SmallInteger
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import uuid

Base = declarative_base()


class Tenant(Base):
    """
    　テナントIDとUUIDを管理するORMクラス
    """
    __tablename__ = 'tenants'
    tenant_id = Column('tenant_id', String(64, collation='ja_JP.utf8'), primary_key=True, nullable=False, comment='テナントID')
    uuid = Column('uuid', String(36, collation='ja_JP.utf8'), nullable=False, unique=True, default=lambda: str(uuid.uuid4()), comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')


class TimeCardLayer(Base):
    """
    　タイムカード層
    """
    __tablename__ = 't_time_card_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード')
    stamping_start_time = Column('stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='出勤時間')
    stamping_end_time = Column('stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='退勤時間')
    start_time_office_code = Column('start_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='出勤打刻_事業所コード')
    end_time_office_code = Column('end_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='退勤打刻_事業所コード')
    telework_flg = Column('telework_flg', Boolean, nullable=True, comment='テレワークフラグ')
    smile_mark = Column('smile_mark', String(10, collation='ja_JP.utf8'), nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class StandardWorkLayer(Base):
    """
    　標準労働層
    """
    __tablename__ = 't_standard_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    ground_code = Column('ground_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='事由コード')
    stamping_start_time = Column('stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='出勤時間')
    stamping_end_time = Column('stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='退勤時間')
    rounded_stamping_start_time = Column('rounded_stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め出勤時間')
    rounded_stamping_end_time = Column('rounded_stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め退勤時間')
    job_start = Column('job_start', String(8, collation='ja_JP.utf8'), nullable=True, comment='始業時間')
    job_end = Column('job_end', String(8, collation='ja_JP.utf8'), nullable=True, comment='終業時間')
    working_interval = Column('working_interval', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class BreakLayer(Base):
    """
    　休憩時間層
    """
    __tablename__ = 't_break_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    break_start_time = Column('break_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='休憩開始時間')
    break_end_time = Column('break_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='休憩終了時間')
    rounded_break_start_time = Column('rounded_break_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め休憩開始時間')
    rounded_break_end_time = Column('rounded_break_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class StatutoryWorkLayer(Base):
    """
    　法定労働層
    """
    __tablename__ = 't_statutory_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    standard_legal_minutes = Column('standard_legal_minutes', Integer, nullable=True, comment='標準法定労働時間')
    legal_job_minutes = Column('legal_job_minutes', Integer, nullable=True, comment='法定労働時間')
    legal_overwork_minutes = Column('legal_overwork_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class PrescribedWorkLayer(Base):
    """
    　所定労働層
    """
    __tablename__ = 't_prescribed_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    standard_job_minutes = Column('standard_job_minutes', Integer, nullable=True, comment='標準所定労働時間')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=True, comment='所定労働時間')
    job_overwork_minutes = Column('job_overwork_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class PrescribedHolidayWorkLayer(Base):
    """
    　所定休日労働層
    """
    __tablename__ = 't_prescribed_holiday_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    prescribed_holiday_work_minutes = Column('prescribed_holiday_work_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class StatutoryHolidayWorkLayer(Base):
    """
    　法定休日労働層
    """
    __tablename__ = 't_statutory_holiday_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    statutory_holiday_work_minutes = Column('statutory_holiday_work_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class NightWorkLayer(Base):
    """
    　深夜労働層
    """
    __tablename__ = 't_night_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    late_night_overwork_minutes = Column('late_night_overwork_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class PaidLeaveLayer(Base):
    """
    　有給休暇層
    """
    __tablename__ = 't_paid_leave_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    paid_holiday_hours = Column('paid_holiday_hours', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class ChildLeaveLayer(Base):
    """
    　育児休暇層
    """
    __tablename__ = 't_child_leave_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    child_time_leave_hours = Column('child_time_leave_hours', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class LateEarlyLayer(Base):
    """
    　遅刻早退層
    """
    __tablename__ = 't_late_early_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    late_minutes = Column('late_minutes', Integer, nullable=True, comment='遅刻時間')
    early_departure_minutes = Column('early_departure_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class AbsenceLayer(Base):
    """
    　欠勤層
    """
    __tablename__ = 't_absence_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    absence_minutes = Column('absence_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class SubstituteLeaveLayer(Base):
    """
    　代休層（日単位、実体は存在のみで表現）
    """
    __tablename__ = 't_substitute_leave_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class SuspensionLayer(Base):
    """
    　休職層（日単位、実体は存在のみで表現）
    """
    __tablename__ = 't_suspension_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


class ClosedLayer(Base):
    """
    　休業層（日単位、実体は存在のみで表現）
    """
    __tablename__ = 't_closed_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_uuid = Column('employee_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='従業員UUID')
    target_date = Column('target_date', Date, nullable=False, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者従業員コード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者従業員コード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')

    __table_args__ = (UniqueConstraint("employee_uuid", "target_date"),)


