

class LineLinkCode(Base):
    """
    LINE連携用ワンタイムコード
    """
    __tablename__ = 't_line_link_code'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    code = Column(String(8, collation='ja_JP.utf8'), nullable=False, unique=True, comment='ワンタイムコード')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), nullable=False, index=True, comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    expires_at = Column(TIMESTAMP, nullable=False, comment="LINE連携用ワンタイムコードが使える期限")
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_line_link_code', "code"), UniqueConstraint("code"),)


class LineBinding(Base):
    """
    LINE userId と従業員マッピング    
    """
    __tablename__ = 'm_line_binding'
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    line_user_id = Column('line_user_id', String(50), nullable=False, comment='LINEユーザーID')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), nullable=False, index=True, comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    bound_at = Column(TIMESTAMP, server_default=func.now(), comment="LINE アカウントと従業員情報をひも付けた日時")
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_line_binding', "line_user_id"), UniqueConstraint("line_user_id"),)


class AccountingClassificationFormat(Base):
    """
    規定会計分類マスタ
    会計分類を管理します。
    """
    __tablename__ = "m_accounting_classification_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    accounting_classification_code = Column('accounting_classification_code', String(20, collation='ja_JP.utf8'), nullable=False, comment='会計分類コード')
    accounting_classification_name = Column('accounting_classification_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='会計分類名')
    accounting_from_classification = Column('accounting_from_classification', EnumType(enum_class=AccountingFromClassification), nullable=False, comment='会計帳票区分')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_accounting_classification_format', "accounting_classification_code"), UniqueConstraint("accounting_classification_code"),)


class FinancialStatementSubjectsFormat(Base):
    """
    規定決算書科目マスタ
    決算書科目を管理します。
    """
    __tablename__ = "m_financial_statement_subjects_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    accounting_classification_code = Column('accounting_classification_code', String(20, collation='ja_JP.utf8'), nullable=False, comment='会計分類コード')
    financial_statement_subjects_code = Column('financial_statement_subjects_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='決算書科目コード')
    financial_statement_subjects_name = Column('financial_statement_subjects_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='決算書科目名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_financial_statement_subjects_format', "financial_statement_subjects_code"), UniqueConstraint("financial_statement_subjects_code"),)


class AccountFormat(Base):
    """
    規定勘定科目マスタ
    勘定科目を管理します。
    """
    __tablename__ = "m_account_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    accounting_classification_code = Column('accounting_classification_code', String(20, collation='ja_JP.utf8'), nullable=False, comment='会計分類コード')
    financial_statement_subjects_code = Column('financial_statement_subjects_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='決算書科目コード')
    account_code = Column('account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='勘定科目コード')
    account_name = Column('account_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='勘定科目名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_account_format', "account_code"), UniqueConstraint("account_code"),)


class SubAccountFormat(Base):
    """
    規定補助勘定科目マスタ
    補助勘定科目を管理します。
    """
    __tablename__ = "m_sub_account_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    account_code = Column('account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='勘定科目コード')
    sub_account_code = Column('sub_account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='補助勘定科目コード')
    sub_account_name = Column('sub_account_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='補助勘定科目名')
    tax_type = Column('tax_type', EnumType(enum_class=TaxType), nullable=False, comment='税種別')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_sub_account_format', "account_code", "sub_account_code"), UniqueConstraint("account_code", "sub_account_code"),)


class SalesManagementAccount(Base):
    """
    売上管理勘定マスタ
    """
    __tablename__ = "m_sales_management_account"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    trading_day = Column('trading_day', Date, nullable=False, comment='取引日')
    number_of_billing_companies = Column('number_of_billing_companies', Integer, nullable=False, comment='請求会社数')
    total_billing_amount = Column('total_billing_amount', Integer, nullable=False, comment='合計請求額')
    number_of_depositing_companies = Column('number_of_depositing_companies', Integer, nullable=False, comment='入金会社数')
    total_deposit_amount = Column('total_deposit_amount', Integer, nullable=False, comment='合計入金額')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_sales_management_account', "trading_day"), UniqueConstraint("trading_day"), )


class StopEngine(Base):
    """
    システム停止マスタ
    """
    __tablename__ = "m_stop_engine"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    engine_name = Column('engine_name', EnumType(enum_class=EngineName), nullable=False, comment='エンジン名')
    emergency_stop_flag = Column('emergency_stop_flag', EnumType(enum_class=EmergencyStopFlag), nullable=False, comment='緊急停止フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_stop_engine', "engine_name"), UniqueConstraint("engine_name"), )



class Menu(Base):
    """
    メニューマスタ
    """
    __tablename__ = "m_menu"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    menu_code = Column('menu_code', String(3, collation='ja_JP.utf8'), nullable=False, comment='メニューコード')
    icon_name = Column('icon_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='アイコン')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_menu', "menu_code"), UniqueConstraint("menu_code"), )


class Help(Base):
    """
    ヘルプマスタ
    """
    __tablename__ = "m_help"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    menu_code = Column('menu_code', String(3, collation='ja_JP.utf8'), ForeignKey('m_menu.menu_code', onupdate='CASCADE', ondelete='CASCADE'), comment='メニューコード')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    help1 = Column('help1', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help2 = Column('help2', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help3 = Column('help3', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help4 = Column('help4', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help5 = Column('help5', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help6 = Column('help6', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help7 = Column('help7', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help8 = Column('help8', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help9 = Column('help9', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help10 = Column('help10', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help11 = Column('help11', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help12 = Column('help12', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help13 = Column('help13', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help14 = Column('help14', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    help15 = Column('help15', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヘルプ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_help', "screen_code"), UniqueConstraint("screen_code"), )


class SalaryItemFormat(Base):
    """
    規定給与項目マスタ
    システム固有の給与項目を管理します。(社会保険、源泉所得税、労働保険、等)
    """
    __tablename__ = "m_salary_item_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    salary_item_code = Column('salary_item_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='給与項目コード')
    salary_item_name = Column('salary_item_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='給与項目名')
    salary_bonus_classification = Column('salary_bonus_classification', EnumType(enum_class=SalaryBonusClassification), nullable=False, comment='支給区分')
    payment_deduction_category = Column('payment_deduction_category', EnumType(enum_class=PaymentDeductionCategory), nullable=False, comment='支給/控除区分')
    year_classification = Column('year_classification', EnumType(enum_class=Availability), nullable=False, comment='年俸制')
    month_classification = Column('month_classification', EnumType(enum_class=Availability), nullable=False, comment='月給制')
    month_day_classification = Column('month_day_classification', EnumType(enum_class=Availability), nullable=False, comment='月給日給制')
    day_month_classification = Column('day_month_classification', EnumType(enum_class=Availability), nullable=False, comment='日給月給制')
    time_classification = Column('time_classification', EnumType(enum_class=Availability), nullable=False, comment='時給制')
    bonus_classification = Column('bonus_classification', EnumType(enum_class=Availability), nullable=False, comment='賞与')
    employment_insurance_target_category = Column('employment_insurance_target_category', EnumType(enum_class=EmploymentInsuranceTargetCategory), nullable=False, comment='雇用保険対象区分')
    tax_target_category = Column('tax_target_category', EnumType(enum_class=TaxTargetCategory), nullable=False, comment='所得税対象区分')
    tax_exemption_limit = Column('tax_exemption_limit', Integer, nullable=True, comment='非課税枠[以下まで]')
    social_insurance_target_category = Column('social_insurance_target_category', EnumType(enum_class=SocialInsuranceTargetCategory), nullable=False, comment='社会保険対象区分')
    fixed_fluctuation = Column('fixed_fluctuation', EnumType(enum_class=FixedFluctuation), nullable=False, comment='計算方法')
    formula = Column('formula', String(255, collation='ja_JP.utf8'), nullable=True, comment='計算式')
    account_code = Column('account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='勘定科目コード')
    sub_account_code = Column('sub_account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='補助勘定科目コード')
    sign = Column('sign', EnumType(enum_class=Sign), nullable=False, comment='符号')
    payment_method = Column('payment_method', EnumType(enum_class=PaymentMethod), nullable=False, comment='支給方法')
    basic_salary = Column('basic_salary', EnumType(enum_class=BasicSalary), nullable=False, comment='基本給区分')
    daily_division = Column('daily_division', EnumType(enum_class=DailyDivision), nullable=True, comment='日割り対象')
    included_fixed_wages_social_security = Column('included_fixed_wages_social_security', Boolean, nullable=True, comment='社会保険料を決定する上での固定賃金に含む')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_salary_item_format', "salary_item_code"), UniqueConstraint("salary_item_code"),)



class Bank(Base):
    """
    銀行マスタ
    """
    __tablename__ = "m_bank"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    bank_code = Column('bank_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='銀行コード')
    bank_japanese_name = Column('bank_japanese_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='銀行名(カナ)')
    bank_name = Column('bank_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='銀行名')
    logical_deletion = Column('logical_deletion', Boolean, nullable=True, comment='論理削除フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_bank', "bank_code"), UniqueConstraint("bank_code"), )


class BankBranch(Base):
    """
    支店マスタ
    """
    __tablename__ = "m_bank_branch"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    bank_code = Column('bank_code', String(4, collation='ja_JP.utf8'), ForeignKey('m_bank.bank_code', onupdate='CASCADE', ondelete='CASCADE'), comment='銀行コード')
    branch_code = Column('branch_code', String(3, collation='ja_JP.utf8'), nullable=False, comment='支店コード')
    branch_japanese_name = Column('branch_japanese_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='支店名(カナ)')
    branch_name = Column('branch_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='支店名')
    logical_deletion = Column('logical_deletion', Boolean, nullable=True, comment='論理削除フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_bank_branch', "bank_code", "branch_code"), UniqueConstraint("bank_code", "branch_code"), )


class FundsTransferAgent(Base):
    """
    資金移動業者マスタ
    """
    __tablename__ = "m_funds_transfer_agent"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    jurisdiction_code = Column('jurisdiction_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='所轄コード')
    funds_transfer_agent_code = Column('funds_transfer_agent_code', String(5, collation='ja_JP.utf8'), nullable=False, comment='登録番号')
    registration_date = Column('registration_date', Date, nullable=False, comment='登録年月日')
    funds_transfer_agent_name = Column('funds_transfer_agent_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='資金移動業者名')
    corporate_number = Column('corporate_number', String(13, collation='ja_JP.utf8'), nullable=False, comment='法人番号')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='郵便番号')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=False, comment='電話番号')
    electoric_money_name = Column('electoric_money_name', String(30, collation='ja_JP.utf8'), nullable=True, comment='電子マネー名称')
    availability = Column('availability', EnumType(enum_class=Availability), nullable=False, comment='アカウント利用')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_funds_transfer_agent', "jurisdiction_code", "funds_transfer_agent_code"), UniqueConstraint("jurisdiction_code", "funds_transfer_agent_code"), )


class CompanyWorker(Base):
    """
    社労士マスタ
    """
    __tablename__ = "m_company_worker"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    social_insurance_labor_consultant = Column('social_insurance_labor_consultant', String(8, collation='ja_JP.utf8'), nullable=False, comment='社会保険労務士番号')
    company_worker_name = Column('company_worker_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='社労士名')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    password = Column('password', String(255, collation='ja_JP.utf8'), nullable=False, comment='パスワード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company_worker', "social_insurance_labor_consultant"), UniqueConstraint("social_insurance_labor_consultant"), )


class LocalGovernment(Base):
    """
    自治体マスタ
    """
    __tablename__ = "m_local_government"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    local_government_code = Column('local_government_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='全国地方公共団体コード')
    prefectures = Column('prefectures', String(6, collation='ja_JP.utf8'), nullable=True, comment='都道府県')
    city = Column('city', String(50, collation='ja_JP.utf8'), nullable=False, comment='市/区')
    person_in_charge = Column('person_in_charge', String(30, collation='ja_JP.utf8'), nullable=False, comment='担当係名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_local_government', "local_government_code"), UniqueConstraint("local_government_code"), )


class Report(Base):
    """
    規定帳票マスタ
    """
    __tablename__ = "m_report"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    report_code = Column('report_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='帳票コード')
    report_name = Column('report_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='帳票名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_report', "report_code"), UniqueConstraint("report_code"), )


class GroupFormat(Base):
    """
    規定部署マスタ
    """
    __tablename__ = "m_group_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    group_code = Column('group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='部署コード')
    group_name = Column('group_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='部署名')
    range = Column('range', EnumType(enum_class=Range), nullable=False, comment='利用権限範囲')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_group_format', "group_code"), UniqueConstraint("group_code"), )


class EmployeeClassificationFormat(Base):
    """
    規定従業員区分マスタ
    """
    __tablename__ = "m_employee_classification_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    employee_classification_code = Column('employee_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員区分')
    employee_classification_name = Column('employee_classification_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='従業員区分名')
    employee_classification_type = Column('employee_classification_type', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_classification_format', "employee_classification_code"), UniqueConstraint("employee_classification_code"),)


class RecruitmentCategoryFormat(Base):
    """
    規定採用区分マスタ
    """
    __tablename__ = "m_recruitment_category_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    recruitment_category_code = Column('recruitment_category_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='採用区分')
    recruitment_category_name = Column('recruitment_category_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='採用区分名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_recruitment_category_format', "recruitment_category_code"), UniqueConstraint("recruitment_category_code"),)


class EmploymentInsuranceRateFormat(Base):
    """
    規定雇用保険料率マスタ
    """
    __tablename__ = "m_employment_insurance_rate_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    general_business_labor_burden = Column('general_business_labor_burden', DECIMAL(3, 1), nullable=False, comment='一般の事業　労働者負担')
    general_business_owner_burden = Column('general_business_owner_burden', DECIMAL(3, 1), nullable=False, comment='一般の事業　事業主負担')
    forestly_business_labor_burden = Column('forestly_business_labor_burden', DECIMAL(3, 1), nullable=False, comment='農林水産・清酒製造の事業　労働者負担')
    forestly_business_owner_burden = Column('forestly_business_owner_burden', DECIMAL(3, 1), nullable=False, comment='農林水産・清酒製造の事業　事業主負担')
    construction_business_labor_burden = Column('construction_business_labor_burden', DECIMAL(3, 1), nullable=False, comment='建設の事業　労働者負担')
    construction_business_owner_burden = Column('construction_business_owner_burden', DECIMAL(3, 1), nullable=False, comment='建設の事業　事業主負担')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employment_insurance_rate_format', "target_date", "term_from"), UniqueConstraint("target_date", "term_from"),)


class WorkersAccidentCompensationInsuranceFormat(Base):
    """
    規定労災保険料率マスタ
    """
    __tablename__ = "m_workers_accident_compensation_insurance_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    business_type_classification = Column('business_type_classification', String(20, collation='ja_JP.utf8'), nullable=False, comment='事業の種類の分類')
    business_type_number = Column('business_type_number', String(2, collation='ja_JP.utf8'), nullable=False, comment='事業の種類')
    business_type_name = Column('business_type_name', String(60, collation='ja_JP.utf8'), nullable=False, comment='事業の種類名')
    workers_accident_compensation_rate = Column('workers_accident_compensation_rate', DECIMAL(3, 1), nullable=False, comment='労災保険料率')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_workers_accident_compensation_insurance_format', "target_date", "business_type_number"), UniqueConstraint("target_date", "business_type_number"),)


class PaidHolidayPaymentFormat(Base):
    """
    規定有給休暇支給マスタ
    有給休暇の付与までの月数、および付与日数をカテゴリー別に管理します。
    """
    __tablename__ = "m_paid_holiday_payment_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    number_of_working_days_per_week = Column('number_of_working_days_per_week', Integer, nullable=False, comment='週の労働日数')
    months_of_service = Column('months_of_service', Integer, nullable=False, comment='継続勤続月数')
    grant_days = Column('grant_days', Integer, nullable=False, comment='付与日数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_paid_holiday_payment_format', "number_of_working_days_per_week", "months_of_service"), UniqueConstraint("number_of_working_days_per_week", "months_of_service"), )



class LaborStandardsActRuleChapterFormat(Base):
    """
    規定労働基準法ルール[章]マスタ
    """
    __tablename__ = "m_labor_standards_act_rule_chapter_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    rule_contents = Column('rule_contents', String(1024, collation='ja_JP.utf8'), nullable=False, comment='内容')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_labor_standards_act_rule_chapter_format', "chapter"), UniqueConstraint("chapter"), )


class LaborStandardsActRuleArticleFormat(Base):
    """
    規定労働基準法ルール[条]マスタ
    """
    __tablename__ = "m_labor_standards_act_rule_article_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    article = Column('article', String(20, collation='ja_JP.utf8'), nullable=False, comment='条')
    rule_contents = Column('rule_contents', String(1024, collation='ja_JP.utf8'), nullable=False, comment='内容')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_labor_standards_act_rule_article_format', "chapter", "article"), UniqueConstraint("chapter", "article"), )


class LaborStandardsActRuleTermFormat(Base):
    """
    規定労働基準法ルール[項]マスタ
    """
    __tablename__ = "m_labor_standards_act_rule_term_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    article = Column('article', String(20, collation='ja_JP.utf8'), nullable=False, comment='条')
    term = Column('term', String(20, collation='ja_JP.utf8'), nullable=False, comment='項')
    rule_contents = Column('rule_contents', String(1024, collation='ja_JP.utf8'), nullable=False, comment='内容')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_labor_standards_act_rule_term_format', "chapter", "article", "term"), UniqueConstraint("chapter", "article", "term"), )


class LaborStandardsActRuleIssueFormat(Base):
    """
    規定労働基準法ルール[号]マスタ
    """
    __tablename__ = "m_labor_standards_act_rule_issue_format"

    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    article = Column('article', String(20, collation='ja_JP.utf8'), nullable=False, comment='条')
    term = Column('term', String(20, collation='ja_JP.utf8'), nullable=False, comment='項')
    issue = Column('issue', String(20, collation='ja_JP.utf8'), nullable=False, comment='号')
    rule_contents = Column('rule_contents', String(1024, collation='ja_JP.utf8'), nullable=False, comment='内容')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_labor_standards_act_rule_issue_format', "chapter", "article", "term", "issue"), UniqueConstraint("chapter", "article", "term", "issue"), )


class LaborStandardsActFormat(Base):
    """
    [規定]労働基準法マスタ
    """
    __tablename__ = "m_labor_standards_act_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    min_minutes = Column('min_minutes', Integer, nullable=False, comment='最小労働時間')
    max_minutes = Column('max_minutes', Integer, nullable=False, comment='最大労働時間')
    legal_job_minutes = Column('legal_job_minutes', Integer, nullable=False, comment='法定労働時間')
    weekly_working_minutes = Column('weekly_working_minutes', Integer, nullable=False, comment='一週間の最大労働時間')
    limit_legal_job_over_work_minutes = Column('limit_legal_job_over_work_minutes', Integer, nullable=False, comment='最大法定外労働時間[月]')
    limit_legal_job_over_work_minutes_year = Column('limit_legal_job_over_work_minutes_year', Integer, nullable=False, comment='最大法定外労働時間[年]')
    special_measures_weekly_working_minutes = Column('special_measures_weekly_working_minutes', Integer, nullable=False, comment='特例措置対象事業場の一週間の最大労働時間')
    legal_holiday_term_day = Column('legal_holiday_term_day', Integer, nullable=False, comment='最低一日の法定休日を取得させなければならない期間')
    late_night_overwork_time_schedule1 = Column('late_night_overwork_time_schedule1', String(11, collation='ja_JP.utf8'), nullable=False, comment='深夜労働時間の範囲1')
    late_night_overwork_time_schedule2 = Column('late_night_overwork_time_schedule2', String(11, collation='ja_JP.utf8'), nullable=False, comment='深夜労働時間の範囲2')
    late_night_overwork_time_schedule3 = Column('late_night_overwork_time_schedule3', String(11, collation='ja_JP.utf8'), nullable=False, comment='深夜労働時間の範囲3')
    late_night_overwork_time_schedule4 = Column('late_night_overwork_time_schedule4', String(11, collation='ja_JP.utf8'), nullable=False, comment='深夜労働時間の範囲4')
    break_time_term_06 = Column('break_time_term_06', Integer, nullable=False, comment='6時間未満の労働時間に対する最低保証休憩時間')
    break_time_term_08 = Column('break_time_term_08', Integer, nullable=False, comment='6時間を超え8時間以下の労働時間に対する最低保証休憩時間')
    break_time_term_08_over = Column('break_time_term_08_over', Integer, nullable=False, comment='8時間を超える労働時間に対する最低保証休憩時間')
    limit_legal_one_month_minutes_one_month = Column('limit_legal_one_month_minutes_one_month', Integer, nullable=False, comment='法定外労働時間[一箇月]　※法定休日労働時間を含む')
    limit_legal_one_month_minutes_average = Column('limit_legal_one_month_minutes_average', Integer, nullable=False, comment='法定外労働時間[一箇月平均]　※法定休日労働時間を含む')
    min_paid_holiday_days = Column('min_paid_holiday_days', Integer, nullable=False, comment='最小有給休暇日数')
    limit_special_provisions_count_year = Column('limit_special_provisions_count_year', Integer, nullable=True, comment='特別条項の回数[一年間]')
    limit_special_provisions_legal_overwork_minutes_one_year = Column('limit_special_provisions_legal_overwork_minutes_one_year', Integer, nullable=True, comment='特別条項の法定外労働時間[一年間]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_labor_standards_act_format', "term_from"), UniqueConstraint("term_from"), )


class MinimumWage(Base):
    """
    最低賃金マスタ
    """
    __tablename__ = "m_minimum_wage"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    minimum_wage = Column('minimum_wage', Integer, nullable=False, comment='最低賃金')
    date_of_issue = Column('date_of_issue', Date, nullable=False, comment='発行年月日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_minimum_wage', "target_date", "state_code"), UniqueConstraint("target_date", "state_code"),)


class IndustryMinimumWage(Base):
    """
    産業別最低賃金マスタ
    """
    __tablename__ = "m_industry_minimum_wage"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    industry_code = Column('industry_code', String(5, collation='ja_JP.utf8'), nullable=False, comment='産業コード')
    industry_name = Column('industry_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='業種名')
    date_of_issue = Column('date_of_issue', Date, nullable=False, comment='発行年月日')
    minimum_wage = Column('minimum_wage', Integer, nullable=False, comment='最低賃金')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_industry_minimum_wage', "state_code", "industry_code", "date_of_issue"), UniqueConstraint("state_code", "industry_code", "date_of_issue"), )


class SalaryIncomeDeduction(Base):
    """
    電算機計算の特例による給与所得控除マスタ
    """
    __tablename__ = "m_salary_income_deduction"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    thats_all = Column('thats_all', Integer, nullable=False, comment='以上')
    less_than = Column('less_than', Integer, nullable=False, comment='未満')
    special_income = Column('special_income', Integer, nullable=False, comment='給与所得控除の額')
    special_tax_rate = Column('special_tax_rate', DECIMAL(5, 3), nullable=False, comment='税率')
    adjust_amount = Column('adjust_amount', Integer, nullable=False, comment='調整額')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_salary_income_deduction', "target_year", "thats_all"), UniqueConstraint("target_year", "thats_all"), )


class SpecialDeductionComputerCalculation(Base):
    """
    電算機計算の特例による扶養控除マスタ
    """
    __tablename__ = "m_special_deduction_computer_calculation"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    spousal_deduction_amount = Column('spousal_deduction_amount', Integer, nullable=False, comment='配偶者控除の額')
    dependent_deduction_amount = Column('dependent_deduction_amount', Integer, nullable=False, comment='扶養控除の額')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_special_deduction_computer_calculation', "target_year"), UniqueConstraint("target_year"), )


class BasicDeductionDueToSpecialComputerCalculation(Base):
    """
    電算機計算の特例による基礎控除マスタ
    """
    __tablename__ = "m_basic_deduction_due_to_special_computer_calculation"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    thats_all = Column('thats_all', Integer, nullable=False, comment='以上')
    less_than = Column('less_than', Integer, nullable=False, comment='未満')
    basic_deduction_amount = Column('basic_deduction_amount', Integer, nullable=False, comment='基礎控除の額')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_basic_deduction_due_to_special_computer_calculation', "target_year", "thats_all"), UniqueConstraint("target_year", "thats_all"), )


class UseSpecialCaseWithholdingTaxAmountMonthly(Base):
    """
    電算機計算の特例による源泉徴収税額表(月額)マスタ
    """
    __tablename__ = "m_use_special_case_withholding_tax_amount_monthly"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    thats_all = Column('thats_all', Integer, nullable=False, comment='以上')
    less_than = Column('less_than', Integer, nullable=False, comment='未満')
    special_tax_rate = Column('special_tax_rate', DECIMAL(5, 3), nullable=False, comment='税率')
    adjust_amount = Column('adjust_amount', Integer, nullable=False, comment='調整額')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_use_special_case_withholding_tax_amount_monthly', "target_year", "thats_all"), UniqueConstraint("target_year", "thats_all"), )


class WithholdingTaxAmountMonthly(Base):
    """
    源泉徴収税額表(月額)マスタ
    """
    __tablename__ = "m_withholding_tax_amount_monthly"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    thats_all = Column('thats_all', Integer, nullable=False, comment='以上')
    less_than = Column('less_than', Integer, nullable=False, comment='未満')
    income_tax_0 = Column('income_tax_0', Integer, nullable=False, comment='所得税_甲_扶養家族0')
    income_tax_1 = Column('income_tax_1', Integer, nullable=False, comment='所得税_甲_扶養家族1')
    income_tax_2 = Column('income_tax_2', Integer, nullable=False, comment='所得税_甲_扶養家族2')
    income_tax_3 = Column('income_tax_3', Integer, nullable=False, comment='所得税_甲_扶養家族3')
    income_tax_4 = Column('income_tax_4', Integer, nullable=False, comment='所得税_甲_扶養家族4')
    income_tax_5 = Column('income_tax_5', Integer, nullable=False, comment='所得税_甲_扶養家族5')
    income_tax_6 = Column('income_tax_6', Integer, nullable=False, comment='所得税_甲_扶養家族6')
    income_tax_7 = Column('income_tax_7', Integer, nullable=False, comment='所得税_甲_扶養家族7')
    income_tax_x = Column('income_tax_x', Integer, nullable=False, comment='所得税_乙')
    income_kou = Column('income_kou', Integer, nullable=False, comment='甲_ベース所得')
    tax_rate_kou = Column('tax_rate_kou', DECIMAL(5, 3), nullable=False, comment='甲_税率')
    income_otsu = Column('income_otsu', Integer, nullable=False, comment='乙_ベース所得')
    tax_rate_otsu = Column('tax_rate_otsu', DECIMAL(5, 3), nullable=False, comment='乙_税率')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_withholding_tax_amount_monthly', "target_date", "thats_all"), UniqueConstraint("target_date", "thats_all"), )


class WithholdingTaxAmountDaily(Base):
    """
    源泉徴収税額表(日額)マスタ
    """
    __tablename__ = "m_withholding_tax_amount_daily"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    thats_all = Column('thats_all', Integer, nullable=False, comment='以上')
    less_than = Column('less_than', Integer, nullable=False, comment='未満')
    income_tax_0 = Column('income_tax_0', Integer, nullable=False, comment='所得税_甲_扶養家族0')
    income_tax_1 = Column('income_tax_1', Integer, nullable=False, comment='所得税_甲_扶養家族1')
    income_tax_2 = Column('income_tax_2', Integer, nullable=False, comment='所得税_甲_扶養家族2')
    income_tax_3 = Column('income_tax_3', Integer, nullable=False, comment='所得税_甲_扶養家族3')
    income_tax_4 = Column('income_tax_4', Integer, nullable=False, comment='所得税_甲_扶養家族4')
    income_tax_5 = Column('income_tax_5', Integer, nullable=False, comment='所得税_甲_扶養家族5')
    income_tax_6 = Column('income_tax_6', Integer, nullable=False, comment='所得税_甲_扶養家族6')
    income_tax_7 = Column('income_tax_7', Integer, nullable=False, comment='所得税_甲_扶養家族7')
    income_tax_x = Column('income_tax_x', Integer, nullable=False, comment='所得税_乙')
    income_kou = Column('income_kou', Integer, nullable=False, comment='甲_ベース所得')
    tax_rate_kou = Column('tax_rate_kou', DECIMAL(5, 3), nullable=False, comment='甲_税率')
    income_otsu = Column('income_otsu', Integer, nullable=False, comment='乙_ベース所得')
    tax_rate_otsu = Column('tax_rate_otsu', DECIMAL(5, 3), nullable=False, comment='乙_税率')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_withholding_tax_amount_daily', "target_date", "thats_all"), UniqueConstraint("target_date", "thats_all"), )


class WithholdingTaxAmountBonus(Base):
    """
    源泉徴収税額表(賞与)マスタ
    """
    __tablename__ = "m_withholding_tax_amount_bonus"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    tax_amount_classification = Column('tax_amount_classification', EnumType(enum_class=TaxAmountClassification), nullable=False, comment='税額区分')
    dependent_relatives = Column('dependent_relatives', Integer, nullable=False, comment='扶養親族')
    thats_all = Column('thats_all', Integer, nullable=False, comment='以上')
    less_than = Column('less_than', Integer, nullable=False, comment='未満')
    tax_rate = Column('tax_rate', DECIMAL(5, 3), nullable=False, comment='税率')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_withholding_tax_amount_bonus', "target_date", "tax_amount_classification", "dependent_relatives", "thats_all"), UniqueConstraint("target_date", "tax_amount_classification", "dependent_relatives", "thats_all"), )


class WelfarePensionGrade(Base):
    """
    厚生年金等級マスタ
    """
    __tablename__ = "m_welfare_pension_grade"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date_from = Column('target_date_from', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象年月[から]')
    target_date_to = Column('target_date_to', String(6, collation='ja_JP.utf8'), nullable=True, comment='対象年月[まで]')
    grade = Column('grade', Integer, nullable=False, comment='等級')
    standard_monthly_fee = Column('standard_monthly_fee', Integer, nullable=False, comment='標準報酬月額')
    thats_all = Column('thats_all', Integer, nullable=False, comment='以上')
    less_than = Column('less_than', Integer, nullable=False, comment='未満')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_welfare_pension_grade', "target_date_from", "grade"), UniqueConstraint("target_date_from", "grade"), )


class HealthInsuranceGrade(Base):
    """
    健康保険等級マスタ
    """
    __tablename__ = "m_health_insurance_grade"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date_from = Column('target_date_from', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象年月[から]')
    target_date_to = Column('target_date_to', String(6, collation='ja_JP.utf8'), nullable=True, comment='対象年月[まで]')
    grade = Column('grade', Integer, nullable=False, comment='等級')
    standard_monthly_fee = Column('standard_monthly_fee', Integer, nullable=False, comment='標準報酬月額')
    thats_all = Column('thats_all', Integer, nullable=False, comment='以上')
    less_than = Column('less_than', Integer, nullable=False, comment='未満')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_health_insurance_grade', "target_date_from", "grade"), UniqueConstraint("target_date_from", "grade"), )


class PublicHoliday(Base):
    """
    祝日マスタ
    """
    __tablename__ = "m_public_holiday"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    country_code = Column('country_code', EnumType(enum_class=CountryCode), comment='国別コード')
    public_holiday = Column('public_holiday', Date, nullable=False, comment='祝日')
    public_holiday_name = Column('public_holiday_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='祝日名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_public_holiday', "country_code", "public_holiday"), UniqueConstraint("country_code", "public_holiday"), )


class OperationNotice(Base):
    """
    運営からのお知らせトラン
    """
    __tablename__ = "t_operation_notice"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    notice_number = Column('notice_number', Integer, nullable=False, comment='お知らせ番号')
    notification = Column('notification', String(4096, collation='ja_JP.utf8'), nullable=False, comment='お知らせ')
    contents = Column('contents', String(4096, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    notification_transmission_date = Column('notification_transmission_date', TIMESTAMP, nullable=False, comment='お知らせ発信日')
    notification_display_date_from = Column('notification_display_date_from', Date, nullable=False, comment='お知らせ表示期間[開始]')
    notification_display_date_to = Column('notification_display_date_to', Date, nullable=True, comment='お知らせ表示期間[終了]')
    notice_type = Column('notice_type', EnumType(enum_class=NoticeType), nullable=False, comment='お知らせの種類')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_operation_notice', "notice_number"), UniqueConstraint("notice_number"),)


class AlertManagementFormat(Base):
    """
    規定申請書別アラート管理マスタ
    """
    __tablename__ = "m_alert_management_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    alert_management_control = Column('alert_management_control', EnumType(enum_class=AlertManagementControl), nullable=False, comment='アラート番号管理区分')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_alert_management_format', "application_form_code"), UniqueConstraint("application_form_code"),)


class Navigation(Base):
    """
    ナビゲーションマスタ
    """
    __tablename__ = "m_navigation"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    navigation_code = Column('navigation_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='ナビゲーションコード')
    navigation_name = Column('navigation_name', String(100, collation='ja_JP.utf8'), nullable=False, comment='ナビゲーション名')
    registration_unit = Column('registration_unit', EnumType(enum_class=RegistrationUnit), nullable=True, comment='登録単位')
    explanation = Column('explanation', String(255, collation='ja_JP.utf8'), nullable=False, comment='説明')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_navigation', "navigation_code"), UniqueConstraint("navigation_code"))


class NavigationDetail(Base):
    """
    ナビゲーション詳細マスタ
    """
    __tablename__ = "m_navigation_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    navigation_code = Column('navigation_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='ナビゲーションコード')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    before_screen_code = Column('before_screen_code', String(6, collation='ja_JP.utf8'), nullable=True, comment='直前の画面コード')
    required_time = Column('required_time', Integer, nullable=False, comment='所要時間[分]')
    display_order = Column('display_order', Integer, nullable=False, comment='表示順')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_navigation_detail', "navigation_code", "screen_code", "before_screen_code"), UniqueConstraint("navigation_code", "screen_code", "before_screen_code"))


class Category(Base):
    """
    カテゴリーマスタ
    """
    __tablename__ = "m_category"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    category = Column('category', String(1, collation='ja_JP.utf8'), nullable=False, comment='カテゴリー')
    category_name = Column('category_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='カテゴリー名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_category', "category"), UniqueConstraint("category"), )


class ScoreType(Base):
    """
    スコア種別マスタ
    """
    __tablename__ = "m_score_type"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    category = Column('category', String(1, collation='ja_JP.utf8'), nullable=False, comment='カテゴリー')
    score_type = Column('score_type', String(2, collation='ja_JP.utf8'), nullable=False, comment='スコア種別')
    score_type_name = Column('score_type_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='スコア種別名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_score_type', "category", "score_type"), UniqueConstraint("category", "score_type"), )


class ScoreDetail(Base):
    """
    スコア詳細マスタ
    """
    __tablename__ = "m_score_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    category = Column('category', String(1, collation='ja_JP.utf8'), nullable=False, comment='カテゴリー')
    score_type = Column('score_type', String(2, collation='ja_JP.utf8'), nullable=False, comment='スコア種別')
    score_detail_code = Column('score_detail_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='スコア詳細')
    score_detail_name = Column('score_detail_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='スコア詳細名')
    weight_factor = Column('weight_factor', Integer, nullable=False, comment='重み係数')
    high_score = Column('high_score', Integer, nullable=False, comment='最高点')
    industry_high_score = Column('industry_high_score', Integer, nullable=True, comment='産業別最高点')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_score_detail', "category", "score_type", "score_detail_code"), UniqueConstraint("category", "score_type", "score_detail_code"), )


class IndustryScoreDetail(Base):
    """
    産業別スコア詳細マスタ
    [毎月勤労統計調査より]
    https://www.mhlw.go.jp/toukei/list/30-1a.html
    """
    __tablename__ = "m_industry_score_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    category = Column('category', String(1, collation='ja_JP.utf8'), nullable=False, comment='カテゴリー')
    score_type = Column('score_type', String(2, collation='ja_JP.utf8'), nullable=False, comment='スコア種別')
    score_detail_code = Column('score_detail_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='スコア詳細')
    industry_code = Column('industry_code', String(5, collation='ja_JP.utf8'), nullable=False, comment='産業コード')
    base_line_score = Column('base_line_score', Integer, nullable=False, comment='ベースラインスコア(分水嶺)')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_industry_score_detail', "target_date", "category", "score_type", "score_detail_code", "industry_code"), UniqueConstraint("target_date", "category", "score_type", "score_detail_code", "industry_code"), )


class PopularityRankingByIndustry(Base):
    """
    業種別人気ランキングマスタ
    """
    __tablename__ = "m_popularity_ranking_by_industry"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    industry_code_big = Column('industry_code_big', String(1, collation='ja_JP.utf8'), nullable=False, comment='業種(大分類)')
    rank = Column('rank', Integer, nullable=False, comment='順位')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_popularity_ranking_by_industry', "target_year", "industry_code_big"), UniqueConstraint("target_year", "industry_code_big"), )


class WorkType(Base):
    """
    作業種別マスタ
    """
    __tablename__ = "m_work_type"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    work_type = Column('work_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業種別コード')
    work_type_name = Column('work_type_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='作業種別名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_work_type', "work_type"), UniqueConstraint("work_type"), )


class WorkPhaseLargeClassification(Base):
    """
    作業フェーズ[大分類]マスタ
    """
    __tablename__ = "m_work_phase_large_classification"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    work_type = Column('work_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業種別コード')
    work_phase_large_classification_code = Column('work_phase_large_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ大分類コード')
    work_phase_large_classification_name = Column('work_phase_large_classification_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ大分類名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_work_phase_large_classification', "work_type", "work_phase_large_classification_code"), UniqueConstraint("work_type", "work_phase_large_classification_code"), )


class WorkPhaseMiddleClassification(Base):
    """
    作業フェーズ[中分類]マスタ
    """
    __tablename__ = "m_work_phase_middle_classification"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    work_type = Column('work_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業種別コード')
    work_phase_large_classification_code = Column('work_phase_large_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ大分類コード')
    work_phase_middle_classification_code = Column('work_phase_middle_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ中分類コード')
    work_phase_middle_classification_name = Column('work_phase_middle_classification_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ中分類名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_work_phase_middle_classification', "work_type", "work_phase_large_classification_code", "work_phase_middle_classification_code"), UniqueConstraint("work_type", "work_phase_large_classification_code", "work_phase_middle_classification_code"), )


class WorkPhaseSmallClassification(Base):
    """
    作業フェーズ[小分類]マスタ
    """
    __tablename__ = "m_work_phase_small_classification"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    work_type = Column('work_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業種別コード')
    work_phase_large_classification_code = Column('work_phase_large_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ大分類コード')
    work_phase_middle_classification_code = Column('work_phase_middle_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ中分類コード')
    work_phase_small_classification_code = Column('work_phase_small_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ小分類コード')
    work_phase_small_classification_name = Column('work_phase_small_classification_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ小分類名')
    labor_cost_category = Column('labor_cost_category', EnumType(enum_class=LaborCostCategory), nullable=False, comment='労務費区分')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_work_phase_small_classification', "work_type", "work_phase_large_classification_code", "work_phase_middle_classification_code", "work_phase_small_classification_code"), UniqueConstraint("work_type", "work_phase_large_classification_code", "work_phase_middle_classification_code", "work_phase_small_classification_code"), )


class LayoutFormat(Base):
    """
    規定レイアウトマスタ
    会社のレイアウトを管理します。
    """
    __tablename__ = "m_layout_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    layout_code = Column('layout_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='レイアウトコード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    layout_name = Column('layout_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='レイアウト名')
    salary_category = Column('salary_category', EnumType(enum_class=SalaryCategory), nullable=False, comment='給与区分')
    payment_salary_item_code1 = Column('payment_salary_item_code1', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード1')
    payment_salary_item_code2 = Column('payment_salary_item_code2', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード2')
    payment_salary_item_code3 = Column('payment_salary_item_code3', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード3')
    payment_salary_item_code4 = Column('payment_salary_item_code4', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード4')
    payment_salary_item_code5 = Column('payment_salary_item_code5', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード5')
    payment_salary_item_code6 = Column('payment_salary_item_code6', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード6')
    payment_salary_item_code7 = Column('payment_salary_item_code7', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード7')
    payment_salary_item_code8 = Column('payment_salary_item_code8', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード8')
    payment_salary_item_code9 = Column('payment_salary_item_code9', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード9')
    payment_salary_item_code10 = Column('payment_salary_item_code10', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード10')
    payment_salary_item_code11 = Column('payment_salary_item_code11', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード11')
    payment_salary_item_code12 = Column('payment_salary_item_code12', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード12')
    payment_salary_item_code13 = Column('payment_salary_item_code13', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード13')
    payment_salary_item_code14 = Column('payment_salary_item_code14', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード14')
    payment_salary_item_code15 = Column('payment_salary_item_code15', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード15')
    payment_salary_item_code16 = Column('payment_salary_item_code16', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード16')
    payment_salary_item_code17 = Column('payment_salary_item_code17', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード17')
    payment_salary_item_code18 = Column('payment_salary_item_code18', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード18')
    payment_salary_item_code19 = Column('payment_salary_item_code19', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード19')
    payment_salary_item_code20 = Column('payment_salary_item_code20', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード20')
    payment_salary_item_code21 = Column('payment_salary_item_code21', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード21')
    payment_salary_item_code22 = Column('payment_salary_item_code22', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード22')
    payment_salary_item_code23 = Column('payment_salary_item_code23', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード23')
    payment_salary_item_code24 = Column('payment_salary_item_code24', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード24')
    payment_salary_item_code25 = Column('payment_salary_item_code25', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード25')
    payment_salary_item_code26 = Column('payment_salary_item_code26', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード26')
    payment_salary_item_code27 = Column('payment_salary_item_code27', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード27')
    payment_salary_item_code28 = Column('payment_salary_item_code28', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード28')
    payment_salary_item_code29 = Column('payment_salary_item_code29', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード29')
    payment_salary_item_code30 = Column('payment_salary_item_code30', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード30')
    deduction_salary_item_code1 = Column('deduction_salary_item_code1', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード1')
    deduction_salary_item_code2 = Column('deduction_salary_item_code2', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード2')
    deduction_salary_item_code3 = Column('deduction_salary_item_code3', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード3')
    deduction_salary_item_code4 = Column('deduction_salary_item_code4', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード4')
    deduction_salary_item_code5 = Column('deduction_salary_item_code5', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード5')
    deduction_salary_item_code6 = Column('deduction_salary_item_code6', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード6')
    deduction_salary_item_code7 = Column('deduction_salary_item_code7', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード7')
    deduction_salary_item_code8 = Column('deduction_salary_item_code8', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード8')
    deduction_salary_item_code9 = Column('deduction_salary_item_code9', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード9')
    deduction_salary_item_code10 = Column('deduction_salary_item_code10', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード10')
    deduction_salary_item_code11 = Column('deduction_salary_item_code11', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード11')
    deduction_salary_item_code12 = Column('deduction_salary_item_code12', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード12')
    deduction_salary_item_code13 = Column('deduction_salary_item_code13', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード13')
    deduction_salary_item_code14 = Column('deduction_salary_item_code14', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード14')
    deduction_salary_item_code15 = Column('deduction_salary_item_code15', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード15')
    deduction_salary_item_code16 = Column('deduction_salary_item_code16', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード16')
    deduction_salary_item_code17 = Column('deduction_salary_item_code17', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード17')
    deduction_salary_item_code18 = Column('deduction_salary_item_code18', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード18')
    deduction_salary_item_code19 = Column('deduction_salary_item_code19', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード19')
    deduction_salary_item_code20 = Column('deduction_salary_item_code20', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード20')
    deduction_salary_item_code21 = Column('deduction_salary_item_code21', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード21')
    deduction_salary_item_code22 = Column('deduction_salary_item_code22', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード22')
    deduction_salary_item_code23 = Column('deduction_salary_item_code23', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード23')
    deduction_salary_item_code24 = Column('deduction_salary_item_code24', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード24')
    deduction_salary_item_code25 = Column('deduction_salary_item_code25', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード25')
    deduction_salary_item_code26 = Column('deduction_salary_item_code26', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード26')
    deduction_salary_item_code27 = Column('deduction_salary_item_code27', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード27')
    deduction_salary_item_code28 = Column('deduction_salary_item_code28', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード28')
    deduction_salary_item_code29 = Column('deduction_salary_item_code29', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード29')
    deduction_salary_item_code30 = Column('deduction_salary_item_code30', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード30')
    availability = Column('availability', EnumType(enum_class=Availability), nullable=False, comment='アカウント利用')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_layout_format', "layout_code", "term_from"), UniqueConstraint("layout_code", "term_from"),)


class TabFormat(Base):
    """
    規定タブマスタ
    """
    __tablename__ = "m_tab_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    tab_code = Column('tab_code', String(1, collation='ja_JP.utf8'), nullable=False, comment='タブコード')
    tab_name = Column('tab_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='タブ名')
    is_use = Column('is_use', Boolean, nullable=False, comment='使用有無')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_tab_format', "tab_code"), UniqueConstraint("tab_code"),)


class ExecutionTime(Base):
    """
    実行ログ
    実行時間を計測します。
    """
    __tablename__ = "t_execution_time"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    api_name = Column('api_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='API名')
    execution_time = Column('execution_time', Integer, nullable=False, comment='実行時間[秒]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_execution_time', "api_name", "create_date"), UniqueConstraint("api_name", "create_date"),)


class Company(Base):
    """
    会社マスタ
    """
    __tablename__ = "m_company"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), nullable=False, index=True, unique=True, comment='会社コード')
    company_name = Column('company_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='会社名')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=True, comment='添付ファイルのパス')
    language = Column('language', String(3, collation='ja_JP.utf8'), nullable=False, comment='言語')
    start_day_of_the_week = Column('start_day_of_the_week', EnumType(enum_class=DayOfTheWeek), nullable=False, comment='週始めの曜日')
    rounding_second = Column('rounding_second', EnumType(enum_class=RoundingSecond), nullable=False, comment='労働時間[秒]の丸め')
    rounding_type = Column('rounding_type', EnumType(enum_class=RoundingType), nullable=False, comment='労働時間[分]の丸め')
    rounding_month = Column('rounding_month', EnumType(enum_class=RoundingMonth), nullable=True, comment='労働時間の単位[分]')
    rounding_term = Column('rounding_term', Integer, nullable=False, comment='法定労働時間の単位[分]')
    rounding_term_over_work = Column('rounding_term_over_work', Integer, nullable=False, comment='法定外労働時間の単位[分]')
    rounding_job_start = Column('rounding_job_start', EnumType(enum_class=RoundingJobStart), nullable=True, comment='出勤時間')
    rounding_job_end = Column('rounding_job_end', EnumType(enum_class=RoundingJobEnd), nullable=True, comment='退勤時間')
    home_page = Column('home_page', String(255, collation='ja_JP.utf8'), nullable=True, comment='ホームページ')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=False, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=False, comment='電話番号')
    fax = Column('fax', String(20, collation='ja_JP.utf8'), nullable=True, comment='ファックス番号')
    industry_code_big = Column('industry_code_big', String(1, collation='ja_JP.utf8'), nullable=False, comment='業種(大分類)')
    industry_code_during = Column('industry_code_during', String(2, collation='ja_JP.utf8'), nullable=False, comment='業種(中分類)')
    industry_code_small = Column('industry_code_small', String(4, collation='ja_JP.utf8'), nullable=False, comment='業種(小分類)')
    system_company_flg = Column('system_company_flg', EnumType(enum_class=SystemCompanyFlg), nullable=False, comment='システム管理会社フラグ')
    corporate_number = Column('corporate_number', String(13, collation='ja_JP.utf8'), nullable=True, comment='法人番号')
    labor_insurance_number = Column('labor_insurance_number', String(18, collation='ja_JP.utf8'), nullable=True, comment='労働保険番号')
    is_smile_mark = Column('is_smile_mark', EnumType(enum_class=IsSmileMark), nullable=True, comment='スマイルマーク利用有無')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=False, index=True, comment='メールアドレス')
    attendance_management = Column('attendance_management', EnumType(enum_class=AttendanceManagement), nullable=True, comment='労働管理')
    payroll_management = Column('payroll_management', EnumType(enum_class=PayrollManagement), nullable=True, comment='賃金管理')
    disclosure_of_company = Column('disclosure_of_company', EnumType(enum_class=DisclosureOfCompany), nullable=True, comment='会社名の公開')
    campaign_price = Column('campaign_price', Integer, nullable=True, comment='利用者当たりの特別価格')
    number_of_working_hours_on_the_28th = Column('number_of_working_hours_on_the_28th', String(6, collation='ja_JP.utf8'), nullable=True, comment='28日の労働時間数')
    number_of_working_hours_on_the_29th = Column('number_of_working_hours_on_the_29th', String(6, collation='ja_JP.utf8'), nullable=True, comment='29日の労働時間数')
    number_of_working_hours_on_the_30th = Column('number_of_working_hours_on_the_30th', String(6, collation='ja_JP.utf8'), nullable=True, comment='30日の労働時間数')
    number_of_working_hours_on_the_31th = Column('number_of_working_hours_on_the_31th', String(6, collation='ja_JP.utf8'), nullable=True, comment='31日の労働時間数')
    flextime_full_two_day_weekend_system = Column('flextime_full_two_day_weekend_system', EnumType(enum_class=FlextimeFullTwoDayWeekendSystem), nullable=True, comment='完全週休二日制におけるフレックスタイムの適用有無')
    collection_of_resident_tax = Column('collection_of_resident_tax', EnumType(enum_class=CollectionOfResidentTax), nullable=True, comment='徴収タイミング')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)

    # 会社単位[マスタ系] 59 tables
    m_resarch_informations = relationship("ResarchInformation", backref="m_company", cascade="all", passive_deletes=True)
    m_resarch_information_supplier_details = relationship("ResarchInformationSupplierDetail", backref="m_company", cascade="all", passive_deletes=True)
    m_resarch_information_customer_details = relationship("ResarchInformationCustomerDetail", backref="m_company", cascade="all", passive_deletes=True)
    m_resarch_information_main_bank_details = relationship("ResarchInformationMainBankDetail", backref="m_company", cascade="all", passive_deletes=True)
    m_resarch_information_recruitment_details = relationship("ResarchInformationRecruitmentDetail", backref="m_company", cascade="all", passive_deletes=True)
    m_resarch_information_performance_details = relationship("ResarchInformationPerformanceDetail", backref="m_company", cascade="all", passive_deletes=True)
    m_service_destinations = relationship("ServiceDestination", backref="m_company", cascade="all", passive_deletes=True)
    m_parlances = relationship("Parlance", backref="m_company", cascade="all", passive_deletes=True)
    m_company_worker_managements = relationship("CompanyWorkerManagement", backref="m_company", cascade="all", passive_deletes=True)
    m_offices = relationship("Office", backref="m_company", cascade="all", passive_deletes=True)
    m_places = relationship("Place", backref="m_company", cascade="all", passive_deletes=True)
    m_businesss = relationship("Business", backref="m_company", cascade="all", passive_deletes=True)
    m_teams = relationship("Team", backref="m_company", cascade="all", passive_deletes=True)
    m_groups = relationship("Group", backref="m_company", cascade="all", passive_deletes=True)
    m_group_applications = relationship("GroupApplication", backref="m_company", cascade="all", passive_deletes=True)
    m_office_applications = relationship("OfficeApplication", backref="m_company", cascade="all", passive_deletes=True)
    m_grounds = relationship("Ground", backref="m_company", cascade="all", passive_deletes=True)
    m_roles = relationship("Role", backref="m_company", cascade="all", passive_deletes=True)
    m_authoritys = relationship("Authority", backref="m_company", cascade="all", passive_deletes=True)
    m_lunch_suppliers = relationship("LunchSupplier", backref="m_company", cascade="all", passive_deletes=True)
    m_lunchs = relationship("Lunch", backref="m_company", cascade="all", passive_deletes=True)
    m_lunch_orders = relationship("LunchOrder", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_classifications = relationship("EmployeeClassification", backref="m_company", cascade="all", passive_deletes=True)
    m_alert_managements = relationship("AlertManagement", backref="m_company", cascade="all", passive_deletes=True)
    m_recruitment_categorys = relationship("RecruitmentCategory", backref="m_company", cascade="all", passive_deletes=True)
    m_company_applications = relationship("CompanyApplication", backref="m_company", cascade="all", passive_deletes=True)
    m_legal_rule_formats = relationship("LegalRuleFormat", backref="m_company", cascade="all", passive_deletes=True)
    m_legal_rules = relationship("LegalRule", backref="m_company", cascade="all", passive_deletes=True)
    m_job_titles = relationship("JobTitle", backref="m_company", cascade="all", passive_deletes=True)
    m_legal_rule_alerts = relationship("LegalRuleAlert", backref="m_company", cascade="all", passive_deletes=True)
    m_break_time_transformation_time_labors = relationship("BreakTimeTransformationTimeLabor", backref="m_company", cascade="all", passive_deletes=True)
    m_transformation_time_labor_weeklys = relationship("TransformationTimeLaborWeekly", backref="m_company", cascade="all", passive_deletes=True)
    m_transformation_time_labor_monthlys = relationship("TransformationTimeLaborMonthly", backref="m_company", cascade="all", passive_deletes=True)
    m_transformation_time_labor_years = relationship("TransformationTimeLaborYear", backref="m_company", cascade="all", passive_deletes=True)
    m_work_schedule_transformation_time_labors = relationship("WorkScheduleTransformationTimeLabor", backref="m_company", cascade="all", passive_deletes=True)
    m_break_times = relationship("BreakTime", backref="m_company", cascade="all", passive_deletes=True)
    m_holidays = relationship("Holiday", backref="m_company", cascade="all", passive_deletes=True)
    m_work_schedules = relationship("WorkSchedule", backref="m_company", cascade="all", passive_deletes=True)
    m_closings = relationship("Closing", backref="m_company", cascade="all", passive_deletes=True)
    m_closing_dates = relationship("ClosingDate", backref="m_company", cascade="all", passive_deletes=True)
    m_paid_holiday_payments = relationship("PaidHolidayPayment", backref="m_company", cascade="all", passive_deletes=True)
    m_paid_holiday_references = relationship("PaidHolidayReference", backref="m_company", cascade="all", passive_deletes=True)
    m_paid_holiday_managements = relationship("PaidHolidayManagement", backref="m_company", cascade="all", passive_deletes=True)
    m_application_classifications = relationship("ApplicationClassification", backref="m_company", cascade="all", passive_deletes=True)
    m_application_forms = relationship("ApplicationForm", backref="m_company", cascade="all", passive_deletes=True)
    m_application_form_routes = relationship("ApplicationFormRoute", backref="m_company", cascade="all", passive_deletes=True)
    m_individual_routes = relationship("IndividualRoute", backref="m_company", cascade="all", passive_deletes=True)
    m_common_routes = relationship("CommonRoute", backref="m_company", cascade="all", passive_deletes=True)
    m_individual_activitys = relationship("IndividualActivity", backref="m_company", cascade="all", passive_deletes=True)
    m_common_activitys = relationship("CommonActivity", backref="m_company", cascade="all", passive_deletes=True)
    m_insurance_enrollments = relationship("InsuranceEnrollment", backref="m_company", cascade="all", passive_deletes=True)
    m_rates = relationship("Rate", backref="m_company", cascade="all", passive_deletes=True)
    m_company_accounts = relationship("CompanyAccount", backref="m_company", cascade="all", passive_deletes=True)
    m_financial_statement_subjectss = relationship("FinancialStatementSubjects", backref="m_company", cascade="all", passive_deletes=True)
    m_accounts = relationship("Account", backref="m_company", cascade="all", passive_deletes=True)
    m_sub_accounts = relationship("SubAccount", backref="m_company", cascade="all", passive_deletes=True)
    m_salary_items = relationship("SalaryItem", backref="m_company", cascade="all", passive_deletes=True)
    m_salary_target_item_renames = relationship("SalaryTargetItemRename", backref="m_company", cascade="all", passive_deletes=True)
    m_layouts = relationship("Layout", backref="m_company", cascade="all", passive_deletes=True)
    m_third_party_payroll_app_layouts = relationship("ThirdPartyPayrollAppLayout", backref="m_company", cascade="all", passive_deletes=True)
    m_salary_closings = relationship("SalaryClosing", backref="m_company", cascade="all", passive_deletes=True)
    m_salary_closing_dates = relationship("SalaryClosingDate", backref="m_company", cascade="all", passive_deletes=True)
    m_shift_schedules = relationship("ShiftSchedule", backref="m_company", cascade="all", passive_deletes=True)
    m_company_navigation_details = relationship("CompanyNavigationDetail", backref="m_company", cascade="all", passive_deletes=True)
    m_company_work_types = relationship("CompanyWorkType", backref="m_company", cascade="all", passive_deletes=True)
    m_company_work_phase_large_classifications = relationship("CompanyWorkPhaseLargeClassification", backref="m_company", cascade="all", passive_deletes=True)
    m_company_work_phase_middle_classifications = relationship("CompanyWorkPhaseMiddleClassification", backref="m_company", cascade="all", passive_deletes=True)
    m_company_work_phase_small_classifications = relationship("CompanyWorkPhaseSmallClassification", backref="m_company", cascade="all", passive_deletes=True)
    m_order_receiveds = relationship("OrderReceived", backref="m_company", cascade="all", passive_deletes=True)
    m_projects = relationship("Project", backref="m_company", cascade="all", passive_deletes=True)
    m_tasks = relationship("Task", backref="m_company", cascade="all", passive_deletes=True)

    # 会社単位[トラン系] 5 tables
    t_payments = relationship("Payment", backref="m_company", cascade="all", passive_deletes=True)
    t_journals = relationship("Journal", backref="m_company", cascade="all", passive_deletes=True)
    t_closing_year_results = relationship("ClosingYearResult", backref="m_company", cascade="all", passive_deletes=True)
    t_closing_date_results = relationship("ClosingDateResult", backref="m_company", cascade="all", passive_deletes=True)

    # 従業員単位[マスタ系] 27 tables
    m_employees = relationship("Employee", backref="m_company", cascade="all", passive_deletes=True)
    m_unions = relationship("Union", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_job_titles = relationship("EmployeeJobTitle", backref="m_company", cascade="all", passive_deletes=True)
    m_paid_annual_account_employees = relationship("PaidAnnualAccountEmployee", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_favolite_screens = relationship("EmployeeFavoliteScreen", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_applications = relationship("EmployeeApplication", backref="m_company", cascade="all", passive_deletes=True)
    m_password = relationship("Password", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_educational_backgrounds = relationship("EmployeeEducationalBackground", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_skills = relationship("EmployeeSkill", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_work_historys = relationship("EmployeeWorkHistory", backref="m_company", cascade="all", passive_deletes=True)
    m_dependents = relationship("Dependent", backref="m_company", cascade="all", passive_deletes=True)
    m_worker_lists = relationship("WorkerList", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_closings = relationship("EmployeeClosing", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_offices = relationship("EmployeeOffice", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_businesss = relationship("EmployeeBusiness", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_groups = relationship("EmployeeGroup", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_teams = relationship("EmployeeTeam", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_group_roles = relationship("EmployeeGroupRole", backref="m_company", cascade="all", passive_deletes=True)
    m_working_schedule_employees = relationship("WorkingScheduleEmployee", backref="m_company", cascade="all", passive_deletes=True)
    m_dashboard_employees = relationship("DashboardEmployee", backref="m_company", cascade="all", passive_deletes=True)
    m_bosss = relationship("Boss", backref="m_company", cascade="all", passive_deletes=True)
    m_deputy_approvels = relationship("DeputyApprovel", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_accounts_payables = relationship("EmployeeAccountsPayable", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_commutes = relationship("EmployeeCommute", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_taxs = relationship("EmployeeTax", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_transfers = relationship("EmployeeTransfer", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_payments = relationship("EmployeePayment", backref="m_company", cascade="all", passive_deletes=True)
    m_application_collaborators = relationship("ApplicationCollaborator", backref="m_company", cascade="all", passive_deletes=True)
    m_employee_navigation_details = relationship("EmployeeNavigationDetail", backref="m_company", cascade="all", passive_deletes=True)

    # 従業員単位[トラン系] 40 tables
    t_employee_desired_shift_schedules = relationship("EmployeeDesiredShiftSchedule", backref="m_company", cascade="all", passive_deletes=True)
    t_employee_confirm_shift_schedules = relationship("EmployeeConfirmShiftSchedule", backref="m_company", cascade="all", passive_deletes=True)
    t_change_passwords = relationship("ChangePassword", backref="m_company", cascade="all", passive_deletes=True)
    t_working_days = relationship("WorkingDay", backref="m_company", cascade="all", passive_deletes=True)
    t_working_day_summarys = relationship("WorkingDaySummary", backref="m_company", cascade="all", passive_deletes=True)
    t_working_months = relationship("WorkingMonth", backref="m_company", cascade="all", passive_deletes=True)
    t_time_cards = relationship("TimeCard", backref="m_company", cascade="all", passive_deletes=True)
    t_break_time_records = relationship("BreakTimeRecord", backref="m_company", cascade="all", passive_deletes=True)
    t_safety_confirmations = relationship("SafetyConfirmation", backref="m_company", cascade="all", passive_deletes=True)
    t_alerts = relationship("Alert", backref="m_company", cascade="all", passive_deletes=True)
    t_employee_notices = relationship("EmployeeNotice", backref="m_company", cascade="all", passive_deletes=True)
    t_user_reports = relationship("UserReport", backref="m_company", cascade="all", passive_deletes=True)
    t_application_objects = relationship("ApplicationObject", backref="m_company", cascade="all", passive_deletes=True)
    t_activity_objects = relationship("ActivityObject", backref="m_company", cascade="all", passive_deletes=True)
    t_appendeds = relationship("Appended", backref="m_company", cascade="all", passive_deletes=True)
    t_route_historys = relationship("RouteHistory", backref="m_company", cascade="all", passive_deletes=True)
    t_ground_confirm_employees = relationship("GroundConfirmEmployee", backref="m_company", cascade="all", passive_deletes=True)
    t_overtime_applications = relationship("OvertimeApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_late_night_overwork_applications = relationship("LateNightOverworkApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_late_time_applications = relationship("LateTimeApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_early_departure_time_applications = relationship("EarlyDepartureTimeApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_imprint_correction_applications = relationship("ImprintCorrectionApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_transfer_holiday_work_applications = relationship("TransferHolidayWorkApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_holiday_work_applications = relationship("HolidayWorkApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_attendance_record_applications = relationship("AttendanceRecordApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_leave_job_applications = relationship("LeaveJobApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_commuting_route_change_applications = relationship("CommutingRouteChangeApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_commuting_route_change_application_details = relationship("CommutingRouteChangeApplicationDetail", backref="m_company", cascade="all", passive_deletes=True)
    t_address_change_applications = relationship("AddressChangeApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_personal_information_change_applications = relationship("PersonalInformationChangeApplication", backref="m_company", cascade="all", passive_deletes=True)
    t_paid_leave_employees = relationship("PaidLeaveEmployee", backref="m_company", cascade="all", passive_deletes=True)
    t_paid_leave_employee_details = relationship("PaidLeaveEmployeeDetail", backref="m_company", cascade="all", passive_deletes=True)
    t_company_partners = relationship("CompanyPartner", backref="m_company", cascade="all", passive_deletes=True)
    t_employee_vaccinations = relationship("EmployeeVaccinationd", backref="m_company", cascade="all", passive_deletes=True)
    t_salary_closing_year_results = relationship("SalaryClosingYearResult", backref="m_company", cascade="all", passive_deletes=True)
    t_salary_closing_date_results = relationship("SalaryClosingDateResult", backref="m_company", cascade="all", passive_deletes=True)
    t_employee_pay_slips = relationship("EmployeePaySlip", backref="m_company", cascade="all", passive_deletes=True)
    t_reserve_send_pay_slips = relationship("ReserveSendPaySlip", backref="m_company", cascade="all", passive_deletes=True)
    t_employee_bonus_pay_slip_headers = relationship("EmployeeBonusPaySlipHeader", backref="m_company", cascade="all", passive_deletes=True)
    t_employee_bonus_pay_slips = relationship("EmployeeBonusPaySlip", backref="m_company", cascade="all", passive_deletes=True)
    t_employee_lunchs = relationship("EmployeeLunch", backref="m_company", cascade="all", passive_deletes=True)
    t_employee_welfare_pension_grades = relationship("EmployeeWelfarePensionGrade", backref="m_company", cascade="all", passive_deletes=True)
    t_paid_payment_managements = relationship("PaidPaymentManagement", backref="m_company", cascade="all", passive_deletes=True)
    t_paid_payment_management_details = relationship("PaidPaymentManagementDetail", backref="m_company", cascade="all", passive_deletes=True)
    t_daily_reports = relationship("DailyReport", backref="m_company", cascade="all", passive_deletes=True)
    t_daily_report_details = relationship("DailyReportDetail", backref="m_company", cascade="all", passive_deletes=True)
    t_request_quotes = relationship("RequestQuote", backref="m_company", cascade="all", passive_deletes=True)

    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company', "company_code"), UniqueConstraint("company_code"), )


class ResarchInformation(Base):
    """
    調査情報マスタ
    """
    __tablename__ = "m_resarch_information"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    capital = Column('capital', Integer, nullable=True, comment='資本金')
    date_of_establishment = Column('date_of_establishment', Date, nullable=True, comment='設立日')
    home_page = Column('home_page', String(255, collation='ja_JP.utf8'), nullable=True, comment='ホームページ')
    number_of_employees = Column('number_of_employees', Integer, nullable=True, comment='従業員数')
    averag_age_of_employees = Column('averag_age_of_employees', DECIMAL(4, 1), nullable=True, comment='従業員の平均年齢')
    gender_ratio_of_employees = Column('gender_ratio_of_employees', DECIMAL(4, 1), nullable=True, comment='従業員の男女比率')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), ForeignKey('m_state.state_code', onupdate='CASCADE', ondelete='CASCADE'), comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=True, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='電話番号')
    listing = Column('listing', EnumType(enum_class=Listing), nullable=True, comment='上場')
    listing_market = Column('listing_market', EnumType(enum_class=ListingMarket), nullable=True, comment='上場市場')
    shareholder_ratio_of_the_founding_family = Column('shareholder_ratio_of_the_founding_family', DECIMAL(4, 1), nullable=True, comment='創業者一族の株主比率')
    scheduled_to_be_listed = Column('scheduled_to_be_listed', EnumType(enum_class=ScheduledToBeListed), nullable=True, comment='上場予定')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_resarch_information', "company_code"), UniqueConstraint("company_code"), )


class WokingItem(Base):
    """
    会社別勤怠項目マスタ
    """
    __tablename__ = "m_working_item"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    working_item_id = Column('working_item_id', String(10), nullable=False, comment='勤怠項目番号')
    working_item_name = Column('working_item_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='勤怠項目名')
    working_item_unit = Column('working_item_unit', String(30, collation='ja_JP.utf8'), nullable=True, comment='単位')
    formula = Column('formula', String(255, collation='ja_JP.utf8'), nullable=True, comment='計算式')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_working_item', "company_code", "working_item_id"), UniqueConstraint("company_code", "working_item_id"), )


class ResarchInformationSupplierDetail(Base):
    """
    調査情報仕入先詳細マスタ
    """
    __tablename__ = "m_resarch_information_supplier_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    supplier_name = Column('supplier_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='弁当業者名')
    listing = Column('listing', EnumType(enum_class=Listing), nullable=True, comment='上場')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_resarch_information_supplier_detail', "company_code", "target_year", "supplier_name"), Index('ix_m_resarch_information_supplier_detail_1', "company_code"), UniqueConstraint("company_code", "target_year", "supplier_name"), )


class ResarchInformationCustomerDetail(Base):
    """
    調査情報取引先詳細マスタ
    """
    __tablename__ = "m_resarch_information_customer_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    customer_name = Column('customer_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='取引先名')
    listing = Column('listing', EnumType(enum_class=Listing), nullable=True, comment='上場')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_resarch_information_customer_detail', "company_code", "target_year", "customer_name"), Index('ix_m_resarch_information_customer_detail_1', "company_code"), UniqueConstraint("company_code", "target_year", "customer_name"), )


class ResarchInformationMainBankDetail(Base):
    """
    調査情報メインバンク詳細マスタ
    """
    __tablename__ = "m_resarch_information_main_bank_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    bank_code = Column('bank_code', String(4, collation='ja_JP.utf8'), ForeignKey('m_bank.bank_code', onupdate='CASCADE', ondelete='CASCADE'), comment='銀行コード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_resarch_information_main_bank_detail', "company_code", "target_year", "bank_code"), Index('ix_m_resarch_information_main_bank_detail_1', "company_code"), UniqueConstraint("company_code", "target_year", "bank_code"), )


class ResarchInformationRecruitmentDetail(Base):
    """
    調査情報採用詳細マスタ
    """
    __tablename__ = "m_resarch_information_recruitment_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    number_of_hires = Column('number_of_hires', Integer, nullable=False, comment='採用人数')
    university_graduate_starting_salary = Column('university_graduate_starting_salary', Integer, nullable=False, comment='大卒初任給')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_resarch_information_recruitment_detail', "company_code", "target_year"), Index('ix_m_resarch_information_recruitment_detail_1', "company_code"), UniqueConstraint("company_code", "target_year"), )


class ResarchInformationPerformanceDetail(Base):
    """
    調査情報業績詳細マスタ
    """
    __tablename__ = "m_resarch_information_performance_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    amount_of_sales = Column('amount_of_sales', Integer, nullable=True, comment='売上高')
    operating_income = Column('operating_income', Integer, nullable=True, comment='営業利益')
    ordinary_income = Column('ordinary_income', Integer, nullable=True, comment='経常利益')
    net_income = Column('net_income', Integer, nullable=True, comment='純利益')
    dividend = Column('dividend', Integer, nullable=True, comment='配当')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_resarch_information_performance_detail', "company_code", "target_year"), Index('ix_m_resarch_information_performance_detail_1', "company_code"), UniqueConstraint("company_code", "target_year"), )


class ServiceDestination(Base):
    """
    サービス提供先マスタ
    """
    __tablename__ = "m_service_destination"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    company_name = Column('company_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='会社名')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    password = Column('password', String(255, collation='ja_JP.utf8'), nullable=False, comment='パスワード')
    emergency_stop_flag = Column('emergency_stop_flag', EnumType(enum_class=EmergencyStopFlag), nullable=False, comment='緊急停止フラグ')
    contents = Column('contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_service_destination', "company_code", "term_from"), Index('ix_m_service_destination_1', "company_code"), UniqueConstraint("company_code", "term_from"), )



class CompanyWorkerManagement(Base):
    """
    社労士管理マスタ
    """
    __tablename__ = "m_company_worker_management"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    social_insurance_labor_consultant = Column('social_insurance_labor_consultant', String(8, collation='ja_JP.utf8'), nullable=False, comment='社会保険労務士番号')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company_worker_management', "company_code", "social_insurance_labor_consultant"), Index('ix_m_company_worker_management_1', "company_code"), Index('ix_m_company_worker_management_2', "social_insurance_labor_consultant"), UniqueConstraint("company_code", "social_insurance_labor_consultant"),)


class Office(Base):
    """
    事業所マスタ
    """
    __tablename__ = "m_office"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    reference_number = Column('reference_number', String(4, collation='ja_JP.utf8'), nullable=True, comment='整理番号')
    office_reference_number = Column('office_reference_number', String(6, collation='ja_JP.utf8'), nullable=True, comment='事業所整理番号')
    office_name = Column('office_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='事業所名')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=False, comment='電話番号')
    fax = Column('fax', String(20, collation='ja_JP.utf8'), nullable=True, comment='ファックス番号')
    industry_code_big = Column('industry_code_big', String(1, collation='ja_JP.utf8'), nullable=False, comment='業種(大分類)')
    industry_code_during = Column('industry_code_during', String(2, collation='ja_JP.utf8'), nullable=False, comment='業種(中分類)')
    industry_code_small = Column('industry_code_small', String(4, collation='ja_JP.utf8'), nullable=False, comment='業種(小分類)')
    industry_code = Column('industry_code', String(5, collation='ja_JP.utf8'), nullable=True, comment='産業コード')
    special_measures = Column('special_measures', EnumType(enum_class=SpecialMeasures), nullable=False, comment='特例措置対象事業場')
    regulatory_grace_exclusion = Column('regulatory_grace_exclusion', Boolean, nullable=False, comment='上限規制の適用を猶予・除外')
    place_code = Column('place_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='場所コード')
    shift_code = Column('shift_code', String(3, collation='ja_JP.utf8'), nullable=True, comment='シフトコード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=False, comment='所定労働時間')
    working_interval = Column('working_interval', Integer, nullable=True, comment='インターバル時間')
    limit_exemption_working_interval = Column('limit_exemption_working_interval', Integer, nullable=True, comment='適用除外を認める回数')
    handling_method_working_interval = Column('handling_method_working_interval', EnumType(enum_class=HandlingMethodWorkingInterval), nullable=True, comment='勤務間インターバル制度の取扱方法')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_office', "company_code", "office_code"), Index('ix_m_office_1', "company_code"), Index('ix_m_office_2', "office_code"), UniqueConstraint("company_code", "office_code"), )


class Place(Base):
    """
    場所マスタ
    """
    __tablename__ = "m_place"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    place_code = Column('place_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='場所コード')
    place_name = Column('place_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='場所名')
    lat = Column('lat', DECIMAL(9, 6), nullable=True, comment='緯度')
    lng = Column('lng', DECIMAL(9, 6), nullable=True, comment='経度')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=False, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    stamping_radius_flg = Column('stamping_radius_flg', Boolean, nullable=True, comment='勤務先近辺のみ打刻を許可します')
    stamping_radius = Column('stamping_radius', Integer, nullable=True, comment='半径')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_place', "company_code", "place_code"), Index('ix_m_place_1', "company_code"), Index('ix_m_place_2', "place_code"), UniqueConstraint("company_code", "place_code"), UniqueConstraint("company_code", "place_name"), )


class Business(Base):
    """
    職種マスタ
    """
    __tablename__ = "m_business"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    business_name = Column('business_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='職種名')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_business', "company_code", "business_type"), Index('ix_m_business_1', "company_code"), Index('ix_m_business_2', "business_type"), UniqueConstraint("company_code", "business_type"), UniqueConstraint("company_code", "business_name"), )


class Team(Base):
    """
    チームマスタ
    """
    __tablename__ = "m_team"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    team_code = Column('team_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='チームコード')
    team_name = Column('team_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='チーム名')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_team', "company_code", "team_code"), Index('ix_m_team_1', "company_code"), Index('ix_m_team_2', "team_code"), UniqueConstraint("company_code", "team_code"), )


class Group(Base):
    """
    部署マスタ
    """
    __tablename__ = "m_group"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    group_code = Column('group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='部署コード')
    group_name = Column('group_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='部署名')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    upper_group_code = Column('upper_group_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='上位部署コード')
    range = Column('range', EnumType(enum_class=Range), nullable=False, comment='利用権限範囲')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_group', "company_code", "group_code"), Index('ix_m_group_1', "company_code"), Index('ix_m_group_2', "group_code"), UniqueConstraint("company_code", "group_code"), )


class GroupApplication(Base):
    """
    部署申請マスタ
    """
    __tablename__ = "m_group_application"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    group_code = Column('group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='部署コード')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    group_application_control = Column('group_application_control', EnumType(enum_class=GroupApplicationControl), nullable=False, comment='部署申請')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_group_application', "company_code", "group_code", "application_form_code"), Index('ix_m_group_application_1', "company_code"), Index('ix_m_group_application_2', "group_code"), Index('ix_m_group_application_3', "application_form_code"), UniqueConstraint("company_code", "group_code", "application_form_code"), ForeignKeyConstraint(['company_code', 'group_code'], ['m_group.company_code', 'm_group.group_code']),)


class OfficeApplication(Base):
    """
    事業所申請マスタ
    """
    __tablename__ = "m_office_application"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    office_application_control = Column('office_application_control', EnumType(enum_class=OfficeApplicationControl), nullable=False, comment='事業所申請')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_office_application', "company_code", "office_code", "application_form_code"), Index('ix_m_office_application_1', "company_code"), Index('ix_m_office_application_2', "office_code"), Index('ix_m_office_application_3', "application_form_code"), UniqueConstraint("company_code", "office_code", "application_form_code"), ForeignKeyConstraint(['company_code', 'office_code'], ['m_office.company_code', 'm_office.office_code']),)


class LunchSupplier(Base):
    """
    弁当仕入先マスタ
    """
    __tablename__ = "m_lunch_supplier"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    supplier_code = Column('supplier_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='弁当業者コード')
    supplier_name = Column('supplier_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='弁当業者名')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=False, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    home_page = Column('home_page', String(255, collation='ja_JP.utf8'), nullable=True, comment='ホームページ')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=False, comment='電話番号')
    fax = Column('fax', String(20, collation='ja_JP.utf8'), nullable=True, comment='ファックス番号')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='メールアドレス')
    date_of_collection = Column('date_of_collection', Integer, nullable=False, comment='集金締日')
    collection_day = Column('collection_day', Integer, nullable=False, comment='集金日')
    entry_start_time = Column('entry_start_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='受付開始時間')
    entry_end_time = Column('entry_end_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='受付終了時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_lunch_supplier', "company_code", "supplier_code"), Index('ix_m_lunch_supplier_1', "company_code"), Index('ix_m_lunch_supplier_2', "supplier_code"), UniqueConstraint("company_code", "supplier_code"), UniqueConstraint("company_code", "supplier_name"), )


class Lunch(Base):
    """
    弁当マスタ
    """
    __tablename__ = "m_lunch"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    supplier_code = Column('supplier_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='弁当業者コード')
    lunch_code = Column('lunch_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='弁当コード')
    lunch_name = Column('lunch_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='弁当名')
    unit_price = Column('unit_price', Integer, nullable=False, comment='単価')
    picture_uri = Column('picture_uri', String(255, collation='ja_JP.utf8'), nullable=True, comment='写真')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_lunch', "company_code", "supplier_code", "lunch_code"), Index('ix_m_lunch_1', "company_code"), Index('ix_m_lunch_2', "supplier_code"), Index('ix_m_lunch_3', "lunch_code"), UniqueConstraint("company_code", "supplier_code", "lunch_code"), ForeignKeyConstraint(['company_code', 'supplier_code'], ['m_lunch_supplier.company_code', 'm_lunch_supplier.supplier_code']),)


class LunchOrder(Base):
    """
    弁当注文受付マスタ
    """
    __tablename__ = "m_lunch_order"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    supplier_code = Column('supplier_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='弁当業者コード')
    acceptable = Column('acceptable', EnumType(enum_class=Acceptable), nullable=False, comment='受付可能')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_lunch_order', "company_code", "supplier_code"), Index('ix_m_lunch_order_1', "company_code"), Index('ix_m_lunch_order_2', "supplier_code"), UniqueConstraint("company_code", "supplier_code"), )


class EmployeeClassification(Base):
    """
    従業員区分マスタ
    """
    __tablename__ = "m_employee_classification"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_classification_code = Column('employee_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員区分')
    employee_classification_name = Column('employee_classification_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='従業員区分名')
    employee_classification_type = Column('employee_classification_type', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_classification', "company_code", "employee_classification_code"), Index('ix_m_employee_classification_1', "company_code"), Index('ix_m_employee_classification_2', "employee_classification_code"), UniqueConstraint("company_code", "employee_classification_code"), UniqueConstraint("company_code", "employee_classification_name"),)


class AlertManagement(Base):
    """
    申請書別アラート管理マスタ
    """
    __tablename__ = "m_alert_management"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    alert_management_control = Column('alert_management_control', EnumType(enum_class=AlertManagementControl), nullable=False, comment='アラート番号管理区分')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_alert_management', "company_code", "application_form_code"), Index('ix_m_alert_management_1', "company_code"), Index('ix_m_alert_management_2', "application_form_code"), UniqueConstraint("company_code", "application_form_code"),)


class RecruitmentCategory(Base):
    """
    採用区分マスタ
    """
    __tablename__ = "m_recruitment_category"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    recruitment_category_code = Column('recruitment_category_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='採用区分')
    recruitment_category_name = Column('recruitment_category_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='採用区分名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_recruitment_category', "company_code", "recruitment_category_code"), Index('ix_m_recruitment_category_1', "company_code"), UniqueConstraint("company_code", "recruitment_category_code"), UniqueConstraint("company_code", "recruitment_category_name"),)


class CompanyApplication(Base):
    """
    会社申請マスタ
    """
    __tablename__ = "m_company_application"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    company_application_control = Column('company_application_control', EnumType(enum_class=CompanyApplicationControl), nullable=False, comment='会社申請')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company_application', "company_code", "application_form_code"), Index('ix_m_company_application_1', "company_code"), Index('ix_m_company_application_2', "application_form_code"), UniqueConstraint("company_code", "application_form_code"), )


class LegalRuleFormat(Base):
    """
    36協定書マスタ
    """
    __tablename__ = "m_legal_rule_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    starting_date = Column('starting_date', Date, nullable=False, comment='起算日')
    document_style = Column('document_style', EnumType(enum_class=DocumentStyle), nullable=False, comment='様式タイプ')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    agreement_date = Column('agreement_date', Date, nullable=False, comment='協定の成立年月日')
    agreement_parties_job_title_code = Column('agreement_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の職名コード')
    agreement_parties_employee_code = Column('agreement_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の従業員番号')
    election_method = Column('election_method', EnumType(enum_class=ElectionMethod), nullable=False, comment='選出方法')
    procedure_of_exceed_the_time_limit = Column('procedure_of_exceed_the_time_limit', String(100, collation='ja_JP.utf8'), nullable=True, comment='限度時間を超えて労働させる場合における手続き')
    procedure_health_code_1 = Column('procedure_health_code_1', EnumType(enum_class=ProcedureHealth), nullable=True, comment='限度時間を超えて労働させる労働者に対する健康及び福祉を確保するための措置(1)')
    procedure_health_code_2 = Column('procedure_health_code_2', EnumType(enum_class=ProcedureHealth), nullable=True, comment='限度時間を超えて労働させる労働者に対する健康及び福祉を確保するための措置(2)')
    procedure_health_code_3 = Column('procedure_health_code_3', EnumType(enum_class=ProcedureHealth), nullable=True, comment='限度時間を超えて労働させる労働者に対する健康及び福祉を確保するための措置(3)')
    specific_content = Column('specific_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='具体的内容')
    filing_date = Column('filing_date', Date, nullable=False, comment='提出日')
    management_parties_job_title_code = Column('management_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の職名コード')
    management_parties_employee_code = Column('management_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の従業員番号')
    labor_standards_inspection_office = Column('labor_standards_inspection_office', String(50, collation='ja_JP.utf8'), nullable=False, comment='労働基準監督署')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_legal_rule_format', "company_code", "office_code", "starting_date", "document_style"), Index('ix_m_legal_rule_format_1', "company_code"), Index('ix_m_legal_rule_format_2', "office_code"), Index('ix_m_legal_rule_format_3', "document_style"), UniqueConstraint("company_code", "office_code", "starting_date", "document_style"), )


class LegalRule(Base):
    """
    36協定マスタ
    """
    __tablename__ = "m_legal_rule"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    starting_date = Column('starting_date', Date, nullable=False, comment='起算日')
    document_style = Column('document_style', EnumType(enum_class=DocumentStyle), nullable=False, comment='様式タイプ')
    reasons_type = Column('reasons_type', EnumType(enum_class=ReasonsType), nullable=False, comment='理由タイプ')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    employee_count = Column('employee_count', Integer, nullable=True, comment='労働者数')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=True, comment='所定労働時間')
    reasons_over_work_contents = Column('reasons_over_work_contents', String(500, collation='ja_JP.utf8'), nullable=False, comment='時間外労働をさせる必要のある具体的事由')
    limit_legal_one_day_minutes = Column('limit_legal_one_day_minutes', Integer, nullable=True, comment='一日の法定労働時間数を超える時間数(分)')
    limit_job_one_day_minutes = Column('limit_job_one_day_minutes', Integer, nullable=True, comment='一日の所定労働時間を超える時間数(分)')
    special_provisions_rate_month = Column('limit_special_provisions_rate_month', DECIMAL(5, 3), nullable=True, comment='特別条項の割増賃金率[一箇月]')
    limit_legal_one_month_minutes = Column('limit_legal_one_month_minutes', Integer, nullable=True, comment='法定外労働時間[一箇月]の警告時間　※法定休日労働時間を含まない')
    limit_legal_one_month_minutes_all = Column('limit_legal_one_month_minutes_all', Integer, nullable=True, comment='法定外労働時間[一箇月]の警告時間　※法定休日労働時間を含む')
    limit_job_one_month_minutes = Column('limit_job_one_month_minutes', Integer, nullable=True, comment='一カ月の最大所定労働時間(分)')
    number_of_legal_holidays_allowed_to_work = Column('number_of_legal_holidays_allowed_to_work', Integer, nullable=True, comment='労働させることができる法定休日の日数[一箇月]')
    limit_legal_one_year_minutes = Column('limit_legal_one_year_minutes', Integer, nullable=True, comment='法定労働時間[一年間]の警告時間　※法定休日労働時間を含む')
    limit_job_one_year_minutes = Column('limit_job_one_year_minutes', Integer, nullable=True, comment='所定外労働時間[一年間]の警告時間')
    special_provisions_year_count = Column('special_provisions_year_count', Integer, nullable=True, comment='特別条項の回数[一年間]')
    special_provisions_rate_year = Column('limit_special_provisions_rate_year', DECIMAL(5, 3), nullable=True, comment='特別条項の回数[一年間]')
    legal_holiday_job_start = Column('legal_holiday_job_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='法定休日始業時間')
    legal_holiday_job_end = Column('legal_holiday_job_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='法定休日終業時間')
    job_holiday_comment = Column('job_holiday_comment', String(100, collation='ja_JP.utf8'), nullable=True, comment='所定休日(任意)')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_legal_rule', "company_code", "office_code", "starting_date", "document_style", "reasons_type", "business_type"), Index('ix_m_legal_rule_1', "company_code"), Index('ix_m_legal_rule_2', "office_code"), Index('ix_m_legal_rule_3', "document_style"), Index('ix_m_legal_rule_4', "reasons_type"), Index('ix_m_legal_rule_5', "business_type"), UniqueConstraint("company_code", "office_code", "starting_date", "document_style", "reasons_type", "business_type"), )


class JobTitle(Base):
    """
    職名マスタ
    """
    __tablename__ = "m_job_title"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    job_title_code = Column('job_title_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='役職コード')
    job_title_name = Column('job_title_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='役職')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_job_title', "company_code", "job_title_code"), Index('ix_m_job_title_1', "company_code"), Index('ix_m_job_title_2', "job_title_code"), UniqueConstraint("company_code", "job_title_code"), )


class LegalRuleAlert(Base):
    """
    36協定警告マスタ
    """
    __tablename__ = "m_legal_rule_alert"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    limit_legal_one_month_minutes = Column('limit_legal_one_month_minutes', Integer, nullable=True, comment='法定外労働時間[一箇月]の警告時間　※法定休日労働時間を含まない')
    limit_legal_one_month_minutes_rate = Column('limit_legal_one_month_minutes_rate', Float, nullable=True, comment='法定外労働時間[一箇月]の警告率　※法定休日労働時間を含まない')
    limit_legal_one_month_minutes_all = Column('limit_legal_one_month_minutes_all', Integer, nullable=True, comment='法定外労働時間[一箇月]の警告時間　※法定休日労働時間を含む')
    limit_legal_one_month_minutes_all_rate = Column('limit_legal_one_month_minutes_all_rate', Float, nullable=True, comment='法定外労働時間[一箇月]の警告率　※法定休日労働時間を含まない')
    limit_month_over_industrial_safety_health_act = Column('limit_month_over_industrial_safety_health_act', Integer, nullable=True, comment='労働安全衛生法上の最大労働時間[一箇月]の警告時間')
    limit_month_over_industrial_safety_health_act_rate = Column('limit_month_over_industrial_safety_health_act_rate', Float, nullable=True, comment='労働安全衛生法上の最大労働時間[一箇月]の警告率')
    limit_legal_one_year_minutes = Column('limit_legal_one_year_minutes', Integer, nullable=True, comment='法定労働時間[一年間]の警告時間　※法定休日労働時間を含む')
    limit_legal_one_year_minutes_rate = Column('limit_legal_one_year_minutes_rate', Float, nullable=True, comment='法定労働時間[一年間]の警告率')
    limit_job_one_year_minutes = Column('limit_job_one_year_minutes', Integer, nullable=True, comment='所定外労働時間[一年間]の警告時間')
    limit_job_one_year_minutes_rate = Column('limit_job_one_year_minutes_rate', Float, nullable=True, comment='所定外労働時間[一年間]の警告率')
    number_of_legal_holidays_allowed_to_work = Column('number_of_legal_holidays_allowed_to_work', Integer, nullable=True, comment='労働させることができる法定休日の日数[一箇月]')
    number_of_legal_holidays_allowed_to_work_rate = Column('number_of_legal_holidays_allowed_to_work_rate', Float, nullable=True, comment='法定休日日数[一箇月]の警告率')
    special_provisions_year_count = Column('special_provisions_year_count', Integer, nullable=True, comment='特別条項の回数[一年間]')
    special_provisions_year_count_rate = Column('special_provisions_year_count_rate', Float, nullable=True, comment='特別条項の回数[一年間]の警告率')
    limit_special_provisions_legal_one_month_minutes_all = Column('limit_special_provisions_legal_one_month_minutes_all', Integer, nullable=True, comment='特別条項の法定外労働時間[一箇月]の警告時間　※法定休日労働時間を含む')
    limit_special_provisions_legal_one_month_minutes_all_rate = Column('limit_special_provisions_legal_one_month_minutes_all_rate', Float, nullable=True, comment='特別条項の法定外労働時間[一箇月]の警告時間の警告率　※法定休日労働時間を含む')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_legal_rule_alert', "company_code", "office_code", "business_type"), Index('ix_m_legal_rule_alert_1', "company_code"), Index('ix_m_legal_rule_alert_2', "office_code"), Index('ix_m_legal_rule_alert_3', "business_type"), UniqueConstraint("company_code", "office_code", "business_type"), )


class BreakTimeTransformationTimeLabor(Base):
    """
    休憩マスタ(変形時間労働制)
    """
    __tablename__ = "m_break_time_transformation_time_labor"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    break_time = Column('break_time', String(11, collation='ja_JP.utf8'), nullable=True, comment='休憩時間の範囲')
    range_break_minutes = Column('range_break_minutes', Integer, nullable=True, comment='拘束時間[以上]')
    break_minutes = Column('break_minutes', Integer, nullable=True, comment='休憩時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_break_time_transformation_time_labor', "company_code", "office_code", "business_type", "target_date", unique=False), Index('ix_m_break_time_transformation_time_labor_1', "company_code"), Index('ix_m_break_time_transformation_time_labor_2', "company_code", "office_code", "business_type"),)


class TransformationTimeLaborWeekly(Base):
    """
    一週間単位の変形時間労働制マスタ
    """
    __tablename__ = "m_transformation_time_labor_weekly"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    starting_date = Column('starting_date', Date, nullable=False, comment='起算日')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    agreement_date = Column('agreement_date', Date, nullable=False, comment='協定の成立年月日')
    agreement_parties_job_title_code = Column('agreement_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の職名コード')
    agreement_parties_employee_code = Column('agreement_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の従業員番号')
    election_method = Column('election_method', EnumType(enum_class=ElectionMethod), nullable=False, comment='選出方法')
    limit_legal_one_weeks_minutes = Column('limit_legal_one_weeks_minutes', Integer, nullable=False, comment='一週間の最大労働時間(分)')
    filing_date = Column('filing_date', Date, nullable=False, comment='提出日')
    management_parties_job_title_code = Column('management_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の職名コード')
    management_parties_employee_code = Column('management_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の従業員番号')
    labor_standards_inspection_office = Column('labor_standards_inspection_office', String(50, collation='ja_JP.utf8'), nullable=False, comment='労働基準監督署')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_transformation_time_labor_weekly', "company_code", "office_code", "starting_date", "business_type"), Index('ix_m_transformation_time_labor_weekly_1', "company_code"), UniqueConstraint("company_code", "office_code", "starting_date", "business_type"), )


class TransformationTimeLaborMonthly(Base):
    """
    一箇月単位の変形時間労働制マスタ
    """
    __tablename__ = "m_transformation_time_labor_monthly"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    starting_date = Column('starting_date', Date, nullable=False, comment='起算日')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    agreement_date = Column('agreement_date', Date, nullable=False, comment='協定の成立年月日')
    agreement_parties_job_title_code = Column('agreement_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の職名コード')
    agreement_parties_employee_code = Column('agreement_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の従業員番号')
    election_method = Column('election_method', EnumType(enum_class=ElectionMethod), nullable=False, comment='選出方法')
    filing_date = Column('filing_date', Date, nullable=False, comment='提出日')
    management_parties_job_title_code = Column('management_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の職名コード')
    management_parties_employee_code = Column('management_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の従業員番号')
    labor_standards_inspection_office = Column('labor_standards_inspection_office', String(50, collation='ja_JP.utf8'), nullable=False, comment='労働基準監督署')
    longest_working_day_working_time = Column('longest_working_day_working_time', Integer, nullable=False, comment='労働時間が最も長い日の労働時間数(分)')
    longest_working_day_working_time_under_18 = Column('longest_working_day_working_time_under_18', Integer, nullable=False, comment='労働時間が最も長い日の労働時間数(18歳未満)(分)')
    longest_working_week_working_time = Column('longest_working_week_working_time', Integer, nullable=False, comment='労働時間が最も長い週の労働時間数(分)')
    longest_working_week_working_time_under_18 = Column('longest_working_week_working_time_under_18', Integer, nullable=False, comment='労働時間が最も長い週の労働時間数(18歳未満)(分)')
    is_job_before_start_time = Column('is_job_before_start_time', EnumType(enum_class=JobBeforeStartTime), nullable=False, comment='始業時間前の労働時間を含む')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_transformation_time_labor_monthly', "company_code", "office_code", "starting_date", "business_type"), Index('ix_m_transformation_time_labor_monthly_1', "company_code"), UniqueConstraint("company_code", "office_code", "starting_date", "business_type"), )


class TransformationTimeLaborYear(Base):
    """
    一年単位の変形時間労働制マスタ
    """
    __tablename__ = "m_transformation_time_labor_year"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    starting_date = Column('starting_date', Date, nullable=False, comment='起算日')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    agreement_date = Column('agreement_date', Date, nullable=False, comment='協定の成立年月日')
    agreement_parties_job_title_code = Column('agreement_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の職名コード')
    agreement_parties_employee_code = Column('agreement_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の従業員番号')
    election_method = Column('election_method', EnumType(enum_class=ElectionMethod), nullable=False, comment='選出方法')
    filing_date = Column('filing_date', Date, nullable=False, comment='提出日')
    management_parties_job_title_code = Column('management_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の職名コード')
    management_parties_employee_code = Column('management_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の従業員番号')
    labor_standards_inspection_office = Column('labor_standards_inspection_office', String(50, collation='ja_JP.utf8'), nullable=False, comment='労働基準監督署')
    average_working_time = Column('average_working_time', Integer, nullable=False, comment='一週間の平均労働時間数(分)')
    longest_working_day_working_time = Column('longest_working_day_working_time', Integer, nullable=False, comment='労働時間が最も長い日の労働時間数(分)')
    longest_working_day_working_time_under_18 = Column('longest_working_day_working_time_under_18', Integer, nullable=False, comment='労働時間が最も長い日の労働時間数(18歳未満)(分)')
    longest_working_week_working_time = Column('longest_working_week_working_time', Integer, nullable=False, comment='労働時間が最も長い週の労働時間数(分)')
    longest_working_week_working_time_under_18 = Column('longest_working_week_working_time_under_18', Integer, nullable=False, comment='労働時間が最も長い週の労働時間数(18歳未満)(分)')
    total_working_days = Column('total_working_days', Integer, nullable=False, comment='総労働日数')
    maximum_consecutive_weeks_with_more_than_48_hours_worked = Column('maximum_consecutive_weeks_with_more_than_48_hours_worked', Integer, nullable=False, comment='労働時間が48時間を超える週の最長連続週数')
    weeks_with_more_than_48_hours_worked = Column('weeks_with_more_than_48_hours_worked', Integer, nullable=False, comment='労働時間が48時間を超える週数')
    target_number_of_consecutive_working_days = Column('target_number_of_consecutive_working_days', Integer, nullable=False, comment='対象期間中の最も長い連続労働日数')
    special_number_of_consecutive_working_days = Column('special_number_of_consecutive_working_days', Integer, nullable=False, comment='特定期間中の最も長い連続労働日数')
    old_term_from = Column('old_term_from', Date, nullable=True, comment='旧協定の対象期間[開始]')
    old_term_to = Column('old_term_to', Date, nullable=True, comment='旧協定の対象期間[終了]')
    old_longest_working_day_working_time = Column('old_longest_working_day_working_time', Integer, nullable=True, comment='旧協定の労働時間が最も長い日の労働時間数(分)')
    old_longest_working_week_working_time = Column('old_longest_working_week_working_time', Integer, nullable=True, comment='旧協定の労働時間が最も長い週の労働時間数(分)')
    old_total_working_days = Column('old_total_working_days', Integer, nullable=True, comment='旧協定の対象期間中の総労働日数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_transformation_time_labor_year', "company_code", "office_code", "starting_date", "business_type"), Index('ix_m_transformation_time_labor_year_1', "company_code"), UniqueConstraint("company_code", "office_code", "starting_date", "business_type"), )


class BreakTime(Base):
    """
    休憩マスタ
    """
    __tablename__ = "m_break_time"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    break_time = Column('break_time', String(11, collation='ja_JP.utf8'), nullable=True, comment='休憩時間の範囲')
    range_break_minutes = Column('range_break_minutes', Integer, nullable=True, comment='拘束時間[以上]')
    break_minutes = Column('break_minutes', Integer, nullable=True, comment='休憩時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_break_time', "company_code", "work_schedule_code", unique=False), Index('ix_m_break_time_1', "company_code"), Index('ix_m_break_time_2', "work_schedule_code"),)


class Holiday(Base):
    """
    休日マスタ
    """
    __tablename__ = "m_holiday"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    jan_calender = Column('jan_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='1月のカレンダー')
    feb_calender = Column('feb_calender', String(29, collation='ja_JP.utf8'), nullable=False, comment='2月のカレンダー')
    mar_calender = Column('mar_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='3月のカレンダー')
    apl_calender = Column('apl_calender', String(30, collation='ja_JP.utf8'), nullable=False, comment='4月のカレンダー')
    may_calender = Column('may_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='5月のカレンダー')
    jun_calender = Column('jun_calender', String(30, collation='ja_JP.utf8'), nullable=False, comment='6月のカレンダー')
    jly_calender = Column('jly_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='7月のカレンダー')
    aug_calender = Column('aug_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='8月のカレンダー')
    sep_calender = Column('sep_calender', String(30, collation='ja_JP.utf8'), nullable=False, comment='9月のカレンダー')
    oct_calender = Column('oct_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='10月のカレンダー')
    nov_calender = Column('nov_calender', String(30, collation='ja_JP.utf8'), nullable=False, comment='11月のカレンダー')
    dec_calender = Column('dec_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='12月のカレンダー')
    count_job_holiday = Column('count_job_holiday', Integer, nullable=True, comment='所定休日日数')
    count_legal_holiday = Column('count_legal_holiday', Integer, nullable=True, comment='法定休日日数')
    count_plan_paid_holiday = Column('count_plan_paid_holiday', Integer, nullable=True, comment='有給奨励日日数')
    count_summer_holiday = Column('count_summer_holiday', Integer, nullable=True, comment='夏季休日日数')
    count_new_year_holiday_season = Column('count_new_year_holiday_season', Integer, nullable=True, comment='年末年始日数')
    count_national_holiday = Column('count_national_holiday', Integer, nullable=True, comment='国民の祝日日数')
    count_plan_grant_of_paid_leave = Column('count_plan_grant_of_paid_leave', Integer, nullable=True, comment='有給休暇の計画的付与日数')
    count_holidays_attribute_to_the_user = Column('count_holidays_attribute_to_the_user', Integer, nullable=True, comment='使用者の責に帰す休業日日数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_holiday', "company_code", "office_code", "target_date"), Index('ix_m_holiday_1', "company_code"), Index('ix_m_holiday_2', "office_code"), Index('ix_m_holiday_3', "company_code", "office_code"), UniqueConstraint("company_code", "office_code", "target_date"), )


class Push(Base):
    """
    プッシュ通知マスタ
    """
    __tablename__ = "m_push"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    device_id = Column('device_id', String(255, collation='ja_JP.utf8'), nullable=True, comment='デバイスID')
    device_name = Column('device_name', String(255, collation='ja_JP.utf8'), nullable=True, comment='デバイス名')
    token = Column('token', String(255, collation='ja_JP.utf8'), nullable=True, comment='トークン')
    pending_flg = Column('pending_flg', EnumType(enum_class=PendingFlg), nullable=False, comment='仮登録フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_push', "company_code", "employee_code", "device_id"), UniqueConstraint("company_code", "employee_code", "device_id"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeePaidLeaveChangeLog(Base):
    """
    従業員有給休暇タブ変更ログ
    従業員有給休暇タブの変更要求を記録します。変更がければ記録しません。
    """
    __tablename__ = "t_employee_paid_leave_change_log"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    execution_date = Column('execution_date', TIMESTAMP, nullable=False, comment='実行日')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    change_details = Column('change_details', Text(collation='ja_JP.utf8'), nullable=True, comment='変更内容')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    mapper_args = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_paid_leave_change_log', "execution_date", "company_code", "employee_code"), UniqueConstraint("execution_date", "company_code", "employee_code"), Index('ix_t_employee_paid_leave_change_log_company_employee', 'company_code', 'employee_code'),)


class PaidLeaveManagementLedger(Base):
    """
    有給休暇管理台帳
    有給休暇管理台帳を記録します。
    """
    __tablename__ = "t_paid_leave_management_ledger"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    hire_date = Column('hire_date', Date, nullable=False, comment='入社年月日')
    payment_date = Column('payment_date', Date, nullable=False, comment='支給年月日')

    hold_days = Column('hold_days', Float, nullable=False, comment='前年度繰越分日数')
    hold_times = Column('hold_times', Integer, nullable=False, comment='前年度繰越分時間')
    get_days = Column('get_days', Float, nullable=False, comment='今年度付与分日数')
    paid_reference_date = Column('paid_reference_date', Date, nullable=True, comment='前回有給付与日')
    total_hold_days = Column('total_hold_days', Float, nullable=False, comment='合計日数')
    total_hold_times = Column('total_hold_times', Integer, nullable=False, comment='合計時間')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=False, comment='所定労働時間')
    hours_in_a_day = Column('hours_in_a_day', Integer, nullable=False, comment='時間単位年休1日の時間数')
    available_in_one_year = Column('available_in_one_year', Integer, nullable=True, comment='一年間で取得可能な時間有給日数')
    employee_name = Column('employee_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='氏名')
    group_code = Column('group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='部署コード')
    group_name = Column('group_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='部署名')
    planned_grant_period = Column('planned_grant_period', Integer, nullable=True, comment='労使協定で定める計画的付与日数')
    total_get_days = Column('total_get_days', Float, nullable=True, comment='取得合計日数')
    total_get_times = Column('total_get_times', Integer, nullable=True, comment='取得合計時間数')
    obligation_to_specify_season_day = Column('obligation_to_specify_season_day', Integer, nullable=True, comment='年5日の時季指定義務を履行するための残日数')
    annual_leave_by_the_hour_get_times = Column('annual_leave_by_the_hour_get_times', Integer, nullable=True, comment='時間単位年休の取得時間')
    equivalent_number_of_days = Column('equivalent_number_of_days', Integer, nullable=True, comment='時間単位年休の換算日数')
    equivalent_number_of_times = Column('equivalent_number_of_times', Integer, nullable=True, comment='時間単位年休の換算時間')
    total_planned_grant_period = Column('total_planned_grant_period', Integer, nullable=True, comment='計画的付与日数の合計')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    mapper_args = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_paid_leave_management_ledger', "company_code", "employee_code", "payment_date"), UniqueConstraint("company_code", "employee_code", "payment_date"),)


class PaidLeaveManagementLedgerDetail(Base):
    """
    有給休暇管理台帳明細
    有給休暇管理台帳明細を記録します。
    """
    __tablename__ = "t_paid_leave_management_ledger_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    payment_date = Column('payment_date', Date, nullable=False, comment='支給年月日')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    designated_category = Column('designated_category', EnumType(enum_class=DesignatedCategory), nullable=False, comment='指定区分')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    term_time_from = Column('term_time_from', String(5, collation='ja_JP.utf8'), nullable=True, comment='時間(開始)')
    term_time_to = Column('term_time_to', String(5, collation='ja_JP.utf8'), nullable=True, comment='時間(終了)')
    get_days = Column('get_days', Float, nullable=True, comment='取得日数')
    get_times = Column('get_times', Integer, nullable=True, comment='取得時間')
    application_number = Column('application_number', Integer, nullable=True, comment='申請番号')
    contents = Column('contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    apply_date = Column('apply_date', TIMESTAMP, nullable=True, comment='申請日')
    person_in_charge_start_date = Column('person_in_charge_start_date', Date, nullable=False, comment='有効開始日')
    person_in_charge_end_date = Column('person_in_charge_end_date', Date, nullable=False, comment='有効終了日')
    person_in_charge_start_time = Column('person_in_charge_start_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='時間(開始)')
    person_in_charge_end_time = Column('person_in_charge_end_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='時間(終了)')
    hold_days = Column('hold_days', Float, nullable=False, comment='有給残日数')
    hold_times = Column('hold_times', Integer, nullable=False, comment='有給残時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    mapper_args = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_paid_leave_management_ledger_detail', "company_code", "employee_code", "payment_date", "serial_number"), UniqueConstraint("company_code", "employee_code", "payment_date", "serial_number"),)


class ShiftPublish(Base):
    """
    シフト公開トラン
    """
    __tablename__ = "t_shift_publish"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    shift_publish_flg = Column('shift_publish_flg', EnumType(enum_class=ShiftPublishFlg), nullable=False, comment='シフト公開フラグ')
    unset_holiday_flg = Column('unset_holiday_flg', Boolean, nullable=True, comment='未設定を所定休日とするフラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_shift_publish', "company_code", "office_code", "target_date"), Index('ix_t_shift_publish_1', "company_code"), UniqueConstraint("company_code", "office_code", "target_date"), {'extend_existing': True})


class ShiftPattern(Base):
    """
    シフトパターンマスタ
    """
    __tablename__ = "m_shift_pattern"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    shift_pattern_code = Column('shift_pattern_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='シフトパターンコード')
    shift_pattern_name = Column('shift_pattern_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='シフトパターン名')
    job_start_mon = Column('job_start_mon', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間(月)')
    job_end_mon = Column('job_end_mon', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間(月)')
    work_status_mon = Column('work_status_mon', EnumType(enum_class=WorkStatus), nullable=False, comment='出勤ステータス(月)')
    job_start_tue = Column('job_start_tue', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間(火)')
    job_end_tue = Column('job_end_tue', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間(火)')
    work_status_tue = Column('work_status_tue', EnumType(enum_class=WorkStatus), nullable=False, comment='出勤ステータス(火)')
    job_start_wed = Column('job_start_wed', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間(水)')
    job_end_wed = Column('job_end_wed', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間(水)')
    work_status_wed = Column('work_status_wed', EnumType(enum_class=WorkStatus), nullable=False, comment='出勤ステータス(水)')
    job_start_thu = Column('job_start_thu', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間(木)')
    job_end_thu = Column('job_end_thu', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間(木)')
    work_status_thu = Column('work_status_thu', EnumType(enum_class=WorkStatus), nullable=False, comment='出勤ステータス(木)')
    job_start_fri = Column('job_start_fri', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間(金)')
    job_end_fri = Column('job_end_fri', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間(金)')
    work_status_fri = Column('work_status_fri', EnumType(enum_class=WorkStatus), nullable=False, comment='出勤ステータス(金)')
    job_start_sat = Column('job_start_sat', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間(土)')
    job_end_sat = Column('job_end_sat', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間(土)')
    work_status_sat = Column('work_status_sat', EnumType(enum_class=WorkStatus), nullable=False, comment='出勤ステータス(土)')
    job_start_sun = Column('job_start_sun', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間(日)')
    job_end_sun = Column('job_end_sun', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間(日)')
    work_status_sun = Column('work_status_sun', EnumType(enum_class=WorkStatus), nullable=False, comment='出勤ステータス(日)')
    work_schedule_code_mon = Column('work_schedule_code_mon', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード(月)')
    work_schedule_code_tue = Column('work_schedule_code_tue', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード(火)')
    work_schedule_code_wed = Column('work_schedule_code_wed', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード(水)')
    work_schedule_code_thu = Column('work_schedule_code_thu', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード(木)')
    work_schedule_code_fri = Column('work_schedule_code_fri', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード(金)')
    work_schedule_code_sat = Column('work_schedule_code_sat', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード(土)')
    work_schedule_code_sun = Column('work_schedule_code_sun', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード(日)')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_shift_pattern', "company_code", "shift_pattern_code"), Index('ix_m_shift_pattern_1', "company_code"), Index('ix_m_shift_pattern_2', "shift_pattern_code"), UniqueConstraint("company_code", "shift_pattern_code"), UniqueConstraint("company_code", "shift_pattern_name"), )


class EmployeeSelectManagement(Base):
    """
    従業員レイアウト選択マスタ
    """
    __tablename__ = "m_employee_select_management"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    attendance_record_layout = Column('attendance_record_layout', EnumType(enum_class=AttendanceRecordLayout), nullable=False, comment='出勤簿レイアウト区分')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_select_management', "company_code", "employee_code"), Index('ix_m_employee_select_management_1', "company_code"), Index('ix_m_employee_select_management_2', "employee_code"), UniqueConstraint("company_code", "employee_code"), {'extend_existing': True})


class OperationDate(Base):
    """
    運用日付トラン
    """
    __tablename__ = "t_operation_date"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    operation_date = Column('operation_date', Date, nullable=False, comment='運用年月日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_operation_date', "company_code", "operation_date"), UniqueConstraint("company_code", "operation_date"))


class EmployeeDesiredShiftSchedule(Base):
    """
    従業員別希望シフトトラン
    """
    __tablename__ = "t_employee_desired_shift_schedule"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_status = Column('work_status', EnumType(enum_class=WorkStatus), nullable=False, comment='出勤ステータス')
    job_start = Column('job_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間')
    job_end = Column('job_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_desired_shift_schedule', "company_code", "employee_code", "office_code", "target_date"), Index('ix_t_employee_desired_shift_schedule_1', "company_code"), UniqueConstraint("company_code", "employee_code", "office_code", "target_date"))


class EmployeeShiftPreference(Base):
    """
    従業員シフト希望設定（繰り返し・日付単発 両対応）
    """
    __tablename__ = "t_employee_shift_preference"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), nullable=False, comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', Date, nullable=True, comment='対象日（スポット希望）')
    weekday = Column('weekday', Integer, nullable=True, comment='曜日（0=月〜6=日）')
    job_start = Column('job_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業希望時間')
    job_end = Column('job_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業希望時間')
    shift_preference_status = Column('shift_preference_status', EnumType(enum_class=ShiftPreferenceStatus), nullable=False, comment='希望シフトステータス')
    reason = Column('reason', String(255, collation='ja_JP.utf8'), nullable=True, comment='希望理由')
    repeat = Column('repeat', Boolean, nullable=False, default=False, comment='繰り返しフラグ（曜日指定の場合）')
    start_date = Column('start_date', Date, nullable=True, comment='繰り返し有効開始日')
    end_date = Column('end_date', Date, nullable=True, comment='繰り返し有効終了日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (
        Index('ix_t_employee_shift_preference', "company_code", "employee_code", "target_date", "weekday"),
    )


class EmployeeShiftPreferencePattern(Base):
    """
    従業員別希望[曜日]シフトトラン
    """
    __tablename__ = "t_employee_shift_preference_pattern"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    week_day = Column('week_day', EnumType(enum_class=DayOfTheWeek), nullable=True, comment='労働日')
    job_start = Column('job_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業希望時間')
    job_end = Column('job_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業希望時間')
    shift_preference_status = Column('shift_preference_status', EnumType(enum_class=ShiftPreferenceStatus), nullable=False, comment='希望シフトステータス')
    reason = Column('reason', String(255, collation='ja_JP.utf8'), nullable=True, comment='希望理由')
    start_date = Column('start_date', Date, nullable=True)
    end_date = Column('end_date', Date, nullable=True)
    repeat = Column('repeat', Boolean, default=True, nullable=False)
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_shift_preference_pattern', "company_code", "employee_code", "week_day"), UniqueConstraint("company_code", "employee_code", "week_day"))


class EmployeeShiftVolumePreference(Base):
    """
    従業員別 月間希望労働量（時間・日数など）
    """
    __tablename__ = "t_employee_shift_volume_preference"

    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_month = Column('target_month', String(7), nullable=False, comment="対象月")
    min_hours = Column('min_hours', Integer, nullable=True, comment="月間最低労働時間")
    max_hours = Column('max_hours', Integer, nullable=True, comment="月間最大労働時間")
    preferred_days = Column('preferred_days', Integer, nullable=True, comment="希望勤務日数")
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_shift_volume_preference', "company_code", "employee_code", "target_month"), UniqueConstraint("company_code", "employee_code", "target_month"))


class EmployeeConfirmShiftSchedule(Base):
    """
    従業員別確定シフトトラン
    """
    __tablename__ = "t_employee_confirm_shift_schedule"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_status = Column('work_status', EnumType(enum_class=WorkStatus), nullable=False, comment='出勤ステータス')
    job_start = Column('job_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='始業時間')
    job_end = Column('job_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='終業時間')
    shift_reflection_flg = Column('shift_reflection_flg', EnumType(enum_class=ShiftReflectionFlg), nullable=True, comment='シフト確定フラグ')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='勤務体系コード')
    fixed_date = Column('fixed_date', TIMESTAMP, nullable=True, comment='確定日')
    shift_publish_flg = Column('shift_publish_flg', EnumType(enum_class=ShiftPublishFlg), nullable=True, comment='シフト公開フラグ')
    satisfaction_rate = Column('satisfaction_rate', Integer, nullable=True, comment='希望反映満足度（%）')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_confirm_shift_schedule', "company_code", "employee_code", "office_code", "target_date", "work_schedule_code"), Index('ix_t_employee_confirm_shift_schedule_1', "company_code"), Index('ix_t_employee_confirm_shift_schedule_2', "employee_code"), Index('ix_t_employee_confirm_shift_schedule_3', "office_code"), UniqueConstraint("company_code", "employee_code", "office_code", "target_date", "work_schedule_code"))


class EmployeeAdjustmentShiftSchedule(Base):
    """
    従業員別シフト調整トラン
    """
    __tablename__ = "t_employee_adjustment_shift_schedule"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    job_start = Column('job_start', String(5, collation='ja_JP.utf8'), nullable=False, comment='始業時間')
    job_end = Column('job_end', String(5, collation='ja_JP.utf8'), nullable=False, comment='終業時間')
    message = Column('message', String(255, collation='ja_JP.utf8'), nullable=True, comment='メッセージ')
    sending_employee_name = Column('sending_employee_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='送信した従業員名')
    sending_date = Column('sending_date', TIMESTAMP, nullable=True, comment='送信日付')
    is_read = Column('is_read', Integer, nullable=False, comment='既読フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_adjustment_shift_schedule', "company_code", "employee_code", "office_code", "target_date", "serial_number"), Index('ix_t_employee_adjustment_shift_schedule_1', "company_code"), Index('ix_t_employee_adjustment_shift_schedule_2', "employee_code"), Index('ix_t_employee_adjustment_shift_schedule_3', "office_code"), UniqueConstraint("company_code", "employee_code", "office_code", "target_date", "serial_number"))


class MutualPairPreference(Base):
    """
    両想いペア（同時シフト希望）
    """
    __tablename__ = "t_mutual_pair_preference"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="サロゲートキー")
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code_from = Column('employee_code_from', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号[自分]')
    employee_code_to = Column('employee_code_to', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号[相手]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)

    __mapper_args__ = {
        'version_id_col': update_count
    }

    __table_args__ = (
        UniqueConstraint('company_code', 'employee_code_from', 'employee_code_to'),
        Index('ix_t_mutual_pair_preference', 'company_code', 'employee_code_from', 'employee_code_to'),
        CheckConstraint("employee_code_from < employee_code_to", name="ck_employee_pair_order"),
    )


class OneSidedPairPreference(Base):
    """
    片想いペア（希望者 → 相手）
    """
    __tablename__ = "t_one_sided_pair_preference"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="サロゲートキー")
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code_from = Column('employee_code_from', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号[自分]')
    employee_code_to = Column('employee_code_to', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号[相手]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)

    __mapper_args__ = {
        'version_id_col': update_count
    }

    __table_args__ = (
        UniqueConstraint('company_code', 'employee_code_from', 'employee_code_to'),
        Index('ix_t_one_sided_pair_preference', 'company_code', 'employee_code_from'),
    )


class NoPairPreference(Base):
    """
    ペア禁止関係（同時シフト禁止）
    """
    __tablename__ = "t_no_pair_preference"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="サロゲートキー")
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code_from = Column('employee_code_from', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号[自分]')
    employee_code_to = Column('employee_code_to', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号[相手]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)

    __mapper_args__ = {
        'version_id_col': update_count
    }

    __table_args__ = (
        UniqueConstraint('company_code', 'employee_code_from', 'employee_code_to'),
        Index('ix_t_no_pair_preference', 'company_code', 'employee_code_from', 'employee_code_to'),
        CheckConstraint("employee_code_from < employee_code_to", name="ck_no_pair_order"),
    )


class EmailTransmissionManagement(Base):
    """
    メール送信管理トラン
    """
    __tablename__ = "t_email_transmission_management"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    sending_employee_code = Column('sending_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='送信した従業員番号')
    receiving_employee_code = Column('receiving_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='受信する従業員番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    subject = Column('subject', String(255, collation='ja_JP.utf8'), nullable=True, comment='件名')
    body_text = Column('body_text', String(4096, collation='ja_JP.utf8'), nullable=True, comment='本文')
    sending_date = Column('sending_date', TIMESTAMP, nullable=True, comment='送信日付')
    send_mail_status = Column('send_mail_status', EnumType(enum_class=SendMailStatus), nullable=False, comment='メール送信ステータス')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_email_transmission_management', "company_code", "sending_employee_code", "receiving_employee_code", "serial_number"), UniqueConstraint("company_code", "sending_employee_code", "receiving_employee_code", "serial_number"), )


class EmailTransmissionManagementAppended(Base):
    """
    メール送信添付オブジェクト
    """
    __tablename__ = "t_email_transmission_management_appended"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    sending_employee_code = Column('sending_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='送信した従業員番号')
    receiving_employee_code = Column('receiving_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='受信する従業員番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    report_serial_number = Column('report_serial_number', Integer, nullable=False, comment='帳票トランのサロゲートキー')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_email_transmission_management_appended', "company_code", "sending_employee_code", "receiving_employee_code", "serial_number", "report_serial_number"), UniqueConstraint("company_code", "sending_employee_code", "receiving_employee_code", "serial_number", "report_serial_number"), )


class AttendanceRecordCalender(Base):
    """
    出勤簿カレンダートラン
    """
    __tablename__ = "t_attendance_record_calender"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    ground_code = Column('ground_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事由コード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_attendance_record_calender', "company_code", "employee_code", "target_date"), UniqueConstraint("company_code", "employee_code", "target_date"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeHoliday(Base):
    """
    従業員休日マスタ
    """
    __tablename__ = "m_employee_holiday"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    jan_calender = Column('jan_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='1月のカレンダー')
    feb_calender = Column('feb_calender', String(29, collation='ja_JP.utf8'), nullable=False, comment='2月のカレンダー')
    mar_calender = Column('mar_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='3月のカレンダー')
    apl_calender = Column('apl_calender', String(30, collation='ja_JP.utf8'), nullable=False, comment='4月のカレンダー')
    may_calender = Column('may_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='5月のカレンダー')
    jun_calender = Column('jun_calender', String(30, collation='ja_JP.utf8'), nullable=False, comment='6月のカレンダー')
    jly_calender = Column('jly_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='7月のカレンダー')
    aug_calender = Column('aug_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='8月のカレンダー')
    sep_calender = Column('sep_calender', String(30, collation='ja_JP.utf8'), nullable=False, comment='9月のカレンダー')
    oct_calender = Column('oct_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='10月のカレンダー')
    nov_calender = Column('nov_calender', String(30, collation='ja_JP.utf8'), nullable=False, comment='11月のカレンダー')
    dec_calender = Column('dec_calender', String(31, collation='ja_JP.utf8'), nullable=False, comment='12月のカレンダー')
    count_job_holiday = Column('count_job_holiday', Integer, nullable=True, comment='所定休日日数')
    count_legal_holiday = Column('count_legal_holiday', Integer, nullable=True, comment='法定休日日数')
    count_plan_paid_holiday = Column('count_plan_paid_holiday', Integer, nullable=True, comment='有給奨励日日数')
    count_summer_holiday = Column('count_summer_holiday', Integer, nullable=True, comment='夏季休日日数')
    count_new_year_holiday_season = Column('count_new_year_holiday_season', Integer, nullable=True, comment='年末年始日数')
    count_national_holiday = Column('count_national_holiday', Integer, nullable=True, comment='国民の祝日日数')
    count_plan_grant_of_paid_leave = Column('count_plan_grant_of_paid_leave', Integer, nullable=True, comment='有給休暇の計画的付与日数')
    count_holidays_attribute_to_the_user = Column('count_holidays_attribute_to_the_user', Integer, nullable=True, comment='使用者の責に帰す休業日日数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_holiday', "company_code", "employee_code", "target_date"), Index('ix_m_employee_holiday_1', "company_code"), Index('ix_m_employee_holiday_2', "company_code", "employee_code"), UniqueConstraint("company_code", "employee_code", "target_date"), )


class FlexRule(Base):
    """
    フレックスタイム制に関する協定書マスタ
    """
    __tablename__ = "m_flex_rule"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    starting_date = Column('starting_date', Date, nullable=False, comment='起算日')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    agreement_date = Column('agreement_date', Date, nullable=False, comment='協定の成立年月日')
    agreement_parties_job_title_code = Column('agreement_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の職名コード')
    agreement_parties_employee_code = Column('agreement_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='協定当事者の従業員番号')
    election_method = Column('election_method', EnumType(enum_class=ElectionMethod), nullable=False, comment='選出方法')
    filing_date = Column('filing_date', Date, nullable=False, comment='提出日')
    management_parties_job_title_code = Column('management_parties_job_title_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の職名コード')
    management_parties_employee_code = Column('management_parties_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='使用者の従業員番号')
    labor_standards_inspection_office = Column('labor_standards_inspection_office', String(50, collation='ja_JP.utf8'), nullable=False, comment='労働基準監督署')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_flex_rule', "company_code", "office_code", "starting_date"), Index('ix_m_flex_rule_1', "company_code"), UniqueConstraint("company_code", "office_code", "starting_date"), )


class FlexRuleDetail(Base):
    """
    フレックスタイム制に関する協定書明細マスタ
    """
    __tablename__ = "m_flex_rule_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    starting_date = Column('starting_date', Date, nullable=False, comment='起算日')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    settlement_period_from = Column('settlement_period_from', String(6, collation='ja_JP.utf8'), nullable=False, comment='精算期間(開始)')
    settlement_period_to = Column('settlement_period_to', String(6, collation='ja_JP.utf8'), nullable=False, comment='精算期間(終了)')
    core_start = Column('core_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='コアタイム[開始]')
    core_end = Column('core_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='コアタイム[終了]')
    flex_start = Column('flex_start', String(5, collation='ja_JP.utf8'), nullable=True, comment='フレキシブルタイム[開始]')
    flex_end = Column('flex_end', String(5, collation='ja_JP.utf8'), nullable=True, comment='フレキシブルタイム[終了]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_flex_rule_detail', "company_code", "office_code", "starting_date", "business_type", "settlement_period_from"), Index('ix_m_flex_rule_detail_1', "company_code"), UniqueConstraint("company_code", "office_code", "starting_date", "business_type", "settlement_period_from"), )


class UploadFile(Base):
    """
    アップロードトラン
    """
    __tablename__ = "t_upload_file"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    file_path = Column('file_path', String(255, collation='ja_JP.utf8'), nullable=False, comment='ファイルパス')
    file_name = Column('file_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='ファイル名')
    file_upload_date = Column('file_create_date', TIMESTAMP, nullable=False, comment='アップロード日')
    upload_status = Column('report_status', EnumType(enum_class=UploadStatus), nullable=False, comment='アップロードステータス')
    err_file_path = Column('err_file_path', String(255, collation='ja_JP.utf8'), nullable=True, comment='エラーファイルパス')
    err_file_name = Column('err_file_name', String(255, collation='ja_JP.utf8'), nullable=True, comment='エラーファイル名')
    report_code = Column('report_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='帳票コード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    mapper_args = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_upload_file', "company_code", "employee_code", "file_name"), UniqueConstraint("company_code", "employee_code", "file_name"), )


class PaidHolidayPayment(Base):
    """
    有給休暇支給マスタ
    有給休暇の付与までの月数、および付与日数をカテゴリー別に管理します。
    """
    __tablename__ = "m_paid_holiday_payment"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    number_of_working_days_per_week = Column('number_of_working_days_per_week', Integer, nullable=False, comment='週の労働日数')
    months_of_service = Column('months_of_service', Integer, nullable=False, comment='継続勤続月数')
    grant_days = Column('grant_days', Integer, nullable=False, comment='付与日数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_paid_holiday_payment', "company_code", "number_of_working_days_per_week", "months_of_service"), Index('ix_m_paid_holiday_payment_1', "company_code"), UniqueConstraint("company_code", "number_of_working_days_per_week", "months_of_service"), )


class PaidHolidayReference(Base):
    """
    有給休暇基準日マスタ
    有給休暇を支給する日(基準日)について対象期間を管理します。
    """
    __tablename__ = "m_paid_holiday_reference"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    reference_month = Column('reference_month', String(5, collation='ja_JP.utf8'), nullable=False, comment='統一支給日')
    number_of_working_days_per_week = Column('number_of_working_days_per_week', Integer, nullable=False, comment='週の労働日数')
    term_from = Column('term_from', String(5, collation='ja_JP.utf8'), nullable=False, comment='有効開始日')
    term_to = Column('term_to', String(5, collation='ja_JP.utf8'), nullable=True, comment='有効終了日')
    grant_days = Column('grant_days', Integer, nullable=False, comment='付与日数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_paid_holiday_reference', "company_code", "reference_month", "number_of_working_days_per_week", "term_from"), Index('ix_m_paid_holiday_reference_1', "company_code"), UniqueConstraint("company_code", "reference_month", "number_of_working_days_per_week", "term_from"), )


class PaidHolidayManagement(Base):
    """
    有給管理マスタ
    有給休暇支給/時効に関するルールを管理します。
    """
    __tablename__ = "m_paid_holiday_management"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    available_in_one_year = Column('available_in_one_year', Integer, nullable=False, comment='一年間で取得可能な時間有給日数')
    roll_over = Column('roll_over', EnumType(enum_class=RollOver), nullable=False, comment='繰り越し可否')
    limit = Column('limit', Integer, nullable=False, comment='時効年数')
    maximum_days = Column('maximum_days', Integer, nullable=False, comment='最大日数')
    digestion_order = Column('digestion_order', EnumType(enum_class=DigestionOrder), nullable=False, comment='消化順序')
    upper_limit = Column('upper_limit', Integer, nullable=False, comment='一度に繰り越しできる上限')
    attendance_rate = Column('attendance_rate', DECIMAL(3, 1), nullable=False, comment='出勤率')
    fraction_of_attendance_rate = Column('fraction_of_attendance_rate', EnumType(enum_class=FractionOfAttendanceRate), nullable=False, comment='出勤率の小数点以下についての端数処理')
    handling_planned_grants = Column('handling_planned_grants', EnumType(enum_class=HandlingPlannedGrants), nullable=False, comment='「計画的付与制度」において年次有給休暇が不足している場合の対応方法')
    paid_leave_granted = Column('paid_leave_granted', EnumType(enum_class=PaidLeaveGranted), nullable=False, comment='有給休暇付与ルール')
    paid_leave_payment_method = Column('paid_leave_payment_method', EnumType(enum_class=PaidLeavePaymentMethod), nullable=True, comment='統一支給方式 ')
    unified_payment_date1 = Column('unified_payment_date1', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日1')
    unified_payment_date2 = Column('unified_payment_date2', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日2')
    unified_payment_date3 = Column('unified_payment_date3', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日3')
    unified_payment_date4 = Column('unified_payment_date4', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日4')
    unified_payment_date5 = Column('unified_payment_date5', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日5')
    unified_payment_date6 = Column('unified_payment_date6', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日6')
    unified_payment_date7 = Column('unified_payment_date7', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日7')
    unified_payment_date8 = Column('unified_payment_date8', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日8')
    unified_payment_date9 = Column('unified_payment_date9', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日9')
    unified_payment_date10 = Column('unified_payment_date10', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日10')
    unified_payment_date11 = Column('unified_payment_date11', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日11')
    unified_payment_date12 = Column('unified_payment_date12', String(5, collation='ja_JP.utf8'), nullable=True, comment='統一支給日12')
    limit_apply_date = Column('limit_apply_date', Integer, nullable=True, comment='有給申請可能期限')
    legal_60_overwork_rate = Column('legal_60_overwork_rate', DECIMAL(3, 1), nullable=True, comment='60時間を超える法定外労働の割増率')
    alternative_leave_flag = Column('alternative_leave_flag', EnumType(enum_class=AlternativeLeaveFlag), nullable=True, comment='代替休暇利用フラグ')
    alternative_leave_rate = Column('alternative_leave_rate', DECIMAL(3, 1), nullable=True, comment='代替休暇を取得した場合に支払う割増賃金率')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_paid_holiday_management', "company_code"), UniqueConstraint("company_code"), )


class InsuranceEnrollment(Base):
    """
    保険加入マスタ
    会社の保険加入有無を管理します。
    """
    __tablename__ = "m_insurance_enrollment"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    social_insurance = Column('social_insurance', EnumType(enum_class=SocialInsurance), nullable=False, comment='社会保険')
    employment_insurance = Column('employment_insurance', EnumType(enum_class=EmploymentInsurance), nullable=False, comment='雇用保険')
    pension_fund_contributions = Column('pension_fund_contributions', EnumType(enum_class=PensionFundContributions), nullable=False, comment='厚生年金基金')
    type_of_business = Column('type_of_business', EnumType(enum_class=TypeOfBusiness), nullable=False, comment='事業の種類')
    business_type_number = Column('business_type_number', Integer, nullable=False, comment='事業の種類')
    collection_of_social_insurance_premiums = Column('collection_of_social_insurance_premiums', EnumType(enum_class=CollectionOfSocialInsurancePremiums), nullable=True, comment='社会保険料の徴収タイミング')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_insurance_enrollment', "company_code"), UniqueConstraint("company_code"), )


class Rate(Base):
    """
    料率マスタ
    会社の保険料率を管理します。
    """
    __tablename__ = "m_rate"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    calculate_withholding_tax = Column('calculate_withholding_tax', EnumType(enum_class=CalculateWithholdingTax), nullable=False, comment='源泉徴収税額の計算方法')
    health_insurance_salary_general_insurance_rate = Column('health_insurance_salary_general_insurance_rate', DECIMAL(6, 3), nullable=False, comment='健康保険(給与)一般')
    health_insurance_salary_adjusted_insurance_rate = Column('health_insurance_salary_adjusted_insurance_rate', DECIMAL(6, 3), nullable=False, comment='健康保険(給与)調整')
    health_insurance_bonus_general_insurance_rate = Column('health_insurance_bonus_general_insurance_rate', DECIMAL(6, 3), nullable=False, comment='健康保険(賞与)一般')
    health_insurance_bonus_adjusted_insurance_rate = Column('health_insurance_bonus_adjusted_insurance_rate', DECIMAL(6, 3), nullable=False, comment='健康保険(賞与)調整')
    health_insurance_nursing_care_fraction = Column('health_insurance_nursing_care_fraction', EnumType(enum_class=HealthInsuranceNursingCareFraction), nullable=False, comment='健康保険/介護保険端数区分')
    welfare_pension_salary_insurance_rate = Column('welfare_pension_salary_insurance_rate', DECIMAL(6, 3), nullable=False, comment='厚生年金(給与)保険料率')
    welfare_pension_bonus_insurance_rate = Column('welfare_pension_bonus_insurance_rate', DECIMAL(6, 3), nullable=False, comment='厚生年金(賞与)保険料率')
    employees_pension_fund_insurance_rate = Column('employees_pension_fund_insurance_rate', DECIMAL(6, 3), nullable=False, comment='厚生年金基金保険料率')
    welfare_pension_fraction_classification = Column('welfare_pension_fraction_classification', EnumType(enum_class=WelfarePensionFractionClassification), nullable=False, comment='厚生年金端数区分')
    duty_free_premium_rate = Column('duty_free_premium_rate', DECIMAL(3, 1), nullable=False, comment='免除保険料率')
    care_insurance_salary_fee_rate = Column('care_insurance_salary_fee_rate', DECIMAL(6, 3), nullable=False, comment='介護保険(給与)料率')
    care_insurance_bonus_fee_rate = Column('care_insurance_bonus_fee_rate', DECIMAL(6, 3), nullable=False, comment='介護保険(賞与)料率')
    employment_insurance_fraction_classification = Column('employment_insurance_fraction_classification', EnumType(enum_class=EmploymentInsuranceFractionClassification), nullable=False, comment='雇用保険端数区分')
    workers_accident_compensation_rate = Column('workers_accident_compensation_rate', DECIMAL(3, 1), nullable=False, comment='労災保険料率')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_rate', "company_code"), UniqueConstraint("company_code"), )


class CompanyAccount(Base):
    """
    会社口座マスタ
    会社の口座情報を管理します。
    """
    __tablename__ = "m_company_account"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    bank_code = Column('bank_code', String(4, collation='ja_JP.utf8'), ForeignKey('m_bank.bank_code', onupdate='CASCADE', ondelete='CASCADE'), comment='銀行コード')
    branch_code = Column('branch_code', String(3, collation='ja_JP.utf8'), nullable=False, comment='支店コード')
    company_code_4_bank = Column('company_code_4_bank', String(10, collation='ja_JP.utf8'), nullable=True, comment='全銀協用会社コード')
    company_name_4_bank = Column('company_name_4_bank', String(40, collation='ja_JP.utf8'), nullable=True, comment='全銀協用会社名')
    account_classification = Column('account_classification', EnumType(enum_class=AccountClassification), nullable=False, comment='口座種別')
    account_number = Column('account_number', String(7, collation='ja_JP.utf8'), nullable=False, comment='口座番号')
    transfer_method = Column('transfer_method', EnumType(enum_class=TransferMethod), nullable=False, comment='振込方法')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company_account', "company_code", "bank_code", "branch_code"), Index('ix_m_company_account_1', "company_code"), UniqueConstraint("company_code", "bank_code", "branch_code"),)


class FinancialStatementSubjects(Base):
    """
    決算書科目マスタ
    会社の決算書科目を管理します。
    """
    __tablename__ = "m_financial_statement_subjects"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    accounting_classification_code = Column('accounting_classification_code', String(20, collation='ja_JP.utf8'), nullable=False, comment='会計分類コード')
    financial_statement_subjects_code = Column('financial_statement_subjects_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='決算書科目コード')
    financial_statement_subjects_name = Column('financial_statement_subjects_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='決算書科目名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_financial_statement_subjects', "company_code", "financial_statement_subjects_code"), Index('ix_m_financial_statement_subjects_1', "company_code"), UniqueConstraint("company_code", "financial_statement_subjects_code"),)


class Account(Base):
    """
    勘定科目マスタ
    会社の勘定科目を管理します。
    """
    __tablename__ = "m_account"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    accounting_classification_code = Column('accounting_classification_code', String(20, collation='ja_JP.utf8'), nullable=False, comment='会計分類コード')
    financial_statement_subjects_code = Column('financial_statement_subjects_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='決算書科目コード')
    account_code = Column('account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='勘定科目コード')
    account_name = Column('account_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='勘定科目名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_account', "company_code", "account_code"), Index('ix_m_account_1', "company_code"), UniqueConstraint("company_code", "account_code"),)


class SubAccount(Base):
    """
    補助科目マスタ
    会社の補助科目を管理します。
    """
    __tablename__ = "m_sub_account"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    account_code = Column('account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='勘定科目コード')
    sub_account_code = Column('sub_account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='補助勘定科目コード')
    sub_account_name = Column('sub_account_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='補助勘定科目名')
    tax_type = Column('tax_type', EnumType(enum_class=TaxType), nullable=False, comment='税種別')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_sub_account', "company_code", "account_code", "sub_account_code"), Index('ix_m_sub_account_1', "company_code"), UniqueConstraint("company_code", "account_code", "sub_account_code"),)


class SalaryItem(Base):
    """
    給与項目マスタ
    会社の給与項目を管理します。
    """
    __tablename__ = "m_salary_item"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    salary_item_code = Column('salary_item_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='給与項目コード')
    salary_item_name = Column('salary_item_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='給与項目名')
    salary_bonus_classification = Column('salary_bonus_classification', EnumType(enum_class=SalaryBonusClassification), nullable=False, comment='支給区分')
    payment_deduction_category = Column('payment_deduction_category', EnumType(enum_class=PaymentDeductionCategory), nullable=False, comment='支給/控除区分')
    year_classification = Column('year_classification', EnumType(enum_class=Availability), nullable=False, comment='年俸制')
    month_classification = Column('month_classification', EnumType(enum_class=Availability), nullable=False, comment='月給制')
    month_day_classification = Column('month_day_classification', EnumType(enum_class=Availability), nullable=False, comment='月給日給制')
    day_month_classification = Column('day_month_classification', EnumType(enum_class=Availability), nullable=False, comment='日給月給制')
    time_classification = Column('time_classification', EnumType(enum_class=Availability), nullable=False, comment='時給制')
    bonus_classification = Column('bonus_classification', EnumType(enum_class=Availability), nullable=False, comment='賞与')
    employment_insurance_target_category = Column('employment_insurance_target_category', EnumType(enum_class=EmploymentInsuranceTargetCategory), nullable=False, comment='雇用保険対象区分')
    tax_target_category = Column('tax_target_category', EnumType(enum_class=TaxTargetCategory), nullable=False, comment='所得税対象区分')
    tax_exemption_limit = Column('tax_exemption_limit', Integer, nullable=True, comment='非課税枠[以下まで]')
    social_insurance_target_category = Column('social_insurance_target_category', EnumType(enum_class=SocialInsuranceTargetCategory), nullable=False, comment='社会保険対象区分')
    fixed_fluctuation = Column('fixed_fluctuation', EnumType(enum_class=FixedFluctuation), nullable=False, comment='計算方法')
    formula = Column('formula', String(255, collation='ja_JP.utf8'), nullable=True, comment='計算式')
    account_code = Column('account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='勘定科目コード')
    sub_account_code = Column('sub_account_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='補助勘定科目コード')
    sign = Column('sign', EnumType(enum_class=Sign), nullable=False, comment='符号')
    allowance = Column('allowance', Integer, nullable=True, comment='共通手当　※従業員ごとに単価設定する必要がない場合は変動項目の計算式に適応する単価をここに設定して下さい。')
    payment_method = Column('payment_method', EnumType(enum_class=PaymentMethod), nullable=False, comment='支給方法')
    availability = Column('availability', EnumType(enum_class=Availability), nullable=False, comment='アカウント利用')
    basic_salary = Column('basic_salary', EnumType(enum_class=BasicSalary), nullable=True, comment='基本給区分')
    daily_division = Column('daily_division', EnumType(enum_class=DailyDivision), nullable=True, comment='日割り対象')
    included_fixed_wages_social_security = Column('included_fixed_wages_social_security', Boolean, nullable=True, comment='社会保険料を決定する上での固定賃金に含む')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_salary_item', "company_code", "salary_item_code"), Index('ix_m_salary_item_1', "company_code"), Index('ix_m_salary_item_2', "salary_item_code"), UniqueConstraint("company_code", "salary_item_code"), UniqueConstraint("company_code", "salary_item_name"),)


class SalaryTargetItemRename(Base):
    """
    給与項目名称変更マスタ
    会社の給与項目を管理します。
    """
    __tablename__ = "m_salary_target_item_rename"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    salary_item_code = Column('salary_item_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='給与項目コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    salary_item_name = Column('salary_item_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='給与項目名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_salary_target_item_rename', "company_code", "salary_item_code", "term_from"), Index('ix_m_salary_target_item_rename_1', "company_code"), Index('ix_m_salary_target_item_rename_2', "salary_item_code"), UniqueConstraint("company_code", "salary_item_code", "term_from"),)


class Layout(Base):
    """
    レイアウトマスタ
    会社のレイアウトを管理します。
    """
    __tablename__ = "m_layout"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    layout_code = Column('layout_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='レイアウトコード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    layout_name = Column('layout_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='レイアウト名')
    salary_category = Column('salary_category', EnumType(enum_class=SalaryCategory), nullable=False, comment='給与区分')
    payment_salary_item_code1 = Column('payment_salary_item_code1', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード1')
    payment_salary_item_code2 = Column('payment_salary_item_code2', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード2')
    payment_salary_item_code3 = Column('payment_salary_item_code3', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード3')
    payment_salary_item_code4 = Column('payment_salary_item_code4', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード4')
    payment_salary_item_code5 = Column('payment_salary_item_code5', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード5')
    payment_salary_item_code6 = Column('payment_salary_item_code6', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード6')
    payment_salary_item_code7 = Column('payment_salary_item_code7', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード7')
    payment_salary_item_code8 = Column('payment_salary_item_code8', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード8')
    payment_salary_item_code9 = Column('payment_salary_item_code9', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード9')
    payment_salary_item_code10 = Column('payment_salary_item_code10', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード10')
    payment_salary_item_code11 = Column('payment_salary_item_code11', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード11')
    payment_salary_item_code12 = Column('payment_salary_item_code12', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード12')
    payment_salary_item_code13 = Column('payment_salary_item_code13', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード13')
    payment_salary_item_code14 = Column('payment_salary_item_code14', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード14')
    payment_salary_item_code15 = Column('payment_salary_item_code15', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード15')
    payment_salary_item_code16 = Column('payment_salary_item_code16', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード16')
    payment_salary_item_code17 = Column('payment_salary_item_code17', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード17')
    payment_salary_item_code18 = Column('payment_salary_item_code18', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード18')
    payment_salary_item_code19 = Column('payment_salary_item_code19', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード19')
    payment_salary_item_code20 = Column('payment_salary_item_code20', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード20')
    payment_salary_item_code21 = Column('payment_salary_item_code21', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード21')
    payment_salary_item_code22 = Column('payment_salary_item_code22', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード22')
    payment_salary_item_code23 = Column('payment_salary_item_code23', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード23')
    payment_salary_item_code24 = Column('payment_salary_item_code24', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード24')
    payment_salary_item_code25 = Column('payment_salary_item_code25', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード25')
    payment_salary_item_code26 = Column('payment_salary_item_code26', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード26')
    payment_salary_item_code27 = Column('payment_salary_item_code27', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード27')
    payment_salary_item_code28 = Column('payment_salary_item_code28', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード28')
    payment_salary_item_code29 = Column('payment_salary_item_code29', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード29')
    payment_salary_item_code30 = Column('payment_salary_item_code30', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード30')
    deduction_salary_item_code1 = Column('deduction_salary_item_code1', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード1')
    deduction_salary_item_code2 = Column('deduction_salary_item_code2', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード2')
    deduction_salary_item_code3 = Column('deduction_salary_item_code3', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード3')
    deduction_salary_item_code4 = Column('deduction_salary_item_code4', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード4')
    deduction_salary_item_code5 = Column('deduction_salary_item_code5', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード5')
    deduction_salary_item_code6 = Column('deduction_salary_item_code6', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード6')
    deduction_salary_item_code7 = Column('deduction_salary_item_code7', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード7')
    deduction_salary_item_code8 = Column('deduction_salary_item_code8', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード8')
    deduction_salary_item_code9 = Column('deduction_salary_item_code9', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード9')
    deduction_salary_item_code10 = Column('deduction_salary_item_code10', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード10')
    deduction_salary_item_code11 = Column('deduction_salary_item_code11', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード11')
    deduction_salary_item_code12 = Column('deduction_salary_item_code12', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード12')
    deduction_salary_item_code13 = Column('deduction_salary_item_code13', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード13')
    deduction_salary_item_code14 = Column('deduction_salary_item_code14', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード14')
    deduction_salary_item_code15 = Column('deduction_salary_item_code15', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード15')
    deduction_salary_item_code16 = Column('deduction_salary_item_code16', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード16')
    deduction_salary_item_code17 = Column('deduction_salary_item_code17', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード17')
    deduction_salary_item_code18 = Column('deduction_salary_item_code18', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード18')
    deduction_salary_item_code19 = Column('deduction_salary_item_code19', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード19')
    deduction_salary_item_code20 = Column('deduction_salary_item_code20', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード20')
    deduction_salary_item_code21 = Column('deduction_salary_item_code21', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード21')
    deduction_salary_item_code22 = Column('deduction_salary_item_code22', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード22')
    deduction_salary_item_code23 = Column('deduction_salary_item_code23', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード23')
    deduction_salary_item_code24 = Column('deduction_salary_item_code24', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード24')
    deduction_salary_item_code25 = Column('deduction_salary_item_code25', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード25')
    deduction_salary_item_code26 = Column('deduction_salary_item_code26', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード26')
    deduction_salary_item_code27 = Column('deduction_salary_item_code27', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード27')
    deduction_salary_item_code28 = Column('deduction_salary_item_code28', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード28')
    deduction_salary_item_code29 = Column('deduction_salary_item_code29', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード29')
    deduction_salary_item_code30 = Column('deduction_salary_item_code30', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード30')
    availability = Column('availability', EnumType(enum_class=Availability), nullable=False, comment='アカウント利用')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_layout', "company_code", "layout_code", "term_from"), Index('ix_m_layout_1', "company_code"), UniqueConstraint("company_code", "layout_code", "term_from"),)


class ThirdPartyPayrollAppLayout(Base):
    """
    サードパーティ給与アプリ用レイアウトマスタ
    サードパーティ給与アプリのレイアウトを管理します。
    """
    __tablename__ = "m_third_party_payroll_app_layout"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    third_party_payroll_layout_code = Column('third_party_payroll_layout_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='サードパーティ給与アプリレイアウトコード')
    third_party_payroll_layout_name = Column('third_party_payroll_layout_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='サードパーティ給与アプリレイアウト名')
    output_direction = Column('output_direction', String(10, collation='ja_JP.utf8'), nullable=False, comment='出力方向')
    is_label_output = Column('is_label_output', EnumType(enum_class=IsLabelOutput), nullable=False, comment='ラベル出力の有無')
    quotation_mark = Column('quotation_mark', EnumType(enum_class=QuotationMark), nullable=False, comment='クォーテーションマーク')
    field_separator = Column('field_separator', EnumType(enum_class=FieldSeparator), nullable=False, comment='フィールドセパレーター')
    time_style = Column('time_style', EnumType(enum_class=TimeStyle), nullable=False, comment='時間形式')
    aggregation_category_code_01 = Column('aggregation_category_code_01', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード1')
    aggregation_category_code_02 = Column('aggregation_category_code_02', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード2')
    aggregation_category_code_03 = Column('aggregation_category_code_03', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード3')
    aggregation_category_code_04 = Column('aggregation_category_code_04', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード4')
    aggregation_category_code_05 = Column('aggregation_category_code_05', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード5')
    aggregation_category_code_06 = Column('aggregation_category_code_06', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード6')
    aggregation_category_code_07 = Column('aggregation_category_code_07', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード7')
    aggregation_category_code_08 = Column('aggregation_category_code_08', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード8')
    aggregation_category_code_09 = Column('aggregation_category_code_09', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード9')
    aggregation_category_code_10 = Column('aggregation_category_code_10', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード10')
    aggregation_category_code_11 = Column('aggregation_category_code_11', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード11')
    aggregation_category_code_12 = Column('aggregation_category_code_12', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード12')
    aggregation_category_code_13 = Column('aggregation_category_code_13', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード13')
    aggregation_category_code_14 = Column('aggregation_category_code_14', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード14')
    aggregation_category_code_15 = Column('aggregation_category_code_15', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード15')
    aggregation_category_code_16 = Column('aggregation_category_code_16', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード16')
    aggregation_category_code_17 = Column('aggregation_category_code_17', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード17')
    aggregation_category_code_18 = Column('aggregation_category_code_18', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード18')
    aggregation_category_code_19 = Column('aggregation_category_code_19', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード19')
    aggregation_category_code_20 = Column('aggregation_category_code_20', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード20')
    aggregation_category_code_21 = Column('aggregation_category_code_21', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード21')
    aggregation_category_code_22 = Column('aggregation_category_code_22', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード22')
    aggregation_category_code_23 = Column('aggregation_category_code_23', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード23')
    aggregation_category_code_24 = Column('aggregation_category_code_24', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード24')
    aggregation_category_code_25 = Column('aggregation_category_code_25', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード25')
    aggregation_category_code_26 = Column('aggregation_category_code_26', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード26')
    aggregation_category_code_27 = Column('aggregation_category_code_27', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード27')
    aggregation_category_code_28 = Column('aggregation_category_code_28', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード28')
    aggregation_category_code_29 = Column('aggregation_category_code_29', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード29')
    aggregation_category_code_30 = Column('aggregation_category_code_30', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード30')
    aggregation_category_code_31 = Column('aggregation_category_code_31', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード31')
    aggregation_category_code_32 = Column('aggregation_category_code_32', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード32')
    aggregation_category_code_33 = Column('aggregation_category_code_33', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード33')
    aggregation_category_code_34 = Column('aggregation_category_code_34', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード34')
    aggregation_category_code_35 = Column('aggregation_category_code_35', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード35')
    aggregation_category_code_36 = Column('aggregation_category_code_36', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード36')
    aggregation_category_code_37 = Column('aggregation_category_code_37', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード37')
    aggregation_category_code_38 = Column('aggregation_category_code_38', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード38')
    aggregation_category_code_39 = Column('aggregation_category_code_39', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード39')
    aggregation_category_code_40 = Column('aggregation_category_code_40', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード40')
    aggregation_category_code_41 = Column('aggregation_category_code_41', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード41')
    aggregation_category_code_42 = Column('aggregation_category_code_42', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード42')
    aggregation_category_code_43 = Column('aggregation_category_code_43', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード43')
    aggregation_category_code_44 = Column('aggregation_category_code_44', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード44')
    aggregation_category_code_45 = Column('aggregation_category_code_45', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード45')
    aggregation_category_code_46 = Column('aggregation_category_code_46', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード46')
    aggregation_category_code_47 = Column('aggregation_category_code_47', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード47')
    aggregation_category_code_48 = Column('aggregation_category_code_48', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード48')
    aggregation_category_code_49 = Column('aggregation_category_code_49', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード49')
    aggregation_category_code_50 = Column('aggregation_category_code_50', String(50, collation='ja_JP.utf8'), nullable=True, comment='集計区分コード50')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_third_party_payroll_app_layout', "company_code", "third_party_payroll_layout_code"), Index('ix_m_third_party_payroll_app_layout_1', "company_code"), UniqueConstraint("company_code", "third_party_payroll_layout_code"),)

class ShiftSchedule(Base):
    """
    シフトスケジュールマスタ
    """
    __tablename__ = "m_shift_schedule"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    sales_plan = Column('sales_plan', Integer, nullable=True, comment='売上計画')
    gross_profit_plan = Column('gross_profit_plan', DECIMAL(4, 1), nullable=True, comment='粗利計画')
    personnel_cost_plan = Column('personnel_cost_plan', Integer, nullable=True, comment='人件費計画')
    planned_labor_cost = Column('planned_labor_cost', Integer, nullable=True, comment='予定人件費')
    planned_gross_profit = Column('planned_gross_profit', DECIMAL(4, 1), nullable=True, comment='予定粗利')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_shift_schedule', "company_code", "office_code", "target_date"), Index('ix_m_shift_schedule_1', "company_code"), UniqueConstraint("company_code", "office_code", "target_date"), {'extend_existing': True})


class ShiftScheduleDetail(Base):
    """
    シフトスケジュール詳細マスタ
    """
    __tablename__ = "m_shift_schedule_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    required_number_of_people = Column('required_number_of_people', Integer, nullable=False, comment='必要人数')
    unit_price = Column('unit_price', Integer, nullable=True, comment='単価')
    adjustment_for_added_line_flag = Column('adjustment_for_added_line_flag', Boolean, nullable=False, comment='調整で追加した行フラグ')
    logical_deletion = Column('logical_deletion', Boolean, nullable=False, comment='論理削除フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_shift_schedule_detail', "company_code", "office_code", "target_date", "business_type", "work_schedule_code"), Index('ix_m_shift_schedule_detail_1', "company_code"), UniqueConstraint("company_code", "office_code", "target_date", "business_type", "work_schedule_code"), {'extend_existing': True})


class CompanyNavigationDetail(Base):
    """
    会社別ナビゲーション詳細マスタ
    """
    __tablename__ = "m_company_navigation_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    navigation_code = Column('navigation_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='ナビゲーションコード')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    before_screen_code = Column('before_screen_code', String(6, collation='ja_JP.utf8'), nullable=True, comment='直前の画面コード')
    registered_flag = Column('registered_flag', Boolean, nullable=False, comment='登録済フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company_navigation_detail', "company_code", "navigation_code", "screen_code", "before_screen_code"), Index('ix_m_company_navigation_detail_1', "company_code"), UniqueConstraint("company_code", "navigation_code", "screen_code", "before_screen_code"))


class CompanyWorkType(Base):
    """
    会社別作業種別マスタ
    """
    __tablename__ = "m_company_work_type"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    work_type = Column('work_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業種別コード')
    work_type_name = Column('work_type_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='作業種別名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company_work_type', "company_code", "work_type"), Index('ix_m_company_work_type_1', "company_code"), UniqueConstraint("company_code", "work_type"), )


class CompanyWorkPhaseLargeClassification(Base):
    """
    会社別作業フェーズ[大分類]マスタ
    """
    __tablename__ = "m_company_work_phase_large_classification"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    work_type = Column('work_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業種別コード')
    work_phase_large_classification_code = Column('work_phase_large_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ大分類コード')
    work_phase_large_classification_name = Column('work_phase_large_classification_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ大分類名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company_work_phase_large_classification', "company_code", "work_type", "work_phase_large_classification_code"), Index('ix_m_company_work_phase_large_classification_1', "company_code"), UniqueConstraint("company_code", "work_type", "work_phase_large_classification_code"), )


class CompanyWorkPhaseMiddleClassification(Base):
    """
    会社別作業フェーズ[中分類]マスタ
    """
    __tablename__ = "m_company_work_phase_middle_classification"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    work_type = Column('work_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業種別コード')
    work_phase_large_classification_code = Column('work_phase_large_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ大分類コード')
    work_phase_middle_classification_code = Column('work_phase_middle_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ中分類コード')
    work_phase_middle_classification_name = Column('work_phase_middle_classification_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ中分類名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company_work_phase_middle_classification', "company_code", "work_type", "work_phase_large_classification_code", "work_phase_middle_classification_code"), Index('ix_m_company_work_phase_middle_classification_1', "company_code"), UniqueConstraint("company_code", "work_type", "work_phase_large_classification_code", "work_phase_middle_classification_code"), )


class CompanyWorkPhaseSmallClassification(Base):
    """
    会社別作業フェーズ[小分類]マスタ
    """
    __tablename__ = "m_company_work_phase_small_classification"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    work_type = Column('work_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業種別コード')
    work_phase_large_classification_code = Column('work_phase_large_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ大分類コード')
    work_phase_middle_classification_code = Column('work_phase_middle_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ中分類コード')
    work_phase_small_classification_code = Column('work_phase_small_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ小分類コード')
    work_phase_small_classification_name = Column('work_phase_small_classification_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='作業フェーズ小分類名')
    labor_cost_category = Column('labor_cost_category', EnumType(enum_class=LaborCostCategory), nullable=False, comment='労務費区分')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_company_work_phase_small_classification', "company_code", "work_type", "work_phase_large_classification_code", "work_phase_middle_classification_code", "work_phase_small_classification_code"), Index('ix_m_company_work_phase_small_classification_1', "company_code"), UniqueConstraint("company_code", "work_type", "work_phase_large_classification_code", "work_phase_middle_classification_code", "work_phase_small_classification_code"), )


class Customer(Base):
    """
    取引先マスタ
    """
    __tablename__ = "m_customer"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    client_code = Column('client_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='取引先コード')
    client_name = Column('client_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='取引先名')
    client_japanese_name = Column('client_japanese_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='取引先名(カナ)')
    client_english_name = Column('client_english_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='取引先名(英字)')
    client_name_abbreviation = Column('client_name_abbreviation', String(4, collation='ja_JP.utf8'), nullable=False, comment='取引先名(略名)')
    transaction_start_date = Column('transaction_start_date', Date, nullable=True, comment='取引開始日')
    transaction_end_date = Column('transaction_end_date', Date, nullable=True, comment='取引終了日')
    transaction_type = Column('transaction_type', EnumType(enum_class=TransactionType), nullable=True, comment='取引区分')
    billing_unit = Column('billing_unit', EnumType(enum_class=BillingUnit), nullable=True, comment='請求単位')
    tax_pass_through_classification = Column('tax_pass_through_classification', EnumType(enum_class=TaxPassThroughClassification), nullable=True, comment='税転嫁区分')
    credit_evaluation_method = Column('credit_evaluation_method', EnumType(enum_class=CreditEvaluationMethod), nullable=True, comment='与信計算方法')
    can_be_translated_to_english_as_credit_limit = Column('can_be_translated_to_english_as_credit_limit', Integer, nullable=True, comment='与信限度額')
    closing_date_unit = Column('closing_date_unit', Integer, nullable=True, comment='締日')
    payment_date_unit = Column('payment_date_unit', EnumType(enum_class=PaymentDateUnit), nullable=True, comment='入金日単位')
    deposit_day = Column('deposit_day', Integer, nullable=True, comment='入金日')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=True, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=True, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='電話番号')
    fax = Column('fax', String(20, collation='ja_JP.utf8'), nullable=True, comment='ファックス番号')
    responsible_employee_code = Column('responsible_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='従業員番号[担当]')
    honorific = Column('honorific', EnumType(enum_class=Honorific), nullable=True, comment='敬称')
    contents = Column('contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_customer', "company_code", "client_code"), Index('ix_m_customer_1', "company_code"), Index('ix_m_customer_2', "client_code"), UniqueConstraint("company_code", "client_code"), )


class CustomerDepartment(Base):
    """
    取引先部門マスタ
    """
    __tablename__ = "m_customer_department"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    client_code = Column('client_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='取引先コード')
    department_code = Column('department_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='部門コード')
    department_name = Column('department_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='部門名')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=True, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=True, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='電話番号')
    fax = Column('fax', String(20, collation='ja_JP.utf8'), nullable=True, comment='ファックス番号')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='メールアドレス')
    position = Column('position', String(10, collation='ja_JP.utf8'), nullable=True, comment='役職')
    customer_contact_name = Column('customer_contact_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='担当者名')
    responsible_employee_code = Column('responsible_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='従業員番号[担当]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_customer_department', "company_code", "client_code", "department_code"), Index('ix_m_customer_department_1', "company_code"), UniqueConstraint("company_code", "client_code", "department_code"), )


class Supplier(Base):
    """
    仕入先マスタ
    """
    __tablename__ = "m_supplier"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    supplier_code = Column('supplier_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='弁当業者コード')
    supplier_name = Column('supplier_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='弁当業者名')
    supplier_japanese_name = Column('supplier_japanese_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='仕入先名(カナ)')
    supplier_english_name = Column('supplier_english_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='仕入先名(英字)')
    supplier_name_abbreviation = Column('supplier_name_abbreviation', String(4, collation='ja_JP.utf8'), nullable=False, comment='仕入先名(略名)')
    transaction_start_date = Column('transaction_start_date', Date, nullable=False, comment='取引開始日')
    transaction_end_date = Column('transaction_end_date', Date, nullable=True, comment='取引終了日')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=True, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=True, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='電話番号')
    fax = Column('fax', String(20, collation='ja_JP.utf8'), nullable=True, comment='ファックス番号')
    responsible_employee_code = Column('responsible_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='従業員番号[担当]')
    honorific = Column('honorific', EnumType(enum_class=Honorific), nullable=True, comment='敬称')
    contents = Column('contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_supplier', "company_code", "supplier_code"), Index('ix_m_supplier_1', "company_code"), Index('ix_m_supplier_2', "supplier_code"), UniqueConstraint("company_code", "supplier_code"), )


class SupplierDepartment(Base):
    """
    仕入先部門マスタ
    """
    __tablename__ = "m_supplier_department"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    supplier_code = Column('supplier_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='弁当業者コード')
    department_code = Column('department_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='部門コード')
    department_name = Column('department_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='部門名')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=True, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=True, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='電話番号')
    fax = Column('fax', String(20, collation='ja_JP.utf8'), nullable=True, comment='ファックス番号')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='メールアドレス')
    position = Column('position', String(10, collation='ja_JP.utf8'), nullable=True, comment='役職')
    customer_contact_name = Column('customer_contact_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='担当者名')
    responsible_employee_code = Column('responsible_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='従業員番号[担当]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_supplier_department', "company_code", "supplier_code", "department_code"), Index('ix_m_supplier_department_1', "company_code"), UniqueConstraint("company_code", "supplier_code", "department_code"), )


class Product(Base):
    """
    品名マスタ
    """
    __tablename__ = "m_product"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    product_code = Column('product_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='品名コード')
    product_name = Column('product_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='品名')
    product_japanese_name = Column('product_japanese_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='品名(カナ)')
    product_english_name = Column('product_english_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='品名(英字)')
    start_of_handling_date = Column('start_of_handling_date', Date, nullable=False, comment='取扱開始日')
    end_of_handling_date = Column('end_of_handling_date', Date, nullable=True, comment='取扱終了日')
    unit_price = Column('unit_price', Integer, nullable=True, comment='単価')
    quantity = Column('quantity', Integer, nullable=True, comment='個数')
    product_item_unit = Column('product_item_unit', EnumType(enum_class=ProductItemUnit), nullable=True, comment='品名単位')
    product_item_unit_name = Column('product_item_unit_name', String(20, collation='ja_JP.utf8'), nullable=True, comment='品名単位[任意]')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    tax_type = Column('tax_type', EnumType(enum_class=TaxType), nullable=True, comment='税種別')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_product', "company_code", "product_code"), Index('ix_m_product_1', "company_code"), UniqueConstraint("company_code", "product_code"), )


class Quotation(Base):
    """
    見積もりトラン
    """
    __tablename__ = "t_quotation"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    request_quote_number = Column('request_quote_number', Integer, nullable=True, comment='見積り番号')
    client_code = Column('client_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='取引先コード')
    honorific = Column('honorific', EnumType(enum_class=Honorific), nullable=True, comment='敬称')
    issue_date = Column('issue_date', Date, nullable=False, comment='発行日')
    request_quote_term_to = Column('request_quote_term_to', Date, nullable=True, comment='見積もり有効期限')
    subject = Column('subject', String(255, collation='ja_JP.utf8'), nullable=False, comment='件名')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    report_code = Column('report_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='帳票コード')
    rounding_off_for_each_line_item = Column('rounding_off_for_each_line_item', EnumType(enum_class=RoundingOffForEachLineItem), nullable=False, comment='明細毎の端数処理')
    rounding_of_consumption_tax = Column('rounding_of_consumption_tax', EnumType(enum_class=RoundingOfConsumptionTax), nullable=False, comment='消費税の端数処理')
    tax_inclusive_exclusive = Column('tax_inclusive_exclusive', EnumType(enum_class=TaxInclusiveExclusive), nullable=False, comment='消費税[内税/外税]')
    subtotal = Column('subtotal', Integer, nullable=False, comment='小計')
    consumption_tax = Column('consumption_tax', Integer, nullable=False, comment='消費税')
    total = Column('total', Integer, nullable=False, comment='合計')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='従業員番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_quotation', "company_code", "request_quote_number"), Index('ix_t_quotation_1', "company_code"), UniqueConstraint("company_code", "request_quote_number"), )


class QuotationDetail(Base):
    """
    見積もり明細トラン
    """
    __tablename__ = "t_quotation_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    request_quote_number = Column('request_quote_number', Integer, nullable=True, comment='見積り番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    client_code = Column('client_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='取引先コード')
    product_code = Column('product_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='品名コード')
    product_name = Column('product_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='品名')
    unit_price = Column('unit_price', Integer, nullable=False, comment='単価')
    quantity = Column('quantity', Integer, nullable=True, comment='個数')
    tax_type = Column('tax_type', EnumType(enum_class=TaxType), nullable=False, comment='税種別')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_quotation_detail_detail', "company_code", "request_quote_number", "serial_number"), Index('ix_t_quotation_detail_detail_1', "company_code"), UniqueConstraint("company_code", "request_quote_number", "serial_number"), )


class OrderReceived(Base):
    """
    受注マスタ
    """
    __tablename__ = "m_order_received"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    order_number = Column('order_number', Integer, nullable=False, comment='受注番号')
    request_quote_number = Column('request_quote_number', Integer, nullable=True, comment='見積り番号')
    order_amount = Column('order_amount', Integer, nullable=False, comment='受注金額')
    scheduled_finalacceptance_date = Column('scheduled_finalacceptance_date', Date, nullable=False, comment='最終検収予定日')
    planned_cost = Column('planned_cost', Integer, nullable=True, comment='予定原価')
    planned_gross_profit = Column('planned_gross_profit', Integer, nullable=True, comment='予定粗利')
    actual_cost = Column('actual_cost', Integer, nullable=True, comment='実績原価')
    actual_gross_profit = Column('actual_gross_profit', Integer, nullable=True, comment='実績粗利')
    sales_employee_code = Column('sales_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='営業担当従業員番号')
    project_manager_employee_code = Column('project_manager_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='PM担当従業員番号')
    project_code = Column('project_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='プロジェクトコード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_order_received', "company_code", "order_number"), Index('ix_m_order_received_1', "company_code"), UniqueConstraint("company_code", "order_number"), )


class Invoice(Base):
    """
    請求書トラン
    """
    __tablename__ = "t_invoice"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    invoice_number = Column('invoice_number', Integer, nullable=True, comment='請求番号')
    order_number = Column('order_number', Integer, nullable=False, comment='受注番号')
    client_code = Column('client_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='取引先コード')
    honorific = Column('honorific', EnumType(enum_class=Honorific), nullable=True, comment='敬称')
    billing_date = Column('billing_date', Date, nullable=False, comment='請求日')
    payment_due_date = Column('payment_due_date', Date, nullable=True, comment='支払い期限')
    subject = Column('subject', String(255, collation='ja_JP.utf8'), nullable=False, comment='件名')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    report_code = Column('report_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='帳票コード')
    rounding_off_for_each_line_item = Column('rounding_off_for_each_line_item', EnumType(enum_class=RoundingOffForEachLineItem), nullable=False, comment='明細毎の端数処理')
    rounding_of_consumption_tax = Column('rounding_of_consumption_tax', EnumType(enum_class=RoundingOfConsumptionTax), nullable=False, comment='消費税の端数処理')
    tax_inclusive_exclusive = Column('tax_inclusive_exclusive', EnumType(enum_class=TaxInclusiveExclusive), nullable=False, comment='消費税[内税/外税]')
    subtotal = Column('subtotal', Integer, nullable=False, comment='小計')
    consumption_tax = Column('consumption_tax', Integer, nullable=False, comment='消費税')
    total = Column('total', Integer, nullable=False, comment='合計')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='従業員番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_invoice', "company_code", "invoice_number"), Index('ix_t_invoice_1', "company_code"), UniqueConstraint("company_code", "invoice_number"), )


class InvoiceDetail(Base):
    """
    請求書明細トラン
    """
    __tablename__ = "t_invoice_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    invoice_number = Column('invoice_number', Integer, nullable=True, comment='請求番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    client_code = Column('client_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='取引先コード')
    product_code = Column('product_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='品名コード')
    product_name = Column('product_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='品名')
    unit_price = Column('unit_price', Integer, nullable=False, comment='単価')
    quantity = Column('quantity', Integer, nullable=True, comment='個数')
    tax_type = Column('tax_type', EnumType(enum_class=TaxType), nullable=False, comment='税種別')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_invoice_detail', "company_code", "invoice_number", "serial_number"), Index('ix_t_invoice_detail_1', "company_code"), UniqueConstraint("company_code", "invoice_number", "serial_number"), )


class SalesRevenue(Base):
    """
    売上マスタ
    """
    __tablename__ = "m_sales_revenue"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    sales_target_date = Column('sales_target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='売上年月')
    amount_of_sales = Column('amount_of_sales', Integer, nullable=False, comment='売上高')
    actual_cost = Column('actual_cost', Integer, nullable=True, comment='実績原価')
    operating_income = Column('operating_income', Integer, nullable=True, comment='営業利益')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_sales_revenue', "company_code", "sales_target_date"), Index('ix_m_sales_revenue_1', "company_code"), UniqueConstraint("company_code", "sales_target_date"), )


class PaymentAllocation(Base):
    """
    入金消込トラン
    """
    __tablename__ = "t_payment_allocation"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    invoice_number = Column('invoice_number', Integer, nullable=True, comment='請求番号')
    billing_amount = Column('billing_amount', Integer, nullable=False, comment='請求額')
    deposit_amount = Column('deposit_amount', Integer, nullable=False, comment='入金額')
    balance = Column('balance', Integer, nullable=False, comment='残高')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    deposited_flag = Column('deposited_flag', Boolean, nullable=False, comment='入金済フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_payment_allocation', "company_code", "invoice_number"), Index('ix_t_payment_allocation_1', "company_code"), UniqueConstraint("company_code", "invoice_number"), )


class PaymentAllocationRelation(Base):
    """
    入金消込-入金関連トラン
    """
    __tablename__ = "t_payment_allocation_relation"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    invoice_number = Column('invoice_number', Integer, nullable=True, comment='請求番号')
    client_code = Column('client_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='取引先コード')
    deposit_date = Column('deposit_date', Date, nullable=False, comment='入金日')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    allocated_amount = Column('allocated_amount', Integer, nullable=False, comment='消込額')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_payment_allocation_relation', "company_code", "invoice_number", "client_code", "deposit_date", "serial_number"), Index('ix_t_payment_allocation_relation_1', "company_code"), UniqueConstraint("company_code", "invoice_number", "client_code", "deposit_date", "serial_number"), )


class BilledAmountPaid(Base):
    """
    請求額入金トラン
    """
    __tablename__ = "t_billed_amount_paid"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    client_code = Column('client_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='取引先コード')
    deposit_date = Column('deposit_date', Date, nullable=False, comment='入金日')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    deposit_amount = Column('deposit_amount', Integer, nullable=False, comment='入金額')
    payment_method = Column('payment_method', EnumType(enum_class=PaymentMethod), nullable=False, comment='支給方法')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    depospayment_allocation_flag = Column('depospayment_allocation_flag', Boolean, nullable=False, comment='入金消込フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_billed_amount_paid', "company_code", "client_code", "deposit_date", "serial_number"), Index('ix_t_billed_amount_paid_1', "company_code"), UniqueConstraint("company_code", "client_code", "deposit_date", "serial_number"), )


class Receipt(Base):
    """
    領収証トラン
    """
    __tablename__ = "t_receipt"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    client_code = Column('client_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='取引先コード')
    deposit_date = Column('deposit_date', Date, nullable=False, comment='入金日')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    issue_date = Column('issue_date', Date, nullable=False, comment='発行日')
    invoice_number = Column('invoice_number', Integer, nullable=True, comment='請求番号')
    subject = Column('subject', String(255, collation='ja_JP.utf8'), nullable=False, comment='件名')
    honorific = Column('honorific', EnumType(enum_class=Honorific), nullable=True, comment='敬称')
    billing_date = Column('billing_date', Date, nullable=False, comment='請求日')
    deposit_amount = Column('deposit_amount', Integer, nullable=False, comment='入金額')
    report_code = Column('report_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='帳票コード')
    subtotal = Column('subtotal', Integer, nullable=False, comment='小計')
    consumption_tax = Column('consumption_tax', Integer, nullable=False, comment='消費税')
    total = Column('total', Integer, nullable=False, comment='合計')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='従業員番号')
    order_number = Column('order_number', Integer, nullable=False, comment='受注番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_receipt', "company_code", "client_code", "deposit_date", "serial_number"), Index('ix_t_receipt_1', "company_code"), UniqueConstraint("company_code", "client_code", "deposit_date", "serial_number"), )


class ErrorLog(Base):
    """
    エラーログトラン
    """
    __tablename__ = "t_error_log"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='会社コード')
    message = Column('message', Text, nullable=False, comment='メッセージ')
    request_json = Column('request_json', Text, nullable=True, comment='request_json')
    exception = Column('exception', Text, nullable=True, comment='例外')
    traceback = Column('traceback', Text, nullable=True, comment='traceback')
    notice_date = Column('notice_date', TIMESTAMP, nullable=False, comment='お知らせ発生日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_error_log', "company_code", "notice_date"), Index('ix_t_error_log_1', "company_code"), UniqueConstraint("company_code", "notice_date"), )


class Payment(Base):
    """
    入金トラン
    """
    __tablename__ = "t_payment"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    trading_day = Column('trading_day', Date, nullable=False, comment='取引日')
    billing_amount = Column('billing_amount', Integer, nullable=False, comment='請求額')
    deposit_amount = Column('deposit_amount', Integer, nullable=False, comment='入金額')
    deposited_flag = Column('deposited_flag', Boolean, nullable=False, comment='入金済フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_payment', "company_code", "trading_day"), Index('ix_t_payment_1', "company_code"), UniqueConstraint("company_code", "trading_day"), )


class Journal(Base):
    """
    仕訳トラン
    """
    __tablename__ = "t_journal"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    target_date = Column('target_date', String(9, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    salary_bonus_classification = Column('salary_bonus_classification', EnumType(enum_class=SalaryBonusClassification), nullable=False, comment='支給区分')
    trading_number = Column('trading_number', Integer, nullable=False, comment='取引No')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    salary_closing_code = Column('salary_closing_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='給与締日コード')
    trading_day = Column('trading_day', Date, nullable=False, comment='取引日')
    account_code = Column('account_code', String(4, collation='ja_JP.utf8'), nullable=True, comment='勘定科目コード')
    sub_account_code = Column('sub_account_code', String(4, collation='ja_JP.utf8'), nullable=True, comment='補助勘定科目コード')
    tax_type = Column('tax_type', EnumType(enum_class=TaxType), nullable=True, comment='税種別')
    department = Column('department', String(20, collation='ja_JP.utf8'), nullable=True, comment='部門')
    partner_account_code = Column('partner_account_code', String(4, collation='ja_JP.utf8'), nullable=True, comment='相手勘定科目コード')
    partner_sub_account_code = Column('partner_sub_account_code', String(4, collation='ja_JP.utf8'), nullable=True, comment='相手補助勘定科目コード')
    partner_tax_type = Column('partner_tax_type', EnumType(enum_class=TaxType), nullable=True, comment='相手税種別')
    partner_department = Column('partner_department', String(20, collation='ja_JP.utf8'), nullable=True, comment='相手部門')
    description = Column('description', String(50, collation='ja_JP.utf8'), nullable=True, comment='摘要')
    debit_amount = Column('debit_amount', Integer, nullable=False, comment='借方金額')
    credit_amount = Column('credit_amount', Integer, nullable=False, comment='貸方金額')
    balance = Column('balance', Integer, nullable=False, comment='残高')
    memo = Column('memo', String(50, collation='ja_JP.utf8'), nullable=True, comment='メモ')
    tag = Column('tag', String(50, collation='ja_JP.utf8'), nullable=True, comment='タグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_journal', "company_code", "target_date", "salary_bonus_classification", "trading_number", "serial_number"), Index('ix_t_journal_1', "company_code"), UniqueConstraint("company_code", "target_date", "salary_bonus_classification", "trading_number", "serial_number"), )


class JournalEmployee(Base):
    """
    従業員別仕訳トラン
    """
    __tablename__ = "t_journal_employee"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    employee_name = Column('employee_name', String(30, collation='ja_JP.utf8'), nullable=True, comment='氏名')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    salary_bonus_classification = Column('salary_bonus_classification', EnumType(enum_class=SalaryBonusClassification), nullable=False, comment='支給区分')
    trading_number = Column('trading_number', Integer, nullable=False, comment='取引No')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    salary_closing_code = Column('salary_closing_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='給与締日コード')
    trading_day = Column('trading_day', Date, nullable=False, comment='取引日')
    account_code = Column('account_code', String(4, collation='ja_JP.utf8'), nullable=True, comment='勘定科目コード')
    sub_account_code = Column('sub_account_code', String(4, collation='ja_JP.utf8'), nullable=True, comment='補助勘定科目コード')
    tax_type = Column('tax_type', EnumType(enum_class=TaxType), nullable=True, comment='税種別')
    department = Column('department', String(20, collation='ja_JP.utf8'), nullable=True, comment='部門')
    partner_account_code = Column('partner_account_code', String(4, collation='ja_JP.utf8'), nullable=True, comment='相手勘定科目コード')
    partner_sub_account_code = Column('partner_sub_account_code', String(4, collation='ja_JP.utf8'), nullable=True, comment='相手補助勘定科目コード')
    partner_tax_type = Column('partner_tax_type', EnumType(enum_class=TaxType), nullable=True, comment='相手税種別')
    partner_department = Column('partner_department', String(20, collation='ja_JP.utf8'), nullable=True, comment='相手部門')
    description = Column('description', String(50, collation='ja_JP.utf8'), nullable=True, comment='摘要')
    debit_amount = Column('debit_amount', Integer, nullable=False, comment='借方金額')
    credit_amount = Column('credit_amount', Integer, nullable=False, comment='貸方金額')
    balance = Column('balance', Integer, nullable=False, comment='残高')
    memo = Column('memo', String(50, collation='ja_JP.utf8'), nullable=True, comment='メモ')
    tag = Column('tag', String(50, collation='ja_JP.utf8'), nullable=True, comment='タグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_journal_employee', "company_code", "employee_code", "target_date", "salary_bonus_classification", "trading_number", "serial_number"), Index('ix_t_journal_employee_1', "company_code"), UniqueConstraint("company_code", "employee_code", "target_date", "salary_bonus_classification", "trading_number", "serial_number"), )


class ClosingYearResult(Base):
    """
    勤怠締年トラン
    """
    __tablename__ = "t_closing_year_result"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    closing_code = Column('closing_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='締日コード')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    is_close = Column('is_close', EnumType(enum_class=IsClose), nullable=False, comment='締め処理済')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_closing_year_result', "company_code", "closing_code", "target_date"), Index('ix_t_closing_year_result_1', "company_code"), UniqueConstraint("company_code", "closing_code", "target_date"), )


class ClosingDateResult(Base):
    """
    勤怠締月トラン
    """
    __tablename__ = "t_closing_date_result"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    closing_code = Column('closing_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='締日コード')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    jan = Column('jan', EnumType(enum_class=IsClose), nullable=False, comment='1月の締め')
    feb = Column('feb', EnumType(enum_class=IsClose), nullable=False, comment='2月の締め')
    mar = Column('mar', EnumType(enum_class=IsClose), nullable=False, comment='3月の締め')
    apl = Column('apl', EnumType(enum_class=IsClose), nullable=False, comment='APIコード')
    may = Column('may', EnumType(enum_class=IsClose), nullable=False, comment='5月の締め')
    jun = Column('jun', EnumType(enum_class=IsClose), nullable=False, comment='6月の締め')
    jly = Column('jly', EnumType(enum_class=IsClose), nullable=False, comment='7月の締め')
    aug = Column('aug', EnumType(enum_class=IsClose), nullable=False, comment='8月の締め')
    sep = Column('sep', EnumType(enum_class=IsClose), nullable=False, comment='9月の締め')
    oct = Column('oct', EnumType(enum_class=IsClose), nullable=False, comment='10月の締め')
    nov = Column('nov', EnumType(enum_class=IsClose), nullable=False, comment='11月の締め')
    dec = Column('dec', EnumType(enum_class=IsClose), nullable=False, comment='12月の締め')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_closing_date_result', "company_code", "closing_code", "target_date"), Index('ix_t_closing_date_result_1', "company_code"), UniqueConstraint("company_code", "closing_code", "target_date"), )


class Employee(Base):
    """
    従業員マスタ
    """
    __tablename__ = "m_employee"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    employee_name = Column('employee_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='氏名')
    pseudonym_reading = Column('pseudonym_reading', String(50, collation='ja_JP.utf8'), nullable=True, comment='氏名（ふりがな）')
    employee_classification_code = Column('employee_classification_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員区分')
    recruitment_category_code = Column('recruitment_category_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='採用区分')
    language = Column('language', String(3, collation='ja_JP.utf8'), nullable=False, comment='言語')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=True, comment='添付ファイルのパス')
    wall_paper_append_path = Column('wall_paper_append_path', String(255, collation='ja_JP.utf8'), nullable=True, comment='壁紙のパス')
    hire_date = Column('hire_date', Date, nullable=False, comment='入社年月日')
    retirement_date = Column('retirement_date', Date, nullable=True, comment='退社年月日')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='メールアドレス')
    sex = Column('sex', EnumType(enum_class=Sex), nullable=False, comment='性別')
    birthday = Column('birthday', Date, nullable=True, comment='生年月日')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='電話番号')
    extension_number = Column('extension_number', String(5, collation='ja_JP.utf8'), nullable=True, comment='内線番号')
    contract_renewal_date = Column('contract_renewal_date', Date, nullable=True, comment='契約更新日')
    attendance_management = Column('attendance_management', EnumType(enum_class=AttendanceManagement), nullable=False, comment='労働管理')
    payroll_management = Column('payroll_management', EnumType(enum_class=PayrollManagement), nullable=False, comment='賃金管理')
    paid_leave_payment = Column('paid_leave_payment', EnumType(enum_class=PaidLeavePayment), nullable=False, comment='有給休暇')
    paid_reference_date = Column('paid_reference_date', Date, nullable=True, comment='次回有給付与日')
    estimated_months_of_service = Column('estimated_months_of_service', Integer, nullable=True, comment='次回予定勤続月数')
    available_in_one_year = Column('available_in_one_year', Integer, nullable=True, comment='一年間で取得可能な時間有給日数')
    availability = Column('availability', EnumType(enum_class=Availability), nullable=False, comment='アカウント利用')
    number_of_working_days_per_week = Column('number_of_working_days_per_week', Integer, nullable=False, comment='週の労働日数')
    feliCa = Column('feliCa', String(16, collation='ja_JP.utf8'), nullable=True, comment='FeliCa')
    my_number = Column('my_number', String(12, collation='ja_JP.utf8'), nullable=True, comment='マイナンバー')
    estimated_overtime_hours = Column('estimated_overtime_hours', Integer, nullable=True, comment='見込み残業時間')
    salary_category = Column('salary_category', EnumType(enum_class=SalaryCategory), nullable=True, comment='給与区分')
    layout_code = Column('layout_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='レイアウトコード')
    unit_price = Column('unit_price', Integer, nullable=True, comment='単価')
    is_visible = Column('is_visible', EnumType(enum_class=IsVisible), nullable=False, comment='パートナー参照可否')
    white_collar_exemption = Column('white_collar_exemption', Boolean, nullable=True, comment='高度プロフェッショナル制度対象者')
    google_token = Column('google_token', String(255, collation='ja_JP.utf8'), nullable=True, comment='googleカレンダー用トークン')
    color_pattern = Column('color_pattern', EnumType(enum_class=ColorPattern), nullable=True, comment='カラーパターン')
    face_data = Column('face_data', String(255, collation='ja_JP.utf8'), nullable=True, comment='顔認証データ')
    logical_deletion = Column('logical_deletion', Boolean, nullable=False, comment='論理削除フラグ')
    attendance_status = Column('attendance_status', EnumType(enum_class=AttendanceStatus), nullable=True, comment='出勤状況')
    is_shift_work = Column('is_shift_work', EnumType(enum_class=IsShiftWork), nullable=True, comment='シフト利用有無')
    memo = Column('memo', String(255, collation='ja_JP.utf8'), nullable=True, comment='メモ')
    opt_in_flg = Column('opt_in_flg', Integer, nullable=True, comment='オプトインフラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee', "company_code", "employee_code"), Index('ix_m_employee_1', "company_code"), Index('ix_m_employee_2', "employee_code"), UniqueConstraint("company_code", "employee_code"), {'extend_existing': True})


class EmployeeUseTab(Base):
    """
    従業員利用タブマスタ
    """
    __tablename__ = "m_employee_use_tab"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    tab_code = Column('tab_code', String(1, collation='ja_JP.utf8'), nullable=False, comment='タブコード')
    is_use = Column('is_use', Boolean, nullable=False, comment='使用有無')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_use_tab', "company_code", "employee_code", "tab_code"), Index('ix_m_employee_use_tab_1', "company_code"), Index('ix_m_employee_use_tab_1_2', "employee_code"), Index('ix_m_employee_use_tab_1_3', "tab_code"), UniqueConstraint("company_code", "employee_code", "tab_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeResidentialStatus(Base):
    """
    従業員在留資格マスタ
    """
    __tablename__ = "m_employee_residential_status"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    residential_number = Column('residential_number', String(12, collation='ja_JP.utf8'), nullable=False, comment='在留カード等番号')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    residential_status = Column('residential_status', EnumType(enum_class=ResidentialStatus), nullable=False, comment='在留資格')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_residential_status', "company_code", "employee_code", "residential_number", "term_to"), Index('ix_m_employee_residential_statu_1', "company_code"), Index('ix_m_employee_residential_statu_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "residential_number", "term_to"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeRounding(Base):
    """
    従業員労働時間丸めマスタ
    """
    __tablename__ = "m_employee_rounding"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    rounding_type = Column('rounding_type', EnumType(enum_class=RoundingType), nullable=False, comment='労働時間[分]の丸め')
    rounding_month = Column('rounding_month', EnumType(enum_class=RoundingMonth), nullable=True, comment='労働時間の単位[分]')
    rounding_term = Column('rounding_term', Integer, nullable=False, comment='法定労働時間の単位[分]')
    rounding_term_over_work = Column('rounding_term_over_work', Integer, nullable=False, comment='法定外労働時間の単位[分]')
    rounding_job_start = Column('rounding_job_start', EnumType(enum_class=RoundingJobStart), nullable=True, comment='出勤時間')
    rounding_job_end = Column('rounding_job_end', EnumType(enum_class=RoundingJobEnd), nullable=True, comment='退勤時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_rounding', "company_code", "employee_code"), Index('ix_m_employee_rounding_1', "company_code"), Index('ix_m_employee_rounding_2', "employee_code"), UniqueConstraint("company_code", "employee_code"), {'extend_existing': True})


class Promotion(Base):
    """
    プロモーションマスタ
    """
    __tablename__ = "m_promotion"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    promotion_code = Column('promotion_code', String(10, collation='ja_JP.utf8'), comment='プロモーションコード')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    unit_price = Column('unit_price', Integer, nullable=False, comment='単価')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    is_use = Column('is_use', Boolean, nullable=False, comment='使用有無')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_promotion', "promotion_code"),)


class ArtemisAlertManagementFormat(Base):
    """
    規定アルテミスアラート管理マスタ
    """
    __tablename__ = "m_artemis_alert_management_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    role_code = Column('role_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='アクセス権コード')
    alert_junl_type = Column('alert_junl_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='アラートタイプ')
    alert_junl_type_name = Column('alert_junl_type_name', String(100, collation='ja_JP.utf8'), nullable=False, comment='アラートタイプ名')
    alert_management_control = Column('alert_management_control', EnumType(enum_class=AlertManagementControl), nullable=False, comment='アラート番号管理区分')
    alert_term = Column('alert_term', Integer, nullable=True, comment='通知の間隔')
    alert_notification_method = Column('alert_notification_method', EnumType(enum_class=AlertNotificationMethod), nullable=True, comment='アラート通知方法')
    alert_term_unit = Column('alert_term_unit', EnumType(enum_class=AlertTermUnit), nullable=True, comment='通知間隔単位')
    before_after_flag = Column('before_after_flag', EnumType(enum_class=BeforeAfterFlag), nullable=True, comment='前後区分')
    alert_code = Column('alert_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='アラートコード')
    enabled = Column('enabled', EnumType(enum_class=Availability), nullable=True, comment='有効')
    sort_number = Column('sort_number', Integer, nullable=True, comment='ソート順')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_artemis_alert_management_format', "role_code", "alert_junl_type"), UniqueConstraint("role_code", "alert_junl_type"), {'extend_existing': True})


class EmployeeArtemisAlertManagement(Base):
    """
    従業員別アルテミスアラート管理マスタ
    """
    __tablename__ = "m_employee_artemis_alert_management"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    role_code = Column('role_code', String(30, collation='ja_JP.utf8'), nullable=False, comment='アクセス権コード')
    alert_junl_type = Column('alert_junl_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='アラートタイプ')
    alert_management_control = Column('alert_management_control', EnumType(enum_class=AlertManagementControl), nullable=False, comment='アラート番号管理区分')
    alert_term = Column('alert_term', Integer, nullable=True, comment='通知の間隔')
    alert_notification_method = Column('alert_notification_method', EnumType(enum_class=AlertNotificationMethod), nullable=True, comment='アラート通知方法')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='メールアドレス')
    alert_term_unit = Column('alert_term_unit', EnumType(enum_class=AlertTermUnit), nullable=True, comment='通知間隔単位')
    before_after_flag = Column('before_after_flag', EnumType(enum_class=BeforeAfterFlag), nullable=True, comment='前後区分')
    alert_code = Column('alert_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='アラートコード')
    enabled = Column('enabled', EnumType(enum_class=Availability), nullable=True, comment='有効')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_artemis_alert_management', "company_code", "employee_code", "role_code", "alert_junl_type"), Index('ix_m_employee_artemis_alert_management_1', "company_code"), Index('ix_m_employee_artemis_alert_management_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "role_code", "alert_junl_type"), {'extend_existing': True})


class EmployeeAlertManagement(Base):
    """
    従業員アラート管理マスタ
    """
    __tablename__ = "m_employee_alert_management"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    alert_junl_management_control = Column('alert_junl_management_control', EnumType(enum_class=AlertJunlManagementControl), nullable=False, comment='アラート通知区分')
    alert_management_control = Column('alert_management_control', EnumType(enum_class=AlertManagementControl), nullable=False, comment='アラート番号管理区分')
    alert_notification_method = Column('alert_notification_method', EnumType(enum_class=AlertNotificationMethod), nullable=False, comment='アラート通知方法')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='メールアドレス')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_alert_management', "company_code", "employee_code", "alert_junl_management_control"), Index('ix_m_employee_alert_management_1', "company_code"), Index('ix_m_employee_alert_management_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "alert_junl_management_control"), {'extend_existing': True})


class Union(Base):
    """
    労働組合マスタ
    """
    __tablename__ = "m_union"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    is_term = Column('is_term', Boolean, nullable=False, comment='任期を定めて指定された委員')
    is_etc_term = Column('is_etc_term', Boolean, nullable=False, comment='その他の委員')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_union', "company_code", "office_code", "employee_code"), Index('ix_m_union_1', "company_code"), UniqueConstraint("company_code", "office_code", "employee_code"), )


class EmployeeJobTitle(Base):
    """
    従業員職名マスタ
    """
    __tablename__ = "m_employee_job_title"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    job_title_code = Column('job_title_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='役職コード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_job_title', "company_code", "employee_code", "job_title_code"), Index('ix_m_employee_job_title_1', "company_code"), Index('ix_m_employee_job_title_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "job_title_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class PaidAnnualAccountEmployee(Base):
    """
    従業員別有給支給年別勘定マスタ
    年度ごとの有給残日数、有給残時間を管理します。
    """
    __tablename__ = "m_paid_annual_account_employee"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    payment_date = Column('payment_date', Date, nullable=False, comment='支給年月日')
    payment_days = Column('payment_days', Float, nullable=False, comment='支給日数')
    payment_times = Column('payment_times', Integer, nullable=False, comment='支給時間')
    payment_reason = Column('payment_reason', EnumType(enum_class=PaidLeaveReason), nullable=False, comment='支給理由')
    expiration_date = Column('expiration_date', Date, nullable=True, comment='失効年月日')
    expiration_days = Column('expiration_days', Float, nullable=True, comment='失効日数')
    expiration_times = Column('expiration_times', Integer, nullable=True, comment='失効時間')
    expiration_reason = Column('expiration_reason', EnumType(enum_class=PaidLeaveReason), nullable=True, comment='失効理由')
    hold_days = Column('hold_days', Float, nullable=False, comment='有給残日数')
    hold_times = Column('hold_times', Integer, nullable=False, comment='有給残時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_paid_annual_account_employee', "company_code", "employee_code", "payment_date"), Index('ix_m_paid_annual_account_employee_1', "company_code"), Index('ix_m_paid_annual_account_employee_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "payment_date"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeFavoliteScreen(Base):
    """
    従業員別お気に入り画面マスタ
    """
    __tablename__ = "m_employee_favolite_screen"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    menu_code = Column('menu_code', String(3, collation='ja_JP.utf8'), ForeignKey('m_menu.menu_code', onupdate='CASCADE', ondelete='CASCADE'), comment='メニューコード')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    sort_number = Column('sort_number', Integer, nullable=False, comment='ソート順')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_favolite_screen', "company_code", "employee_code", "menu_code", "screen_code"), Index('ix_m_employee_favolite_screen_1', "company_code"), UniqueConstraint("company_code", "employee_code", "menu_code", "screen_code"), )


class EmployeeApplication(Base):
    """
    従業員申請マスタ
    """
    __tablename__ = "m_employee_application"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    employee_application_control = Column('employee_application_control', EnumType(enum_class=EmployeeApplicationControl), nullable=False, comment='従業員申請')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_application', "company_code", "employee_code", "application_form_code"), Index('ix_m_employee_application_1', "company_code"), UniqueConstraint("company_code", "employee_code", "application_form_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class Password(Base):
    """
    パスワードマスタ
    """
    __tablename__ = "m_password"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    password = Column('password', String(255, collation='ja_JP.utf8'), nullable=False, comment='パスワード')
    hint = Column('hint', String(255, collation='ja_JP.utf8'), nullable=True, comment='ヒント')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_password', "company_code", "employee_code"), Index('ix_m_password_1', "company_code"), UniqueConstraint("company_code", "employee_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeEducationalBackground(Base):
    """
    学歴マスタ
    """
    __tablename__ = "m_employee_educational_background"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    event_date = Column('event_date', Date, nullable=False, comment='年月日')
    event = Column('event', String(255, collation='ja_JP.utf8'), nullable=False, comment='学歴')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_educational_background', "company_code", "employee_code", "event_date"), Index('ix_m_employee_educational_background_1', "company_code"), Index('ix_m_employee_educational_background_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "event_date"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeSkill(Base):
    """
    スキルマスタ
    """
    __tablename__ = "m_employee_skill"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    event_date = Column('event_date', Date, nullable=False, comment='年月日')
    skill = Column('skill', String(255, collation='ja_JP.utf8'), nullable=False, comment='保有資格')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_skill', "company_code", "employee_code", "event_date"), Index('ix_m_employee_skill_1', "company_code"), Index('ix_m_employee_skill_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "event_date"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeWorkHistory(Base):
    """
    職歴マスタ
    """
    __tablename__ = "m_employee_work_history"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    event_date = Column('event_date', Date, nullable=False, comment='年月日')
    work_history = Column('work_history', String(255, collation='ja_JP.utf8'), nullable=False, comment='職歴')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_work_history', "company_code", "employee_code", "event_date"), Index('ix_m_employee_work_history_1', "company_code"), Index('ix_m_employee_work_history_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "event_date"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class Dependent(Base):
    """
    扶養家族マスタ
    """
    __tablename__ = "m_dependent"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    dependent_code = Column('dependent_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='扶養家族コード')
    dependent_name = Column('dependent_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='扶養家族名')
    pseudonym_reading = Column('pseudonym_reading', String(50, collation='ja_JP.utf8'), nullable=True, comment='氏名（ふりがな）')
    sex = Column('sex', EnumType(enum_class=Sex), nullable=False, comment='性別')
    birthday = Column('birthday', Date, nullable=False, comment='生年月日')
    relationship = Column('relationship', EnumType(enum_class=Relationship), nullable=False, comment='続柄')
    day_of_death = Column('day_of_death', Date, nullable=True, comment='死亡日')
    deductible_spouse = Column('deductible_spouse', Boolean, nullable=False, comment='配偶者控除')
    disability_classification = Column('disability_classification', EnumType(enum_class=DisabilityClassification), nullable=True, comment='障害者区分')
    living_together = Column('living_together', EnumType(enum_class=LivingTogether), nullable=False, comment='同居区分')
    dependent_relative_classification = Column('dependent_relative_classification', EnumType(enum_class=DependentRelativeClassification), nullable=False, comment='扶養親族区分')
    my_number = Column('my_number', String(12, collation='ja_JP.utf8'), nullable=True, comment='マイナンバー')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_dependent', "company_code", "employee_code", "dependent_code"), Index('ix_m_dependent_1', "company_code"), Index('ix_m_dependent_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "dependent_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class WorkerList(Base):
    """
    労働者名簿マスタ
    """
    __tablename__ = "m_worker_list"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=True, comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=True, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='電話番号')
    emergency_contact = Column('emergency_contact', String(20, collation='ja_JP.utf8'), nullable=True, comment='緊急連絡先')
    other = Column('other', String(255, collation='ja_JP.utf8'), nullable=True, comment='その他')
    reason_for_retirement = Column('reason_for_retirement', String(255, collation='ja_JP.utf8'), nullable=True, comment='退職理由')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_worker_list', "company_code", "employee_code"), Index('ix_m_worker_list_1', "company_code"), Index('ix_m_worker_list_2', "employee_code"), UniqueConstraint("company_code", "employee_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeClosing(Base):
    """
    従業員締日マスタ
    """
    __tablename__ = "m_employee_closing"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    closing_code = Column('closing_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='締日コード')
    salary_closing_code = Column('salary_closing_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='給与締日コード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_closing', "company_code", "employee_code"), Index('ix_m_employee_closing_1', "company_code"), UniqueConstraint("company_code", "employee_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeOffice(Base):
    """
    従業員事業所マスタ
    """
    __tablename__ = "m_employee_office"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_office', "company_code", "employee_code"), Index('ix_m_employee_office_1', "company_code"), Index('ix_m_employee_office_2', "employee_code"), UniqueConstraint("company_code", "employee_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeBusiness(Base):
    """
    従業員職種マスタ
    """
    __tablename__ = "m_employee_business"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_business', "company_code", "employee_code"), Index('ix_m_employee_business_1', "company_code"), Index('ix_m_employee_business_2', "employee_code"), UniqueConstraint("company_code", "employee_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeGroup(Base):
    """
    従業員部署マスタ
    """
    __tablename__ = "m_employee_group"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    group_code = Column('group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='部署コード')
    default_group_code = Column('default_group_code', EnumType(enum_class=DefaultGroupFlg), nullable=True, comment='規定部署コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    range = Column('range', EnumType(enum_class=Range), nullable=False, comment='利用権限範囲')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_group', "company_code", "employee_code", "group_code"), Index('ix_m_employee_group_1', "company_code"), Index('ix_m_employee_group_2', "employee_code"), Index('ix_m_employee_group_3', "group_code"), UniqueConstraint("company_code", "employee_code", "group_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeTeam(Base):
    """
    従業員チームマスタ
    """
    __tablename__ = "m_employee_team"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    team_code = Column('team_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='チームコード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_team', "company_code", "employee_code", "team_code"), Index('ix_m_employee_team_1', "company_code"), Index('ix_m_employee_team_2', "employee_code"), Index('ix_m_employee_team_3', "team_code"), UniqueConstraint("company_code", "employee_code", "team_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class WorkingScheduleEmployee(Base):
    """
    従業員勤務体系マスタ
    """
    __tablename__ = "m_working_schedule_employee"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    off_site_deemed_working_hours_flag = Column('off_site_deemed_working_hours_flag', Boolean, nullable=False, comment='事業場外みなし労働時間制フラグ')
    default_work_schedule_code = Column('default_work_schedule_code', EnumType(enum_class=DefaultWorkScheduleFlg), nullable=False, comment='デフォルト勤務体系フラグ')  # FLGとすべきをCODEと命名しているが修正大のため放置
    is_need_gps = Column('is_need_gps', Boolean, nullable=True, comment='GPS打刻必須')
    is_disp_late_time = Column('is_disp_late_time', Boolean, nullable=True, comment='遅刻/早退時間表示フラグ')
    logical_deletion = Column('logical_deletion', Boolean, nullable=False, comment='論理削除フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_working_schedule_employee', "company_code", "employee_code", "work_schedule_code"), Index('ix_m_working_schedule_employee_1', "company_code"), Index('ix_m_working_schedule_employee_2', "employee_code"), Index('ix_m_working_schedule_employee_3', "work_schedule_code"), UniqueConstraint("company_code", "employee_code", "work_schedule_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class DashboardEmployee(Base):
    """
    従業員別ダッシュボードマスタ
    """
    __tablename__ = "m_dashboard_employee"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    sort_number = Column('sort_number', Integer, nullable=False, comment='ソート順')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_dashboard_employee', "company_code", "employee_code", "sort_number"), Index('ix_m_dashboard_employee_1', "company_code"), UniqueConstraint("company_code", "employee_code", "sort_number"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']), {'extend_existing': True})


class Boss(Base):
    """
    上司マスタ
    """
    __tablename__ = "m_boss"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    group_code = Column('group_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='部署コード')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='申請書コード')
    boss_company_code = Column('boss_company_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='直属上司の会社コード')
    boss_group_code = Column('boss_group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='直属上司の部署コード')
    boss_employee_code = Column('boss_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='直属上司の従業員番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_boss', "company_code", "group_code", "employee_code", "application_form_code"), Index('ix_m_boss_1', "company_code"), UniqueConstraint("company_code", "group_code", "employee_code", "application_form_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class DeputyApprovel(Base):
    """
    代理承認者マスタ
    """
    __tablename__ = "m_deputy_approvel"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    group_code = Column('group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='部署コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    deputy_approverl_company_code = Column('deputy_approverl_company_code', String(10, collation='ja_JP.utf8'), comment='代理承認者の会社コード')
    deputy_approverl_group_code = Column('deputy_approverl_group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='代理承認者の部署コード')
    deputy_approverl_employee_code = Column('deputy_approverl_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='代理承認者の従業員番号')
    deputy_contents = Column('deputy_contents', String(255, collation='ja_JP.utf8'), nullable=False, comment='依頼理由')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_deputy_approvel', "company_code", "group_code", "employee_code"), Index('ix_m_deputy_approvel_1', "company_code"), UniqueConstraint("company_code", "group_code", "employee_code"), )


class EmployeeAccountsPayable(Base):
    """
    未払金マスタ
    従業員の未払金を管理します。
    """
    __tablename__ = "m_employee_accounts_payable"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    salary_deduction = Column('salary_deduction', Integer, nullable=False, comment='給与天引額')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_accounts_payable', "company_code", "employee_code", "target_date"), Index('ix_m_employee_accounts_payable_1', "company_code"), UniqueConstraint("company_code", "employee_code", "target_date"),)


class EmployeeCommute(Base):
    """
    従業員通勤費マスタ
    従業員の通勤費を管理します。
    """
    __tablename__ = "m_employee_commute"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    traffic_division = Column('traffic_division', EnumType(enum_class=TrafficDivision), nullable=False, comment='交通区分')
    distance_to_use_transportation_equipment = Column('distance_to_use_transportation_equipment', EnumType(enum_class=DistanceToUseTransportationEquipment), nullable=True, comment='交通用具を使用する距離')
    payment_unit = Column('payment_unit', EnumType(enum_class=PaymentUnit), nullable=False, comment='支給単位')
    target_month = Column('target_month', EnumType(enum_class=TargetMonth), nullable=True, comment='支給月度')
    payment_amount = Column('payment_amount', Integer, nullable=False, comment='支給額')
    transportation_name = Column('transportation_name', String(40, collation='ja_JP.utf8'), nullable=True, comment='交通機関名')
    start_section = Column('start_section', String(32, collation='ja_JP.utf8'), nullable=True, comment='開始区間')
    end_section = Column('end_section', String(32, collation='ja_JP.utf8'), nullable=True, comment='終了区間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_commute', "company_code", "employee_code", "serial_number"), Index('ix_m_employee_commute_1', "company_code"), Index('ix_m_employee_commute_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "serial_number"),)


class EmployeeTax(Base):
    """
    従業員税金マスタ
    従業員の税金を管理します。
    """
    __tablename__ = "m_employee_tax"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    local_government_code = Column('local_government_code', String(6, collation='ja_JP.utf8'), nullable=True, comment='全国地方公共団体コード')
    first_month_cost = Column('first_month_cost', Integer, nullable=True, comment='住民税　初月費用')
    costs_from_the_next_month = Column('costs_from_the_next_month', Integer, nullable=True, comment='住民税　翌月以降の費用')
    social_insurance = Column('social_insurance', EnumType(enum_class=SocialInsurance), nullable=False, comment='社会保険')
    social_insurance_date = Column('social_insurance_date', Date, nullable=True, comment='社会保険取得日')
    health_insurance_sign = Column('health_insurance_sign', String(8, collation='ja_JP.utf8'), nullable=True, comment='健康保険記号')
    health_insurance_no = Column('health_insurance_no', String(8, collation='ja_JP.utf8'), nullable=True, comment='保険者番号')
    basic_pension_number = Column('basic_pension_number', String(11, collation='ja_JP.utf8'), nullable=True, comment='基礎年金番号')
    insured_person_reference_number = Column('insured_person_reference_number', Integer, nullable=True, comment='被保険者整理番号')
    monthl_reward = Column('monthl_reward', Integer, nullable=False, comment='報酬月額')
    last_update_date_of_monthly_reward = Column('last_update_date_of_monthly_reward', Date, nullable=False, comment='報酬月額の最終更新日')
    is_long_term_care_insurance_care_category = Column('is_long_term_care_insurance_care_category', EnumType(enum_class=IsLongTermCareInsuranceTargetCategory), nullable=True, comment='介護保険')
    pension_fund_contributions = Column('pension_fund_contributions', EnumType(enum_class=PensionFundContributions), nullable=False, comment='厚生年金基金')
    pension_fund_contributions_date = Column('pension_fund_contributions_date', Date, nullable=True, comment='厚生年金基金取得日[加入を選択した場合は入力必須]')
    employment_insurance = Column('employment_insurance', EnumType(enum_class=EmploymentInsurance), nullable=False, comment='雇用保険')
    employment_insurance_date = Column('employment_insurance_date', Date, nullable=True, comment='雇用保険取得日')
    employment_insurance_number = Column('employment_insurance_number', String(13, collation='ja_JP.utf8'), nullable=True, comment='雇用保険番号')
    tax_amount_classification = Column('tax_amount_classification', EnumType(enum_class=TaxAmountClassification), nullable=False, comment='税額区分')
    is_widow = Column('is_widow', EnumType(enum_class=IsWidow), nullable=True, comment='寡婦/ひとり親')
    is_working_student = Column('is_working_student', EnumType(enum_class=IsWorkingStudent), nullable=True, comment='勤労学生')
    dependent_count = Column('dependent_count', Integer, nullable=True, comment='税法上の扶養家族人数')
    premium_exemption_during_childcare_leave = Column('premium_exemption_during_childcare_leave', EnumType(enum_class=PremiumExemptionDuringChildcareLeave), nullable=True, comment='育児 ・介護 休業中の社会保険料免除')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_tax', "company_code", "employee_code"), Index('ix_m_employee_tax_1', "company_code"), Index('ix_m_employee_tax_2', "employee_code"), UniqueConstraint("company_code", "employee_code"),)


class ResidentTax(Base):
    """
    住民税マスタ
    住民税を管理します。
    """
    __tablename__ = "m_resident_tax"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    local_government_code = Column('local_government_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='全国地方公共団体コード')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    designated_number = Column('designated_number', String(10, collation='ja_JP.utf8'), nullable=True, comment='指定番号')
    addressee_number = Column('addressee_number', String(10, collation='ja_JP.utf8'), nullable=True, comment='宛名番号')
    resident_municipality_code = Column('resident_municipality_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='住民税市町村コード')
    beneficiary_number = Column('beneficiary_number', String(10, collation='ja_JP.utf8'), nullable=True, comment='受給者番号')
    remarks_others = Column('remarks_others', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考／その他')
    is_taxable = Column('is_taxable', Boolean, nullable=False, comment='課税フラグ')
    resident_tax_jun = Column('resident_tax_jun', Integer, nullable=False, comment='住民税　6月分')
    resident_tax_jly = Column('resident_tax_jly', Integer, nullable=False, comment='住民税　7月分')
    resident_tax_aug = Column('resident_tax_aug', Integer, nullable=False, comment='住民税　8月分')
    resident_tax_sep = Column('resident_tax_sep', Integer, nullable=False, comment='住民税　9月分')
    resident_tax_oct = Column('resident_tax_oct', Integer, nullable=False, comment='住民税　10月分')
    resident_tax_nov = Column('resident_tax_nov', Integer, nullable=False, comment='住民税　11月分')
    resident_tax_dec = Column('resident_tax_dec', Integer, nullable=False, comment='住民税　12月分')
    resident_tax_jan = Column('resident_tax_jan', Integer, nullable=False, comment='住民税　1月分')
    resident_tax_feb = Column('resident_tax_feb', Integer, nullable=False, comment='住民税　2月分')
    resident_tax_mar = Column('resident_tax_mar', Integer, nullable=False, comment='住民税　3月分')
    resident_tax_apl = Column('resident_tax_apl', Integer, nullable=False, comment='住民税　4月分')
    resident_tax_may = Column('resident_tax_may', Integer, nullable=False, comment='住民税　5月分')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_resident_tax', "company_code", "local_government_code", "target_year", "employee_code"),)


class AlternativeHolidayEmployee(Base):
    """
    従業員別代替休暇勘定マスタ
    代替休暇を管理します。
    """
    __tablename__ = "m_alternative_holiday_employee"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    alternative_holiday_hold_times = Column('alternative_holiday_hold_times', Float, nullable=False, comment='代替休暇保持時間数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_alternative_holiday_employee', "company_code", "employee_code"), Index('ix_m_alternative_holiday_employee_1', "company_code"), Index('ix_m_alternative_holiday_employee_2', "employee_code"), UniqueConstraint("company_code", "employee_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class EmployeeSocialInsurance(Base):
    """
    従業員健康保険・厚生年金保険被保険者標準報酬月額トラン
    従業員健康保険・厚生年金保険被保険者標準報酬月額を管理します。
    """
    __tablename__ = "t_employee_social_insurance"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    modification_date_ymd = Column('modification_date_ymd', Date, nullable=False, comment='改定年月日')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    grade_health_insurance_standard_monthly_salary = Column('grade_health_insurance_standard_monthly_salary', Integer, nullable=True, comment='従前の健康保険等級')
    health_insurance_standard_monthly_salary = Column('health_insurance_standard_monthly_salary', Integer, nullable=True, comment='健康保険標準報酬月額')
    grade_welfare_pension_standard_monthly_salary = Column('grade_welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='従前の厚生年金等級')
    welfare_pension_standard_monthly_salary = Column('welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='厚生年金標準報酬月額')
    social_insurance_amount = Column('social_insurance_amount', Integer, nullable=False, comment='社会保険対象額')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_social_insurance', "company_code", "office_code", "modification_date_ymd", "employee_code"), Index('ix_t_employee_social_insurance_1', "company_code"), UniqueConstraint("company_code", "office_code", "modification_date_ymd", "employee_code"),)


class DecisionSocialInsurance(Base):
    """
    健康保険・厚生年金保険被保険者標準報酬月額算定基礎届トラン
    健康保険・厚生年金保険被保険者標準報酬月額算定基礎届を管理します。
    """
    __tablename__ = "t_decision_social_insurance"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    notification_date = Column('notification_date', Date, nullable=False, comment='届出日')
    office_name = Column('office_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='事業所名')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='郵便番号')
    state_name = Column('state_name', String(6, collation='ja_JP.utf8'), nullable=False, comment='都道府県名')
    municipality_name = Column('municipality_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='市町村名')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=False, comment='電話番号')
    owner_name = Column('owner_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='事業主名')
    social_insurance_labor_consultant = Column('social_insurance_labor_consultant', String(8, collation='ja_JP.utf8'), nullable=True, comment='社会保険労務士番号')
    company_worker_name = Column('company_worker_name', String(30, collation='ja_JP.utf8'), nullable=True, comment='社労士名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_decision_social_insurance', "company_code", "office_code", "notification_date"), Index('ix_t_decision_social_insurance_1', "company_code"), UniqueConstraint("company_code", "office_code", "notification_date"),)


class DecisionSocialInsuranceDetail(Base):
    """
    健康保険・厚生年金保険被保険者標準報酬月額算定基礎届明細トラン
    健康保険・厚生年金保険被保険者標準報酬月額算定基礎届の内訳を管理します。
    """
    __tablename__ = "t_decision_social_insurance_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    notification_date = Column('notification_date', Date, nullable=False, comment='届出日')
    insured_person_code = Column('insured_person_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='被保険者番号')
    insured_person_name = Column('insured_person_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='被保険者名')
    birthday = Column('birthday', Date, nullable=True, comment='生年月日')
    basic_pension_number = Column('basic_pension_number', String(11, collation='ja_JP.utf8'), nullable=True, comment='基礎年金番号')
    modification_date = Column('modification_date', String(6, collation='ja_JP.utf8'), nullable=True, comment='改定年月　※給与明細トランの労働月と同義')
    change_before_modification_date = Column('change_before_modification_date', String(6, collation='ja_JP.utf8'), nullable=True, comment='従前の改定年月')
    change_before_grade_health_insurance_standard_monthly_salary = Column('change_before_grade_health_insurance_standard_monthly_salary', Integer, nullable=True, comment='従前の健康保険等級')
    change_before_health_insurance_standard_monthly_salary = Column('change_before_health_insurance_standard_monthly_salary', Integer, nullable=True, comment='従前の健康保険標準報酬月額')
    change_before_grade_welfare_pension_standard_monthly_salary = Column('change_before_grade_welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='従前の厚生年金等級')
    change_before_welfare_pension_standard_monthly_salary = Column('change_before_welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='従前の厚生年金標準報酬月額')
    salary_change_month = Column('salary_change_month', Integer, nullable=True, comment='昇給/降給月')
    salary_change = Column('salary_change', EnumType(enum_class=SalaryChange), nullable=True, comment='昇給降給区分')
    retroactive_payment_month = Column('retroactive_payment_month', String(6, collation='ja_JP.utf8'), nullable=True, comment='遡及支払月')
    retroactive_payment_amount = Column('retroactive_payment_amount', Integer, nullable=True, comment='遡及支払額')
    payroll_month1 = Column('payroll_month1', String(6, collation='ja_JP.utf8'), nullable=True, comment='給与支給月1')
    job_total_days1 = Column('job_total_days1', Integer, nullable=True, comment='給与計算の基礎日数1')
    cash_payment_amount1 = Column('cash_payment_amount1', Integer, nullable=True, comment='通貨によるものの額1')
    in_kind_payment_amount1 = Column('in_kind_payment_amount1', Integer, nullable=True, comment='現物によるものの額1')
    total_payment_amount1 = Column('total_payment_amount1', Integer, nullable=True, comment='合計1')
    payroll_month2 = Column('payroll_month2', String(6, collation='ja_JP.utf8'), nullable=True, comment='給与支給月2')
    job_total_days2 = Column('job_total_days2', Integer, nullable=True, comment='給与計算の基礎日数2')
    cash_payment_amount2 = Column('cash_payment_amount2', Integer, nullable=True, comment='通貨によるものの額2')
    in_kind_payment_amount2 = Column('in_kind_payment_amount2', Integer, nullable=True, comment='現物によるものの額2')
    total_payment_amount2 = Column('total_payment_amount2', Integer, nullable=True, comment='合計2')
    payroll_month3 = Column('payroll_month3', String(6, collation='ja_JP.utf8'), nullable=True, comment='給与支給月3')
    job_total_days3 = Column('job_total_days3', Integer, nullable=True, comment='給与計算の基礎日数3')
    cash_payment_amount3 = Column('cash_payment_amount3', Integer, nullable=True, comment='通貨によるものの額3')
    in_kind_payment_amount3 = Column('in_kind_payment_amount3', Integer, nullable=True, comment='現物によるものの額3')
    total_payment_amount3 = Column('total_payment_amount3', Integer, nullable=True, comment='合計3')
    total_payment_amount_summary = Column('total_payment_amount_summary', Integer, nullable=True, comment='総合計')
    total_payment_amount_average = Column('total_payment_amount_average', Integer, nullable=True, comment='平均')
    salary_increase = Column('salary_increase', Integer, nullable=True, comment='昇給額')
    decision_reason = Column('decision_reason', EnumType(enum_class=DecisionReason), nullable=True, comment='給料決定理由')
    grade_health_insurance_standard_monthly_salary = Column('grade_health_insurance_standard_monthly_salary', Integer, nullable=True, comment='従前の健康保険等級')
    health_insurance_standard_monthly_salary = Column('health_insurance_standard_monthly_salary', Integer, nullable=True, comment='健康保険標準報酬月額')
    grade_welfare_pension_standard_monthly_salary = Column('grade_welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='従前の厚生年金等級')
    welfare_pension_standard_monthly_salary = Column('welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='厚生年金標準報酬月額')
    modified_average_amount = Column('modified_average_amount', Integer, nullable=True, comment='修正平均額')
    remarks_others = Column('remarks_others', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考／その他')
    employee_classification_type1 = Column('employee_classification_type1', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ1')
    employee_classification_type2 = Column('employee_classification_type2', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ2')
    employee_classification_type3 = Column('employee_classification_type3', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ3')
    remarks_reason1 = Column('remarks_reason1', Integer, nullable=True, comment='備考／算定基礎月1')
    remarks_reason2 = Column('remarks_reason2', Integer, nullable=True, comment='備考／算定基礎月2')
    is_non_change = Column('is_non_change', Boolean, nullable=True, comment='変更不要フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_decision_social_insurance_detail', "company_code", "office_code", "notification_date", "insured_person_code"), Index('ix_t_decision_social_insurance_detail_1', "company_code"), UniqueConstraint("company_code", "office_code", "notification_date", "insured_person_code"),)


class ChangeSocialInsurance(Base):
    """
    健康保険・厚生年金保険被保険者標準報酬月額変更届トラン
    健康保険・厚生年金保険被保険者標準報酬月額変更届を管理します。
    """
    __tablename__ = "t_change_social_insurance"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    notification_date = Column('notification_date', Date, nullable=False, comment='届出日')
    office_name = Column('office_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='事業所名')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='郵便番号')
    state_name = Column('state_name', String(6, collation='ja_JP.utf8'), nullable=False, comment='都道府県名')
    municipality_name = Column('municipality_name', String(20, collation='ja_JP.utf8'), nullable=False, comment='市町村名')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=False, comment='電話番号')
    owner_name = Column('owner_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='事業主名')
    social_insurance_labor_consultant = Column('social_insurance_labor_consultant', String(8, collation='ja_JP.utf8'), nullable=True, comment='社会保険労務士番号')
    company_worker_name = Column('company_worker_name', String(30, collation='ja_JP.utf8'), nullable=True, comment='社労士名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_change_social_insurance', "company_code", "office_code", "notification_date"), Index('ix_t_change_social_insurance_1', "company_code"), UniqueConstraint("company_code", "office_code", "notification_date"),)


class ChangeSocialInsuranceDetail(Base):
    """
    健康保険・厚生年金保険被保険者標準報酬月額変更届明細トラン
    健康保険・厚生年金保険被保険者標準報酬月額変更届の内訳を管理します。
    """
    __tablename__ = "t_change_social_insurance_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    notification_date = Column('notification_date', Date, nullable=False, comment='届出日')
    insured_person_code = Column('insured_person_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='被保険者番号')
    insured_person_name = Column('insured_person_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='被保険者名')
    birthday = Column('birthday', Date, nullable=True, comment='生年月日')
    basic_pension_number = Column('basic_pension_number', String(11, collation='ja_JP.utf8'), nullable=True, comment='基礎年金番号')
    modification_date = Column('modification_date', String(6, collation='ja_JP.utf8'), nullable=True, comment='改定年月　※給与明細トランの労働月と同義')
    change_before_modification_date = Column('change_before_modification_date', String(6, collation='ja_JP.utf8'), nullable=True, comment='従前の改定年月')
    change_before_grade_health_insurance_standard_monthly_salary = Column('change_before_grade_health_insurance_standard_monthly_salary', Integer, nullable=True, comment='従前の健康保険等級')
    change_before_health_insurance_standard_monthly_salary = Column('change_before_health_insurance_standard_monthly_salary', Integer, nullable=True, comment='従前の健康保険標準報酬月額')
    change_before_grade_welfare_pension_standard_monthly_salary = Column('change_before_grade_welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='従前の厚生年金等級')
    change_before_welfare_pension_standard_monthly_salary = Column('change_before_welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='従前の厚生年金標準報酬月額')
    salary_change_month = Column('salary_change_month', Integer, nullable=True, comment='昇給/降給月')
    salary_change = Column('salary_change', EnumType(enum_class=SalaryChange), nullable=True, comment='昇給降給区分')
    retroactive_payment_month = Column('retroactive_payment_month', String(6, collation='ja_JP.utf8'), nullable=True, comment='遡及支払月')
    retroactive_payment_amount = Column('retroactive_payment_amount', Integer, nullable=True, comment='遡及支払額')
    payroll_month1 = Column('payroll_month1', String(6, collation='ja_JP.utf8'), nullable=True, comment='給与支給月1')
    job_total_days1 = Column('job_total_days1', Integer, nullable=True, comment='給与計算の基礎日数1')
    cash_payment_amount1 = Column('cash_payment_amount1', Integer, nullable=True, comment='通貨によるものの額1')
    in_kind_payment_amount1 = Column('in_kind_payment_amount1', Integer, nullable=True, comment='現物によるものの額1')
    total_payment_amount1 = Column('total_payment_amount1', Integer, nullable=True, comment='合計1')
    payroll_month2 = Column('payroll_month2', String(6, collation='ja_JP.utf8'), nullable=True, comment='給与支給月2')
    job_total_days2 = Column('job_total_days2', Integer, nullable=True, comment='給与計算の基礎日数2')
    cash_payment_amount2 = Column('cash_payment_amount2', Integer, nullable=True, comment='通貨によるものの額2')
    in_kind_payment_amount2 = Column('in_kind_payment_amount2', Integer, nullable=True, comment='現物によるものの額2')
    total_payment_amount2 = Column('total_payment_amount2', Integer, nullable=True, comment='合計2')
    payroll_month3 = Column('payroll_month3', String(6, collation='ja_JP.utf8'), nullable=True, comment='給与支給月3')
    job_total_days3 = Column('job_total_days3', Integer, nullable=True, comment='給与計算の基礎日数3')
    cash_payment_amount3 = Column('cash_payment_amount3', Integer, nullable=True, comment='通貨によるものの額3')
    in_kind_payment_amount3 = Column('in_kind_payment_amount3', Integer, nullable=True, comment='現物によるものの額3')
    total_payment_amount3 = Column('total_payment_amount3', Integer, nullable=True, comment='合計3')
    total_payment_amount_summary = Column('total_payment_amount_summary', Integer, nullable=True, comment='総合計')
    total_payment_amount_average = Column('total_payment_amount_average', Integer, nullable=True, comment='平均')
    salary_increase = Column('salary_increase', Integer, nullable=True, comment='昇給額')
    change_reason = Column('change_reason', EnumType(enum_class=ChangeReason), nullable=True, comment='昇給降給区分')
    modified_average_amount = Column('modified_average_amount', Integer, nullable=True, comment='修正平均額')
    remarks_reason = Column('remarks_reason', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考／昇給・降給の理由')
    remarks_others = Column('remarks_others', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考／その他')
    grade_health_insurance_standard_monthly_salary = Column('grade_health_insurance_standard_monthly_salary', Integer, nullable=True, comment='従前の健康保険等級')
    health_insurance_standard_monthly_salary = Column('health_insurance_standard_monthly_salary', Integer, nullable=True, comment='健康保険標準報酬月額')
    grade_welfare_pension_standard_monthly_salary = Column('grade_welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='従前の厚生年金等級')
    welfare_pension_standard_monthly_salary = Column('welfare_pension_standard_monthly_salary', Integer, nullable=True, comment='厚生年金標準報酬月額')
    employee_classification_type1 = Column('employee_classification_type1', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ1')
    employee_classification_type2 = Column('employee_classification_type2', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ2')
    employee_classification_type3 = Column('employee_classification_type3', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ3')
    is_non_change = Column('is_non_change', Boolean, nullable=True, comment='変更不要フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_change_social_insurance_detail', "company_code", "office_code", "notification_date", "insured_person_code"), Index('ix_t_change_social_insurance_detail_1', "company_code"), UniqueConstraint("company_code", "office_code", "notification_date", "insured_person_code"),)


class EmployeeTransfer(Base):
    """
    従業員振込マスタ
    従業員の振込を管理します。
    """
    __tablename__ = "m_employee_transfer"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    transfer_method_1 = Column('transfer_method_1', EnumType(enum_class=TransferMethod), nullable=False, comment='第一振込先　振込方法')
    jurisdiction_code = Column('jurisdiction_code', String(2, collation='ja_JP.utf8'), nullable=True, comment='所轄コード')
    funds_transfer_agent_code = Column('funds_transfer_agent_code', String(5, collation='ja_JP.utf8'), nullable=True, comment='登録番号')
    bank_code_1 = Column('bank_code_1', String(4, collation='ja_JP.utf8'), ForeignKey('m_bank.bank_code', onupdate='CASCADE', ondelete='CASCADE'), comment='第一振込先　銀行コード')
    branch_code_1 = Column('branch_code_1', String(3, collation='ja_JP.utf8'), nullable=True, comment='第一振込先　支店コード')
    account_classification_1 = Column('account_classification_1', EnumType(enum_class=AccountClassification), nullable=True, comment='第一振込先　口座種別')
    account_number_1 = Column('account_number_1', String(7, collation='ja_JP.utf8'), nullable=True, comment='第一振込先　口座番号')
    transfer_amount_of_money_1 = Column('transfer_amount_of_money_1', Integer, nullable=True, comment='第一振込先　振込金額')
    transfer_method_2 = Column('transfer_method_2', EnumType(enum_class=TransferMethod), nullable=True, comment='第二振込先　振込方法')
    bank_code_2 = Column('bank_code_2', String(4, collation='ja_JP.utf8'), ForeignKey('m_bank.bank_code', onupdate='CASCADE', ondelete='CASCADE'), comment='第二振込先　銀行コード')
    branch_code_2 = Column('branch_code_2', String(3, collation='ja_JP.utf8'), nullable=True, comment='第二振込先　支店コード')
    account_classification_2 = Column('account_classification_2', EnumType(enum_class=AccountClassification), nullable=True, comment='第二振込先　口座種別')
    account_number_2 = Column('account_number_2', String(7, collation='ja_JP.utf8'), nullable=True, comment='第二振込先　口座番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ixm_employee_transfer', "company_code", "employee_code"), Index('ixm_employee_transfer_1', "company_code"), UniqueConstraint("company_code", "employee_code"),)


class EmployeePayment(Base):
    """
    従業員給与マスタ
    従業員の給与情報を管理します。
    """
    __tablename__ = "m_employee_payment"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    salary_item_code = Column('salary_item_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='給与項目コード')
    basic_price = Column('basic_price', Integer, nullable=False, comment='基本単価')
    working_time = Column('working_time', String(11, collation='ja_JP.utf8'), nullable=True, comment='労働時間の範囲')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_payment', "company_code", "employee_code", "salary_item_code"), Index('ix_m_employee_payment_1', "company_code"), UniqueConstraint("company_code", "employee_code", "salary_item_code"),)


class ApplicationCollaborator(Base):
    """
    申請番号別コラボレータマスタ
    """
    __tablename__ = "m_application_collaborator"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_application_collaborator', "company_code", "application_number", "employee_code"), Index('ix_m_application_collaborator_1', "company_code"), UniqueConstraint("company_code", "application_number", "employee_code"), )


class EmployeeNavigationDetail(Base):
    """
    従業員別ナビゲーション詳細マスタ
    """
    __tablename__ = "m_employee_navigation_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    navigation_code = Column('navigation_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='ナビゲーションコード')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    before_screen_code = Column('before_screen_code', String(6, collation='ja_JP.utf8'), nullable=True, comment='直前の画面コード')
    registered_flag = Column('registered_flag', Boolean, nullable=False, comment='登録済フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_navigation_detail', "company_code", "employee_code", "navigation_code", "screen_code", "before_screen_code"), Index('ix_m_employee_navigation_detail_1', "company_code"), UniqueConstraint("company_code", "employee_code", "navigation_code", "screen_code", "before_screen_code"))


class MachineLearningFormulas(Base):
    """
    機械学習計算結果マスタ
    """
    __tablename__ = "m_machine_learning_formulas"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), comment='会社コード')
    calculation_category = Column('calculation_category', EnumType(enum_class=AiCalculationCategory), nullable=True, comment='算定区分')
    learning_formula = Column('learning_formula', String(8192, collation='ja_JP.utf8'), nullable=False, comment='計算式')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_machine_learning_formulas', "company_code", "calculation_category"), Index('ix_m_machine_learning_formulas_1', "company_code"), UniqueConstraint("company_code", "calculation_category"), )


class Salary_increase_simulation_plan(Base):
    """
    昇給シミュレーション計画マスタ
    """
    __tablename__ = "m_salary_increase_simulation_plan"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), comment='会社コード')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    target_month = Column('target_month', String(2, collation='ja_JP.utf8'), nullable=False, comment='支給月度')
    target_year_from = Column('target_year_from', String(4, collation='ja_JP.utf8'), nullable=False, comment='有効期間(開始)')
    target_year_to = Column('target_year_to', String(4, collation='ja_JP.utf8'), nullable=False, comment='有効期間(終了)')
    annual_sales_revenue = Column('annual_sales_revenue', Integer, nullable=True, comment='売上高[年間]')
    annual_labor_costs = Column('annual_labor_costs', Integer, nullable=True, comment='人件費[年間]')
    annual_statutory_welfare_expenses_social_insurance = Column('annual_statutory_welfare_expenses_social_insurance', Integer, nullable=True, comment='法定福利費[社会保険][年間]')
    annual_statutory_welfare_expenses_labor_insurance = Column('annual_statutory_welfare_expenses_labor_insurance', Integer, nullable=True, comment='法定福利費[労働保険][年間]')
    labor_share_of_income = Column('labor_share_of_income', DECIMAL(4, 1), nullable=True, comment='労働分配率[予測]')
    annual_change_in_labor_costs = Column('annual_change_in_labor_costs', Integer, nullable=True, comment='人件費増減額[年間]')
    annual_labor_cost_change_rate = Column('annual_labor_cost_change_rate', DECIMAL(4, 1), nullable=True, comment='人件費増減率[年間]')
    inflation_rate = Column('inflation_rate', DECIMAL(4, 1), nullable=True, comment='物価上昇率')
    next_fiscal_year_sales_revenue = Column('next_fiscal_year_sales_revenue', Integer, nullable=True, comment='売上高[来期]')
    annualnext_fiscal_year_labor_costs = Column('annualnext_fiscal_year_labor_costs', Integer, nullable=True, comment='人件費[来期]')
    next_fiscal_year_labor_share_of_income = Column('next_fiscal_year_labor_share_of_income', DECIMAL(4, 1), nullable=True, comment='労働分配率[来期]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_salary_increase_simulation_plan', "company_code", "target_year", "target_month"), Index('ix_m_salary_increase_simulation_plan_1', "company_code"), UniqueConstraint("company_code", "target_year", "target_month"), )


class Employee_specific_salary_increase_simulation_plan(Base):
    """
    従業員別昇給シミュレーション計画マスタ
    """
    __tablename__ = "m_employee_specific_salary_increase_simulation_plan"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), comment='会社コード')
    target_year = Column('target_year', String(4, collation='ja_JP.utf8'), nullable=False, comment='対象年')
    target_month = Column('target_month', String(2, collation='ja_JP.utf8'), nullable=False, comment='支給月度')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    labor_costs = Column('labor_costs', Integer, nullable=True, comment='人件費')
    variance_from_plan = Column('variance_from_plan', Integer, nullable=True, comment='計画との差')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    direct_sales_performance = Column('direct_sales_performance', Integer, nullable=True, comment='売上実績[直接]')
    indirect_sales_performance = Column('indirect_sales_performance', Integer, nullable=True, comment='売上実績[間接]')
    actual_labor_share_of_income = Column('actual_labor_share_of_income', DECIMAL(4, 1), nullable=True, comment='労働分配率[実績]')
    direct_sales_forecast = Column('direct_sales_forecast', Integer, nullable=True, comment='売上予測[直接]')
    indirect_sales_forecast = Column('indirect_sales_forecast', Integer, nullable=True, comment='売上予測[間接]')
    monthly_salary_increase_amount = Column('monthly_salary_increase_amount', Integer, nullable=True, comment='昇給額[月額]')
    annual_labor_costs = Column('annual_labor_costs', Integer, nullable=True, comment='人件費[年間]')
    labor_share_of_income = Column('labor_share_of_income', DECIMAL(4, 1), nullable=True, comment='労働分配率[予測]')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_employee_specific_salary_increase_simulation_plan', "company_code", "target_year", "target_month", "employee_code"), Index('ix_m_employee_specific_salary_increase_simulation_plan_1', "company_code"), UniqueConstraint("company_code", "target_year", "target_month", "employee_code"), )


class CompanyScore(Base):
    """
    会社別スコアトラン
    """
    __tablename__ = "t_company_score"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), comment='会社コード')
    company_name = Column('company_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='会社名')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    working_environment_score = Column('working_environment_score', Integer, nullable=False, comment='労働環境スコア')
    wage_status_score = Column('wage_status_score', Integer, nullable=False, comment='賃金状況スコア')
    company_stability_score = Column('company_stability_score', Integer, nullable=False, comment='会社の安定度スコア')
    legal_compliance_status_score = Column('legal_compliance_status_score', Integer, nullable=False, comment='法令遵守状況スコア')
    total_score = Column('total_score', Integer, nullable=False, comment='総合スコア')
    industry_ranking = Column('industry_ranking', Integer, nullable=False, comment='業種別ランキング')
    regional_ranking = Column('regional_ranking', Integer, nullable=False, comment='地域別ランキング')
    scale_ranking = Column('scale_ranking', Integer, nullable=False, comment='規模別ランキング')
    total_ranking = Column('total_ranking', Integer, nullable=False, comment='総合ランキング')
    industry_code_big = Column('industry_code_big', String(1, collation='ja_JP.utf8'), nullable=False, comment='業種(大分類)')
    industry_code_during = Column('industry_code_during', String(2, collation='ja_JP.utf8'), nullable=False, comment='業種(中分類)')
    industry_code_small = Column('industry_code_small', String(4, collation='ja_JP.utf8'), nullable=False, comment='業種(小分類)')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    sales_amount = Column('sales_amount', Integer, nullable=True, comment='売上高')
    profitable = Column('profitable', Integer, nullable=True, comment='利益高')
    capital = Column('capital', Integer, nullable=True, comment='資本金')
    growth_rate = Column('growth_rate', DECIMAL(4, 1), nullable=True, comment='成長率')
    number_of_employees = Column('number_of_employees', Integer, nullable=False, comment='従業員数')
    average_age = Column('average_age', Float, nullable=True, comment='従業員の平均年齢')
    male_rate = Column('male_rate', DECIMAL(4, 1), nullable=True, comment='男性比率')
    female_rate = Column('female_rate', DECIMAL(4, 1), nullable=True, comment='女性比率')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_company_score', "company_code", "target_date"), Index('ix_t_company_score_1', "company_code"), UniqueConstraint("company_code", "target_date"), )


class CompanyScoreDetail(Base):
    """
    会社別スコア詳細トラン
    """
    __tablename__ = "t_company_score_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), comment='会社コード')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    category = Column('category', String(1, collation='ja_JP.utf8'), nullable=False, comment='カテゴリー')
    score_type = Column('score_type', String(2, collation='ja_JP.utf8'), nullable=False, comment='スコア種別')
    score_detail_code = Column('score_detail_code', String(4, collation='ja_JP.utf8'), nullable=False, comment='スコア詳細')
    score = Column('score', Integer, nullable=False, comment='スコア')
    message = Column('message', String(255, collation='ja_JP.utf8'), nullable=False, comment='メッセージ')
    industry_score = Column('industry_score', Integer, nullable=True, comment='産業別スコア')
    industry_message = Column('industry_message', String(255, collation='ja_JP.utf8'), nullable=True, comment='産業別メッセージ')
    summary_data = Column('summary_data', String(255, collation='ja_JP.utf8'), nullable=True, comment='集計値')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=True, comment='画面コード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_company_score_detail', "company_code", "target_date", "category", "score_type", "score_detail_code"), Index('ix_t_company_score_detail_1', "company_code"), UniqueConstraint("company_code", "target_date", "category", "score_type", "score_detail_code"), )


class CompanyCount(Base):
    """
    会社数トラン
    """
    __tablename__ = "t_company_count"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    number_of_applicable_companies = Column('number_of_applicable_companies', Integer, nullable=False, comment='該当会社数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_company_count', "target_date"), UniqueConstraint("target_date"), )


class IndustryCompanyCount(Base):
    """
    業種別会社数トラン
    """
    __tablename__ = "t_industry_company_count"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    industry_code_big = Column('industry_code_big', String(1, collation='ja_JP.utf8'), nullable=False, comment='業種(大分類)')
    industry_code_during = Column('industry_code_during', String(2, collation='ja_JP.utf8'), nullable=False, comment='業種(中分類)')
    industry_code_small = Column('industry_code_small', String(4, collation='ja_JP.utf8'), nullable=False, comment='業種(小分類)')
    number_of_applicable_companies = Column('number_of_applicable_companies', Integer, nullable=False, comment='該当会社数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_industry_company_count', "target_date", "industry_code_big", "industry_code_during", "industry_code_small"), UniqueConstraint("target_date", "industry_code_big", "industry_code_during", "industry_code_small"), )


class PrefecturesCompanyCount(Base):
    """
    都道府県別会社数トラン
    """
    __tablename__ = "t_prefectures_company_count"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), nullable=False, comment='都道府県コード')
    number_of_applicable_companies = Column('number_of_applicable_companies', Integer, nullable=False, comment='該当会社数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_prefectures_company_count', "target_date", "state_code"), UniqueConstraint("target_date", "state_code"), )


class SalesScaleCompanyCount(Base):
    """
    売上高規模別会社数トラン
    """
    __tablename__ = "t_sales_scale_company_count"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    sales_amount_from = Column('sales_amount_from', Integer, nullable=False, comment='売上高[以上]')
    sales_amount_to = Column('sales_amount_to', Integer, nullable=True, comment='売上高[以下]')
    number_of_applicable_companies = Column('number_of_applicable_companies', Integer, nullable=False, comment='該当会社数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_sales_scale_company_count', "target_date", "sales_amount_from"), UniqueConstraint("target_date", "sales_amount_from"), )


class ProfitScaleCompanyCount(Base):
    """
    利益高規模別会社数トラン
    """
    __tablename__ = "t_profit_scale_company_count"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    profitable_from = Column('profitable_from', Integer, nullable=False, comment='開始')
    profitable_to = Column('profitable_to', Integer, nullable=True, comment='終了')
    number_of_applicable_companies = Column('number_of_applicable_companies', Integer, nullable=False, comment='該当会社数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_profit_scale_company_count', "target_date", "profitable_from"), UniqueConstraint("target_date", "profitable_from"), )


class CapitalScaleCompanyCount(Base):
    """
    資本金規模別会社数トラン
    """
    __tablename__ = "t_capital_scale_company_count"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    capital_from = Column('capital_from', Integer, nullable=False, comment='利益高[以上]')
    capital_to = Column('capital_to', Integer, nullable=True, comment='利益高[以下]')
    number_of_applicable_companies = Column('number_of_applicable_companies', Integer, nullable=False, comment='該当会社数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_capital_scale_company_count', "target_date", "capital_from"), UniqueConstraint("target_date", "capital_from"), )


class GrowthRateCompanyCount(Base):
    """
    成長率規模別会社数トラン
    """
    __tablename__ = "t_growth_rate_company_count"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    growth_rate_from = Column('growth_rate_from', Integer, nullable=False, comment='成長率[以上]')
    growth_rate_to = Column('growth_rate_to', Integer, nullable=True, comment='成長率[以下]')
    number_of_applicable_companies = Column('number_of_applicable_companies', Integer, nullable=False, comment='該当会社数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_growth_rate_company_count', "target_date", "growth_rate_from"), UniqueConstraint("target_date", "growth_rate_from"), )


class NumberOfEmployeesCompanyCount(Base):
    """
    従業員規模別会社数トラン
    """
    __tablename__ = "t_number_of_employees_company_count"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    number_of_employees_from = Column('number_of_employees_from', Integer, nullable=False, comment='従業員数[以上]')
    number_of_employees_to = Column('number_of_employees_to', Integer, nullable=True, comment='従業員数[以下]')
    number_of_applicable_companies = Column('number_of_applicable_companies', Integer, nullable=False, comment='該当会社数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_number_of_employees_company_count', "target_date", "number_of_employees_from"), UniqueConstraint("target_date", "number_of_employees_from"), )


class ApplicationChat(Base):
    """
    申請番号別チャットトラン
    """
    __tablename__ = "t_application_chat"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    chat_datetime = Column('chat_datetime', TIMESTAMP, nullable=False, comment='送信日付')
    chat = Column('chat_contents', String(255, collation='ja_JP.utf8'), nullable=False, unique=True, comment='チャット')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=True, comment='添付ファイルのパス')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_application_chat', "company_code", "application_number", "employee_code", "chat_datetime"), Index('ix_t_application_chat_1', "company_code"), UniqueConstraint("company_code", "application_number", "employee_code", "chat_datetime"), )


class ChangePassword(Base):
    """
    パスワード変更トラン
    """
    __tablename__ = "t_change_password"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    token = Column('token', String(255, collation='ja_JP.utf8'), nullable=False, unique=True, comment='トークン')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_change_password', "company_code", "employee_code"), Index('ix_t_change_password_1', "company_code"), UniqueConstraint("company_code", "employee_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class TimeCardBreakTimeRecord(Base):
    """
    タイムカード休憩トラン
    """
    __tablename__ = "t_time_card_break_time_record"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    start_time = Column('start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='開始時間')
    end_time = Column('end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='終了時間')
    break_time_start_time_office_code = Column('break_time_start_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='休憩開始打刻した事業所コード')
    break_time_end_time_office_code = Column('break_time_end_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='休憩終了打刻した事業所コード')
    break_time_start_lat = Column('break_time_start_lat', DECIMAL(9, 6), nullable=True, comment='休憩開始打刻した緯度')
    break_time_start_lng = Column('break_time_start_lng', DECIMAL(9, 6), nullable=True, comment='休憩開始打刻した経度')
    break_time_end_lat = Column('break_time_end_lat', DECIMAL(9, 6), nullable=True, comment='休憩終了打刻した緯度')
    break_time_end_lng = Column('break_time_end_lng', DECIMAL(9, 6), nullable=True, comment='休憩終了打刻した経度')
    reflection_flg = Column('reflection_flg', EnumType(enum_class=ReflectionFlg), nullable=False, comment='反映フラグ')
    break_time_start_time_entry_flg = Column('break_time_start_time_entry_flg', EnumType(enum_class=EntryFlg), nullable=True, comment='休憩開始の打刻方法')
    break_time_end_time_entry_flg = Column('break_time_end_time_entry_flg', EnumType(enum_class=EntryFlg), nullable=True, comment='退休憩終了の打刻方法')
    menstrual_leave_flg = Column('menstrual_leave_flg', Boolean, nullable=True, comment='生理休暇フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_time_card_break_time_record', "company_code", "employee_code", "target_date", "work_schedule_code", "start_time"), Index('ix_t_time_card_break_time_record_1', "company_code"), Index('ix_t_time_card_break_time_record_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "target_date", "work_schedule_code", "start_time"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']))


class TimeCardHistory(Base):
    """
    打刻履歴トラン
    """
    __tablename__ = "t_time_card_history"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    typing_stamping_time = Column('typing_stamping_time', String(8, collation='ja_JP.utf8'), nullable=False, comment='打刻した時間')
    typing_office_code = Column('typing_office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='打刻/退勤した事業所コード')
    lat = Column('lat', DECIMAL(9, 6), nullable=True, comment='緯度')
    lng = Column('lng', DECIMAL(9, 6), nullable=True, comment='経度')
    stamping_type = Column('stamping_type', EnumType(enum_class=StampingType), nullable=False, comment='打刻タイプ')
    entry_flg = Column('entry_flg', EnumType(enum_class=EntryFlg), nullable=False, comment='打刻方法')
    smile_mark = Column('smile_mark', EnumType(enum_class=SmileMark), nullable=True, comment='スマイルマーク')
    telework_flg = Column('telework_flg', Boolean, nullable=True, comment='テレワークフラグ')
    is_success = Column('is_success', Boolean, nullable=False, comment='ステータス')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_time_card_history', "company_code", "employee_code", "target_date", "work_schedule_code", "typing_stamping_time"), Index('ix_t_time_card_history_1', "company_code"), Index('ix_t_time_card_history_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "target_date", "work_schedule_code", "typing_stamping_time"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class BreakTimeRecord(Base):
    """
    休憩トラン
    """
    __tablename__ = "t_break_time_record"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    start_time = Column('start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='開始時間')
    end_time = Column('end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='終了時間')
    break_time_start_time_office_code = Column('break_time_start_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='休憩開始打刻した事業所コード')
    break_time_end_time_office_code = Column('break_time_end_time_office_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='休憩終了打刻した事業所コード')
    break_time_start_lat = Column('break_time_start_lat', DECIMAL(9, 6), nullable=True, comment='休憩開始打刻した緯度')
    break_time_start_lng = Column('break_time_start_lng', DECIMAL(9, 6), nullable=True, comment='休憩開始打刻した経度')
    break_time_end_lat = Column('break_time_end_lat', DECIMAL(9, 6), nullable=True, comment='休憩終了打刻した緯度')
    break_time_end_lng = Column('break_time_end_lng', DECIMAL(9, 6), nullable=True, comment='休憩終了打刻した経度')
    reflection_flg = Column('reflection_flg', EnumType(enum_class=ReflectionFlg), nullable=False, comment='反映フラグ')
    break_time_start_time_entry_flg = Column('break_time_start_time_entry_flg', EnumType(enum_class=EntryFlg), nullable=True, comment='休憩開始の打刻方法')
    break_time_end_time_entry_flg = Column('break_time_end_time_entry_flg', EnumType(enum_class=EntryFlg), nullable=True, comment='退休憩終了の打刻方法')
    menstrual_leave_flg = Column('menstrual_leave_flg', Boolean, nullable=True, comment='生理休暇フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_break_time_record', "company_code", "employee_code", "target_date", "work_schedule_code", "start_time"), Index('ix_t_break_time_record_1', "company_code"), Index('ix_t_break_time_record_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "target_date", "work_schedule_code", "start_time"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']))


class SafetyConfirmation(Base):
    """
    安否確認トラン
    """
    __tablename__ = "t_safety_confirmation"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    check_date = Column('check_date', TIMESTAMP, nullable=False, comment='安否確認日')
    safety_of_the_person = Column('safety_of_the_person', EnumType(enum_class=SafetyOfThePerson), nullable=False, comment='本人の安否')
    coming_to_work = Column('coming_to_work', EnumType(enum_class=ComingToWork), nullable=True, comment='出勤可否')
    transportation_train = Column('transportation_train', Boolean, nullable=True, comment='交通手段[電車]')
    transportation_bus = Column('transportation_bus', Boolean, nullable=True, comment='交通手段[バス]')
    transportation_car = Column('transportation_car', Boolean, nullable=True, comment='交通手段[自動車]')
    transportation_bicycle = Column('transportation_bicycle', Boolean, nullable=True, comment='交通手段[自転車]')
    transportation_on_foot = Column('transportation_on_foot', Boolean, nullable=True, comment='交通手段[徒歩]')
    present_place = Column('present_place', Date, nullable=True, comment='現在地')
    lat = Column('lat', DECIMAL(9, 6), nullable=True, comment='緯度')
    lng = Column('lng', DECIMAL(9, 6), nullable=True, comment='経度')
    message = Column('message', String(255, collation='ja_JP.utf8'), nullable=False, comment='メッセージ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_safety_confirmation', "company_code", "employee_code", "check_date"), Index('ix_t_safety_confirmation_1', "company_code"), Index('ix_t_safety_confirmation_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "check_date"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']), {'extend_existing': True})


class Alert(Base):
    """
    アラートトラン
    """
    __tablename__ = "t_alert"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    aleat_number = Column('aleat_number', Integer, nullable=False, comment='アラート番号')
    notification = Column('notification', String(255, collation='ja_JP.utf8'), nullable=False, comment='お知らせ')
    parameter = Column('parameter', String(255, collation='ja_JP.utf8'), nullable=True, comment='パラメータ')
    notice_date = Column('notice_date', TIMESTAMP, nullable=False, comment='お知らせ発生日')
    notice_type = Column('notice_type', EnumType(enum_class=NoticeType), nullable=False, comment='お知らせの種類')
    table_name = Column('table_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='テーブル名')
    search_key = Column('search_key', String(4096, collation='ja_JP.utf8'), nullable=True, comment='検索キー')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_alert', "company_code", "employee_code", "screen_code", "aleat_number"), Index('ix_t_alert_1', "company_code"), Index('ix_t_alert_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "screen_code", "aleat_number"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']), {'extend_existing': True})


class ArtemisAlertTrigger(Base):
    """
    アルテミスアラートトリガーマスタ
    """
    __tablename__ = "m_artemis_alert_trigger"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    alert_code = Column('alert_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='アラートコード')
    trigger_api_prefix = Column('trigger_api_prefix', String(255, collation='ja_JP.utf8'), nullable=False, comment='トリガーAPIプレフィックス')
    executor_name = Column('executor_name', String(255, collation='ja_JP.utf8'), nullable=False, comment='実行クラス名')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    mapper_args = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_artemis_alert_trigger', "alert_code", "trigger_api_prefix"), UniqueConstraint("alert_code", "trigger_api_prefix"), {'extend_existing': True})


class EmployeeNotice(Base):
    """
    従業員お知らせ既読トラン
    """
    __tablename__ = "t_employee_notice"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    notice_number = Column('notice_number', Integer, nullable=False, comment='お知らせ番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_notice', "company_code", "employee_code", "notice_number"), Index('ix_t_employee_notice_1', "company_code"), Index('ix_t_employee_notice_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "notice_number"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']), {'extend_existing': True})


class UserReport(Base):
    """
    帳票トラン
    """
    __tablename__ = "t_user_report"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    report_code = Column('report_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='帳票コード')
    search_key = Column('search_key', String(4096, collation='ja_JP.utf8'), nullable=False, comment='検索キー')
    file_name = Column('file_name', String(255, collation='ja_JP.utf8'), nullable=True, comment='ファイル名')
    file_size = Column('file_size', Integer, nullable=True, comment='ファイルサイズ')
    file_create_date = Column('file_create_date', TIMESTAMP, nullable=True, comment='ファイル作成日')
    report_status = Column('report_status', EnumType(enum_class=ReportStatus), nullable=False, comment='帳票ステータス')
    web_socket = Column('web_socket', String(2048), nullable=True, comment='websocket情報')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_user_report', "company_code", "employee_code", "file_name"), Index('ix_t_user_report_1', "company_code"), Index('ix_t_user_report_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "file_name"), )


class ApplicationObject(Base):
    """
    申請オブジェクト
    """
    __tablename__ = "t_application_object"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    re_application_number = Column('re_application_number', Integer, nullable=True, comment='旧申請番号')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    target_company_code = Column('target_company_code', String(10, collation='ja_JP.utf8'), comment='対象者の会社コード')
    target_group_code = Column('target_group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='対象者の部署コード')
    target_employee_code = Column('target_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='対象者の従業員番号')
    applicant_company_code = Column('applicant_company_code', String(10, collation='ja_JP.utf8'), comment='申請者の会社コード')
    applicant_group_code = Column('applicant_group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請者の部署コード')
    applicant_employee_code = Column('applicant_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請者の従業員番号')
    apply_date = Column('apply_date', TIMESTAMP, nullable=False, comment='申請日')
    approval_date = Column('approval_date', TIMESTAMP, nullable=True, comment='承認日')
    application_status = Column('application_status', EnumType(enum_class=ApplicationStatus), nullable=False, comment='申請書状態')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_application_object', "company_code", "application_number"), Index('ix_t_application_object_1', "company_code"), UniqueConstraint("company_code", "application_number"), )


class ActivityObject(Base):
    """
    申請明細オブジェクト
    """
    __tablename__ = "t_activity_object"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    route_type = Column('route_type', Integer, nullable=False, comment='ルートタイプ')
    route_number = Column('route_number', Integer, nullable=False, comment='ルートナンバー')
    approverl_company_code = Column('approverl_company_code', String(10, collation='ja_JP.utf8'), comment='承認者の会社コード')
    approverl_role_code = Column('approverl_role_code', String(30, collation='ja_JP.utf8'), nullable=True, comment='承認者の利用権限コード')
    approverl_group_code = Column('approverl_group_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='承認者の部署コード')
    approverl_employee_code = Column('approverl_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='承認者の従業員番号')
    deputy_approverl_company_code = Column('deputy_approverl_company_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='代理承認者の会社コード')
    deputy_approverl_group_code = Column('deputy_approverl_group_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='代理承認者の部署コード')
    deputy_approverl_employee_code = Column('deputy_approverl_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='代理承認者の従業員番号')
    deputy_contents = Column('deputy_contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='依頼理由')
    function = Column('function', EnumType(enum_class=ApprovalFunction), nullable=False, comment='承認画面の機能')
    reaching_date = Column('reaching_date', TIMESTAMP, nullable=True, comment='到達日')
    process_date = Column('process_date', TIMESTAMP, nullable=True, comment='処理日')
    activity_status = Column('activity_status', EnumType(enum_class=ActivityStatus), nullable=True, comment='承認者状態')
    approverl_comment = Column('approverl_comment', String(255, collation='ja_JP.utf8'), nullable=True, comment='承認者のコメント')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_activity_object', "company_code", "application_number", "route_type", "route_number", "approverl_company_code", "approverl_group_code", "approverl_employee_code"), Index('ix_t_activity_object_1', "company_code"), Index('ix_t_activity_object_2', "company_code", "application_number"), UniqueConstraint("company_code", "application_number", "route_type", "route_number", "approverl_company_code", "approverl_group_code", "approverl_employee_code"), )


class Appended(Base):
    """
    添付オブジェクト
    """
    __tablename__ = "t_appended"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    route_type = Column('route_type', Integer, nullable=False, comment='ルートタイプ')
    route_number = Column('route_number', Integer, nullable=False, comment='ルートナンバー')
    approverl_company_code = Column('approverl_company_code', String(10, collation='ja_JP.utf8'), comment='承認者の会社コード')
    approverl_group_code = Column('approverl_group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='承認者の部署コード')
    approverl_employee_code = Column('approverl_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='承認者の従業員番号')
    append_title = Column('append_title', String(255, collation='ja_JP.utf8'), nullable=False, comment='添付ファイルの説明')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=False, comment='添付ファイルのパス')
    append_date = Column('append_date', TIMESTAMP, nullable=False, comment='添付ファイルの登録日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_appended', "company_code", "application_number", "route_type", "route_number"), Index('ix_t_appended_1', "company_code"), Index('ix_t_appended_2', "company_code", "application_number"), UniqueConstraint("company_code", "application_number", "route_type", "route_number"), )


class RouteHistory(Base):
    """
    申請書履歴オブジェクト
    """
    __tablename__ = "t_route_history"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    company_name = Column('company_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='会社名')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    re_application_number = Column('re_application_number', Integer, nullable=True, comment='旧申請番号')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    application_form_name = Column('application_form_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='申請書名')
    target_company_code = Column('target_company_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='対象者の会社コード')
    target_company_name = Column('target_company_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='対象者の会社名')
    target_group_code = Column('target_group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='対象者の部署コード')
    target_group_name = Column('target_group_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='対象者の部署名')
    target_employee_code = Column('target_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='対象者の従業員番号')
    target_employee_name = Column('target_employee_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='対象者の氏名')
    applicant_company_code = Column('applicant_company_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請者の会社コード')
    applicant_company_name = Column('applicant_company_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='申請者の会社名')
    applicant_group_code = Column('applicant_group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請者の部署コード')
    applicant_group_name = Column('applicant_group_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='申請者の部署名')
    applicant_employee_code = Column('applicant_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請者の従業員番号')
    applicant_employee_name = Column('applicant_employee_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='申請者の氏名')
    apply_date = Column('apply_date', TIMESTAMP, nullable=False, comment='申請日')
    approval_date = Column('approval_date', TIMESTAMP, nullable=True, comment='承認日')
    application_status = Column('application_status', EnumType(enum_class=ApplicationStatus), nullable=False, comment='申請書状態')
    applicant_status = Column('applicant_status', EnumType(enum_class=ApplicantStatus), nullable=True, comment='申請者状態')
    route_type = Column('route_type', Integer, nullable=True, comment='ルートタイプ')
    route_number = Column('route_number', Integer, nullable=True, comment='ルートナンバー')
    approverl_company_code = Column('approverl_company_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='承認者の会社コード')
    approverl_company_name = Column('approverl_company_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='承認者の会社名')
    approverl_role_code = Column('approverl_role_code', String(30, collation='ja_JP.utf8'), nullable=True, comment='承認者の利用権限コード')
    approverl_role_name = Column('approverl_role_name', String(30, collation='ja_JP.utf8'), nullable=True, comment='承認者の利用権限名')
    approverl_group_code = Column('approverl_group_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='承認者の部署コード')
    approverl_group_name = Column('approverl_group_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='承認者の部署名')
    approverl_employee_code = Column('approverl_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='承認者の従業員番号')
    approverl_employee_name = Column('approverl_employee_name', String(30, collation='ja_JP.utf8'), nullable=True, comment='承認者')
    deputy_approverl_company_code = Column('deputy_approverl_company_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='代理承認者の会社コード')
    deputy_approverl_company_name = Column('deputy_approverl_company_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='代理承認者の会社名')
    deputy_approverl_group_code = Column('deputy_approverl_group_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='代理承認者の部署コード')
    deputy_approverl_group_name = Column('deputy_approverl_group_name', String(50, collation='ja_JP.utf8'), nullable=True, comment='代理承認者の部署名')
    deputy_approverl_employee_code = Column('deputy_approverl_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='代理承認者の従業員番号')
    deputy_approverl_employee_name = Column('deputy_approverl_employee_name', String(30, collation='ja_JP.utf8'), nullable=True, comment='代理承認者')
    deputy_contents = Column('deputy_contents', String(255, collation='ja_JP.utf8'), nullable=True, comment='依頼理由')
    function = Column('function', EnumType(enum_class=ApprovalFunction), nullable=True, comment='承認画面の機能')
    reaching_date = Column('reaching_date', TIMESTAMP, nullable=True, comment='到達日')
    process_date = Column('process_date', TIMESTAMP, nullable=True, comment='処理日')
    activity_status = Column('activity_status', EnumType(enum_class=ActivityStatus), nullable=True, comment='承認者状態')
    approverl_comment = Column('approverl_comment', String(255, collation='ja_JP.utf8'), nullable=True, comment='承認者のコメント')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_route_history', "company_code", "application_number", "route_type", "route_number", "approverl_company_code", "approverl_group_code", "approverl_employee_code"), Index('ix_t_route_history_1', "company_code"), Index('ix_t_route_history_2', "company_code", "application_number"), UniqueConstraint("id"), )


class AllApproverl(Base):
    """
    一括承認オブジェクト
    """
    __tablename__ = "t_all_approverl"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    screen_mode = Column('screen_mode', EnumType(enum_class=ScreenMode), nullable=False, comment='画面モード')
    route_type = Column('route_type', Integer, nullable=False, comment='ルートタイプ')
    route_number = Column('route_number', Integer, nullable=False, comment='ルートナンバー')
    target_company_code = Column('target_company_code', String(10, collation='ja_JP.utf8'), comment='対象者の会社コード')
    target_group_code = Column('target_group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='対象者の部署コード')
    target_employee_code = Column('target_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='対象者の従業員番号')
    approverl_company_code = Column('approverl_company_code', String(10, collation='ja_JP.utf8'), comment='承認者の会社コード')
    approverl_role_code = Column('approverl_role_code', String(30, collation='ja_JP.utf8'), nullable=True, comment='承認者の利用権限コード')
    approverl_group_code = Column('approverl_group_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='承認者の部署コード')
    approverl_employee_code = Column('approverl_employee_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='承認者の従業員番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_all_approverl', "company_code", "application_number", "route_type", "route_number", "approverl_company_code", "approverl_group_code", "approverl_employee_code"), Index('ix_t_all_approverl_1', "company_code"), UniqueConstraint("company_code", "application_number", "route_type", "route_number", "approverl_company_code", "approverl_group_code", "approverl_employee_code"), )



class StampingCorrectionByThirdParty(Base):
    """
    第三者打刻補正トラン
    """
    __tablename__ = "t_stamping_correction_by_third_party"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    work_schedule_code = Column('work_schedule_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='勤務体系コード')
    stamping_start_time = Column('stamping_start_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='出勤時間')
    stamping_end_time = Column('stamping_end_time', String(5, collation='ja_JP.utf8'), nullable=True, comment='退勤時間')
    telework_flg = Column('telework_flg', Boolean, nullable=True, comment='テレワークフラグ')
    imprint_correction_content = Column('imprint_correction_content', String(100, collation='ja_JP.utf8'), nullable=True, comment='補正理由')
    re_correction_stamping_start_time = Column('re_correction_stamping_start_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='補正前打刻出勤時間')
    re_correction_stamping_end_time = Column('re_correction_stamping_end_time', String(8, collation='ja_JP.utf8'), nullable=True, comment='補正前打刻退勤時間')
    re_telework_change_flg = Column('re_telework_change_flg', Boolean, nullable=True, comment='補正前テレワーク変更フラグ')
    correction_company_code = Column('correction_company_code', String(10, collation='ja_JP.utf8'), comment='補正者の会社コード')
    correction_group_code = Column('correction_group_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='補正者の部署コード')
    correction_employee_code = Column('correction_employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='補正者の従業員番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_stamping_correction_by_third_party', "company_code", "employee_code", "target_date"), Index('ix_t_stamping_correction_by_third_party_1', "company_code"), UniqueConstraint("company_code"), )





class AlternativeHoliday(Base):
    """
    従業員別代替休暇トラン
    代替休暇を管理します。
    """
    __tablename__ = "t_alternative_holiday"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    payment_date = Column('payment_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='支給年月日')
    alternative_holiday_times = Column('alternative_holiday_times', Float, nullable=False, comment='代替休暇時間数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_alternative_holiday', "company_code", "employee_code", "payment_date"), Index('ix_t_alternative_holiday_1', "company_code"), Index('ix_t_alternative_holiday_2', "employee_code"), UniqueConstraint("company_code", "employee_code", "payment_date"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']),)


class PaidLeaveEmployeeDetail(Base):
    """
    従業員別有給支給年別勘定復旧トラン
    """
    __tablename__ = "t_paid_leave_employee_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    payment_date = Column('payment_date', Date, nullable=False, comment='支給年月日')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    get_days = Column('get_days', Float, nullable=True, comment='取得日数')
    get_times = Column('get_times', Integer, nullable=True, comment='取得時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_paid_leave_employee_detail', "company_code", "application_number", "payment_date"), Index('ix_t_paid_leave_employee_detail_1', "company_code"), Index('ix_t_paid_leave_employee_detail_2', "company_code", "application_number"), UniqueConstraint("company_code", "application_number", "payment_date"),)


class DashBoardMemo(Base):
    """
    ダッシュボードメモトラン
    """
    __tablename__ = "t_dash_board_memo"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    memo = Column('memo', String(500, collation='ja_JP.utf8'), nullable=True, comment='メモ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_dash_board_memo', "company_code", "employee_code"), Index('ix_t_dash_board_memo_1', "company_code"), Index('ix_t_dash_board_memo_2', "employee_code"), UniqueConstraint("company_code", "employee_code"), )



class EmployeePaySlip(Base):
    """
    給与明細トラン
    従業員の給与明細を管理します。
    """
    __tablename__ = "t_employee_pay_slip"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    term_from = Column('term_from', Date, nullable=True, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    real_total_minutes = Column('real_total_minutes', Integer, nullable=False, comment='労働時間')
    job_total_days = Column('job_total_days', Integer, nullable=False, comment='所定労働日数')
    absent_total_days = Column('absent_total_days', Integer, nullable=False, comment='欠勤日数')
    standard_job_minutes = Column('standard_job_minutes', Integer, nullable=True, comment='標準所定労働時間')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=False, comment='所定労働時間')
    job_overwork_minutes = Column('job_overwork_minutes', Integer, nullable=False, comment='所定外労働時間')
    job_holiday_days = Column('job_holiday_days', Integer, nullable=False, comment='所定休日労働日数')
    job_holiday_hours = Column('job_holiday_hours', Integer, nullable=False, comment='所定休日労働時間')
    legal_job_minutes = Column('legal_job_minutes', Integer, nullable=False, comment='法定労働時間')
    standard_legal_minutes = Column('standard_legal_minutes', Integer, nullable=True, comment='標準法定労働時間')
    legal_overwork_minutes = Column('legal_overwork_minutes', Integer, nullable=False, comment='法定外労働時間')
    legal_holiday_overwork_days = Column('legal_holiday_overwork_days', Integer, nullable=False, comment='法定休日労働日数')
    legal_holiday_overwork_minutes = Column('legal_holiday_overwork_minutes', Integer, nullable=False, comment='法定休日労働時間')
    late_night_overwork_minutes = Column('late_night_overwork_minutes', Integer, nullable=False, comment='深夜労働時間')
    break_minutes = Column('break_minutes', Integer, nullable=False, comment='休憩時間')
    late_days = Column('late_days', Integer, nullable=False, comment='遅刻回数')
    late_minutes = Column('late_minutes', Integer, nullable=False, comment='遅刻時間')
    early_departure_days = Column('early_departure_days', Integer, nullable=False, comment='早退回数')
    early_departure_minutes = Column('early_departure_minutes', Integer, nullable=False, comment='早退時間')
    paid_holiday_days = Column('paid_holiday_days', Float, nullable=False, comment='有給日数')
    paid_holiday_hours = Column('paid_holiday_hours', Integer, comment='有給時間数')
    child_time_leave_days = Column('child_time_leave_days', Float, nullable=True, comment='育児休暇日数')
    child_time_leave_hours = Column('child_time_leave_hours', Integer, nullable=True, comment='育児時間休暇数')
    compensatory_holiday_days = Column('compensatory_holiday_days', Integer, nullable=False, comment='代休日数')
    leave_days = Column('leave_days', Integer, nullable=True, comment='休職日数')
    closed_days = Column('closed_days', Integer, nullable=False, comment='休業日数')
    blackout_days = Column('blackout_days', Integer, nullable=True, comment='除外日数')
    legal_within_45_overwork_minutes = Column('legal_within_45_overwork_minutes', Integer, nullable=False, comment='45時間以内の法定外労働時間')
    legal_45_overwork_minutes = Column('legal_45_overwork_minutes', Integer, nullable=False, comment='45時間を超過した法定外労働時間')
    legal_60_overwork_minutes = Column('legal_60_overwork_minutes', Integer, nullable=False, comment='60時間を超過した法定外労働時間')
    lack_minutes = Column('lack_minutes', Integer, nullable=False, comment='集計期間の不足時間(給与控除が必要な時間)')
    estimated_overtime_hours = Column('estimated_overtime_hours', Integer, nullable=True, comment='見込み残業時間')
    telework_count = Column('telework_count', Integer, nullable=True, comment='テレワーク回数')
    alternative_leave_flg = Column('alternative_leave_flg', Boolean, nullable=True, comment='代替休暇取得フラグ')
    layout_code = Column('layout_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='レイアウトコード')
    payment_salary_item_code1 = Column('payment_salary_item_code1', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード1')
    payment_salary_item_name1 = Column('payment_salary_item_name1', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名1')
    payment_salary_item_code1_amount = Column('payment_salary_item_code1_amount', Integer, nullable=True, comment='支給給与項目コード1　金額')
    payment_salary_item_code2 = Column('payment_salary_item_code2', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード2')
    payment_salary_item_name2 = Column('payment_salary_item_name2', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名2')
    payment_salary_item_code2_amount = Column('payment_salary_item_code2_amount', Integer, nullable=True, comment='支給給与項目コード2　金額')
    payment_salary_item_code3 = Column('payment_salary_item_code3', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード3')
    payment_salary_item_name3 = Column('payment_salary_item_name3', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名3')
    payment_salary_item_code3_amount = Column('payment_salary_item_code3_amount', Integer, nullable=True, comment='支給給与項目コード3　金額')
    payment_salary_item_code4 = Column('payment_salary_item_code4', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード4')
    payment_salary_item_name4 = Column('payment_salary_item_name4', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名4')
    payment_salary_item_code4_amount = Column('payment_salary_item_code4_amount', Integer, nullable=True, comment='支給給与項目コード4　金額')
    payment_salary_item_code5 = Column('payment_salary_item_code5', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード5')
    payment_salary_item_name5 = Column('payment_salary_item_name5', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名5')
    payment_salary_item_code5_amount = Column('payment_salary_item_code5_amount', Integer, nullable=True, comment='支給給与項目コード5　金額')
    payment_salary_item_code6 = Column('payment_salary_item_code6', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード6')
    payment_salary_item_name6 = Column('payment_salary_item_name6', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名6')
    payment_salary_item_code6_amount = Column('payment_salary_item_code6_amount', Integer, nullable=True, comment='支給給与項目コード6　金額')
    payment_salary_item_code7 = Column('payment_salary_item_code7', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード7')
    payment_salary_item_name7 = Column('payment_salary_item_name7', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名7')
    payment_salary_item_code7_amount = Column('payment_salary_item_code7_amount', Integer, nullable=True, comment='支給給与項目コード7　金額')
    payment_salary_item_code8 = Column('payment_salary_item_code8', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード8')
    payment_salary_item_name8 = Column('payment_salary_item_name8', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名8')
    payment_salary_item_code8_amount = Column('payment_salary_item_code8_amount', Integer, nullable=True, comment='支給給与項目コード8　金額')
    payment_salary_item_code9 = Column('payment_salary_item_code9', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード9')
    payment_salary_item_name9 = Column('payment_salary_item_name9', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名9')
    payment_salary_item_code9_amount = Column('payment_salary_item_code9_amount', Integer, nullable=True, comment='支給給与項目コード9　金額')
    payment_salary_item_code10 = Column('payment_salary_item_code10', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード10')
    payment_salary_item_name10 = Column('payment_salary_item_name10', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名10')
    payment_salary_item_code10_amount = Column('payment_salary_item_code10_amount', Integer, nullable=True, comment='支給給与項目コード10　金額')
    payment_salary_item_code11 = Column('payment_salary_item_code11', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード11')
    payment_salary_item_name11 = Column('payment_salary_item_name11', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名11')
    payment_salary_item_code11_amount = Column('payment_salary_item_code11_amount', Integer, nullable=True, comment='支給給与項目コード11　金額')
    payment_salary_item_code12 = Column('payment_salary_item_code12', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード12')
    payment_salary_item_name12 = Column('payment_salary_item_name12', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名12')
    payment_salary_item_code12_amount = Column('payment_salary_item_code12_amount', Integer, nullable=True, comment='支給給与項目コード12　金額')
    payment_salary_item_code13 = Column('payment_salary_item_code13', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード13')
    payment_salary_item_name13 = Column('payment_salary_item_name13', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名13')
    payment_salary_item_code13_amount = Column('payment_salary_item_code13_amount', Integer, nullable=True, comment='支給給与項目コード13　金額')
    payment_salary_item_code14 = Column('payment_salary_item_code14', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード14')
    payment_salary_item_name14 = Column('payment_salary_item_name14', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名14')
    payment_salary_item_code14_amount = Column('payment_salary_item_code14_amount', Integer, nullable=True, comment='支給給与項目コード14　金額')
    payment_salary_item_code15 = Column('payment_salary_item_code15', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード15')
    payment_salary_item_name15 = Column('payment_salary_item_name15', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名15')
    payment_salary_item_code15_amount = Column('payment_salary_item_code15_amount', Integer, nullable=True, comment='支給給与項目コード15　金額')
    payment_salary_item_code16 = Column('payment_salary_item_code16', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード16')
    payment_salary_item_name16 = Column('payment_salary_item_name16', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名16')
    payment_salary_item_code16_amount = Column('payment_salary_item_code16_amount', Integer, nullable=True, comment='支給給与項目コード16　金額')
    payment_salary_item_code17 = Column('payment_salary_item_code17', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード17')
    payment_salary_item_name17 = Column('payment_salary_item_name17', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名17')
    payment_salary_item_code17_amount = Column('payment_salary_item_code17_amount', Integer, nullable=True, comment='支給給与項目コード17　金額')
    payment_salary_item_code18 = Column('payment_salary_item_code18', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード18')
    payment_salary_item_name18 = Column('payment_salary_item_name18', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名18')
    payment_salary_item_code18_amount = Column('payment_salary_item_code18_amount', Integer, nullable=True, comment='支給給与項目コード18　金額')
    payment_salary_item_code19 = Column('payment_salary_item_code19', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード19')
    payment_salary_item_name19 = Column('payment_salary_item_name19', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名19')
    payment_salary_item_code19_amount = Column('payment_salary_item_code19_amount', Integer, nullable=True, comment='支給給与項目コード19　金額')
    payment_salary_item_code20 = Column('payment_salary_item_code20', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード20')
    payment_salary_item_name20 = Column('payment_salary_item_name20', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名20')
    payment_salary_item_code20_amount = Column('payment_salary_item_code20_amount', Integer, nullable=True, comment='支給給与項目コード20　金額')
    payment_salary_item_code21 = Column('payment_salary_item_code21', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード21')
    payment_salary_item_name21 = Column('payment_salary_item_name21', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名21')
    payment_salary_item_code21_amount = Column('payment_salary_item_code21_amount', Integer, nullable=True, comment='支給給与項目コード21　金額')
    payment_salary_item_code22 = Column('payment_salary_item_code22', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード22')
    payment_salary_item_name22 = Column('payment_salary_item_name22', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名22')
    payment_salary_item_code22_amount = Column('payment_salary_item_code22_amount', Integer, nullable=True, comment='支給給与項目コード22　金額')
    payment_salary_item_code23 = Column('payment_salary_item_code23', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード23')
    payment_salary_item_name23 = Column('payment_salary_item_name23', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名23')
    payment_salary_item_code23_amount = Column('payment_salary_item_code23_amount', Integer, nullable=True, comment='支給給与項目コード23　金額')
    payment_salary_item_code24 = Column('payment_salary_item_code24', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード24')
    payment_salary_item_name24 = Column('payment_salary_item_name24', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名24')
    payment_salary_item_code24_amount = Column('payment_salary_item_code24_amount', Integer, nullable=True, comment='支給給与項目コード24　金額')
    payment_salary_item_code25 = Column('payment_salary_item_code25', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード25')
    payment_salary_item_name25 = Column('payment_salary_item_name25', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名25')
    payment_salary_item_code25_amount = Column('payment_salary_item_code25_amount', Integer, nullable=True, comment='支給給与項目コード25　金額')
    payment_salary_item_code26 = Column('payment_salary_item_code26', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード26')
    payment_salary_item_name26 = Column('payment_salary_item_name26', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名26')
    payment_salary_item_code26_amount = Column('payment_salary_item_code26_amount', Integer, nullable=True, comment='支給給与項目コード26　金額')
    payment_salary_item_code27 = Column('payment_salary_item_code27', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード27')
    payment_salary_item_name27 = Column('payment_salary_item_name27', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名27')
    payment_salary_item_code27_amount = Column('payment_salary_item_code27_amount', Integer, nullable=True, comment='支給給与項目コード27　金額')
    payment_salary_item_code28 = Column('payment_salary_item_code28', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード28')
    payment_salary_item_name28 = Column('payment_salary_item_name28', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名28')
    payment_salary_item_code28_amount = Column('payment_salary_item_code28_amount', Integer, nullable=True, comment='支給給与項目コード28　金額')
    payment_salary_item_code29 = Column('payment_salary_item_code29', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード29')
    payment_salary_item_name29 = Column('payment_salary_item_name29', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名29')
    payment_salary_item_code29_amount = Column('payment_salary_item_code29_amount', Integer, nullable=True, comment='支給給与項目コード29　金額')
    payment_salary_item_code30 = Column('payment_salary_item_code30', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード30')
    payment_salary_item_name30 = Column('payment_salary_item_name30', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名30')
    payment_salary_item_code30_amount = Column('payment_salary_item_code30_amount', Integer, nullable=True, comment='支給給与項目コード30　金額')
    deduction_salary_item_code1 = Column('deduction_salary_item_code1', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード1')
    deduction_salary_item_name1 = Column('deduction_salary_item_name1', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名1')
    deduction_salary_item_code1_amount = Column('deduction_salary_item_code1_amount', Integer, nullable=True, comment='控除給与項目コード1　金額')
    deduction_salary_item_code2 = Column('deduction_salary_item_code2', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード2')
    deduction_salary_item_name2 = Column('deduction_salary_item_name2', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名2')
    deduction_salary_item_code2_amount = Column('deduction_salary_item_code2_amount', Integer, nullable=True, comment='控除給与項目コード2　金額')
    deduction_salary_item_code3 = Column('deduction_salary_item_code3', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード3')
    deduction_salary_item_name3 = Column('deduction_salary_item_name3', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名3')
    deduction_salary_item_code3_amount = Column('deduction_salary_item_code3_amount', Integer, nullable=True, comment='控除給与項目コード3　金額')
    deduction_salary_item_code4 = Column('deduction_salary_item_code4', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード4')
    deduction_salary_item_name4 = Column('deduction_salary_item_name4', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名4')
    deduction_salary_item_code4_amount = Column('deduction_salary_item_code4_amount', Integer, nullable=True, comment='控除給与項目コード4　金額')
    deduction_salary_item_code5 = Column('deduction_salary_item_code5', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード5')
    deduction_salary_item_name5 = Column('deduction_salary_item_name5', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名5')
    deduction_salary_item_code5_amount = Column('deduction_salary_item_code5_amount', Integer, nullable=True, comment='控除給与項目コード5　金額')
    deduction_salary_item_code6 = Column('deduction_salary_item_code6', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード6')
    deduction_salary_item_name6 = Column('deduction_salary_item_name6', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名6')
    deduction_salary_item_code6_amount = Column('deduction_salary_item_code6_amount', Integer, nullable=True, comment='控除給与項目コード6　金額')
    deduction_salary_item_code7 = Column('deduction_salary_item_code7', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード7')
    deduction_salary_item_name7 = Column('deduction_salary_item_name7', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名7')
    deduction_salary_item_code7_amount = Column('deduction_salary_item_code7_amount', Integer, nullable=True, comment='控除給与項目コード7　金額')
    deduction_salary_item_code8 = Column('deduction_salary_item_code8', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード8')
    deduction_salary_item_name8 = Column('deduction_salary_item_name8', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名8')
    deduction_salary_item_code8_amount = Column('deduction_salary_item_code8_amount', Integer, nullable=True, comment='控除給与項目コード8　金額')
    deduction_salary_item_code9 = Column('deduction_salary_item_code9', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード9')
    deduction_salary_item_name9 = Column('deduction_salary_item_name9', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名9')
    deduction_salary_item_code9_amount = Column('deduction_salary_item_code9_amount', Integer, nullable=True, comment='控除給与項目コード9　金額')
    deduction_salary_item_code10 = Column('deduction_salary_item_code10', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード10')
    deduction_salary_item_name10 = Column('deduction_salary_item_name10', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名10')
    deduction_salary_item_code10_amount = Column('deduction_salary_item_code10_amount', Integer, nullable=True, comment='控除給与項目コード11　金額')
    deduction_salary_item_code11 = Column('deduction_salary_item_code11', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード11')
    deduction_salary_item_name11 = Column('deduction_salary_item_name11', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名11')
    deduction_salary_item_code11_amount = Column('deduction_salary_item_code11_amount', Integer, nullable=True, comment='控除給与項目コード11　金額')
    deduction_salary_item_code12 = Column('deduction_salary_item_code12', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード12')
    deduction_salary_item_name12 = Column('deduction_salary_item_name12', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名12')
    deduction_salary_item_code12_amount = Column('deduction_salary_item_code12_amount', Integer, nullable=True, comment='控除給与項目コード12　金額')
    deduction_salary_item_code13 = Column('deduction_salary_item_code13', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード13')
    deduction_salary_item_name13 = Column('deduction_salary_item_name13', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名13')
    deduction_salary_item_code13_amount = Column('deduction_salary_item_code13_amount', Integer, nullable=True, comment='控除給与項目コード13　金額')
    deduction_salary_item_code14 = Column('deduction_salary_item_code14', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード14')
    deduction_salary_item_name14 = Column('deduction_salary_item_name14', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名14')
    deduction_salary_item_code14_amount = Column('deduction_salary_item_code14_amount', Integer, nullable=True, comment='控除給与項目コード14　金額')
    deduction_salary_item_code15 = Column('deduction_salary_item_code15', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード15')
    deduction_salary_item_name15 = Column('deduction_salary_item_name15', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名15')
    deduction_salary_item_code15_amount = Column('deduction_salary_item_code15_amount', Integer, nullable=True, comment='控除給与項目コード15　金額')
    deduction_salary_item_code16 = Column('deduction_salary_item_code16', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード16')
    deduction_salary_item_name16 = Column('deduction_salary_item_name16', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名16')
    deduction_salary_item_code16_amount = Column('deduction_salary_item_code16_amount', Integer, nullable=True, comment='控除給与項目コード16　金額')
    deduction_salary_item_code17 = Column('deduction_salary_item_code17', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード17')
    deduction_salary_item_name17 = Column('deduction_salary_item_name17', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名17')
    deduction_salary_item_code17_amount = Column('deduction_salary_item_code17_amount', Integer, nullable=True, comment='控除給与項目コード17　金額')
    deduction_salary_item_code18 = Column('deduction_salary_item_code18', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード18')
    deduction_salary_item_name18 = Column('deduction_salary_item_name18', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名18')
    deduction_salary_item_code18_amount = Column('deduction_salary_item_code18_amount', Integer, nullable=True, comment='控除給与項目コード18　金額')
    deduction_salary_item_code19 = Column('deduction_salary_item_code19', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード19')
    deduction_salary_item_name19 = Column('deduction_salary_item_name19', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名19')
    deduction_salary_item_code19_amount = Column('deduction_salary_item_code19_amount', Integer, nullable=True, comment='控除給与項目コード19　金額')
    deduction_salary_item_code20 = Column('deduction_salary_item_code20', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード20')
    deduction_salary_item_name20 = Column('deduction_salary_item_name20', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名20')
    deduction_salary_item_code20_amount = Column('deduction_salary_item_code20_amount', Integer, nullable=True, comment='控除給与項目コード20　金額')
    deduction_salary_item_code21 = Column('deduction_salary_item_code21', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード21')
    deduction_salary_item_name21 = Column('deduction_salary_item_name21', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名21')
    deduction_salary_item_code21_amount = Column('deduction_salary_item_code21_amount', Integer, nullable=True, comment='控除給与項目コード21　金額')
    deduction_salary_item_code22 = Column('deduction_salary_item_code22', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード22')
    deduction_salary_item_name22 = Column('deduction_salary_item_name22', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名22')
    deduction_salary_item_code22_amount = Column('deduction_salary_item_code22_amount', Integer, nullable=True, comment='控除給与項目コード22　金額')
    deduction_salary_item_code23 = Column('deduction_salary_item_code23', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード23')
    deduction_salary_item_name23 = Column('deduction_salary_item_name23', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名23')
    deduction_salary_item_code23_amount = Column('deduction_salary_item_code23_amount', Integer, nullable=True, comment='控除給与項目コード23　金額')
    deduction_salary_item_code24 = Column('deduction_salary_item_code24', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード24')
    deduction_salary_item_name24 = Column('deduction_salary_item_name24', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名24')
    deduction_salary_item_code24_amount = Column('deduction_salary_item_code24_amount', Integer, nullable=True, comment='控除給与項目コード24　金額')
    deduction_salary_item_code25 = Column('deduction_salary_item_code25', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード25')
    deduction_salary_item_name25 = Column('deduction_salary_item_name25', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名25')
    deduction_salary_item_code25_amount = Column('deduction_salary_item_code25_amount', Integer, nullable=True, comment='控除給与項目コード25　金額')
    deduction_salary_item_code26 = Column('deduction_salary_item_code26', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード26')
    deduction_salary_item_name26 = Column('deduction_salary_item_name26', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名26')
    deduction_salary_item_code26_amount = Column('deduction_salary_item_code26_amount', Integer, nullable=True, comment='控除給与項目コード26　金額')
    deduction_salary_item_code27 = Column('deduction_salary_item_code27', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード27')
    deduction_salary_item_name27 = Column('deduction_salary_item_name27', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名27')
    deduction_salary_item_code27_amount = Column('deduction_salary_item_code27_amount', Integer, nullable=True, comment='控除給与項目コード27　金額')
    deduction_salary_item_code28 = Column('deduction_salary_item_code28', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード28')
    deduction_salary_item_name28 = Column('deduction_salary_item_name28', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名28')
    deduction_salary_item_code28_amount = Column('deduction_salary_item_code28_amount', Integer, nullable=True, comment='控除給与項目コード28　金額')
    deduction_salary_item_code29 = Column('deduction_salary_item_code29', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード29')
    deduction_salary_item_name29 = Column('deduction_salary_item_name29', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名29')
    deduction_salary_item_code29_amount = Column('deduction_salary_item_code29_amount', Integer, nullable=True, comment='控除給与項目コード29　金額')
    deduction_salary_item_code30 = Column('deduction_salary_item_code30', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード30')
    deduction_salary_item_name30 = Column('deduction_salary_item_name30', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名30')
    deduction_salary_item_code30_amount = Column('deduction_salary_item_code30_amount', Integer, nullable=True, comment='控除給与項目コード30　金額')
    is_general_health_insurance_hand_type = Column('is_general_health_insurance_hand_type', String(1, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[健康保険　一般]')
    general_health_insurance = Column('general_health_insurance', Integer, nullable=True, comment='健康保険　基本')
    is_health_insurance_adjustment_hand_type = Column('is_health_insurance_adjustment_hand_type', String(1, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[健康保険　調整]')
    health_insurance_adjustment = Column('health_insurance_adjustment', Integer, nullable=True, comment='健康保険　特定')
    is_care_insurance_hand_type = Column('is_care_insurance_hand_type', String(1, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[介護保険]')
    care_insurance = Column('care_insurance', Integer, nullable=True, comment='介護保険')
    taxable_amount = Column('taxable_amount', Integer, nullable=False, comment='給与所得額')
    taxable_amount_2 = Column('taxable_amount_2', Integer, nullable=False, comment='課税対象額')
    employement_insurance_amount = Column('employement_insurance_amount', Integer, nullable=False, comment='雇用保険対象額')
    social_insurance_amount = Column('social_insurance_amount', Integer, nullable=False, comment='社会保険対象額')
    social_insurance_total = Column('social_insurance_total', Integer, nullable=False, comment='社会保険計')
    total_payment_amount = Column('total_payment_amount', Integer, nullable=False, comment='支給額合計')
    total_deduction_amount = Column('total_deduction_amount', Integer, nullable=False, comment='控除額合計')
    deduction_amount = Column('deduction_amount', Integer, nullable=False, comment='差引支給額')
    electoric_money_amount = Column('electoric_money_amount', Integer, nullable=True, comment='電子マネー振込額')
    first_transfer_amount = Column('first_transfer_amount', Integer, nullable=True, comment='第一振込先　金額')
    second_transfer_amount = Column('second_transfer_amount', Integer, nullable=True, comment='第二振込先　金額')
    cash_payment_amount = Column('cash_payment_amount', Integer, nullable=False, comment='現金支給額')
    in_kind_payment_amount = Column('in_kind_payment_amount', Integer, nullable=False, comment='現物支給額')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    date_of_sending_pay_slip = Column('date_of_sending_pay_slip', TIMESTAMP, nullable=True, comment='送信日')
    current_grade = Column('current_grade', Integer, nullable=True, comment='現在の等級')
    employee_classification_type = Column('employee_classification_type', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ')
    is_payment_hand_type = Column('is_payment_hand_type', String(30, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[支給項目]')
    is_deduction_hand_type = Column('is_deduction_hand_type', String(30, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[控除項目]')
    trail_update_date = Column('trail_update_date', TIMESTAMP, nullable=True)
    trail_update_employee_code = Column('trail_update_employee_code', String(10, collation='ja_JP.utf8'), nullable=True)
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_pay_slip', "company_code", "employee_code", "target_date"), Index('ix_t_employee_pay_slip_1', "company_code"), UniqueConstraint("company_code", "employee_code", "target_date"),)


class ReserveSendPaySlip(Base):
    """
    給与明細送信予約トラン
    従業員の給与明細のメール送信予約状況を管理します。
    """
    __tablename__ = "t_reserve_send_pay_slip"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(9, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    date_of_sending_pay_slip = Column('date_of_sending_pay_slip', Date, nullable=True, comment='送信日')
    salary_bonus_classification = Column('salary_bonus_classification', EnumType(enum_class=SalaryBonusClassification), nullable=False, comment='支給区分')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_reserve_send_pay_slip', "company_code", "employee_code", "target_date", "salary_bonus_classification"), Index('ix_t_reserve_send_pay_slip_1', "company_code"), UniqueConstraint("company_code", "employee_code", "target_date", "salary_bonus_classification"),)


class EmployeeBonusPaySlipHeader(Base):
    """
    賞与明細キートラン
    従業員の賞与明細を管理します。
    """
    __tablename__ = "t_employee_bonus_pay_slip_header"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    target_date = Column('target_date', String(9, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    bonus_pay_slip_name = Column('bonus_pay_slip_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='賞与支給名称')
    employee_pay_slip_target_date = Column('employee_pay_slip_target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='直近給与月')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_bonus_pay_slip_header', "company_code", "target_date"), Index('ix_t_employee_bonus_pay_slip_header_1', "company_code"), UniqueConstraint("company_code", "target_date"),)


class EmployeeBonusPaySlip(Base):
    """
    賞与明細トラン
    従業員の賞与明細を管理します。
    """
    __tablename__ = "t_employee_bonus_pay_slip"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(9, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    term_from = Column('term_from', Date, nullable=True, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    layout_code = Column('layout_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='レイアウトコード')
    payment_salary_item_code1 = Column('payment_salary_item_code1', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード1')
    payment_salary_item_name1 = Column('payment_salary_item_name1', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名1')
    payment_salary_item_code1_amount = Column('payment_salary_item_code1_amount', Integer, nullable=True, comment='支給給与項目コード1　金額')
    payment_salary_item_code2 = Column('payment_salary_item_code2', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード2')
    payment_salary_item_name2 = Column('payment_salary_item_name2', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名2')
    payment_salary_item_code2_amount = Column('payment_salary_item_code2_amount', Integer, nullable=True, comment='支給給与項目コード2　金額')
    payment_salary_item_code3 = Column('payment_salary_item_code3', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード3')
    payment_salary_item_name3 = Column('payment_salary_item_name3', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名3')
    payment_salary_item_code3_amount = Column('payment_salary_item_code3_amount', Integer, nullable=True, comment='支給給与項目コード3　金額')
    payment_salary_item_code4 = Column('payment_salary_item_code4', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード4')
    payment_salary_item_name4 = Column('payment_salary_item_name4', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名4')
    payment_salary_item_code4_amount = Column('payment_salary_item_code4_amount', Integer, nullable=True, comment='支給給与項目コード4　金額')
    payment_salary_item_code5 = Column('payment_salary_item_code5', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード5')
    payment_salary_item_name5 = Column('payment_salary_item_name5', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名5')
    payment_salary_item_code5_amount = Column('payment_salary_item_code5_amount', Integer, nullable=True, comment='支給給与項目コード5　金額')
    payment_salary_item_code6 = Column('payment_salary_item_code6', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード6')
    payment_salary_item_name6 = Column('payment_salary_item_name6', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名6')
    payment_salary_item_code6_amount = Column('payment_salary_item_code6_amount', Integer, nullable=True, comment='支給給与項目コード6　金額')
    payment_salary_item_code7 = Column('payment_salary_item_code7', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード7')
    payment_salary_item_name7 = Column('payment_salary_item_name7', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名7')
    payment_salary_item_code7_amount = Column('payment_salary_item_code7_amount', Integer, nullable=True, comment='支給給与項目コード7　金額')
    payment_salary_item_code8 = Column('payment_salary_item_code8', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード8')
    payment_salary_item_name8 = Column('payment_salary_item_name8', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名8')
    payment_salary_item_code8_amount = Column('payment_salary_item_code8_amount', Integer, nullable=True, comment='支給給与項目コード8　金額')
    payment_salary_item_code9 = Column('payment_salary_item_code9', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード9')
    payment_salary_item_name9 = Column('payment_salary_item_name9', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名9')
    payment_salary_item_code9_amount = Column('payment_salary_item_code9_amount', Integer, nullable=True, comment='支給給与項目コード9　金額')
    payment_salary_item_code10 = Column('payment_salary_item_code10', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード10')
    payment_salary_item_name10 = Column('payment_salary_item_name10', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名10')
    payment_salary_item_code10_amount = Column('payment_salary_item_code10_amount', Integer, nullable=True, comment='支給給与項目コード10　金額')
    payment_salary_item_code11 = Column('payment_salary_item_code11', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード11')
    payment_salary_item_name11 = Column('payment_salary_item_name11', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名11')
    payment_salary_item_code11_amount = Column('payment_salary_item_code11_amount', Integer, nullable=True, comment='支給給与項目コード11　金額')
    payment_salary_item_code12 = Column('payment_salary_item_code12', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード12')
    payment_salary_item_name12 = Column('payment_salary_item_name12', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名12')
    payment_salary_item_code12_amount = Column('payment_salary_item_code12_amount', Integer, nullable=True, comment='支給給与項目コード12　金額')
    payment_salary_item_code13 = Column('payment_salary_item_code13', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード13')
    payment_salary_item_name13 = Column('payment_salary_item_name13', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名13')
    payment_salary_item_code13_amount = Column('payment_salary_item_code13_amount', Integer, nullable=True, comment='支給給与項目コード13　金額')
    payment_salary_item_code14 = Column('payment_salary_item_code14', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード14')
    payment_salary_item_name14 = Column('payment_salary_item_name14', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名14')
    payment_salary_item_code14_amount = Column('payment_salary_item_code14_amount', Integer, nullable=True, comment='支給給与項目コード14　金額')
    payment_salary_item_code15 = Column('payment_salary_item_code15', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード15')
    payment_salary_item_name15 = Column('payment_salary_item_name15', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名15')
    payment_salary_item_code15_amount = Column('payment_salary_item_code15_amount', Integer, nullable=True, comment='支給給与項目コード15　金額')
    payment_salary_item_code16 = Column('payment_salary_item_code16', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード16')
    payment_salary_item_name16 = Column('payment_salary_item_name16', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名16')
    payment_salary_item_code16_amount = Column('payment_salary_item_code16_amount', Integer, nullable=True, comment='支給給与項目コード16　金額')
    payment_salary_item_code17 = Column('payment_salary_item_code17', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード17')
    payment_salary_item_name17 = Column('payment_salary_item_name17', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名17')
    payment_salary_item_code17_amount = Column('payment_salary_item_code17_amount', Integer, nullable=True, comment='支給給与項目コード17　金額')
    payment_salary_item_code18 = Column('payment_salary_item_code18', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード18')
    payment_salary_item_name18 = Column('payment_salary_item_name18', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名18')
    payment_salary_item_code18_amount = Column('payment_salary_item_code18_amount', Integer, nullable=True, comment='支給給与項目コード18　金額')
    payment_salary_item_code19 = Column('payment_salary_item_code19', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード19')
    payment_salary_item_name19 = Column('payment_salary_item_name19', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名19')
    payment_salary_item_code19_amount = Column('payment_salary_item_code19_amount', Integer, nullable=True, comment='支給給与項目コード19　金額')
    payment_salary_item_code20 = Column('payment_salary_item_code20', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード20')
    payment_salary_item_name20 = Column('payment_salary_item_name20', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名20')
    payment_salary_item_code20_amount = Column('payment_salary_item_code20_amount', Integer, nullable=True, comment='支給給与項目コード20　金額')
    payment_salary_item_code21 = Column('payment_salary_item_code21', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード21')
    payment_salary_item_name21 = Column('payment_salary_item_name21', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名21')
    payment_salary_item_code21_amount = Column('payment_salary_item_code21_amount', Integer, nullable=True, comment='支給給与項目コード21　金額')
    payment_salary_item_code22 = Column('payment_salary_item_code22', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード22')
    payment_salary_item_name22 = Column('payment_salary_item_name22', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名22')
    payment_salary_item_code22_amount = Column('payment_salary_item_code22_amount', Integer, nullable=True, comment='支給給与項目コード22　金額')
    payment_salary_item_code23 = Column('payment_salary_item_code23', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード23')
    payment_salary_item_name23 = Column('payment_salary_item_name23', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名23')
    payment_salary_item_code23_amount = Column('payment_salary_item_code23_amount', Integer, nullable=True, comment='支給給与項目コード23　金額')
    payment_salary_item_code24 = Column('payment_salary_item_code24', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード24')
    payment_salary_item_name24 = Column('payment_salary_item_name24', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名24')
    payment_salary_item_code24_amount = Column('payment_salary_item_code24_amount', Integer, nullable=True, comment='支給給与項目コード24　金額')
    payment_salary_item_code25 = Column('payment_salary_item_code25', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード25')
    payment_salary_item_name25 = Column('payment_salary_item_name25', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名25')
    payment_salary_item_code25_amount = Column('payment_salary_item_code25_amount', Integer, nullable=True, comment='支給給与項目コード25　金額')
    payment_salary_item_code26 = Column('payment_salary_item_code26', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード26')
    payment_salary_item_name26 = Column('payment_salary_item_name26', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名26')
    payment_salary_item_code26_amount = Column('payment_salary_item_code26_amount', Integer, nullable=True, comment='支給給与項目コード26　金額')
    payment_salary_item_code27 = Column('payment_salary_item_code27', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード27')
    payment_salary_item_name27 = Column('payment_salary_item_name27', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名27')
    payment_salary_item_code27_amount = Column('payment_salary_item_code27_amount', Integer, nullable=True, comment='支給給与項目コード27　金額')
    payment_salary_item_code28 = Column('payment_salary_item_code28', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード28')
    payment_salary_item_name28 = Column('payment_salary_item_name28', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名28')
    payment_salary_item_code28_amount = Column('payment_salary_item_code28_amount', Integer, nullable=True, comment='支給給与項目コード28　金額')
    payment_salary_item_code29 = Column('payment_salary_item_code29', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード29')
    payment_salary_item_name29 = Column('payment_salary_item_name29', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名29')
    payment_salary_item_code29_amount = Column('payment_salary_item_code29_amount', Integer, nullable=True, comment='支給給与項目コード29　金額')
    payment_salary_item_code30 = Column('payment_salary_item_code30', String(10, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目コード30')
    payment_salary_item_name30 = Column('payment_salary_item_name30', String(20, collation='ja_JP.utf8'), nullable=True, comment='支給給与項目名30')
    payment_salary_item_code30_amount = Column('payment_salary_item_code30_amount', Integer, nullable=True, comment='支給給与項目コード30　金額')
    deduction_salary_item_code1 = Column('deduction_salary_item_code1', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード1')
    deduction_salary_item_name1 = Column('deduction_salary_item_name1', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名1')
    deduction_salary_item_code1_amount = Column('deduction_salary_item_code1_amount', Integer, nullable=True, comment='控除給与項目コード1　金額')
    deduction_salary_item_code2 = Column('deduction_salary_item_code2', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード2')
    deduction_salary_item_name2 = Column('deduction_salary_item_name2', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名2')
    deduction_salary_item_code2_amount = Column('deduction_salary_item_code2_amount', Integer, nullable=True, comment='控除給与項目コード2　金額')
    deduction_salary_item_code3 = Column('deduction_salary_item_code3', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード3')
    deduction_salary_item_name3 = Column('deduction_salary_item_name3', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名3')
    deduction_salary_item_code3_amount = Column('deduction_salary_item_code3_amount', Integer, nullable=True, comment='控除給与項目コード3　金額')
    deduction_salary_item_code4 = Column('deduction_salary_item_code4', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード4')
    deduction_salary_item_name4 = Column('deduction_salary_item_name4', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名4')
    deduction_salary_item_code4_amount = Column('deduction_salary_item_code4_amount', Integer, nullable=True, comment='控除給与項目コード4　金額')
    deduction_salary_item_code5 = Column('deduction_salary_item_code5', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード5')
    deduction_salary_item_name5 = Column('deduction_salary_item_name5', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名5')
    deduction_salary_item_code5_amount = Column('deduction_salary_item_code5_amount', Integer, nullable=True, comment='控除給与項目コード5　金額')
    deduction_salary_item_code6 = Column('deduction_salary_item_code6', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード6')
    deduction_salary_item_name6 = Column('deduction_salary_item_name6', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名6')
    deduction_salary_item_code6_amount = Column('deduction_salary_item_code6_amount', Integer, nullable=True, comment='控除給与項目コード6　金額')
    deduction_salary_item_code7 = Column('deduction_salary_item_code7', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード7')
    deduction_salary_item_name7 = Column('deduction_salary_item_name7', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名7')
    deduction_salary_item_code7_amount = Column('deduction_salary_item_code7_amount', Integer, nullable=True, comment='控除給与項目コード7　金額')
    deduction_salary_item_code8 = Column('deduction_salary_item_code8', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード8')
    deduction_salary_item_name8 = Column('deduction_salary_item_name8', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名8')
    deduction_salary_item_code8_amount = Column('deduction_salary_item_code8_amount', Integer, nullable=True, comment='控除給与項目コード8　金額')
    deduction_salary_item_code9 = Column('deduction_salary_item_code9', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード9')
    deduction_salary_item_name9 = Column('deduction_salary_item_name9', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名9')
    deduction_salary_item_code9_amount = Column('deduction_salary_item_code9_amount', Integer, nullable=True, comment='控除給与項目コード9　金額')
    deduction_salary_item_code10 = Column('deduction_salary_item_code10', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード10')
    deduction_salary_item_name10 = Column('deduction_salary_item_name10', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名10')
    deduction_salary_item_code10_amount = Column('deduction_salary_item_code10_amount', Integer, nullable=True, comment='控除給与項目コード11　金額')
    deduction_salary_item_code11 = Column('deduction_salary_item_code11', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード11')
    deduction_salary_item_name11 = Column('deduction_salary_item_name11', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名11')
    deduction_salary_item_code11_amount = Column('deduction_salary_item_code11_amount', Integer, nullable=True, comment='控除給与項目コード11　金額')
    deduction_salary_item_code12 = Column('deduction_salary_item_code12', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード12')
    deduction_salary_item_name12 = Column('deduction_salary_item_name12', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名12')
    deduction_salary_item_code12_amount = Column('deduction_salary_item_code12_amount', Integer, nullable=True, comment='控除給与項目コード12　金額')
    deduction_salary_item_code13 = Column('deduction_salary_item_code13', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード13')
    deduction_salary_item_name13 = Column('deduction_salary_item_name13', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名13')
    deduction_salary_item_code13_amount = Column('deduction_salary_item_code13_amount', Integer, nullable=True, comment='控除給与項目コード13　金額')
    deduction_salary_item_code14 = Column('deduction_salary_item_code14', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード14')
    deduction_salary_item_name14 = Column('deduction_salary_item_name14', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名14')
    deduction_salary_item_code14_amount = Column('deduction_salary_item_code14_amount', Integer, nullable=True, comment='控除給与項目コード14　金額')
    deduction_salary_item_code15 = Column('deduction_salary_item_code15', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード15')
    deduction_salary_item_name15 = Column('deduction_salary_item_name15', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名15')
    deduction_salary_item_code15_amount = Column('deduction_salary_item_code15_amount', Integer, nullable=True, comment='控除給与項目コード15　金額')
    deduction_salary_item_code16 = Column('deduction_salary_item_code16', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード16')
    deduction_salary_item_name16 = Column('deduction_salary_item_name16', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名16')
    deduction_salary_item_code16_amount = Column('deduction_salary_item_code16_amount', Integer, nullable=True, comment='控除給与項目コード16　金額')
    deduction_salary_item_code17 = Column('deduction_salary_item_code17', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード17')
    deduction_salary_item_name17 = Column('deduction_salary_item_name17', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名17')
    deduction_salary_item_code17_amount = Column('deduction_salary_item_code17_amount', Integer, nullable=True, comment='控除給与項目コード17　金額')
    deduction_salary_item_code18 = Column('deduction_salary_item_code18', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード18')
    deduction_salary_item_name18 = Column('deduction_salary_item_name18', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名18')
    deduction_salary_item_code18_amount = Column('deduction_salary_item_code18_amount', Integer, nullable=True, comment='控除給与項目コード18　金額')
    deduction_salary_item_code19 = Column('deduction_salary_item_code19', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード19')
    deduction_salary_item_name19 = Column('deduction_salary_item_name19', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名19')
    deduction_salary_item_code19_amount = Column('deduction_salary_item_code19_amount', Integer, nullable=True, comment='控除給与項目コード19　金額')
    deduction_salary_item_code20 = Column('deduction_salary_item_code20', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード20')
    deduction_salary_item_name20 = Column('deduction_salary_item_name20', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名20')
    deduction_salary_item_code20_amount = Column('deduction_salary_item_code20_amount', Integer, nullable=True, comment='控除給与項目コード20　金額')
    deduction_salary_item_code21 = Column('deduction_salary_item_code21', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード21')
    deduction_salary_item_name21 = Column('deduction_salary_item_name21', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名21')
    deduction_salary_item_code21_amount = Column('deduction_salary_item_code21_amount', Integer, nullable=True, comment='控除給与項目コード21　金額')
    deduction_salary_item_code22 = Column('deduction_salary_item_code22', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード22')
    deduction_salary_item_name22 = Column('deduction_salary_item_name22', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名22')
    deduction_salary_item_code22_amount = Column('deduction_salary_item_code22_amount', Integer, nullable=True, comment='控除給与項目コード22　金額')
    deduction_salary_item_code23 = Column('deduction_salary_item_code23', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード23')
    deduction_salary_item_name23 = Column('deduction_salary_item_name23', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名23')
    deduction_salary_item_code23_amount = Column('deduction_salary_item_code23_amount', Integer, nullable=True, comment='控除給与項目コード23　金額')
    deduction_salary_item_code24 = Column('deduction_salary_item_code24', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード24')
    deduction_salary_item_name24 = Column('deduction_salary_item_name24', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名24')
    deduction_salary_item_code24_amount = Column('deduction_salary_item_code24_amount', Integer, nullable=True, comment='控除給与項目コード24　金額')
    deduction_salary_item_code25 = Column('deduction_salary_item_code25', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード25')
    deduction_salary_item_name25 = Column('deduction_salary_item_name25', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名25')
    deduction_salary_item_code25_amount = Column('deduction_salary_item_code25_amount', Integer, nullable=True, comment='控除給与項目コード25　金額')
    deduction_salary_item_code26 = Column('deduction_salary_item_code26', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード26')
    deduction_salary_item_name26 = Column('deduction_salary_item_name26', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名26')
    deduction_salary_item_code26_amount = Column('deduction_salary_item_code26_amount', Integer, nullable=True, comment='控除給与項目コード26　金額')
    deduction_salary_item_code27 = Column('deduction_salary_item_code27', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード27')
    deduction_salary_item_name27 = Column('deduction_salary_item_name27', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名27')
    deduction_salary_item_code27_amount = Column('deduction_salary_item_code27_amount', Integer, nullable=True, comment='控除給与項目コード27　金額')
    deduction_salary_item_code28 = Column('deduction_salary_item_code28', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード28')
    deduction_salary_item_name28 = Column('deduction_salary_item_name28', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名28')
    deduction_salary_item_code28_amount = Column('deduction_salary_item_code28_amount', Integer, nullable=True, comment='控除給与項目コード28　金額')
    deduction_salary_item_code29 = Column('deduction_salary_item_code29', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード29')
    deduction_salary_item_name29 = Column('deduction_salary_item_name29', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名29')
    deduction_salary_item_code29_amount = Column('deduction_salary_item_code29_amount', Integer, nullable=True, comment='控除給与項目コード29　金額')
    deduction_salary_item_code30 = Column('deduction_salary_item_code30', String(10, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目コード30')
    deduction_salary_item_name30 = Column('deduction_salary_item_name30', String(20, collation='ja_JP.utf8'), nullable=True, comment='控除給与項目名30')
    deduction_salary_item_code30_amount = Column('deduction_salary_item_code30_amount', Integer, nullable=True, comment='控除給与項目コード30　金額')
    is_general_health_insurance_hand_type = Column('is_general_health_insurance_hand_type', String(1, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[健康保険　一般]')
    general_health_insurance = Column('general_health_insurance', Integer, nullable=True, comment='健康保険　基本')
    is_health_insurance_adjustment_hand_type = Column('is_health_insurance_adjustment_hand_type', String(1, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[健康保険　調整]')
    health_insurance_adjustment = Column('health_insurance_adjustment', Integer, nullable=True, comment='健康保険　特定')
    is_care_insurance_hand_type = Column('is_care_insurance_hand_type', String(1, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[介護保険]')
    care_insurance = Column('care_insurance', Integer, nullable=True, comment='介護保険')
    taxable_amount = Column('taxable_amount', Integer, nullable=False, comment='給与所得額')
    taxable_amount_2 = Column('taxable_amount_2', Integer, nullable=False, comment='課税対象額')
    employement_insurance_amount = Column('employement_insurance_amount', Integer, nullable=False, comment='雇用保険対象額')
    social_insurance_amount = Column('social_insurance_amount', Integer, nullable=False, comment='社会保険対象額')
    social_insurance_total = Column('social_insurance_total', Integer, nullable=False, comment='社会保険計')
    total_payment_amount = Column('total_payment_amount', Integer, nullable=False, comment='支給額合計')
    total_deduction_amount = Column('total_deduction_amount', Integer, nullable=False, comment='控除額合計')
    deduction_amount = Column('deduction_amount', Integer, nullable=False, comment='差引支給額')
    electoric_money_amount = Column('electoric_money_amount', Integer, nullable=True, comment='電子マネー振込額')
    first_transfer_amount = Column('first_transfer_amount', Integer, nullable=True, comment='第一振込先　金額')
    second_transfer_amount = Column('second_transfer_amount', Integer, nullable=True, comment='第二振込先　金額')
    cash_payment_amount = Column('cash_payment_amount', Integer, nullable=False, comment='現金支給額')
    in_kind_payment_amount = Column('in_kind_payment_amount', Integer, nullable=False, comment='現物支給額')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    date_of_sending_pay_slip = Column('date_of_sending_pay_slip', TIMESTAMP, nullable=True, comment='送信日')
    is_payment_hand_type = Column('is_payment_hand_type', String(30, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[支給項目]')
    is_deduction_hand_type = Column('is_deduction_hand_type', String(30, collation='ja_JP.utf8'), nullable=True, comment='手修正項目[控除項目]')
    trail_update_date = Column('trail_update_date', TIMESTAMP, nullable=True)
    trail_update_employee_code = Column('trail_update_employee_code', String(10, collation='ja_JP.utf8'), nullable=True)
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_bonus_pay_slip', "company_code", "employee_code", "target_date"), Index('ix_t_employee_bonus_pay_slip_1', "company_code"), UniqueConstraint("company_code", "employee_code", "target_date"),)


class EmployeeLunch(Base):
    """
    従業員弁当トラン
    """
    __tablename__ = "t_employee_lunch"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    supplier_code = Column('supplier_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='弁当業者コード')
    lunch_code = Column('lunch_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='弁当コード')
    order_date = Column('order_date', TIMESTAMP, nullable=False, comment='予約日')
    purchase_date = Column('purchase_date', Date, nullable=False, comment='購入日')
    unit_price = Column('unit_price', Integer, nullable=False, comment='単価')
    quantity = Column('quantity', Integer, nullable=False, comment='個数')
    price = Column('price', Integer, nullable=False, comment='金額')
    catch_flg = Column('catch_flg', EnumType(enum_class=CatchFlg), nullable=False, comment='受取済フラグ')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=True, comment='対象日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_lunch', "company_code", "employee_code", "supplier_code", "lunch_code", "order_date"), Index('ix_t_employee_lunch_1', "company_code"), UniqueConstraint("company_code", "employee_code", "supplier_code", "lunch_code", "order_date"),)


class EmployeeWelfarePensionGrade(Base):
    """
    従業員厚生年金等級トラン
    """
    __tablename__ = "t_employee_welfare_pension_grade"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    basic_payment_days = Column('basic_payment_days', Integer, nullable=False, comment='支払基礎日数')
    calculation_category = Column('calculation_category', EnumType(enum_class=CalculationCategory), nullable=False, comment='算定区分')
    fixed_part = Column('fixed_part', Integer, nullable=False, comment='固定的部分')
    non_fixed_part = Column('non_fixed_part', Integer, nullable=False, comment='非固定的部分')
    social_insurance_amount = Column('social_insurance_amount', Integer, nullable=False, comment='社会保険対象額')
    social_insurance_amount_last_month = Column('social_insurance_amount_last_month', Integer, nullable=False, comment='前月の報酬月額')
    social_insurance_amount_two_month_ago = Column('social_insurance_amount_two_month_ago', Integer, nullable=False, comment='現在の標準報酬月額')
    fixed_part_last_month = Column('fixed_part_last_month', Integer, nullable=False, comment='前月の固定的部分')
    fixed_part_two_month_ago = Column('fixed_part_two_month_ago', Integer, nullable=False, comment='前々月の固定的部分')
    basic_payment_days_last_month = Column('basic_payment_days_last_month', Integer, nullable=False, comment='前月の支払基礎日数')
    basic_payment_days_two_month_ago = Column('basic_payment_days_two_month_ago', Integer, nullable=False, comment='前々月の支払基礎日数')
    employee_classification_type = Column('employee_classification_type', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='従業員区分タイプ')
    employee_classification_type_last_month = Column('employee_classification_type_last_month', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='前月の従業員区分タイプ')
    employee_classification_type_two_month_ago = Column('employee_classification_type_two_month_ago', EnumType(enum_class=EmployeeClassificationType), nullable=True, comment='前々月の従業員区分タイプ')
    total_payment_amount = Column('total_payment_amount', Integer, nullable=False, comment='支給額合計')
    total_payment_amount_last_month = Column('total_payment_amount_last_month', Integer, nullable=False, comment='前月の支給額合計')
    total_payment_amount_two_month_ago = Column('total_payment_amount_two_month_ago', Integer, nullable=False, comment='前々月の支給額合計')
    current_social_insurance_amount_standard = Column('current_social_insurance_amount_standard', Integer, nullable=False, comment='現在の標準報酬月額')
    current_grade = Column('current_grade', Integer, nullable=False, comment='現在の等級')
    this_month_grade = Column('this_month_grade', Integer, nullable=False, comment='今月の等級')
    grade_update_flg = Column('grade_update_flg', EnumType(enum_class=GradeUpdateFlg), nullable=False, comment='等級変更確認フラグ')
    months_that_need_to_be_regraded = Column('months_that_need_to_be_regraded', String(6, collation='ja_JP.utf8'), nullable=True, comment='等級変更が必要な労働月')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_welfare_pension_grade', "company_code", "employee_code", "target_date"), Index('ix_t_employee_welfare_pension_grade_1', "company_code"), UniqueConstraint("company_code", "employee_code", "target_date"),)


class BatchExecution(Base):
    """
    バッチ処理監視
    実行中のバッチ情報がセットされます。
    """
    __tablename__ = "t_batch_execution"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    batch_type = Column('batch_type', EnumType(enum_class=BatchType), nullable=False, comment='バッチの種類')
    batch_action = Column('batch_action', EnumType(enum_class=BatchAction), nullable=False, comment='バッチ実行状態')
    target_date = Column('target_date', String(4, collation='ja_JP.utf8'), nullable=True, comment='対象日')
    start_date = Column('start_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    end_date = Column('end_date', TIMESTAMP, nullable=True, comment='終了日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_batch_execution', "company_code", "batch_type"), UniqueConstraint("company_code", "batch_type"),)


class PaidPaymentManagement(Base):
    """
    有給支給管理トラン
    有給支給バッチの結果を管理します。
    """
    __tablename__ = "t_paid_payment_management"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    batch_target_date = Column('batch_target_date', Date, nullable=False, comment='実施日')
    total_employees = Column('total_employees', Integer, nullable=False, comment='全従業員数')
    total_target_employees = Column('total_target_employees', Integer, nullable=False, comment='有給支給対象の従業員数')
    meet_commuting_rate = Column('meet_commuting_rate', Integer, nullable=False, comment='出勤率の条件を満たした従業員数')
    non_meet_commuting_rate = Column('non_meet_commuting_rate', Integer, nullable=False, comment='出勤率の条件を満たさなかった従業員数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_paid_payment_management', "company_code", "batch_target_date"), Index('ix_t_paid_payment_management_1', "company_code"), UniqueConstraint("company_code", "batch_target_date"),)


class PaidPaymentManagementDetail(Base):
    """
    有給支給管理明細トラン
    有給支給バッチの支給結果の詳細を管理します。
    """
    __tablename__ = "t_paid_payment_management_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    batch_target_date = Column('batch_target_date', Date, nullable=False, comment='実施日')
    number = Column('number', Integer, nullable=False, comment='支給/失効')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    payment_result = Column('payment_result', String(255, collation='ja_JP.utf8'), nullable=True, comment='結果')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_paid_payment_management_detail', "company_code", "batch_target_date", "number", "employee_code"), Index('ix_t_paid_payment_management_detail_1', "company_code"), UniqueConstraint("company_code", "batch_target_date", "number", "employee_code"), ForeignKeyConstraint(['company_code', 'batch_target_date'], ['t_paid_payment_management.company_code', 't_paid_payment_management.batch_target_date']),)


class PlannedPaidLeaveByOffice(Base):
    """
    事業所別有給休暇の計画的付与トラン
    """
    __tablename__ = "t_planned_paid_leave_by_office"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    payment_date = Column('payment_date', Date, nullable=False, comment='支給年月日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_planned_paid_leave_by_office', "company_code", "office_code", "payment_date"), Index('ix_t_planned_paid_leave_by_office_1', "company_code"), UniqueConstraint("company_code", "office_code", "payment_date"),)


class PlannedPaidLeaveByEmployee(Base):
    """
    従業員別有給休暇の計画的付与トラン
    """
    __tablename__ = "t_planned_paid_leave_by_employee"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    payment_date = Column('payment_date', Date, nullable=False, comment='支給年月日')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_planned_paid_leave_by_employee', "company_code", "employee_code", "payment_date"), Index('ix_t_planned_paid_leave_by_employee_1', "company_code"), UniqueConstraint("company_code", "employee_code", "payment_date"),)


class ClosingManagement(Base):
    """
    締め管理トラン
    """
    __tablename__ = "t_closing_management"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    closing_code = Column('closing_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='締日コード')
    closing_classification = Column('closing_classification', EnumType(enum_class=ClosingClassification), nullable=False, comment='締め区分')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    is_close = Column('is_close', EnumType(enum_class=IsClose), nullable=False, comment='締め処理済')
    batch_status = Column('batch_status', EnumType(enum_class=BatchStatus), nullable=False, comment='バッチ処理ステータス')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_closing_management', "company_code", "closing_code", "closing_classification"), Index('ix_t_closing_management_1', "company_code"), UniqueConstraint("company_code", "closing_code", "closing_classification"), )


class SocialInsuranceAmountTrigger(Base):
    """
    報酬月額反映トリガートラン
    バッチ起動のトリガーを管理します。
    """
    __tablename__ = "t_social_insurance_amount_trigger"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    social_insurance_amount = Column('social_insurance_amount', Integer, nullable=False, comment='社会保険対象額')
    reflected_flg = Column('reflected_flg', EnumType(enum_class=ReflectedFlg), nullable=False, comment='反映済フラグ')
    change_before_monthl_reward = Column('change_before_monthl_reward', Integer, nullable=True, comment='従前報酬月額')
    change_before_last_update_date_of_monthly_reward = Column('change_before_last_update_date_of_monthly_reward', Date, nullable=True, comment='従前報酬月額の最終更新日')
    is_social_insurance = Column('is_social_insurance', Boolean, nullable=True, comment='従業員健康保険・厚生年金保険被保険者標準報酬月額')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_social_insurance_amount_trigger', "company_code", "employee_code", "target_date"), Index('ix_t_social_insurance_amount_trigger_1', "company_code"), UniqueConstraint("company_code", "employee_code", "target_date"),)


class ChangeSocialInsuranceTrigger(Base):
    """
    健康保険・厚生年金保険被保険者標準報酬月額変更反映トリガートラン
    """
    __tablename__ = "t_change_social_insurance_trigger"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    salary_closing_ym = Column('salary_closing_ym', String(6, collation='ja_JP.utf8'), nullable=False, comment='給与締年月')
    salary_closing_code = Column('salary_closing_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='給与締日コード')
    is_close = Column('is_close', EnumType(enum_class=IsClose), nullable=False, comment='締め処理済')
    reflected_flg = Column('reflected_flg', EnumType(enum_class=ReflectedFlg), nullable=False, comment='反映済フラグ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_change_social_insurance_trigger', "company_code", "salary_closing_ym", "salary_closing_code"), Index('ix_t_change_social_insurance_trigger_1', "company_code"), UniqueConstraint("company_code", "salary_closing_ym", "salary_closing_code"),)


class SessionUser(Base):
    """
    セッションユーザートラン
    """
    __tablename__ = "t_session_user"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    user_id = Column('user_id', String(255, collation='ja_JP.utf8'), comment='セッションユーザーID')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_user_id = Column('create_user_id', String(255, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_user_id = Column('update_user_id', String(255, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __table_args__ = (Index('ix_t_session_user', "user_id"), UniqueConstraint("user_id"),)


class EmployeeAlert(Base):
    """
    従業員アラートトラン
    """
    __tablename__ = "t_employee_alert"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), comment='会社コード')
    aleat_number = Column('aleat_number', Integer, nullable=False, comment='アラート番号')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    alert_day = Column('alert_day', String(5, collation='ja_JP.utf8'), nullable=True, comment='通知日')
    alert_time = Column('alert_time', String(5, collation='ja_JP.utf8'), nullable=False, comment='通知時刻')
    alert_notification_method = Column('alert_notification_method', EnumType(enum_class=AlertNotificationMethod), nullable=False, comment='アラート通知方法')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='メールアドレス')
    message = Column('message', Text, nullable=False, comment='メッセージ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_user_code = Column('create_user_code', String(255, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_user_code = Column('update_user_code', String(255, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_employee_alert', "company_code", "aleat_number"), Index('ix_t_employee_alert_1', "company_code"), UniqueConstraint("company_code", "aleat_number"),)


class ForgotImprintNotification(Base):
    """
    打刻忘れ通知マスタ
    """
    __tablename__ = "m_forgot_imprint_notification"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    attendance_type = Column('attendance_type', EnumType(enum_class=AttendanceType), nullable=False, comment='出退勤区分')
    before_after_flag = Column('before_after_flag', EnumType(enum_class=BeforeAfterFlag), nullable=False, comment='前後区分')
    relative_time = Column('relative_time', Integer, nullable=False, comment='相対時刻')
    alert_management_control = Column('alert_management_control', EnumType(enum_class=AlertManagementControl), nullable=False, comment='アラート番号管理区分')
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_forgot_imprint_notification', "company_code", "attendance_type"), Index('ix_m_forgot_imprint_notification_1', "company_code"), UniqueConstraint("company_code", "attendance_type"),)


class User(Base):
    """
    ユーザーマスタ
    """
    __tablename__ = "m_user"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    mail_address = Column('mail_address', String(255, collation='ja_JP.utf8'), nullable=False, index=True, unique=True, comment='メールアドレス')
    user_name = Column('user_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='ユーザー名')
    password = Column('password', String(255, collation='ja_JP.utf8'), nullable=False, comment='パスワード')
    customer_id = Column('customer_id', String(255, collation='ja_JP.utf8'), nullable=True, comment='カスタマーID')
    token = Column('token', String(255, collation='ja_JP.utf8'), nullable=False, unique=True, comment='トークン')
    corporate = Column('corporate', EnumType(enum_class=Corporate), nullable=False, comment='法人フラグ')
    language = Column('language', String(3, collation='ja_JP.utf8'), nullable=False, comment='言語')
    append_path = Column('append_path', String(255, collation='ja_JP.utf8'), nullable=True, comment='添付ファイルのパス')
    sex = Column('sex', EnumType(enum_class=Sex), nullable=False, comment='性別')
    birthday = Column('birthday', Date, nullable=True, comment='生年月日')
    availability = Column('availability', EnumType(enum_class=Availability), nullable=False, comment='アカウント利用')
    pending_flg = Column('pending_flg', EnumType(enum_class=PendingFlg), nullable=False, comment='仮登録フラグ')
    post_code = Column('post_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='郵便番号')
    state_code = Column('state_code', String(2, collation='ja_JP.utf8'), ForeignKey('m_state.state_code', onupdate='CASCADE', ondelete='CASCADE'), comment='都道府県コード')
    municipality_code = Column('municipality_code', String(3, collation='ja_JP.utf8'), nullable=True, comment='市町村コード')
    town = Column('town', String(50, collation='ja_JP.utf8'), nullable=True, comment='町/村')
    building = Column('building', String(30, collation='ja_JP.utf8'), nullable=True, comment='ビル/番地')
    tel = Column('tel', String(20, collation='ja_JP.utf8'), nullable=True, comment='電話番号')
    system_company_flg = Column('system_company_flg', EnumType(enum_class=SystemCompanyFlg), nullable=False, comment='システム管理会社フラグ')
    charge_exemption_flg = Column('charge_exemption_flg', EnumType(enum_class=ChargeExemptionFlg), nullable=True, comment='課金免除フラグ')
    campaign_code = Column('campaign_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='キャンペーンコード')
    default_company_code = Column('default_company_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='標準会社コード')
    access_mail_address = Column('access_mail_address', String(255, collation='ja_JP.utf8'), nullable=True, comment='連絡用メールアドレス')
    promotion_code = Column('promotion_code', String(10, collation='ja_JP.utf8'), nullable=True, comment='プロモーションコード')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_user_code = Column('create_user_code', String(255, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_user_code = Column('update_user_code', String(255, collation='ja_JP.utf8'), nullable=False, comment='最終更新者のユーザーコード')
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_user', "mail_address"), UniqueConstraint("mail_address"), )


class Campaign(Base):
    """
    キャンペーンマスタ
    """
    __tablename__ = "m_campaign"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    campaign_code = Column('campaign_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='キャンペーンコード')
    campaign_name = Column('campaign_name', String(50, collation='ja_JP.utf8'), nullable=False, comment='キャンペーン名')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=True, comment='有効終了日')
    campaign_price = Column('campaign_price', Integer, nullable=True, comment='利用者当たりの特別価格')
    campaign_free_term = Column('campaign_free_term', Integer, nullable=True, comment='無料期間')
    api_id = Column('api_id', String(255, collation='ja_JP.utf8'), nullable=False, comment='Stripe API ID')
    tax_inclusive_exclusive = Column('tax_inclusive_exclusive', EnumType(enum_class=TaxInclusiveExclusive), nullable=True, comment='消費税[内税/外税]')
    min_user = Column('min_user', Integer, nullable=True, comment='最低利用人数')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_user_code = Column('create_user_code', String(255, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_user_code = Column('update_user_code', String(255, collation='ja_JP.utf8'), nullable=False, comment='最終更新者のユーザーコード')
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_campaign', "campaign_code"), UniqueConstraint("campaign_code"), )


class Watch(Base):
    """
    ウォッチリストマスタ
    """
    __tablename__ = "m_watch"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    application_form_code = Column('application_form_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='申請書コード')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_watch', "company_code", "employee_code", "application_form_code"), Index('ix_m_watch_1', "company_code"), UniqueConstraint("company_code", "employee_code", "application_form_code"), )


class Violator(Base):
    """
    36協定監視結果トラン
    """
    __tablename__ = "t_violator"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    business_type = Column('business_type', String(10, collation='ja_JP.utf8'), nullable=False, comment='職種コード')
    real_total_minutes = Column('real_total_minutes', Integer, nullable=False, comment='労働時間')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=False, comment='所定労働時間')
    job_overwork_minutes = Column('job_overwork_minutes', Integer, nullable=False, comment='所定外労働時間')
    job_holiday_days = Column('job_holiday_days', Integer, nullable=False, comment='所定休日労働日数')
    job_holiday_hours = Column('job_holiday_hours', Integer, nullable=False, comment='所定休日労働時間')
    legal_job_minutes = Column('legal_job_minutes', Integer, nullable=False, comment='法定労働時間')
    legal_overwork_minutes = Column('legal_overwork_minutes', Integer, nullable=False, comment='法定外労働時間')
    legal_holiday_overwork_days = Column('legal_holiday_overwork_days', Integer, nullable=False, comment='法定休日労働日数')
    legal_holiday_overwork_minutes = Column('legal_holiday_overwork_minutes', Integer, nullable=False, comment='法定休日労働時間')
    late_night_overwork_minutes = Column('late_night_overwork_minutes', Integer, nullable=False, comment='深夜労働時間')
    break_minutes = Column('break_minutes', Integer, nullable=False, comment='休憩時間')
    paid_holiday_days = Column('paid_holiday_days', Float, nullable=False, comment='有給日数')
    paid_holiday_hours = Column('paid_holiday_hours', Integer, nullable=False, comment='有給時間数')
    child_time_leave_days = Column('child_time_leave_days', Float, nullable=False, comment='育児休暇日数')
    child_time_leave_hours = Column('child_time_leave_hours', Integer, nullable=False, comment='育児時間休暇数')
    compensatory_holiday_days = Column('compensatory_holiday_days', Integer, nullable=False, comment='代休日数')
    leave_days = Column('leave_days', Integer, nullable=False, comment='休職日数')
    closed_days = Column('closed_days', Integer, nullable=False, comment='休業日数')
    count_rush_to_work = Column('count_rush_to_work', Integer, nullable=False, comment='駆け込み出勤回数')
    count_scheduled_dash = Column('count_scheduled_dash', Integer, nullable=False, comment='定時ダッシュ回数')
    late_days = Column('late_days', Integer, nullable=False, comment='遅刻回数')
    late_minutes = Column('late_minutes', Integer, nullable=False, comment='遅刻時間')
    early_departure_days = Column('early_departure_days', Integer, nullable=False, comment='早退回数')
    early_departure_minutes = Column('early_departure_minutes', Integer, nullable=False, comment='早退時間')
    absent_total_days = Column('absent_total_days', Integer, nullable=False, comment='欠勤日数')
    overwork_days = Column('overwork_days', Integer, nullable=False, comment='残業日数')
    holiday_overwork_days = Column('holiday_overwork_days', Integer, nullable=False, comment='休日出勤日数')
    paid_holiday_days_before = Column('paid_holiday_days_before', Float, nullable=False, comment='有給日数[事前申請]')
    paid_holiday_days_after = Column('paid_holiday_days_after', Float, nullable=False, comment='有給日数[事後申請]')
    digestion_days = Column('digestion_days', DECIMAL(5, 2), nullable=False, comment='有給消化率')
    count_telework = Column('count_telework', Integer, nullable=False, comment='テレワーク回数')
    working_interval = Column('working_interval', Integer, nullable=False, comment='インターバル時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_violator', "company_code", "term_from", "term_to", "office_code", "employee_code"), Index('ix_t_violator_1', "company_code"), UniqueConstraint("company_code", "term_from", "term_to", "office_code", "employee_code"), )


class CsvExportTemplateFormat(Base):
    """
    規定CSVテンプレートマスタ
    """
    __tablename__ = "m_csv_export_template_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    template_number = Column('template_number', Integer, nullable=False, comment='テンプレート番号')
    template_name = Column('template_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='テンプレート名')
    encode = Column('encode', EnumType(enum_class=Encode), nullable=False, comment='文字コード')
    quotation_mark = Column('quotation_mark', EnumType(enum_class=QuotationMark), nullable=False, comment='クォーテーションマーク')
    field_separator = Column('field_separator', EnumType(enum_class=FieldSeparator), nullable=False, comment='フィールドセパレーター')
    is_header_disp = Column('is_header_disp', Boolean, nullable=False, comment='列名表示有無')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_csv_export_template_format', "template_number"), UniqueConstraint("template_number"), )


class CsvExportTemplateDetailFormat(Base):
    """
    規定CSVテンプレート詳細マスタ
    """
    __tablename__ = "m_csv_export_template_detail_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    template_number = Column('template_number', Integer, nullable=False, comment='テンプレート番号')
    working_item = Column('working_item', String(128), nullable=False, comment='勤怠項目')
    working_item_unit = Column('working_item_unit', String(30, collation='ja_JP.utf8'), nullable=True, comment='単位')
    format_serial_number = Column('format_serial_number', Integer, nullable=True, comment='フォーマット連番')
    is_quotation = Column('is_quotation', Boolean, nullable=False, comment='囲み有無')
    is_zero_suppress = Column('is_zero_suppress', Boolean, nullable=False, comment='ゼロサプレス有無')
    zero_suppress_count = Column('zero_suppress_count', Integer, nullable=False, comment='ゼロサプレスカウント')
    sort_number = Column('sort_number', Integer, nullable=False, comment='ソート順')
    enabled = Column('enabled', EnumType(enum_class=Availability), nullable=False, comment='有効')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_csv_export_template_detail_format', "template_number", "working_item"), UniqueConstraint("template_number", "working_item"), )


class WokingItemFormat(Base):
    """
    規定勤怠項目マスタ
    """
    __tablename__ = "m_working_item_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    working_item = Column('working_item', String(128), nullable=False, comment='勤怠項目')
    working_item_name = Column('working_item_name', String(30), nullable=True, comment='勤怠項目名')
    working_item_unit = Column('working_item_unit', String(30, collation='ja_JP.utf8'), nullable=True, comment='単位')
    table_item = Column('table_item', String(255, collation='ja_JP.utf8'), nullable=True, comment='テーブル項目')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_working_item_format', "working_item", "working_item_unit"), UniqueConstraint("working_item", "working_item_unit"), )


class WorkingItemUnitFormat(Base):
    """
    規定単位マスタ
    """
    __tablename__ = "m_working_item_unit_format"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    working_item_unit = Column('working_item_unit', String(30, collation='ja_JP.utf8'), nullable=False, comment='単位')
    working_item_name = Column('working_item_name', String(30), nullable=True, comment='単位名')
    format_serial_number = Column('format_serial_number', Integer, nullable=False, comment='フォーマット連番')
    unit_format = Column('unit_format', String(30, collation='ja_JP.utf8'), nullable=False, comment='単位のフォーマット')
    formula = Column('formula', String(255, collation='ja_JP.utf8'), nullable=True, comment='計算式')
    remark = Column('remark', String(255, collation='ja_JP.utf8'), nullable=True, comment='備考')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_working_item_unit_format', "working_item_unit", "format_serial_number"), UniqueConstraint("working_item_unit", "format_serial_number"), )


class CsvExportTemplate(Base):
    """
    CSVテンプレートマスタ
    """
    __tablename__ = "m_csv_export_template"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    template_number = Column('template_number', Integer, nullable=False, comment='テンプレート番号')
    template_name = Column('template_name', String(30, collation='ja_JP.utf8'), nullable=False, comment='テンプレート名')
    encode = Column('encode', EnumType(enum_class=Encode), nullable=False, comment='文字コード')
    quotation_mark = Column('quotation_mark', EnumType(enum_class=QuotationMark), nullable=False, comment='クォーテーションマーク')
    field_separator = Column('field_separator', EnumType(enum_class=FieldSeparator), nullable=False, comment='フィールドセパレーター')
    is_header_disp = Column('is_header_disp', Boolean, nullable=False, comment='列名表示有無')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_csv_export_template', "company_code", "template_number"), UniqueConstraint("company_code", "template_number"), )


class CsvExportTemplateDetail(Base):
    """
    CSVテンプレート詳細マスタ
    """
    __tablename__ = "m_csv_export_template_detail"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    template_number = Column('template_number', Integer, nullable=False, comment='テンプレート番号')
    working_item = Column('working_item', String(128), nullable=False, comment='勤怠項目')
    working_item_unit = Column('working_item_unit', String(30, collation='ja_JP.utf8'), nullable=True, comment='単位')
    format_serial_number = Column('format_serial_number', Integer, nullable=True, comment='フォーマット連番')
    is_quotation = Column('is_quotation', Boolean, nullable=False, comment='囲み有無')
    is_zero_suppress = Column('is_zero_suppress', Boolean, nullable=False, comment='ゼロサプレス有無')
    zero_suppress_count = Column('zero_suppress_count', Integer, nullable=False, comment='ゼロサプレスカウント')
    sort_number = Column('sort_number', Integer, nullable=False, comment='ソート順')
    enabled = Column('enabled', EnumType(enum_class=Availability), nullable=False, comment='有効')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_m_csv_export_template_detail', "company_code", "template_number", "working_item"), Index('ix_m_csv_export_template_detail_1', "company_code"), UniqueConstraint("company_code", "template_number", "working_item"), )


class ViolatorErrorList(Base):
    """
    36協定監視結果トランエラーリスト
    """
    __tablename__ = "t_violator_error_list"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    agreement = Column('agreement', Integer, nullable=False, comment='規則')
    actual_time = Column('actual_time', Integer, nullable=False, comment='実績')
    data_unit = Column('data_unit', EnumType(enum_class=DataUnit), nullable=False, comment='データ単位')
    pan_error_contents = Column('pan_error_contents', String(255, collation='ja_JP.utf8'), nullable=False, comment='警告内容')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    article = Column('article', String(20, collation='ja_JP.utf8'), nullable=False, comment='条')
    term = Column('term', String(20, collation='ja_JP.utf8'), nullable=False, comment='項')
    issue = Column('issue', String(20, collation='ja_JP.utf8'), nullable=False, comment='号')
    color = Column('color', EnumType(enum_class=Color), nullable=False, comment='色')
    error_item = Column('error_item', EnumType(enum_class=ErrorItem), nullable=False, comment='エラー項目')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_violator_error_list', "company_code", "term_from", "term_to", "office_code", "employee_code", "serial_number"), Index('ix_t_violator_error_list_1', "company_code"), UniqueConstraint("company_code", "term_from", "term_to", "office_code", "employee_code", "serial_number"), )


class ViolatorWarningList(Base):
    """
    36協定監視結果トラン警告リスト
    """
    __tablename__ = "t_violator_warning_list"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    agreement = Column('agreement', Integer, nullable=False, comment='規則')
    actual_time = Column('actual_time', Integer, nullable=False, comment='実績')
    data_unit = Column('data_unit', EnumType(enum_class=DataUnit), nullable=False, comment='データ単位')
    pan_error_contents = Column('pan_error_contents', String(255, collation='ja_JP.utf8'), nullable=False, comment='警告内容')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    article = Column('article', String(20, collation='ja_JP.utf8'), nullable=False, comment='条')
    term = Column('term', String(20, collation='ja_JP.utf8'), nullable=False, comment='項')
    issue = Column('issue', String(20, collation='ja_JP.utf8'), nullable=False, comment='号')
    color = Column('color', EnumType(enum_class=Color), nullable=False, comment='色')
    error_item = Column('error_item', EnumType(enum_class=ErrorItem), nullable=False, comment='エラー項目')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_violator_warning_list', "company_code", "term_from", "term_to", "office_code", "employee_code", "serial_number"), Index('ix_t_violator_warning_list_1', "company_code"), UniqueConstraint("company_code", "term_from", "term_to", "office_code", "employee_code", "serial_number"), )


class ViolatorMonthlyReport(Base):
    """
    36協定監視結果の月別勤怠情報
    """
    __tablename__ = "t_violator_monthly_report"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    job_total_days = Column('job_total_days', Integer, nullable=True, comment='所定労働日数')
    real_total_minutes = Column('real_total_minutes', Integer, nullable=False, comment='労働時間')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=False, comment='所定労働時間')
    job_overwork_minutes = Column('job_overwork_minutes', Integer, nullable=False, comment='所定外労働時間')
    job_holiday_days = Column('job_holiday_days', Integer, nullable=False, comment='所定休日労働日数')
    job_holiday_hours = Column('job_holiday_hours', Integer, nullable=False, comment='所定休日労働時間')
    legal_job_minutes = Column('legal_job_minutes', Integer, nullable=False, comment='法定労働時間')
    legal_overwork_minutes = Column('legal_overwork_minutes', Integer, nullable=False, comment='法定外労働時間')
    legal_holiday_overwork_days = Column('legal_holiday_overwork_days', Integer, nullable=False, comment='法定休日労働日数')
    legal_holiday_overwork_minutes = Column('legal_holiday_overwork_minutes', Integer, nullable=False, comment='法定休日労働時間')
    late_night_overwork_minutes = Column('late_night_overwork_minutes', Integer, nullable=False, comment='深夜労働時間')
    break_minutes = Column('break_minutes', Integer, nullable=False, comment='休憩時間')
    paid_holiday_days = Column('paid_holiday_days', Float, nullable=False, comment='有給日数')
    paid_holiday_hours = Column('paid_holiday_hours', Integer, nullable=False, comment='有給時間数')
    child_time_leave_days = Column('child_time_leave_days', Float, nullable=False, comment='育児休暇日数')
    child_time_leave_hours = Column('child_time_leave_hours', Integer, nullable=False, comment='育児時間休暇数')
    compensatory_holiday_days = Column('compensatory_holiday_days', Integer, nullable=False, comment='代休日数')
    leave_days = Column('leave_days', Integer, nullable=False, comment='休職日数')
    closed_days = Column('closed_days', Integer, nullable=False, comment='休業日数')
    count_rush_to_work = Column('count_rush_to_work', Integer, nullable=False, comment='駆け込み出勤回数')
    count_scheduled_dash = Column('count_scheduled_dash', Integer, nullable=False, comment='定時ダッシュ回数')
    late_days = Column('late_days', Integer, nullable=False, comment='遅刻回数')
    late_minutes = Column('late_minutes', Integer, nullable=False, comment='遅刻時間')
    early_departure_days = Column('early_departure_days', Integer, nullable=False, comment='早退回数')
    early_departure_minutes = Column('early_departure_minutes', Integer, nullable=False, comment='早退時間')
    absent_total_days = Column('absent_total_days', Integer, nullable=False, comment='欠勤日数')
    overwork_days = Column('overwork_days', Integer, nullable=False, comment='残業日数')
    overwork_minutes = Column('overwork_minutes', Integer, nullable=False, comment='残業時間')
    holiday_overwork_days = Column('holiday_overwork_days', Integer, nullable=False, comment='休日出勤日数')
    holiday_overwork_minutes = Column('holiday_overwork_minutes', Integer, nullable=False, comment='休日出勤時間')
    paid_holiday_days_before = Column('paid_holiday_days_before', Float, nullable=False, comment='有給日数[事前申請]')
    paid_holiday_days_after = Column('paid_holiday_days_after', Float, nullable=False, comment='有給日数[事後申請]')
    count_telework = Column('count_telework', Integer, nullable=False, comment='テレワーク回数')
    working_interval = Column('working_interval', Integer, nullable=False, comment='インターバル時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_violator_monthly_report', "company_code", "term_from", "term_to", "office_code", "employee_code", "target_date"), Index('ix_t_violator_monthly_report_1', "company_code"), UniqueConstraint("company_code", "term_from", "term_to", "office_code", "employee_code", "target_date"), )


class ViolatorMonthlyErrorList(Base):
    """
    36協定監視結果トラン月別エラーリスト
    """
    __tablename__ = "t_violator_monthly_error_list"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    agreement = Column('agreement', Integer, nullable=False, comment='規則')
    actual_time = Column('actual_time', Integer, nullable=False, comment='実績')
    data_unit = Column('data_unit', EnumType(enum_class=DataUnit), nullable=False, comment='データ単位')
    pan_error_contents = Column('pan_error_contents', String(255, collation='ja_JP.utf8'), nullable=False, comment='警告内容')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    article = Column('article', String(20, collation='ja_JP.utf8'), nullable=False, comment='条')
    term = Column('term', String(20, collation='ja_JP.utf8'), nullable=False, comment='項')
    issue = Column('issue', String(20, collation='ja_JP.utf8'), nullable=False, comment='号')
    color = Column('color', EnumType(enum_class=Color), nullable=False, comment='色')
    error_item = Column('error_item', EnumType(enum_class=ErrorItem), nullable=False, comment='エラー項目')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_violator_monthly_error_list', "company_code", "term_from", "term_to", "office_code", "employee_code", "target_date", "serial_number"), Index('ix_t_violator_monthly_error_list_1', "company_code"), UniqueConstraint("company_code", "term_from", "term_to", "office_code", "employee_code", "target_date", "serial_number"), )


class ViolatorMonthlyWarningList(Base):
    """
    36協定監視結果トラン月別警告リスト
    """
    __tablename__ = "t_violator_monthly_warning_list"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', String(6, collation='ja_JP.utf8'), nullable=False, comment='対象日')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    agreement = Column('agreement', Integer, nullable=False, comment='規則')
    actual_time = Column('actual_time', Integer, nullable=False, comment='実績')
    data_unit = Column('data_unit', EnumType(enum_class=DataUnit), nullable=False, comment='データ単位')
    pan_error_contents = Column('pan_error_contents', String(255, collation='ja_JP.utf8'), nullable=False, comment='警告内容')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    article = Column('article', String(20, collation='ja_JP.utf8'), nullable=False, comment='条')
    term = Column('term', String(20, collation='ja_JP.utf8'), nullable=False, comment='項')
    issue = Column('issue', String(20, collation='ja_JP.utf8'), nullable=False, comment='号')
    color = Column('color', EnumType(enum_class=Color), nullable=False, comment='色')
    error_item = Column('error_item', EnumType(enum_class=ErrorItem), nullable=False, comment='エラー項目')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_violator_monthly_warning_list', "company_code", "term_from", "term_to", "office_code", "employee_code", "target_date", "serial_number"), Index('ix_t_violator_monthly_warning_list_1', "company_code"), UniqueConstraint("company_code", "term_from", "term_to", "office_code", "employee_code", "target_date", "serial_number"), )


class ViolatorDailylyReport(Base):
    """
    36協定監視結果の日別勤怠情報
    """
    __tablename__ = "t_violator_daily_report"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_month = Column('target_month', String(6, collation='ja_JP.utf8'), nullable=False, comment='支給月度')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    real_total_minutes = Column('real_total_minutes', Integer, nullable=False, comment='労働時間')
    job_total_minutes = Column('job_total_minutes', Integer, nullable=False, comment='所定労働時間')
    job_overwork_minutes = Column('job_overwork_minutes', Integer, nullable=False, comment='所定外労働時間')
    job_holiday_hours = Column('job_holiday_hours', Integer, nullable=False, comment='所定休日労働時間')
    legal_job_minutes = Column('legal_job_minutes', Integer, nullable=False, comment='法定労働時間')
    legal_overwork_minutes = Column('legal_overwork_minutes', Integer, nullable=False, comment='法定外労働時間')
    legal_holiday_overwork_minutes = Column('legal_holiday_overwork_minutes', Integer, nullable=False, comment='法定休日労働時間')
    late_night_overwork_minutes = Column('late_night_overwork_minutes', Integer, nullable=False, comment='深夜労働時間')
    break_minutes = Column('break_minutes', Integer, nullable=False, comment='休憩時間')
    paid_holiday_days = Column('paid_holiday_days', Float, nullable=False, comment='有給日数')
    paid_holiday_hours = Column('paid_holiday_hours', Integer, nullable=False, comment='有給時間数')
    child_time_leave_days = Column('child_time_leave_days', Float, nullable=False, comment='育児休暇日数')
    child_time_leave_hours = Column('child_time_leave_hours', Integer, nullable=False, comment='育児時間休暇数')
    compensatory_holiday_days = Column('compensatory_holiday_days', Integer, nullable=False, comment='代休日数')
    late_minutes = Column('late_minutes', Integer, nullable=False, comment='遅刻時間')
    early_departure_minutes = Column('early_departure_minutes', Integer, nullable=False, comment='早退時間')
    leave_days = Column('leave_days', Integer, nullable=False, comment='休職日数')
    closed_days = Column('closed_days', Integer, nullable=False, comment='休業日数')
    telework_flg = Column('telework_flg', Boolean, nullable=True, comment='テレワークフラグ')
    working_interval = Column('working_interval', Integer, nullable=False, comment='インターバル時間')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_violator_daily_report', "company_code", "term_from", "term_to", "office_code", "employee_code", "target_date"), Index('ix_t_violator_daily_report_1', "company_code"), UniqueConstraint("company_code", "term_from", "term_to", "office_code", "employee_code", "target_date"), )


class ViolatorDailyErrorList(Base):
    """
    36協定監視結果トラン日別エラーリスト
    """
    __tablename__ = "t_violator_daily_error_list"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    agreement = Column('agreement', Integer, nullable=False, comment='規則')
    actual_time = Column('actual_time', Integer, nullable=False, comment='実績')
    data_unit = Column('data_unit', EnumType(enum_class=DataUnit), nullable=False, comment='データ単位')
    pan_error_contents = Column('pan_error_contents', String(255, collation='ja_JP.utf8'), nullable=False, comment='警告内容')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    article = Column('article', String(20, collation='ja_JP.utf8'), nullable=False, comment='条')
    term = Column('term', String(20, collation='ja_JP.utf8'), nullable=False, comment='項')
    issue = Column('issue', String(20, collation='ja_JP.utf8'), nullable=False, comment='号')
    color = Column('color', EnumType(enum_class=Color), nullable=False, comment='色')
    error_item = Column('error_item', EnumType(enum_class=ErrorItem), nullable=False, comment='エラー項目')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_violator_daily_error_list', "company_code", "term_from", "term_to", "office_code", "employee_code", "target_date", "serial_number"), Index('ix_t_violator_daily_error_list_1', "company_code"), UniqueConstraint("company_code", "term_from", "term_to", "office_code", "employee_code", "target_date", "serial_number"), )


class ViolatorDailyWarningList(Base):
    """
    36協定監視結果トラン月別警告リスト
    """
    __tablename__ = "t_violator_daily_warning_list"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    term_from = Column('term_from', Date, nullable=False, comment='有効開始日')
    term_to = Column('term_to', Date, nullable=False, comment='有効終了日')
    office_code = Column('office_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='事業所コード')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    target_date = Column('target_date', Date, nullable=False, comment='対象日')
    serial_number = Column('serial_number', Integer, nullable=False, comment='シリアル番号')
    agreement = Column('agreement', Integer, nullable=False, comment='規則')
    actual_time = Column('actual_time', Integer, nullable=False, comment='実績')
    data_unit = Column('data_unit', EnumType(enum_class=DataUnit), nullable=False, comment='データ単位')
    pan_error_contents = Column('pan_error_contents', String(255, collation='ja_JP.utf8'), nullable=False, comment='警告内容')
    chapter = Column('chapter', String(20, collation='ja_JP.utf8'), nullable=False, comment='章')
    article = Column('article', String(20, collation='ja_JP.utf8'), nullable=False, comment='条')
    term = Column('term', String(20, collation='ja_JP.utf8'), nullable=False, comment='項')
    issue = Column('issue', String(20, collation='ja_JP.utf8'), nullable=False, comment='号')
    color = Column('color', EnumType(enum_class=Color), nullable=False, comment='色')
    error_item = Column('error_item', EnumType(enum_class=ErrorItem), nullable=False, comment='エラー項目')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_violator_daily_warning_list', "company_code", "term_from", "term_to", "office_code", "employee_code", "target_date", "serial_number"), Index('ix_t_violator_daily_warning_list_1', "company_code"), UniqueConstraint("company_code", "term_from", "term_to", "office_code", "employee_code", "target_date", "serial_number"), )


class ArtemisAlertApplication(Base):
    """
    [ワークフロー用]アルテミスアラートトラン
    """
    __tablename__ = "t_artemis_alert_application"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    company_code = Column('company_code', String(10, collation='ja_JP.utf8'), ForeignKey('m_company.company_code', onupdate='CASCADE', ondelete='CASCADE'), comment='会社コード')
    application_number = Column('application_number', Integer, nullable=False, comment='申請番号')
    employee_code = Column('employee_code', String(10, collation='ja_JP.utf8'), nullable=False, comment='従業員番号')
    mail_subject = Column('mail_subject', String(255, collation='ja_JP.utf8'), nullable=False, comment='メール件名')
    mail_body = Column('mail_body', String(4096, collation='ja_JP.utf8'), nullable=False, comment='メール本文')
    screen_code = Column('screen_code', String(6, collation='ja_JP.utf8'), nullable=False, comment='画面コード')
    alert_notification = Column('alert_notification', String(255, collation='ja_JP.utf8'), nullable=False, comment='お知らせ')
    alert_parameter = Column('alert_parameter', String(255, collation='ja_JP.utf8'), nullable=True, comment='パラメータ')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_employee_code = Column('create_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_employee_code = Column('update_employee_code', String(10, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_artemis_alert_application', "company_code", "application_number", "employee_code"), Index('ix_t_artemis_alert_application_1', "company_code"), Index('ix_t_artemis_alert_application_2', "company_code", "application_number"), UniqueConstraint("company_code", "application_number", "employee_code"), ForeignKeyConstraint(['company_code', 'employee_code'], ['m_employee.company_code', 'm_employee.employee_code']))

    __table_args__ = (Index('ix_t_error_log_private', "mail_address"), UniqueConstraint("mail_address", "notice_date"), )

class OperationNoticeMyCollier(Base):
    """
    運営からのお知らせトラン
    """
    __tablename__ = "t_operation_notice_my_collier"
    id = Column('id', Integer, primary_key=True, autoincrement=True, comment='サロゲートキー')
    notice_number = Column('notice_number', Integer, nullable=False, comment='お知らせ番号')
    notification = Column('notification', String(4096, collation='ja_JP.utf8'), nullable=False, comment='お知らせ')
    contents = Column('contents', String(4096, collation='ja_JP.utf8'), nullable=True, comment='補足説明')
    notification_transmission_date = Column('notification_transmission_date', TIMESTAMP, nullable=False, comment='お知らせ発信日')
    notification_display_date_from = Column('notification_display_date_from', Date, nullable=False, comment='お知らせ表示期間[開始]')
    notification_display_date_to = Column('notification_display_date_to', Date, nullable=True, comment='お知らせ表示期間[終了]')
    notice_type = Column('notice_type', EnumType(enum_class=NoticeType), nullable=False, comment='お知らせの種類')
    create_date = Column('create_date', TIMESTAMP, default=datetime.now, nullable=False)
    create_user_code = Column('create_user_code', String(255, collation='ja_JP.utf8'), nullable=False)
    update_date = Column('update_date', TIMESTAMP, default=datetime.now, nullable=False, onupdate=datetime.now)
    update_user_code = Column('update_user_code', String(255, collation='ja_JP.utf8'), nullable=False)
    update_count = Column('update_count', Integer, nullable=False)
    __mapper_args__ = {
        'version_id_col': update_count
    }
    __table_args__ = (Index('ix_t_operation_notice_my_collier', "notice_number"), UniqueConstraint("notice_number"),)
