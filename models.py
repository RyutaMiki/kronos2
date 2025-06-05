
from datetime import datetime
from sqlalchemy import (
    Column, String, Text, Integer, Float, Boolean, Date, TIMESTAMP, DECIMAL,
    Index, UniqueConstraint, ForeignKey, ForeignKeyConstraint,
    PrimaryKeyConstraint, CheckConstraint, text, func, SmallInteger
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import uuid
from enumType import EnumType
from specifiedValue import *
Base = declarative_base()


class Users(Base):
    """
    　実在する利用者（人）を一意に管理するテーブル
    """
    __tablename__ = 'm_users'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, unique=True, default="lambda: str(uuid.uuid4())", comment='ユーザーUUID')
    user_name = Column('user_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='氏名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')



class Tenants(Base):
    """
    　会社ごとのテナント情報
    """
    __tablename__ = 'm_tenants'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, unique=True, default="lambda: str(uuid.uuid4())", comment='テナントUUID')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        ForeignKeyConstraint(['user_uuid'], ['m_users.user_uuid']),
        ForeignKeyConstraint(['tenant_uuid'], ['m_tenants.tenant_uuid']),
        UniqueConstraint('tenant_uuid', 'user_uuid', 'belong_start_date')
    )


class Closing(Base):
    """
    　締日マスタ（勤怠・弁当・交通費なども含めた汎用化可能）
    """
    __tablename__ = 'm_closing'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    closing_code = Column('closing_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='締日コード（給与・勤怠など用途別）')
    closing_name = Column('closing_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='締日名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_closing_tenant_uuid_closing_code', tenant_uuid, closing_code),
        UniqueConstraint(tenant_uuid, closing_code),
        UniqueConstraint(tenant_uuid, closing_name)
    )


class ClosingDateDetail(Base):
    """
    　締日ごとの年月別設定（開始日・終了日の定義）
    """
    __tablename__ = 'm_closing_date_detail'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    closing_code = Column('closing_code', String(10, collation='ja_JP.utf8'), nullable=False)
    year = Column('year', Integer, nullable=False)
    month = Column('month', Integer, nullable=False)
    term_from = Column('term_from', Date, nullable=False)
    term_to = Column('term_to', Date, nullable=False)
    __table_args__ = (
        Index('ix_m_closing_date_detail_tenant_uuid_closing_code_year_month', tenant_uuid, closing_code, year, month),
        UniqueConstraint(tenant_uuid, closing_code, year, month)
    )


class SalaryClosing(Base):
    """
    　給与締日マスタ（勤怠締日と紐付け可能）
    """
    __tablename__ = 'm_salary_closing'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    salary_closing_code = Column('salary_closing_code', String(10, collation='ja_JP.utf8'), nullable=False)
    salary_closing_name = Column('salary_closing_name', String(30, collation='ja_JP.utf8'), nullable=False)
    closing_code = Column('closing_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='紐づける勤怠締日コード')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_salary_closing_tenant_uuid_salary_closing_code', tenant_uuid, salary_closing_code),
        UniqueConstraint(tenant_uuid, salary_closing_code),
        UniqueConstraint(tenant_uuid, salary_closing_name)
    )


