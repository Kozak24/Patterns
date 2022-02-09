from enum import IntEnum


class AccessLevels(IntEnum):
    OWNER = 3
    ADMIN = 2
    MANAGER = 1
    USER = 0
    UNKNOWN = -1

    @classmethod
    def _missing_(cls, value):
        return AccessLevels.UNKNOWN
