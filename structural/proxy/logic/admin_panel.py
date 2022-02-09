from structural.proxy.data import User


class AdminPanel:
    def __init__(self, user: User) -> None:
        self._user = user
        print(f"{self.user} initialized the Admin Panel")

    def switch_user(self, user: User) -> None:
        log_off_msg = f"{user} took control over admin panel"
        log_off_msg = f"{log_off_msg} and forced log off of {self.user}" if self.user is not None else log_off_msg
        print(log_off_msg)
        self._user = user

    def log_out(self) -> None:
        print(f"{self.user} logged out")
        self._user = None

    def perform_admin_action(self) -> None:
        if self.user is None:
            print("Cannot perform the action, since no active user at the moment")

        print(f"{self.user} performed admin action")

    @property
    def user(self) -> User:
        return self._user