class SalaryClosingDateDetail(Base):
    """
    　給与締日ごとの支払予定日＋給与計算対象期間（年月別）
    """
    __tablename__ = 'm_salary_closing_date_detail'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    salary_closing_code = Column('salary_closing_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='給与締日コード')
    year = Column('year', Integer, nullable=False, comment='年（西暦）')
    month = Column('month', Integer, nullable=False, comment='月（1〜12）')
    term_from = Column('term_from', Date, nullable=False, comment='給与計算対象期間の開始日')
    term_to = Column('term_to', Date, nullable=False, comment='給与計算対象期間の終了日')
    payment_due_date = Column('payment_due_date', Date, nullable=True, comment='給与支払予定日（任意）')
    __table_args__ = (
        Index('ix_m_salary_closing_date_detail_tenant_uuid_salary_closing_code_year_month', tenant_uuid, salary_closing_code, year, month),
        UniqueConstraint(tenant_uuid, salary_closing_code, year, month)
    )


class GroundFormat(Base):
    """
    　規定・事由マスタ（出勤ステータス）
    """
    __tablename__ = 'm_ground_format'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    ground_code = Column('ground_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事由コード')
    ground_name = Column('ground_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='事由名')
    is_user_selectable = Column('is_user_selectable', Boolean, nullable=False, comment='出勤簿画面でユーザーが選択可能な事由か（falseの場合は固定表示される）')
    is_stamp_required = Column('is_stamp_required', Boolean, nullable=False, comment='打刻入力が必要か（欠勤日などは false）')
    is_working_day = Column('is_working_day', Boolean, nullable=False, comment='出勤簿で勤務日扱いするか')
    require_workflow = Column('require_workflow', Boolean, nullable=False, comment='ワークフロー申請が必要か')
    color = Column('color', String(7, collation='ja_JP.utf8'), nullable=False, comment='表示色（例: #FF0000）')
    contents = Column('contents', String(4096, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': "update_count"    }
    __table_args__ = (
        Index('ix_m_ground_format', ground_code),
        UniqueConstraint(ground_code)
    )


class AttendanceRatioRule(Base):
    """
    　規定・出勤率のルール定義（年休用など）
    """
    __tablename__ = 'attendance_ratio_rules'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー（業務では使用しない）')
    rule_id = Column('rule_id', String(20, collation='ja_JP.utf8'), nullable=False, unique=True, comment='業務用のルールID（例：ANNUAL_LEAVE）')
    name = Column('name', String(100, collation='ja_JP.utf8'), nullable=False, comment='ルール名（表示用）')
    description = Column('description', Text, nullable=True, comment='補足説明')
    start_date = Column('start_date', Date, nullable=False, comment='適用開始日')
    end_date = Column('end_date', Date, nullable=True, comment='適用終了日（NULLなら無期限）')



class AttendanceRatioRuleDetail(Base):
    """
    　規定・出勤率ルールにおける事由ごとの重み
    """
    __tablename__ = 'attendance_ratio_rule_details'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    rule_id = Column('rule_id', String(20, collation='ja_JP.utf8'), nullable=False, comment='業務用ルールID（親ルールへの参照）')
    ground_code = Column('ground_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='対象となる事由コード')
    labor_weight = Column('labor_weight', Float, nullable=False, comment='分母の重み（0.0〜1.0）')
    attendance_weight = Column('attendance_weight', Float, nullable=False, comment='分子の重み（0.0〜1.0）')



class WorkSchedule(Base):
    """
    　勤務体系マスタ（共通）
    """
    __tablename__ = 'm_work_schedule'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    work_schedule_name = Column('work_schedule_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='勤務体系名')
    working_system_abbreviation = Column('working_system_abbreviation', String(4, collation='ja_JP.utf8'), nullable=False, comment='勤務体系略名')
    working_system_type = Column('working_system_type', EnumType(enum_class=WorkingSystemType), nullable=False, comment='勤務の種類')
    is_job_before_start_time = Column('is_job_before_start_time', EnumType(enum_class=JobBeforeStartTime), nullable=True, comment='始業前労働を含む')
    job_start = Column('job_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間')
    job_end = Column('job_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    type = Column('type', String(20, collation='ja_JP.utf8'), nullable=False, default="normal", comment='勤務体系種別')
    __mapper_args__ = {
        'polymorphic_on': "type",        'polymorphic_identity': "normal",        'version_id_col': "update_count"    }



class FlexWorkSchedule(WorkSchedule):
    """
    　勤務体系マスタ（フレックス）
    """
    __tablename__ = 'm_work_schedule_flex'
    id = Column('id', Integer, primary_key=True)
    core_start = Column('core_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='コアタイム[開始]')
    core_end = Column('core_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='コアタイム[終了]')
    flex_start = Column('flex_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='フレキシブルタイム[開始]')
    flex_end = Column('flex_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='フレキシブルタイム[終了]')
    __mapper_args__ = {
        'polymorphic_identity': "flex"    }



class TransformationWorkSchedule(WorkSchedule):
    """
    　勤務体系マスタ（変形時間労働制）
    """
    __tablename__ = 'm_work_schedule_transformation'
    id = Column('id', Integer, primary_key=True)
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    flexible_labor_type = Column('flexible_labor_type', EnumType(enum_class=FlexibleLaborType), nullable=True, comment='変形時間労働制のタイプ')
    ground_code = Column('ground_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事由コード')
    job_start = Column('job_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間')
    job_end = Column('job_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間')
    __mapper_args__ = {
        'polymorphic_identity': "transformation"    }



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
    smile_mark = Column('smile_mark', String(10, collation='ja_JP.utf8'), nullable=True, comment='スマイルマーク')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class TimeCardLayerHistory(Base):
    """
    　タイムカード層の履歴（保証トランザクション対応）  
    　更新・削除・ロールバックなどの際に履歴を保持する
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
    smile_mark = Column('smile_mark', String(10, collation='ja_JP.utf8'), nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態（pending/committed/rolledback等）')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    working_interval = Column('working_interval', Integer, nullable=True, comment='インターバル時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class StandardWorkLayerHistory(Base):
    """
    　標準労働層の履歴（保証トランザクション対応）
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態（pending/committed/rolledback等）')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    rounded_break_end_time = Column('rounded_break_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='丸め休憩終了時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class BreakLayerHistory(Base):
    """
    　休憩時間層の履歴（保証トランザクション対応）
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態（pending/committed/rolledback等）')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    legal_overwork_minutes = Column('legal_overwork_minutes', Integer, nullable=True, comment='法定外労働時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date)
    )


class StatutoryWorkLayerHistory(Base):
    """
    　法定労働層の履歴（保証トランザクション対応）
    """
    __tablename__ = 't_statutory_work_layer_history'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='履歴ID')
    original_id = Column('original_id', Integer, nullable=False, comment='元テーブル（StatutoryWorkLayer）のID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    standard_legal_minutes = Column('standard_legal_minutes', Integer, nullable=True, comment='標準法定労働時間')
    legal_job_minutes = Column('legal_job_minutes', Integer, nullable=True, comment='法定労働時間')
    legal_overwork_minutes = Column('legal_overwork_minutes', Integer, nullable=True, comment='法定外労働時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態（pending/committed/rolledback等）')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    job_overwork_minutes = Column('job_overwork_minutes', Integer, nullable=True, comment='所定外労働時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    prescribed_holiday_work_minutes = Column('prescribed_holiday_work_minutes', Integer, nullable=True, comment='所定休日労働時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    statutory_holiday_work_minutes = Column('statutory_holiday_work_minutes', Integer, nullable=True, comment='法定休日労働時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    late_night_overwork_minutes = Column('late_night_overwork_minutes', Integer, nullable=True, comment='深夜労働時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    paid_holiday_hours = Column('paid_holiday_hours', Integer, nullable=True, comment='有給時間数')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    child_time_leave_hours = Column('child_time_leave_hours', Integer, nullable=True, comment='育児時間休暇')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    early_departure_minutes = Column('early_departure_minutes', Integer, nullable=True, comment='早退時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    absence_minutes = Column('absence_minutes', Integer, nullable=True, comment='欠勤時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
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
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
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
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='作成者ユーザーコード')
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now, comment='更新日時')
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False, comment='更新者ユーザーコード')
    update_count = Column('update_count', Integer, nullable=False, comment='更新回数')
    transaction_id = Column('transaction_id', String(36, collation='ja_JP.utf8'), nullable=False, comment='トランザクションID')
    history_version = Column('history_version', Integer, nullable=False, comment='履歴バージョン')
    operation_type = Column('operation_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='操作種別（I/U/D）')
    transaction_status = Column('transaction_status', String(20, collation='ja_JP.utf8'), nullable=False, comment='トランザクション状態')
    operated_at = Column('operated_at', TIMESTAMP, nullable=False, default="datetime.now", comment='操作日時')
    operated_by = Column('operated_by', String(36, collation='ja_JP.utf8'), nullable=False, comment='操作者UUID')
    is_latest = Column('is_latest', Boolean, nullable=False, default=true, comment='最新レコードフラグ')
    __table_args__ = (
        UniqueConstraint('original_id', 'history_version')
    )


class SupportWorkRecord(Base):
    """
    　他部署・他事業所への応援勤務時間を記録するテーブル
    """
    __tablename__ = 't_support_work_record'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    support_department_code = Column('support_department_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='応援先の部署コード')
    support_office_code = Column('support_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='応援先の事業所コード')
    support_start_time = Column('support_start_time', String(8, collation='ja_JP.utf8'), nullable=False, comment='応援開始時間')
    support_end_time = Column('support_end_time', String(8, collation='ja_JP.utf8'), nullable=False, comment='応援終了時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        UniqueConstraint(user_uuid, target_date, support_start_time)
    )


class WorkTaskRecord(Base):
    """
    　プロジェクト・タスクごとの工数を記録するテーブル
    """
    __tablename__ = 't_work_task_record'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    project_code = Column('project_code', String(20, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    task_code = Column('task_code', String(20, collation='ja_JP.utf8'), nullable=False, comment='タスクコード')
    work_minutes = Column('work_minutes', Integer, nullable=False, comment='作業時間（分）')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_work_task_record_user_uuid_target_date', user_uuid, target_date)
    )


class Role(Base):
    """
    　ロール（役割）マスタ
    """
    __tablename__ = 'm_role'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    role_code = Column('role_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='ロールコード')
    role_name = Column('role_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='ロール名')
    permission = Column('permission', EnumType(enum_class=Permission), nullable=False, comment='代行可能')
    system_company_flg = Column('system_company_flg', EnumType(enum_class=SystemCompanyFlg), nullable=False, comment='システム管理会社フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': "update_count"    }
    __table_args__ = (
        Index('ix_m_role', role_code),
        UniqueConstraint(role_code)
    )


class Policy(Base):
    """
    　アクセス制御ポリシーマスタ
    """
    __tablename__ = 'm_policy'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    principal_type = Column('principal_type', EnumType(enum_class=PrincipalType, int_enum=True), nullable=False, comment='主体種別')
    principal_id = Column('principal_id', String(64, collation='ja_JP.utf8'), nullable=False, comment='主体ID')
    resource_type = Column('resource_type', EnumType(enum_class=ResourceType, int_enum=True), nullable=False, comment='リソース種別')
    resource_id = Column('resource_id', String(64, collation='ja_JP.utf8'), nullable=False, comment='リソースID')
    action = Column('action', EnumType(enum_class=ActionType, int_enum=True), nullable=False, comment='アクション')
    effect = Column('effect', EnumType(enum_class=EffectType, int_enum=True), nullable=False, comment='許可 or 拒否')
    condition = Column('condition', Text, nullable=True, comment='条件[JSON]')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now", comment='作成日時')
    create_user_uuid = Column('create_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_user_uuid = Column('update_user_uuid', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': "update_count"    }
    __table_args__ = (
        Index('ix_m_policy_principal_type_principal_id_resource_type_resource_id_action', principal_type, principal_id, resource_type, resource_id, action),
        UniqueConstraint(principal_type, principal_id, resource_type, resource_id, action)
    )


class Screen(Base):
    """
    　画面マスタ
    """
    __tablename__ = 'm_screen'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    screen_name = Column('screen_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='画面名')
    __table_args__ = (
        Index('ix_m_screen', screen_code),
        UniqueConstraint(screen_code)
    )


class Api(Base):
    """
    　APIマスタ
    """
    __tablename__ = 'm_api'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    api_name = Column('api_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='API名')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    __table_args__ = (
        Index('ix_m_api_api_name_screen_code', api_name, screen_code),
        UniqueConstraint(api_name, screen_code)
    )


class ProjectCharter(Base):
    """
    　プロジェクト憲章マスタ
    """
    __tablename__ = 'm_project_charter'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    management_issues = Column('management_issues', String(4096, collation='ja_JP.utf8'), nullable=True, comment='経営課題')
    project_objective = Column('project_objective', String(4096, collation='ja_JP.utf8'), nullable=True, comment='プロジェクトの目的')
    project_goals = Column('project_goals', String(4096, collation='ja_JP.utf8'), nullable=True, comment='プロジェクトの目標')
    project_scope = Column('project_scope', String(4096, collation='ja_JP.utf8'), nullable=True, comment='プロジェクトのスコープ')
    assumptions = Column('assumptions', String(4096, collation='ja_JP.utf8'), nullable=True, comment='前提条件・制約条件')
    project_schedule = Column('project_schedule', String(4096, collation='ja_JP.utf8'), nullable=True, comment='プロジェクトのスケジュール')
    project_cost = Column('project_cost', String(4096, collation='ja_JP.utf8'), nullable=True, comment='プロジェクトのコスト')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_project_charter_tenant_uuid_project_code', tenant_uuid, project_code),
        UniqueConstraint(tenant_uuid, project_code)
    )


class ProjectPlan(Base):
    """
    　プロジェクト計画書マスタ
    """
    __tablename__ = 'm_project_plan'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    design_policy = Column('design_policy', String(4096, collation='ja_JP.utf8'), nullable=True, comment='設計方針')
    software_development_methodology = Column('software_development_methodology', String(4096, collation='ja_JP.utf8'), nullable=True, comment='ソフトウェア開発方式')
    development_goals = Column('development_goals', String(4096, collation='ja_JP.utf8'), nullable=True, comment='開発目標')
    deliverables = Column('deliverables', String(4096, collation='ja_JP.utf8'), nullable=True, comment='納品物')
    partner_company_management_plan = Column('partner_company_management_plan', String(4096, collation='ja_JP.utf8'), nullable=True, comment='パートナー会社管理計画')
    assumptions_partner_company_management_plan = Column('assumptions_partner_company_management_plan', String(4096, collation='ja_JP.utf8'), nullable=True, comment='パートナー会社管理計画　前提事項')
    progress_meeting = Column('progress_meeting', String(4096, collation='ja_JP.utf8'), nullable=True, comment='進捗会議')
    project_meeting = Column('project_meeting', String(4096, collation='ja_JP.utf8'), nullable=True, comment='プロジェクト会議')
    quality_management_plan = Column('quality_management_plan', String(4096, collation='ja_JP.utf8'), nullable=True, comment='品質管理計画')
    change_management_plan = Column('change_management_plan', String(4096, collation='ja_JP.utf8'), nullable=True, comment='変更管理計画')
    environment_setup_management_plan = Column('environment_setup_management_plan', String(4096, collation='ja_JP.utf8'), nullable=True, comment='環境整備管理計画')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_project_plan_tenant_uuid_project_code', tenant_uuid, project_code),
        UniqueConstraint(tenant_uuid, project_code)
    )


class Project(Base):
    """
    　プロジェクトマスタ
    """
    __tablename__ = 'm_project'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    project_name = Column('project_name', String(100, collation='ja_JP.utf8'), nullable=False, comment='プロジェクト名')
    expected_period_from = Column('expected_period_from', Date, nullable=True, comment='予定期間(From)')
    expected_period_to = Column('expected_period_to', Date, nullable=True, comment='予定期間(To)')
    planned_cost = Column('planned_cost', Integer, nullable=True, comment='予定原価')
    actual_period_from = Column('actual_period_from', Date, nullable=True, comment='実績期間(From)')
    actual_period_to = Column('actual_period_to', Date, nullable=True, comment='実績期間(To)')
    actual_cost = Column('actual_cost', Integer, nullable=True, comment='実績原価')
    budget_utilization_rate = Column('budget_utilization_rate', DECIMAL(3, 1), nullable=True, comment='予算消化率')
    completion_flag = Column('completion_flag', Boolean, nullable=False, comment='完了フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_project_tenant_uuid_project_code', tenant_uuid, project_code),
        UniqueConstraint(tenant_uuid, project_code)
    )


class Task(Base):
    """
    　タスクマスタ
    """
    __tablename__ = 'm_task'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    task_code = Column('task_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='タスクコード')
    task_name = Column('task_name', String(100, collation='ja_JP.utf8'), nullable=False, comment='タスク名')
    before_task_code = Column('before_task_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='直前のタスクコード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='従業員番号')
    expected_period_from = Column('expected_period_from', Date, nullable=True, comment='予定期間(From)')
    expected_period_to = Column('expected_period_to', Date, nullable=True, comment='予定期間(To)')
    planned_cost = Column('planned_cost', Integer, nullable=True, comment='予定原価')
    actual_period_from = Column('actual_period_from', Date, nullable=True, comment='実績期間(From)')
    actual_period_to = Column('actual_period_to', Date, nullable=True, comment='実績期間(To)')
    actual_cost = Column('actual_cost', Integer, nullable=True, comment='実績原価')
    budget_utilization_rate = Column('budget_utilization_rate', DECIMAL(3, 1), nullable=True, comment='予算消化率')
    work_phase_large_classification_code = Column('work_phase_large_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ大分類コード')
    work_phase_middle_classification_code = Column('work_phase_middle_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ中分類コード')
    work_phase_small_classification_code = Column('work_phase_small_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ小分類コード')
    completion_flag = Column('completion_flag', Boolean, nullable=False, comment='完了フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_task_tenant_uuid_project_code_task_code_before_task_code', tenant_uuid, project_code, task_code, before_task_code),
        UniqueConstraint(tenant_uuid, project_code, task_code, before_task_code)
    )


class AccidentWeeklyReport(Base):
    """
    　事故報告[週]トラン
    """
    __tablename__ = 't_accident_weekly_report'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    accident_report_number = Column('accident_report_number', Integer, nullable=False, comment='事故報告連番')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    subject = Column('subject', String(255, collation='ja_JP.utf8'), nullable=False, comment='件名')
    report_date_from = Column('report_date_from', Date, nullable=False, comment='報告日[開始]')
    report_date_to = Column('report_date_to', Date, nullable=False, comment='報告日[終了]')
    total_number_of_accidents_this_week = Column('total_number_of_accidents_this_week', Integer, nullable=False, comment='今週の事故総数')
    transaction_related_this_week = Column('transaction_related_this_week', Integer, nullable=False, comment='今週分の取引関連事故数')
    business_related_this_week = Column('business_related_this_week', Integer, nullable=False, comment='今週分の業務関連事故数')
    resolved_this_week = Column('resolved_this_week', Integer, nullable=False, comment='今週分の解決済事故数')
    transaction_related_cumulative = Column('transaction_related_cumulative', Integer, nullable=False, comment='累積の取引関連事故数')
    business_related_cumulative = Column('business_related_cumulative', Integer, nullable=False, comment='累積の業務関連事故数')
    resolved_cumulative = Column('resolved_cumulative', Integer, nullable=False, comment='累積の解決済事故数')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_accident_weekly_report_tenant_uuid_accident_report_number', tenant_uuid, accident_report_number),
        UniqueConstraint(tenant_uuid, accident_report_number)
    )


class AccidentDetailWeeklyReport(Base):
    """
    　事故報告[週]明細トラン
    """
    __tablename__ = 't_accident_detail_weekly_report'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    accident_report_number = Column('accident_report_number', Integer, nullable=False, comment='事故報告連番')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    accident_date = Column('accident_date', Date, nullable=False, comment='発生日')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='従業員番号')
    client_name = Column('client_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='取引先名')
    subject = Column('subject', String(4096, collation='ja_JP.utf8'), nullable=True, comment='件名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_accident_detail_weekly_report_tenant_uuid_accident_report_number_serial_number', tenant_uuid, accident_report_number, serial_number),
        UniqueConstraint(tenant_uuid, accident_report_number, serial_number)
    )


class ChangeManagement(Base):
    """
    　変更管理票トラン
    """
    __tablename__ = 't_change_management'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    change_management_number = Column('change_management_number', Integer, nullable=False, comment='変更管理番号')
    subject = Column('subject', String(255, collation='ja_JP.utf8'), nullable=False, comment='件名')
    estimated_man_hours = Column('estimated_man_hours', Integer, nullable=False, comment='見積工数')
    estimate_unit = Column('estimate_unit', EnumType(enum_class=EstimateUnit), nullable=False, comment='見積単位')
    actual_man_hours = Column('actual_man_hours', Integer, nullable=False, comment='実績工数')
    number_of_correction_steps = Column('number_of_correction_steps', Integer, nullable=True, comment='修正ステップ数')
    change_request_date = Column('change_request_date', Date, nullable=False, comment='変更依頼日')
    change_requester = Column('change_requester', String(50, collation='ja_JP.utf8'), nullable=True, comment='変更依頼者')
    deadline_date = Column('deadline_date', Date, nullable=True, comment='期限')
    task_assignee = Column('task_assignee', String(50, collation='ja_JP.utf8'), nullable=True, comment='作業担当者')
    completion_date = Column('completion_date', Date, nullable=True, comment='完了日')
    change_details = Column('change_details', String(4096, collation='ja_JP.utf8'), nullable=False, comment='変更内容')
    explanation = Column('explanation', String(4096, collation='ja_JP.utf8'), nullable=False, comment='説明')
    change_category = Column('change_category', EnumType(enum_class=ChangeCategory), nullable=False, comment='変更区分')
    change_status = Column('change_status', EnumType(enum_class=ChangeStatus), nullable=False, comment='変更状態')
    meeting_minutes_number = Column('meeting_minutes_number', Integer, nullable=True, comment='打ち合わせ覚書連番')
    meeting_minutes_serial_number = Column('meeting_minutes_serial_number', Integer, nullable=True, comment='打ち合わせ覚書シリアルナンバー')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_change_management_tenant_uuid_project_code_change_management_number', tenant_uuid, project_code, change_management_number),
        UniqueConstraint(tenant_uuid, project_code, change_management_number)
    )


class ProblemPoint(Base):
    """
    　問題点トラン
    """
    __tablename__ = 't_problem_point'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    problem_management_number = Column('problem_management_number', Integer, nullable=False, comment='問題点管理番号')
    accident_date = Column('accident_date', Date, nullable=False, comment='発生日')
    details_of_the_issue = Column('details_of_the_issue', String(4096, collation='ja_JP.utf8'), nullable=False, comment='問題内容')
    issuer = Column('issuer', String(50, collation='ja_JP.utf8'), nullable=False, comment='発行者')
    cause_of_the_problem = Column('cause_of_the_problem', EnumType(enum_class=CauseOfTheProblem), nullable=False, comment='問題の原因')
    revision_date = Column('revision_date', Date, nullable=True, comment='修正日')
    change_details = Column('change_details', String(4096, collation='ja_JP.utf8'), nullable=True, comment='変更内容')
    task_assignee = Column('task_assignee', String(50, collation='ja_JP.utf8'), nullable=True, comment='作業担当者')
    completion_date = Column('completion_date', Date, nullable=True, comment='完了日')
    completion_flag = Column('completion_flag', Boolean, nullable=False, comment='完了フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_problem_point_tenant_uuid_project_code_problem_management_number', tenant_uuid, project_code, problem_management_number),
        UniqueConstraint(tenant_uuid, project_code, problem_management_number)
    )


class MeetingMinutes(Base):
    """
    　打ち合わせ覚書トラン
    """
    __tablename__ = 't_meeting_minutes'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    meeting_minutes_number = Column('meeting_minutes_number', Integer, nullable=False, comment='打ち合わせ覚書連番')
    subject = Column('subject', String(255, collation='ja_JP.utf8'), nullable=False, comment='件名')
    meeting_date = Column('meeting_date', Date, nullable=False, comment='会議日')
    meeting_start_time = Column('meeting_start_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='会議開始時間')
    meeting_end_time = Column('meeting_end_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='会議終了時間')
    meeting_place_name = Column('meeting_place_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='会議場所')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_meeting_minutes_tenant_uuid_project_code_meeting_minutes_number', tenant_uuid, project_code, meeting_minutes_number),
        UniqueConstraint(tenant_uuid, project_code, meeting_minutes_number)
    )


class MeetingMinutesParticipants(Base):
    """
    　打ち合わせ覚書参加者トラン
    """
    __tablename__ = 't_meeting_minutes_participants'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    meeting_minutes_number = Column('meeting_minutes_number', Integer, nullable=False, comment='打ち合わせ覚書連番')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    company_name = Column('company_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='会社名')
    group_name = Column('group_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='部署名')
    position_name = Column('position_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='役職')
    meeting_participants_name = Column('meeting_participants_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='参加者名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_meeting_minutes_participants_tenant_uuid_project_code_meeting_minutes_number_serial_number', tenant_uuid, project_code, meeting_minutes_number, serial_number),
        UniqueConstraint(tenant_uuid, project_code, meeting_minutes_number, serial_number)
    )


class MeetingMinutesMaterials(Base):
    """
    　打ち合わせ覚書資料トラン
    """
    __tablename__ = 't_meeting_minutes_materials'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    meeting_minutes_number = Column('meeting_minutes_number', Integer, nullable=False, comment='打ち合わせ覚書連番')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    append_number = Column('append_number', Integer, nullable=False, comment='添付番号')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=False, comment='添付ファイルのパス')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_meeting_minutes_materials_tenant_uuid_project_code_meeting_minutes_number_serial_number_append_number', tenant_uuid, project_code, meeting_minutes_number, serial_number, append_number),
        UniqueConstraint(tenant_uuid, project_code, meeting_minutes_number, serial_number, append_number)
    )


class MeetingMinutesContents(Base):
    """
    　打ち合わせ覚書内容トラン
    """
    __tablename__ = 't_meeting_minutes_contents'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    meeting_minutes_number = Column('meeting_minutes_number', Integer, nullable=False, comment='打ち合わせ覚書連番')
    meeting_minutes_serial_number = Column('meeting_minutes_serial_number', Integer, nullable=False, comment='打ち合わせ覚書シリアルナンバー')
    agenda_title = Column('agenda_title', String(100, collation='ja_JP.utf8'), nullable=False, comment='議題')
    agenda_contents = Column('agenda_contents', String(255, collation='ja_JP.utf8'), nullable=False, comment='内容')
    deadline_date = Column('deadline_date', Date, nullable=False, comment='期限')
    conclusion = Column('conclusion', String(255, collation='ja_JP.utf8'), nullable=True, comment='結論')
    action_contents = Column('action_contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='結論')
    person_in_change = Column('person_in_change', String(50, collation='ja_JP.utf8'), nullable=False, comment='担当者')
    comunication_number = Column('comunication_number', Integer, nullable=True, comment='管理番号')
    omunication_serial_number = Column('omunication_serial_number', Integer, nullable=True, comment='コミュニケーション連番')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_meeting_minutes_contents_tenant_uuid_project_code_meeting_minutes_number_meeting_minutes_serial_number', tenant_uuid, project_code, meeting_minutes_number, meeting_minutes_serial_number),
        UniqueConstraint(tenant_uuid, project_code, meeting_minutes_number, meeting_minutes_serial_number)
    )


class Comunication(Base):
    """
    　コミュニケーショントラン
    """
    __tablename__ = 't_comunication'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    comunication_number = Column('comunication_number', Integer, nullable=False, comment='管理番号')
    omunication_serial_number = Column('omunication_serial_number', Integer, nullable=False, comment='コミュニケーション連番')
    date_of_issuance = Column('date_of_issuance', Date, nullable=False, comment='起票日')
    drafter = Column('drafter', String(50, collation='ja_JP.utf8'), nullable=False, comment='起票者')
    deadline_date = Column('deadline_date', Date, nullable=True, comment='期限')
    respondent = Column('respondent', String(50, collation='ja_JP.utf8'), nullable=True, comment='回答者')
    response_date = Column('response_date', Date, nullable=True, comment='回答日')
    question_content = Column('question_content', String(255, collation='ja_JP.utf8'), nullable=False, comment='質問内容')
    answer = Column('answer', String(255, collation='ja_JP.utf8'), nullable=True, comment='質問回答')
    completion_flag = Column('completion_flag', Boolean, nullable=False, comment='完了フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_comunication_tenant_uuid_project_code_comunication_number_omunication_serial_number', tenant_uuid, project_code, comunication_number, omunication_serial_number),
        UniqueConstraint(tenant_uuid, project_code, comunication_number, omunication_serial_number)
    )


class ComunicationMaterials(Base):
    """
    　コミュニケーション資料トラン
    """
    __tablename__ = 't_comunication_materials'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    comunication_number = Column('comunication_number', Integer, nullable=False, comment='管理番号')
    append_number = Column('append_number', Integer, nullable=False, comment='添付番号')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=False, comment='添付ファイルのパス')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_comunication_materials_tenant_uuid_project_code_comunication_number_append_number', tenant_uuid, project_code, comunication_number, append_number),
        UniqueConstraint(tenant_uuid, project_code, comunication_number, append_number)
    )


class RiskSheet(Base):
    """
    　リスクシートトラン
    """
    __tablename__ = 't_risk_sheet'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    sentence_number = Column('sentence_number', String(50, collation='ja_JP.utf8'), nullable=False, comment='文章番号')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_risk_sheet_tenant_uuid_sentence_number', tenant_uuid, sentence_number),
        UniqueConstraint(tenant_uuid, sentence_number)
    )


class RiskSheetDetail(Base):
    """
    　リスクシート明細トラン
    """
    __tablename__ = 't_risk_sheet_detail'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    sentence_number = Column('sentence_number', String(50, collation='ja_JP.utf8'), nullable=False, comment='文章番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    subject = Column('subject', String(4096, collation='ja_JP.utf8'), nullable=False, comment='件名')
    possibility_risk = Column('possibility_risk', EnumType(enum_class=PossibilityRisk), nullable=False, comment='リスクの可能性')
    intensity_risk = Column('intensity_risk', EnumType(enum_class=IntensityRisk), nullable=False, comment='リスクの強度')
    occurrence_date = Column('occurrence_date', String(20, collation='ja_JP.utf8'), nullable=False, comment='発生時期')
    specified_person = Column('specified_person', String(20, collation='ja_JP.utf8'), nullable=False, comment='特定者')
    owner_employee_code = Column('owner_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='所有者')
    type_of_risk = Column('type_of_risk', EnumType(enum_class=TypeOfRisk), nullable=False, comment='リスクの種類')
    results_of_the_countermeasure = Column('results_of_the_countermeasure', String(4096, collation='ja_JP.utf8'), nullable=False, comment='処理策の結果')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_risk_sheet_detail_tenant_uuid_sentence_number_serial_number', tenant_uuid, sentence_number, serial_number),
        UniqueConstraint(tenant_uuid, sentence_number, serial_number)
    )


class Stakeholder(Base):
    """
    　ステークホルダートラン
    """
    __tablename__ = 't_stakeholder'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_stakeholder_tenant_uuid_project_code', tenant_uuid, project_code),
        UniqueConstraint(tenant_uuid, project_code)
    )


class StakeholderDetail(Base):
    """
    　ステークホルダー明細トラン
    """
    __tablename__ = 't_stakeholder_detail'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    stakeholder = Column('stakeholder', String(50, collation='ja_JP.utf8'), nullable=False, comment='ステークホルダー')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_stakeholder_detail_tenant_uuid_project_code_stakeholder', tenant_uuid, project_code, stakeholder),
        UniqueConstraint(tenant_uuid, project_code, stakeholder)
    )


class Minutes(Base):
    """
    　議事録トラン
    """
    __tablename__ = 't_minutes'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    minutes_serial_number = Column('minutes_serial_number', Integer, nullable=False, comment='議事録連番')
    subject = Column('subject', String(255, collation='ja_JP.utf8'), nullable=False, comment='件名')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    meeting_start_time = Column('meeting_start_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='会議開始時間')
    meeting_end_time = Column('meeting_end_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='会議終了時間')
    meeting_place_name = Column('meeting_place_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='会議場所')
    next_agenda = Column('next_agenda', String(255, collation='ja_JP.utf8'), nullable=False, comment='次回予定')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_minutes_tenant_uuid_project_code_minutes_serial_number', tenant_uuid, project_code, minutes_serial_number),
        UniqueConstraint(tenant_uuid, project_code, minutes_serial_number)
    )


class MeetingParticipants(Base):
    """
    　会議参加者トラン
    """
    __tablename__ = 't_meeting_participants'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    minutes_serial_number = Column('minutes_serial_number', Integer, nullable=False, comment='議事録連番')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    company_name = Column('company_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='会社名')
    group_name = Column('group_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='部署名')
    position_name = Column('position_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='役職')
    meeting_participants_name = Column('meeting_participants_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='参加者名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_meeting_participants_tenant_uuid_project_code_minutes_serial_number_serial_number', tenant_uuid, project_code, minutes_serial_number, serial_number),
        UniqueConstraint(tenant_uuid, project_code, minutes_serial_number, serial_number)
    )


class MeetingMaterials(Base):
    """
    　会議資料トラン
    """
    __tablename__ = 't_meeting_materials'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    minutes_serial_number = Column('minutes_serial_number', Integer, nullable=False, comment='議事録連番')
    append_number = Column('append_number', Integer, nullable=False, comment='添付番号')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=False, comment='添付ファイルのパス')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_meeting_materials_tenant_uuid_project_code_minutes_serial_number_append_number', tenant_uuid, project_code, minutes_serial_number, append_number),
        UniqueConstraint(tenant_uuid, project_code, minutes_serial_number, append_number)
    )


class MeetingContents(Base):
    """
    　会議内容トラン
    """
    __tablename__ = 't_meeting_contents'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    minutes_serial_number = Column('minutes_serial_number', Integer, nullable=False, comment='議事録連番')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    resolved_matters = Column('resolved_matters', String(255, collation='ja_JP.utf8'), nullable=False, comment='決定事項・検討事項')
    person_in_change = Column('person_in_change', String(50, collation='ja_JP.utf8'), nullable=False, comment='担当者')
    deadline_date = Column('deadline_date', Date, nullable=False, comment='期限')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_meeting_contents_tenant_uuid_project_code_minutes_serial_number_serial_number', tenant_uuid, project_code, minutes_serial_number, serial_number),
        UniqueConstraint(tenant_uuid, project_code, minutes_serial_number, serial_number)
    )


class PendingItem(Base):
    """
    　宿題事項トラン
    """
    __tablename__ = 't_pending_item'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    minutes_serial_number = Column('minutes_serial_number', Integer, nullable=False, comment='議事録連番')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    pending_contents = Column('pending_contents', String(255, collation='ja_JP.utf8'), nullable=False, comment='宿題内容')
    person_in_change = Column('person_in_change', String(50, collation='ja_JP.utf8'), nullable=False, comment='担当者')
    deadline_date = Column('deadline_date', Date, nullable=False, comment='期限')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_pending_item_tenant_uuid_project_code_minutes_serial_number_serial_number', tenant_uuid, project_code, minutes_serial_number, serial_number),
        UniqueConstraint(tenant_uuid, project_code, minutes_serial_number, serial_number)
    )


class ProjectCompletionReport(Base):
    """
    　プロジェクト完了報告トラン
    """
    __tablename__ = 'm_project_completion_report'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    purpose = Column('purpose', String(4096, collation='ja_JP.utf8'), nullable=True, comment='目的')
    thoughts_on_cost = Column('thoughts_on_cost', String(4096, collation='ja_JP.utf8'), nullable=True, comment='費用管理の所感')
    thoughts_on_progress_management = Column('thoughts_on_progress_management', String(4096, collation='ja_JP.utf8'), nullable=True, comment='進捗管理の所感')
    thoughts_on_quality_management = Column('thoughts_on_quality_management', String(4096, collation='ja_JP.utf8'), nullable=True, comment='品質管理の所感')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_project_completion_report_tenant_uuid_project_code', tenant_uuid, project_code),
        UniqueConstraint(tenant_uuid, project_code)
    )


class ApplicationBase(Base):
    """
    　申請共通ベース（全申請に共通する情報を保持）
    """
    __tablename__ = 't_application_base'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, unique=True, comment='申請番号（ユニーク）')
    form_type = Column('form_type', String(20, collation='ja_JP.utf8'), nullable=False, comment='フォーム種別（例: accident, leave, overtime）')
    approval_status = Column('approval_status', EnumType(enum_class=ApprovalStatus), nullable=False, comment='承認状態')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_application_base_tenant_uuid_application_number', tenant_uuid, application_number)
    )


class AccidentReport(Base):
    """
    　事故報告申請トラン（申請番号により t_application_base と連携）
    """
    __tablename__ = 't_accident_report'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号（t_application_base に外部キー）')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    accident_date = Column('accident_date', Date, nullable=False, comment='発生日')
    client_name = Column('client_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='取引先名')
    subject = Column('subject', String(4096, collation='ja_JP.utf8'), nullable=False, comment='件名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_accident_report', application_number)
    )


class OvertimeApplication(Base):
    """
    　残業申請トラン（申請番号により t_application_base と連携）
    """
    __tablename__ = 't_overtime_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号（t_application_base に外部キー）')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    overwork_minutes = Column('overwork_minutes', Integer, nullable=True, comment='残業時間')
    reasons_over_work_contents = Column('reasons_over_work_contents', String(500, collation='ja_JP.utf8'), nullable=True, comment='時間外労働をさせる必要のある具体的事由')
    business_content = Column('business_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='業務内容')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    legal_overwork_minutes_now = Column('legal_overwork_minutes_now', Integer, nullable=True, comment='今月の法定外労働時間')
    limit_job_one_month_minutes = Column('limit_job_one_month_minutes', Integer, nullable=True, comment='一カ月の最大所定労働時間(分)')
    time_left = Column('time_left', Integer, nullable=True, comment='残り時間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_overtime_application', application_number)
    )


class LateNightOverworkApplication(Base):
    """
    　深夜労働申請トラン（申請番号により t_application_base と連携）
    """
    __tablename__ = 't_late_night_overwork_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号（t_application_base に外部キー）')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    late_night_overwork_minutes = Column('late_night_overwork_minutes', Integer, nullable=True, comment='深夜労働時間')
    business_content = Column('business_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='業務内容')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_late_night_overwork_application', application_number)
    )


class LateTimeApplication(Base):
    """
    　遅刻申請トラン（申請番号により t_application_base と連携）
    """
    __tablename__ = 't_late_time_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号（t_application_base に外部キー）')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    late_minutes = Column('late_minutes', Integer, nullable=True, comment='遅刻時間')
    late_content = Column('late_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='遅刻理由')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_late_time_application', application_number)
    )


class EarlyDepartureTimeApplication(Base):
    """
    　早退申請トラン（申請番号により t_application_base と連携）
    """
    __tablename__ = 't_early_departure_time_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号（t_application_base に外部キー）')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    early_departure_minutes = Column('early_departure_minutes', Integer, nullable=True, comment='早退時間')
    early_departure_content = Column('early_departure_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='早退理由')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_early_departure_time_application_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class HolidayWorkApplication(Base):
    """
    　法定休日出勤申請トラン（申請番号により t_application_base と連携）
    """
    __tablename__ = 't_holiday_work_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号（t_application_base に外部キー）')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    holiday_work_hours = Column('holiday_work_hours', Integer, nullable=True, comment='休日労働時間')
    business_content = Column('business_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='業務内容')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    re_ground_code = Column('re_ground_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='補正前事由コード')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_holiday_work_application_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class LeaveJobApplication(Base):
    """
    　休職申請トラン（申請番号により t_application_base と連携）
    """
    __tablename__ = 't_leave_job_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号（t_application_base に外部キー）')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    leave_job_start_date = Column('leave_job_start_date', Date, nullable=False, comment='休職開始日')
    leave_job_end_date = Column('leave_job_end_date', Date, nullable=False, comment='休職終了日')
    leave_job_content = Column('leave_job_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='休職理由')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_leave_job_application_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class LeaveJobApplicationDocument(Base):
    """
    　休職申請添付トラン（休職申請に紐づく添付資料を管理）
    """
    __tablename__ = 't_leave_job_application_document'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号（t_application_base に外部キー）')
    append_number = Column('append_number', Integer, nullable=False, comment='添付番号')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=False, comment='添付ファイルのパス')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_leave_job_application_document_tenant_uuid_application_number_append_number', tenant_uuid, application_number, append_number),
        UniqueConstraint(tenant_uuid, application_number, append_number)
    )


class RequestQuote(Base):
    """
    　見積もり申請トラン（プロジェクトに関連する見積申請の内容を管理）
    """
    __tablename__ = 't_request_quote'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号（t_application_base に外部キー）')
    request_quote_number = Column('request_quote_number', Integer, nullable=False, comment='見積り番号')
    request_quote_date = Column('request_quote_date', Date, nullable=False, comment='見積もり日付')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    estimated_amount = Column('estimated_amount', Integer, nullable=False, comment='見積金額')
    business_content = Column('business_content', String(100, collation='ja_JP.utf8'), nullable=False, comment='業務内容')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_request_quote_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class ParentalLeave(Base):
    """
    　育児休暇取得トラン
    """
    __tablename__ = 't_parental_leave'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    get_days = Column('get_days', Float, nullable=True, comment='取得日数')
    term_time_from = Column('term_time_from', String(5, collation='ja_JP.utf8'), nullable=True, comment='時間(開始)')
    term_time_to = Column('term_time_to', String(5, collation='ja_JP.utf8'), nullable=True, comment='時間(終了)')
    get_times = Column('get_times', Integer, nullable=True, comment='取得時間')
    parental_leave_type = Column('parental_leave_type', Enum, nullable=False, comment='種類')
    contents = Column('contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_parental_leave_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class DailyReport(Base):
    """
    　日報申請トラン
    """
    __tablename__ = 't_daily_report'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    business_content = Column('business_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='業務内容')
    approverl_flg = Column('approverl_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_daily_report_tenant_uuid_application_number', tenant_uuid, application_number)
    )


class DailyReportDetail(Base):
    """
    　日報申請明細トラン
    """
    __tablename__ = 't_daily_report_detail'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    task_code = Column('task_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='タスクコード')
    real_total_minutes = Column('real_total_minutes', Integer, nullable=False, comment='労働時間')
    business_content = Column('business_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='業務内容')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_daily_report_detail_tenant_uuid_application_number_project_code_task_code', tenant_uuid, application_number, project_code, task_code)
    )


class ExpenseClaim(Base):
    """
    　経費申請トラン
    """
    __tablename__ = 't_expense_claim'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=True, comment='プロジェクトコード')
    tax_inclusive_amount = Column('tax_inclusive_amount', Integer, nullable=False, comment='税込み金額')
    business_content = Column('business_content', String(100, collation='ja_JP.utf8'), nullable=False, comment='業務内容')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_expense_claim_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class ExpenseReportItemization(Base):
    """
    　経費申請明細トラン
    """
    __tablename__ = 't_expense_report_itemization'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    paid_target_date = Column('paid_target_date', Date, nullable=False, comment='支払日')
    business_content = Column('business_content', String(1024, collation='ja_JP.utf8'), nullable=False, comment='業務内容')
    tax_inclusive_amount = Column('tax_inclusive_amount', Integer, nullable=False, comment='税込み金額')
    account_code = Column('account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='勘定科目コード')
    sub_account_code = Column('sub_account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='補助勘定科目コード')
    receipt_availability = Column('receipt_availability', Boolean, nullable=True, comment='領収証有無')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_expense_report_itemization_tenant_uuid_application_number_serial_number', tenant_uuid, application_number, serial_number),
        UniqueConstraint(tenant_uuid, application_number, serial_number)
    )


class ExpenseReportAttachment(Base):
    """
    　経費申請添付トラン
    """
    __tablename__ = 't_expense_report_attachment'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    append_number = Column('append_number', Integer, nullable=False, comment='添付番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=False, comment='添付ファイルのパス')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_expense_report_attachment_tenant_uuid_application_number_append_number', tenant_uuid, application_number, append_number),
        UniqueConstraint(tenant_uuid, application_number, append_number)
    )


class TransferHolidayWorkApplication(Base):
    """
    　振替休出申請トラン
    """
    __tablename__ = 't_transfer_holiday_work_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    transfer_work_date = Column('transfer_work_date', Date, nullable=False, comment='振替出勤予定日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード')
    transfer_holiday_date = Column('transfer_holiday_date', Date, nullable=False, comment='振替休日予定日')
    business_content = Column('business_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='業務内容')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_transfer_holiday_work_application_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class ImprintCorrectionApplication(Base):
    """
    　打刻補正申請トラン
    """
    __tablename__ = 't_imprint_correction_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    stamping_start_time = Column('stamping_start_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='出勤時間')
    stamping_end_time = Column('stamping_end_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='退勤時間')
    telework_flg = Column('telework_flg', Boolean, nullable=True, comment='テレワークフラグ')
    imprint_correction_content = Column('imprint_correction_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='補正理由')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    re_correction_start_entry_flg = Column('re_correction_start_entry_flg', Enum, nullable=True, comment='補正前出勤時間打刻方法')
    re_correction_end_entry_flg = Column('re_correction_end_entry_flg', Enum, nullable=True, comment='補正前退勤時間打刻方法')
    re_correction_stamping_start_time = Column('re_correction_stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='補正前打刻出勤時間')
    re_correction_stamping_end_time = Column('re_correction_stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='補正前打刻退勤時間')
    re_telework_change_flg = Column('re_telework_change_flg', Boolean, nullable=True, comment='補正前テレワーク変更フラグ')
    stamping_start_time_change_flg = Column('stamping_start_time_change_flg', Boolean, nullable=True, comment='出勤時間変更フラグ')
    stamping_end_time_change_flg = Column('stamping_end_time_change_flg', Boolean, nullable=True, comment='退勤時間変更フラグ')
    telework_change_flg = Column('telework_change_flg', Boolean, nullable=True, comment='テレワーク変更フラグ')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_imprint_correction_application_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class ImprintCorrectionApplicationDetail(Base):
    """
    　打刻補正申請明細トラン
    """
    __tablename__ = 't_imprint_correction_application_detail'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    line_number = Column('line_number', Integer, nullable=False, comment='行番号')
    start_time = Column('start_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='開始時間')
    end_time = Column('end_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='終了時間')
    re_correction_start_time = Column('re_correction_start_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='補正前休憩開始時間')
    re_correction_end_time = Column('re_correction_end_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='補正前休憩終了時間')
    menstrual_leave_flg = Column('menstrual_leave_flg', Boolean, nullable=True, comment='生理休暇フラグ')
    menstrual_leave_chanhe_flg = Column('menstrual_leave_chanhe_flg', Boolean, nullable=True, comment='生理休暇変更フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_imprint_correction_application_detail_tenant_uuid_application_number_line_number', tenant_uuid, application_number, line_number),
        UniqueConstraint(tenant_uuid, application_number, line_number)
    )


class GroundConfirmEmployee(Base):
    """
    　事由確定トラン
    """
    __tablename__ = 't_ground_confirm_employee'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    confirm_day = Column('confirm_day', Date, nullable=False, comment='事由確定日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード')
    ground_code = Column('ground_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事由コード')
    contents = Column('contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    re_ground_code = Column('re_ground_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='補正前事由コード')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_ground_confirm_employee_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class AttendanceRecordApplication(Base):
    """
    　出勤簿申請トラン
    """
    __tablename__ = 't_attendance_record_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    job_month = Column('job_month', String(6, collation='ja_JP.utf8'), nullable=False, comment='労働月')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_attendance_record_application_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class CommutingRouteChangeApplication(Base):
    """
    　通勤経路変更申請トラン
    """
    __tablename__ = 't_commuting_route_change_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    commute_route_start_date = Column('commute_route_start_date', Date, nullable=True, comment='通勤経路開始日')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_commuting_route_change_application_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class CommutingRouteChangeApplicationDetail(Base):
    """
    　従業員通勤費トラン
    """
    __tablename__ = 't_commuting_route_change_application_detail'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    application_number = Column('application_number', Integer, nullable=True, comment='申請番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    traffic_division = Column('traffic_division', Enum, nullable=True, comment='交通区分')
    distance_to_use_transportation_equipment = Column('distance_to_use_transportation_equipment', Enum, nullable=True, comment='交通用具を使用する距離')
    payment_unit = Column('payment_unit', Enum, nullable=True, comment='支給単位')
    target_month = Column('target_month', Enum, nullable=True, comment='支給月度')
    payment_method = Column('payment_method', Enum, nullable=True, comment='支給方法')
    payment_amount = Column('payment_amount', Integer, nullable=True, comment='支給額')
    transportation_name = Column('transportation_name', String(40, collation='ja_JP.utf8'), nullable=True, comment='交通機関名')
    start_section = Column('start_section', String(32, collation='ja_JP.utf8'), nullable=True, comment='開始区間')
    end_section = Column('end_section', String(32, collation='ja_JP.utf8'), nullable=True, comment='終了区間')
    before_traffic_division = Column('before_traffic_division', Enum, nullable=True, comment='変更前_交通区分')
    before_distance_to_use_transportation_equipment = Column('before_distance_to_use_transportation_equipment', Enum, nullable=True, comment='変更前_交通用具を使用する距離')
    before_payment_unit = Column('before_payment_unit', Enum, nullable=True, comment='変更前_支給単位')
    before_target_month = Column('before_target_month', Enum, nullable=True, comment='変更前_支給月度')
    before_payment_method = Column('before_payment_method', Enum, nullable=True, comment='変更前_支給方法')
    before_payment_amount = Column('before_payment_amount', Integer, nullable=True, comment='変更前_支給額')
    before_transportation_name = Column('before_transportation_name', String(40, collation='ja_JP.utf8'), nullable=True, comment='変更前_交通機関名')
    before_start_section = Column('before_start_section', String(32, collation='ja_JP.utf8'), nullable=True, comment='変更前_開始区間')
    before_end_section = Column('before_end_section', String(32, collation='ja_JP.utf8'), nullable=True, comment='変更前_終了区間')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_commuting_route_change_application_detail_tenant_uuid_application_number_serial_number', tenant_uuid, application_number, serial_number),
        UniqueConstraint(tenant_uuid, application_number, serial_number)
    )


class AddressChangeApplication(Base):
    """
    　住所変更申請トラン
    """
    __tablename__ = 't_address_change_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=False, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='電話番号')
    emergency_contact = Column('emergency_contact', String(20, collation='ja_JP.utf8'), nullable=True, comment='緊急連絡先')
    other = Column('other', String(255, collation='ja_JP.utf8'), nullable=True, comment='その他')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    before_post_code = Column('before_post_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='変更前_郵便番号')
    before_state_code = Column('before_state_code', String(2, collation='ja_JP.utf8'), nullable=True, comment='変更前_都道府県コード')
    before_municipality_code = Column('before_municipality_code', String(3, collation='ja_JP.utf8'), nullable=True, comment='変更前_市町村コード')
    before_town = Column('before_town', String(50, collation='ja_JP.utf8'), nullable=True, comment='変更前_町村')
    before_building = Column('before_building', String(30, collation='ja_JP.utf8'), nullable=True, comment='変更前_ビル/番地')
    before_tel = Column('before_tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='変更前_電話番号')
    before_emergency_contact = Column('before_emergency_contact', String(20, collation='ja_JP.utf8'), nullable=True, comment='変更前_緊急連絡先')
    before_other = Column('before_other', String(255, collation='ja_JP.utf8'), nullable=True, comment='変更前_その他')
    moving_day = Column('moving_day', Date, nullable=True, comment='引っ越し日')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_address_change_application_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class AddressChangeApplicationDocument(Base):
    """
    　住所変更添付トラン
    """
    __tablename__ = 't_address_change_application_document'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    append_number = Column('append_number', Integer, nullable=False, comment='添付番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=False, comment='添付ファイルのパス')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_address_change_application_document_tenant_uuid_application_number_append_number', tenant_uuid, application_number, append_number),
        UniqueConstraint(tenant_uuid, application_number, append_number)
    )


class PersonalInformationChangeApplication(Base):
    """
    　個人情報変更申請トラン
    """
    __tablename__ = 't_personal_information_change_application'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    employee_name = Column('employee_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='氏名')
    pseudonym_reading = Column('pseudonym_reading', String(50, collation='ja_JP.utf8'), nullable=True, comment='氏名（ふりがな）')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='メールアドレス')
    sex = Column('sex', Enum, nullable=False, comment='性別')
    before_employee_name = Column('before_employee_name', String(30, collation='ja_JP.utf8'), nullable=True, comment='変更前_氏名')
    before_mail_address = Column('before_mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='変更前_メールアドレス')
    before_sex = Column('before_sex', Enum, nullable=True, comment='変更前_性別')
    supplement = Column('supplement', String(100, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_personal_information_change_application_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class CompanyPartner(Base):
    """
    　パートナーシップ申請トラン
    """
    __tablename__ = 't_company_partner'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    partner_tenant_uuid = Column('partner_tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='パートナーテナントUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    approval_flg = Column('approval_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_company_partner_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class EmployeeVaccination(Base):
    """
    　ワクチン接種トラン
    """
    __tablename__ = 't_employee_vaccination'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    application_number = Column('application_number', Integer, nullable=True, comment='申請番号')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    maker = Column('maker', Enum, nullable=False, comment='メーカー')
    vaccination = Column('vaccination', Enum, nullable=False, comment='ワクチン種類')
    inoculation_first_date = Column('inoculation_first_date', Date, nullable=True, comment='一回目接種日[接種予定日]')
    first_serial_number = Column('first_serial_number', String(255, collation='ja_JP.utf8'), nullable=True, comment='一回目製造番号')
    first_inoculation_ticket_number = Column('first_inoculation_ticket_number', String(255, collation='ja_JP.utf8'), nullable=True, comment='一回目接種券番号')
    first_inoculation_venue = Column('first_inoculation_venue', String(255, collation='ja_JP.utf8'), nullable=True, comment='一回目接種会場')
    first_physical_condition = Column('first_physical_condition', String(255, collation='ja_JP.utf8'), nullable=True, comment='一回目接種後の体調')
    inoculation_second_date = Column('inoculation_second_date', Date, nullable=True, comment='二回目接種日[接種予定日]')
    second_serial_number = Column('second_serial_number', String(255, collation='ja_JP.utf8'), nullable=True, comment='二回目製造番号')
    second_inoculation_ticket_number = Column('second_inoculation_ticket_number', String(255, collation='ja_JP.utf8'), nullable=True, comment='二回目接種券番号')
    second_inoculation_venue = Column('second_inoculation_venue', String(255, collation='ja_JP.utf8'), nullable=True, comment='二回目接種会場')
    second_physical_condition = Column('second_physical_condition', String(255, collation='ja_JP.utf8'), nullable=True, comment='二回目接種後の体調')
    inoculation_third_date = Column('inoculation_third_date', Date, nullable=True, comment='三回目接種日[接種予定日]')
    third_serial_number = Column('third_serial_number', String(255, collation='ja_JP.utf8'), nullable=True, comment='三回目製造番号')
    third_inoculation_ticket_number = Column('third_inoculation_ticket_number', String(255, collation='ja_JP.utf8'), nullable=True, comment='三回目接種券番号')
    third_inoculation_venue = Column('third_inoculation_venue', String(255, collation='ja_JP.utf8'), nullable=True, comment='三回目接種会場')
    third_physical_condition = Column('third_physical_condition', String(255, collation='ja_JP.utf8'), nullable=True, comment='三回目接種後の体調')
    approval_flg = Column('approval_flg', Enum, nullable=True, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_employee_vaccination_tenant_uuid_user_uuid_application_number', tenant_uuid, user_uuid, application_number),
        UniqueConstraint(tenant_uuid, user_uuid, application_number)
    )


class PaidLeaveEmployee(Base):
    """
    　従業員別有給休暇取得トラン
    """
    __tablename__ = 't_paid_leave_employee'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    user_uuid = Column('user_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='ユーザーUUID')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    get_days = Column('get_days', Float, nullable=True, comment='取得日数')
    term_time_from = Column('term_time_from', String(5, collation='ja_JP.utf8'), nullable=True, comment='時間(開始)')
    term_time_to = Column('term_time_to', String(5, collation='ja_JP.utf8'), nullable=True, comment='時間(終了)')
    get_times = Column('get_times', Integer, nullable=True, comment='取得時間')
    paid_holiday_type = Column('paid_holiday_type', Enum, nullable=False, comment='種類')
    contents = Column('contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    apply_change_term_from = Column('apply_change_term_from', Date, nullable=True, comment='申請者により申請された有効開始日')
    apply_change_term_to = Column('apply_change_term_to', Date, nullable=True, comment='申請者により申請された有効終了日')
    apply_change_term_time_from = Column('apply_change_term_time_from', String(5, collation='ja_JP.utf8'), nullable=True, comment='申請者により申請された時間(開始)')
    apply_change_term_time_to = Column('apply_change_term_time_to', String(5, collation='ja_JP.utf8'), nullable=True, comment='申請者により申請された時間(終了)')
    user_change_term_from = Column('user_change_term_from', Date, nullable=True, comment='使用者による時季変更行使時の有効開始日')
    user_change_term_to = Column('user_change_term_to', Date, nullable=True, comment='使用者による時季変更行使時の有効終了日')
    user_change_term_time_from = Column('user_change_term_time_from', String(5, collation='ja_JP.utf8'), nullable=True, comment='使用者による時季変更行使時の時間(開始)')
    user_change_term_time_to = Column('user_change_term_time_to', String(5, collation='ja_JP.utf8'), nullable=True, comment='使用者による時季変更行使時の時間(終了)')
    approverl_flg = Column('approverl_flg', Enum, nullable=False, comment='承認済フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_t_paid_leave_employee_tenant_uuid_application_number', tenant_uuid, application_number),
        UniqueConstraint(tenant_uuid, application_number)
    )


class IndustryBig(Base):
    """
    　業種マスタ(大分類) - 総務省 日本標準産業分類に準拠
    """
    __tablename__ = 'm_industry_big'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    industry_code_big = Column('industry_code_big', String(1, collation='ja_JP.utf8'), nullable=False, comment='業種(大分類)')
    industry_name = Column('industry_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='業種名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_industry_big', industry_code_big),
        UniqueConstraint(industry_code_big)
    )


class IndustryDuring(Base):
    """
    　業種マスタ(中分類) - 総務省 日本標準産業分類に準拠
    """
    __tablename__ = 'm_industry_during'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    industry_code_big = Column('industry_code_big', String(1, collation='ja_JP.utf8'), nullable=False, comment='業種(大分類)')
    industry_code_during = Column('industry_code_during', String(2, collation='ja_JP.utf8'), nullable=False, comment='業種(中分類)')
    industry_name = Column('industry_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='業種名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_industry_during_industry_code_big_industry_code_during', industry_code_big, industry_code_during),
        UniqueConstraint(industry_code_big, industry_code_during)
    )


class IndustrySmall(Base):
    """
    　業種マスタ(小分類) - 総務省 日本標準産業分類に準拠
    """
    __tablename__ = 'm_industry_small'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    industry_code_big = Column('industry_code_big', String(1, collation='ja_JP.utf8'), nullable=False, comment='業種(大分類)')
    industry_code_during = Column('industry_code_during', String(2, collation='ja_JP.utf8'), nullable=False, comment='業種(中分類)')
    industry_code_small = Column('industry_code_small', String(3, collation='ja_JP.utf8'), nullable=False, comment='業種(小分類)')
    industry_name = Column('industry_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='業種名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_industry_small_industry_code_big_industry_code_during_industry_code_small', industry_code_big, industry_code_during, industry_code_small),
        UniqueConstraint(industry_code_big, industry_code_during, industry_code_small)
    )


class State(Base):
    """
    　都道府県マスタ
    """
    __tablename__ = 'm_state'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    state_name = Column('state_name', String(6, collation='ja_JP.utf8'), nullable=False, comment='都道府県名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_state', state_code),
        UniqueConstraint(state_code)
    )


class Municipality(Base):
    """
    　市町村マスタ
    """
    __tablename__ = 'm_municipality'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=False, comment='市町村コード')
    municipality_name = Column('municipality_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='市町村名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_municipality_state_code_municipality_code', state_code, municipality_code),
        UniqueConstraint(state_code, municipality_code)
    )


class Language(Base):
    """
    　言語マスタ ISO 639-2
    """
    __tablename__ = 'm_language'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    language = Column('language', String(3, collation='ja_JP.utf8'), nullable=False, comment='言語')
    field_name = Column('field_name', String(128, collation='ja_JP.utf8'), nullable=False, comment='基本単語')
    label_name = Column('label_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='名称')
    abbreviated_name = Column('abbreviated_name', String(128, collation='ja_JP.utf8'), nullable=False, comment='略名')
    change_ok_flg = Column('change_ok_flg', Enum, nullable=True, comment='変更可能フラグ')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_language_language_field_name', language, field_name),
        Index('ix_m_language', language),
        Index('ix_m_language', field_name),
        Index('ix_m_language', label_name),
        Index('ix_m_language', abbreviated_name),
        UniqueConstraint(language, field_name)
    )


class Message(Base):
    """
    　メッセージマスタ ISO 639-2
    """
    __tablename__ = 'm_message'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    language = Column('language', String(3, collation='ja_JP.utf8'), nullable=False, comment='言語')
    message_id = Column('message_id', String(10, collation='ja_JP.utf8'), nullable=False, comment='メッセージID')
    message = Column('message', String(255, collation='ja_JP.utf8'), nullable=False, comment='メッセージ')
    correspondence_action = Column('correspondence_action', String(255, collation='ja_JP.utf8'), nullable=True, comment='対応方法')
    message_type = Column('message_type', Enum, nullable=False, comment='メッセージタイプ')
    message_classification = Column('message_classification', Enum, nullable=False, comment='分類')
    cause = Column('cause', Enum, nullable=False, comment='原因')
    correspondence = Column('correspondence', Enum, nullable=False, comment='対応')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_message_language_message_id', language, message_id),
        UniqueConstraint(language, message_id)
    )


class LanguageType(Base):
    """
    　言語種類マスタ
    """
    __tablename__ = 'm_language_type'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    language = Column('language', String(3, collation='ja_JP.utf8'), nullable=False, comment='言語')
    language_name = Column('language_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='言語')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_language_type', language),
        UniqueConstraint(language)
    )


class ApplicationClassificationFormat(Base):
    """
    　規定申請分類マスタ
    """
    __tablename__ = 'm_application_classification_format'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    application_classification_code = Column('application_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請分類コード')
    application_classification_name = Column('application_classification_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='申請分類名')
    sort_number = Column('sort_number', Integer, nullable=False, comment='ソート順')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_application_classification_format', application_classification_code),
        UniqueConstraint(application_classification_code)
    )


class ApplicationFormFormat(Base):
    """
    　規定申請書マスタ
    """
    __tablename__ = 'm_application_form_format'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    application_form_name = Column('application_form_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='申請書名')
    application_classification_code = Column('application_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請分類コード')
    skip_apply_employee = Column('skip_apply_employee', Boolean, nullable=False, comment='申請者を承認から外す判定')
    auto_approverl_flag = Column('auto_approverl_flag', Enum, nullable=False, comment='自動承認フラグ')
    pulling_flag = Column('pulling_flag', Enum, nullable=False, comment='引き戻し区分')
    withdrawal_flag = Column('withdrawal_flag', Enum, nullable=False, comment='取り下げ区分')
    route_flag = Column('route_flag', Enum, nullable=False, comment='直接部門の扱い')
    sort_number = Column('sort_number', Integer, nullable=False, comment='ソート順')
    table_name = Column('table_name', String(50, collation='ja_JP.utf8'), nullable=False, unique=True, comment='テーブル名')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_application_form_format', application_form_code),
        UniqueConstraint(application_form_code)
    )


class Parlance(Base):
    """
    　会社別用語マスタ ISO 639-2
    """
    __tablename__ = 'm_parlance'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    tenant_uuid = Column('tenant_uuid', String(36, collation='ja_JP.utf8'), nullable=False, comment='テナントUUID')
    language = Column('language', String(3, collation='ja_JP.utf8'), nullable=False, comment='言語')
    field_name = Column('field_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='基本単語')
    label_name = Column('label_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='名称')
    abbreviated_name = Column('abbreviated_name', String(128, collation='ja_JP.utf8'), nullable=False, comment='略名')
    create_date = Column('create_date', TIMESTAMP, nullable=False, default="datetime.now")
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, nullable=False, default="datetime.now", onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (
        Index('ix_m_parlance_tenant_uuid_language_field_name', tenant_uuid, language, field_name),
        Index('ix_m_parlance', tenant_uuid),
        Index('ix_m_parlance', language),
        Index('ix_m_parlance', field_name),
        UniqueConstraint(tenant_uuid, language, field_name)
    )