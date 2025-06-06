
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