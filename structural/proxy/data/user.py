from structural.proxy.data.access_levels import AccessLevels


class User:
    def __init__(self, name: str, access_level: AccessLevels) -> None:
        self.name = name
        self.access_level = access_level

    def __str__(self) -> str:
        return f"User '{self.name}' with '{self.access_level.name}' access level"
