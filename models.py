
from datetime import datetime
from sqlalchemy import (
    Column, String, Text, Integer, Float, Boolean, Date, TIMESTAMP, DECIMAL,
    Index, UniqueConstraint, ForeignKey, ForeignKeyConstraint,
    PrimaryKeyConstraint, CheckConstraint, text, func, SmallInteger
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import uuid
from enumType import EnumType

Base = declarative_base()


class User(Base):
    """
    　実在する利用者（人）を一意に管理するテーブル
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, unique=True, default=lambda: str(uuid.uuid4()), comment='ユーザーUUID')
    user_name = Column('user_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='氏名')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')



class Tenant(Base):
    """
    　会社ごとのテナント情報
    """
    __tablename__ = 'tenants'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, unique=True, default=lambda: str(uuid.uuid4()), comment='テナントUUID')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')



class Employee(Base):
    """
    　会社ごとにどのユーザーが所属しているか管理
    　同じユーザーが再入社した場合は新しいレコードを追加し、履歴を保持する
    """
    __tablename__ = 'employees'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    belong_start_date = Column('belong_start_date', Date, nullable=False, comment='所属開始日')
    belong_end_date = Column('belong_end_date', Date, nullable=True, comment='所属終了日（現役中はNULL）')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        ForeignKeyConstraint(['user_uuid'], ['users.user_uuid']),
        ForeignKeyConstraint(['tenant_uuid'], ['tenants.tenant_uuid']),
        UniqueConstraint('tenant_uuid', 'user_uuid', 'belong_start_date')
    )


class TimeCardLayer(Base):
    """
    　タイムカード層
    """
    __tablename__ = 't_time_card_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード')
    stamping_start_time = Column('stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='出勤時間')
    stamping_end_time = Column('stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='退勤時間')
    start_time_office_code = Column('start_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='出勤打刻_事業所コード')
    end_time_office_code = Column('end_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='退勤打刻_事業所コード')
    telework_flg = Column('telework_flg', Boolean, nullable=True, comment='テレワークフラグ')
    smile_mark = Column('smile_mark', String(10, collation='ja_JP.utf8'), nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class TimeCardLayerHistory(Base):
    """
    　タイムカード層の履歴（保証トランザクション対応）。  
    　更新・削除・ロールバックなどの際に履歴を保持する。
    """
    __tablename__ = 't_time_card_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（TimeCardLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード')
    stamping_start_time = Column('stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='出勤時間')
    stamping_end_time = Column('stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='退勤時間')
    start_time_office_code = Column('start_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='出勤打刻_事業所コード')
    end_time_office_code = Column('end_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='退勤打刻_事業所コード')
    telework_flg = Column('telework_flg', Boolean, nullable=True, comment='テレワークフラグ')
    smile_mark = Column('smile_mark', String(10, collation='ja_JP.utf8'), nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態（pending/committed/rolledback等）')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class StandardWorkLayer(Base):
    """
    　標準労働層
    """
    __tablename__ = 't_standard_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    ground_code = Column('ground_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='事由コード')
    stamping_start_time = Column('stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='出勤時間')
    stamping_end_time = Column('stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='退勤時間')
    rounded_stamping_start_time = Column('rounded_stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め出勤時間')
    rounded_stamping_end_time = Column('rounded_stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め退勤時間')
    job_start = Column('job_start', String(8, collation='ja_JP.utf8'), nullable=True, comment='始業時間')
    job_end = Column('job_end', String(8, collation='ja_JP.utf8'), nullable=True, comment='終業時間')
    working_interval = Column('working_interval', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class StandardWorkLayerHistory(Base):
    """
    　標準労働層の履歴（保証トランザクション対応）。
    """
    __tablename__ = 't_standard_work_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（StandardWorkLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    ground_code = Column('ground_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='事由コード')
    stamping_start_time = Column('stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='出勤時間')
    stamping_end_time = Column('stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='退勤時間')
    rounded_stamping_start_time = Column('rounded_stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め出勤時間')
    rounded_stamping_end_time = Column('rounded_stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め退勤時間')
    job_start = Column('job_start', String(8, collation='ja_JP.utf8'), nullable=True, comment='始業時間')
    job_end = Column('job_end', String(8, collation='ja_JP.utf8'), nullable=True, comment='終業時間')
    working_interval = Column('working_interval', Integer, nullable=True, comment='インターバル時間')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態（pending/committed/rolledback等）')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class BreakLayer(Base):
    """
    　休憩時間層
    """
    __tablename__ = 't_break_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    break_start_time = Column('break_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='休憩開始時間')
    break_end_time = Column('break_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='休憩終了時間')
    rounded_break_start_time = Column('rounded_break_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め休憩開始時間')
    rounded_break_end_time = Column('rounded_break_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class BreakLayerHistory(Base):
    """
    　休憩時間層の履歴（保証トランザクション対応）。
    """
    __tablename__ = 't_break_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（BreakLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    break_start_time = Column('break_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='休憩開始時間')
    break_end_time = Column('break_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='休憩終了時間')
    rounded_break_start_time = Column('rounded_break_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め休憩開始時間')
    rounded_break_end_time = Column('rounded_break_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め休憩終了時間')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態（pending/committed/rolledback等）')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class StatutoryWorkLayer(Base):
    """
    　法定労働層
    """
    __tablename__ = 't_statutory_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    standard_legal_minutes = Column('standard_legal_minutes', Integer, nullable=True, comment='標準法定労働時間')
    legal_job_minutes = Column('legal_job_minutes', Integer, nullable=True, comment='法定労働時間')
    legal_overwork_minutes = Column('legal_overwork_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class StatutoryWorkLayerHistory(Base):
    """
    　法定労働層の履歴（保証トランザクション対応）。
    """
    __tablename__ = 't_statutory_work_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（StatutoryWorkLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    standard_legal_minutes = Column('standard_legal_minutes', Integer, nullable=True, comment='標準法定労働時間')
    legal_job_minutes = Column('legal_job_minutes', Integer, nullable=True, comment='法定労働時間')
    legal_overwork_minutes = Column('legal_overwork_minutes', Integer, nullable=True, comment='法定外労働時間')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態（pending/committed/rolledback等）')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class PrescribedWorkLayer(Base):
    """
    　所定労働層
    """
    __tablename__ = 't_prescribed_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    standard_job_minutes = Column('standard_job_minutes', Integer, nullable=True, comment='標準所定労働時間')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=True, comment='所定労働時間')
    job_overwork_minutes = Column('job_overwork_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class PrescribedWorkLayerHistory(Base):
    """
    　所定労働層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_prescribed_work_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（PrescribedWorkLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    standard_job_minutes = Column('standard_job_minutes', Integer, nullable=True, comment='標準所定労働時間')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=True, comment='所定労働時間')
    job_overwork_minutes = Column('job_overwork_minutes', Integer, nullable=True, comment='所定外労働時間')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class PrescribedHolidayWorkLayer(Base):
    """
    　所定休日労働層
    """
    __tablename__ = 't_prescribed_holiday_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    prescribed_holiday_work_minutes = Column('prescribed_holiday_work_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class PrescribedHolidayWorkLayerHistory(Base):
    """
    　所定休日労働層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_prescribed_holiday_work_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（PrescribedHolidayWorkLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    prescribed_holiday_work_minutes = Column('prescribed_holiday_work_minutes', Integer, nullable=True, comment='所定休日労働時間')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class StatutoryHolidayWorkLayer(Base):
    """
    　法定休日労働層
    """
    __tablename__ = 't_statutory_holiday_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    statutory_holiday_work_minutes = Column('statutory_holiday_work_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class StatutoryHolidayWorkLayerHistory(Base):
    """
    　法定休日労働層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_statutory_holiday_work_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（StatutoryHolidayWorkLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    statutory_holiday_work_minutes = Column('statutory_holiday_work_minutes', Integer, nullable=True, comment='法定休日労働時間')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class NightWorkLayer(Base):
    """
    　深夜労働層
    """
    __tablename__ = 't_night_work_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    late_night_overwork_minutes = Column('late_night_overwork_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class NightWorkLayerHistory(Base):
    """
    　深夜労働層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_night_work_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（NightWorkLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    late_night_overwork_minutes = Column('late_night_overwork_minutes', Integer, nullable=True, comment='深夜労働時間')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class PaidLeaveLayer(Base):
    """
    　有給休暇層
    """
    __tablename__ = 't_paid_leave_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    paid_holiday_hours = Column('paid_holiday_hours', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class PaidLeaveLayerHistory(Base):
    """
    　有給休暇層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_paid_leave_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（PaidLeaveLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    paid_holiday_hours = Column('paid_holiday_hours', Integer, nullable=True, comment='有給時間数')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class ChildLeaveLayer(Base):
    """
    　育児休暇層
    """
    __tablename__ = 't_child_leave_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    child_time_leave_hours = Column('child_time_leave_hours', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class ChildLeaveLayerHistory(Base):
    """
    　育児休暇層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_child_leave_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（ChildLeaveLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    child_time_leave_hours = Column('child_time_leave_hours', Integer, nullable=True, comment='育児時間休暇')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class LateEarlyLayer(Base):
    """
    　遅刻早退層
    """
    __tablename__ = 't_late_early_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    late_minutes = Column('late_minutes', Integer, nullable=True, comment='遅刻時間')
    early_departure_minutes = Column('early_departure_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class LateEarlyLayerHistory(Base):
    """
    　遅刻早退層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_late_early_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（LateEarlyLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    late_minutes = Column('late_minutes', Integer, nullable=True, comment='遅刻時間')
    early_departure_minutes = Column('early_departure_minutes', Integer, nullable=True, comment='早退時間')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class AbsenceLayer(Base):
    """
    　欠勤層
    """
    __tablename__ = 't_absence_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    absence_minutes = Column('absence_minutes', Integer, nullable=True, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class AbsenceLayerHistory(Base):
    """
    　欠勤層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_absence_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（AbsenceLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    absence_minutes = Column('absence_minutes', Integer, nullable=True, comment='欠勤時間')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class SubstituteLeaveLayer(Base):
    """
    　代休層（日単位、実体は存在のみで表現）
    """
    __tablename__ = 't_substitute_leave_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class SubstituteLeaveLayerHistory(Base):
    """
    　代休層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_substitute_leave_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（SubstituteLeaveLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class SuspensionLayer(Base):
    """
    　休職層（日単位、実体は存在のみで表現）
    """
    __tablename__ = 't_suspension_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class SuspensionLayerHistory(Base):
    """
    　休職層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_suspension_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（SuspensionLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class ClosedLayer(Base):
    """
    　休業層（日単位、実体は存在のみで表現）
    """
    __tablename__ = 't_closed_layer'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, index=True, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='作成日時')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class ClosedLayerHistory(Base):
    """
    　休業層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_closed_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（ClosedLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新日時')
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default=datetime.now, comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=True, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )