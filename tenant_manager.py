import uuid


class TenantManager:
    """
    テナントIDとUUIDの管理を行うクラス。

    このクラスは、テナントIDに対して一意なUUIDを割り当て・管理し、
    テナントIDからUUID、UUIDからテナントIDへの検索機能を提供します。
    """

    def __init__(self):
        """
        TenantManagerの新しいインスタンスを初期化します。

        インスタンス生成時に空のマッピング辞書を作成します。
        """
        self.tenant_id_map = {}

    def create_tenant(self, tenant_id: str) -> str:
        """
        新しいテナントIDにUUIDを割り当てて登録します。

        既存のテナントIDに対して再度呼び出すと、UUIDが上書きされます。

        Args:
            tenant_id (str): 登録するテナントID

        Returns:
            str: 割り当てられたUUID（文字列）
        """
        new_uuid = str(uuid.uuid4())
        self.tenant_id_map[tenant_id] = new_uuid
        print(f"テナント '{tenant_id}' にUUID割り当て: {new_uuid}")
        return new_uuid

    def get_uuid_by_tenant_id(self, tenant_id: str) -> str | None:
        """
        テナントIDからUUIDを取得します。

        Args:
            tenant_id (str): 検索対象のテナントID

        Returns:
            str | None: 対応するUUID（存在しない場合はNone）
        """
        return self.tenant_id_map.get(tenant_id)

    def get_tenant_id_by_uuid(self, search_uuid: str) -> str | None:
        """
        UUIDからテナントIDを取得します。

        Args:
            search_uuid (str): 検索対象のUUID

        Returns:
            str | None: 対応するテナントID（存在しない場合はNone）
        """
        for tenant_id, uid in self.tenant_id_map.items():
            if uid == search_uuid:
                return tenant_id
        return None


if __name__ == "__main__":
    manager = TenantManager()
    manager.create_tenant("pocketsoft")
    manager.create_tenant("awesome_company")

    print(manager.get_uuid_by_tenant_id("pocketsoft"))
    print(manager.get_tenant_id_by_uuid(
        list(manager.tenant_id_map.values())[0]
    ))
