from enum import IntEnum


class PrincipalType(IntEnum):
    ROLE = 1
    USER = 2
    GROUP = 3


class ResourceType(IntEnum):
    SCREEN = 1
    API = 2
    MENU = 3


class ActionType(IntEnum):
    ENTRY = 1
    UPDATE = 2
    DELETE = 3
    PRINT = 4
    SEARCH = 5
    UPLOAD = 6
    DOWNLOAD = 7
    PREVIEW = 8
    CALL = 9


class EffectType(IntEnum):
    ALLOW = 1
    DENY = 2


class Availability(IntEnum):
    AVAILABLE = 1
    UNUSABLE = 2


class WorkingSystemType(IntEnum):
    NORMAL = 1
    FLEX = 2
    TRANSFORMATION = 3


class FlexibleLaborType(IntEnum):
    ONE_MONTH = 1
    ONE_YEAR = 2


class JobBeforeStartTime(IntEnum):
    INCLUDE = 1
    EXCLUDE = 2


"""
Enum:所定労働日区分
ON 　所定労働日扱い
OFF　所定労働日扱いしない
"""


class LaborDayClassification(IntEnum):
    ON = 1
    OFF = 2

"""
Enum:出勤日扱い区分
ON 　出勤日扱いする
OFF　出勤日扱いしない
"""


class AttendanceDateClassification(IntEnum):
    ON = 1
    OFF = 2


"""
Enum:賃金支給区分
ON 　賃金支給する
OFF　賃金支給しない
"""


class WageClassification(IntEnum):
    ON = 1
    OFF = 2

"""
Enum:事由マスタ　出勤簿利用可否
AVAILABLE 利用可能
UNAVAILABLE 利用不可
OUT 利用不可[変更不可]
"""


class TimecardAvailableFlg(IntEnum):
    AVAILABLE = 1
    UNAVAILABLE = 2
    OUT = 9


class NonStampFlg(IntEnum):
    AVAILABLE = 1
    UNAVAILABLE = 2


"""
Enum:色
BLACK 黒色
BLUE 青色
RED 赤色
GREEN 緑色
"""


class Color(IntEnum):
    BLACK = 1
    BLUE = 2
    RED = 3
    GREEN = 4


"""
Enum:申請対象フラグ
ON 対象
OFF 対象外
OUT 対象外[利用不可]
"""


class WorkflowFlg(IntEnum):
    ON = 1
    OFF = 2
    OUT = 9


"""
Enum:システム画面フラグ
ON システム画面
OFF システム画面以外
"""


class SystemScreenFlg(IntEnum):
    ON = 1
    OFF = 2

    @property
    def label(self) -> str:
        return {
            SystemScreenFlg.ON: "システム画面",
            SystemScreenFlg.OFF: "システム画面以外",
        }[self]


"""
Enum:画面種別
MAIN メイン画面
POPUP ポップアップ画面
DASH_BOARD ダッシュボード
"""


class ScreenType(IntEnum):
    MAIN = 1
    POPUP = 2
    DASH_BOARD = 3

    @property
    def label(self) -> str:
        return {
            ScreenType.MAIN: "メイン画面",
            ScreenType.POPUP: "ポップアップ画面",
            ScreenType.DASH_BOARD: "ダッシュボード",
        }[self]


"""
Enum:システム管理会社フラグ
ON システム管理会社
OFF 一般会社
"""


class SystemCompanyFlg(IntEnum):
    ON = 1
    OFF = 2

    @property
    def label(self) -> str:
        return {
            SystemCompanyFlg.ON: "システム管理会社",
            SystemCompanyFlg.OFF: "一般会社",
        }[self]


"""
Enum:承認画面の機能
EXAMINATION 審査
AUTHORIZER_AUTOMATIC_APPROVAL 自動承認
FUNCTION_CONFIRMATION 確認
AUTHORIZER_FORCED_APPROVAL 強制承認
"""


class ApprovalFunction(IntEnum):
    EXAMINATION = 1
    AUTHORIZER_AUTOMATIC_APPROVAL = 2
    FUNCTION_CONFIRMATION = 3
    AUTHORIZER_FORCED_APPROVAL = 4


"""
Enum:権限の譲渡フラグ
AVAILABLE 可能です
UNUSABLE 出来ません
"""


class Permission(IntEnum):
    AVAILABLE = 1
    UNUSABLE = 2
