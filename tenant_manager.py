import uuid


class TenantManager:
    """テナントIDとUUIDを管理するクラス"""

    def __init__(self):
        # テナントID -> UUIDのマッピング
        self.tenant_id_map = {}

    def create_tenant(self, tenant_id: str) -> str:
        """新しいテナントを追加し、UUIDを割り当てる"""
        new_uuid = str(uuid.uuid4())
        self.tenant_id_map[tenant_id] = new_uuid
        print(f"テナント '{tenant_id}' にUUID割り当て: {new_uuid}")
        return new_uuid

    def get_uuid_by_tenant_id(self, tenant_id: str) -> str | None:
        """テナントIDからUUIDを取得"""
        return self.tenant_id_map.get(tenant_id)

    def get_tenant_id_by_uuid(self, search_uuid: str) -> str | None:
        """UUIDからテナントIDを取得"""
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
