from structural.proxy.data import User, AccessLevels
from structural.proxy.logic import AdminPanel


class AdminPanelProxy:
    def __init__(self, user: User) -> None:
        self.admin_panel = AdminPanel(user)

    def switch_user(self, user: User) -> None:
        current_user = self.admin_panel.user
        if current_user is not None and current_user.access_level > user.access_level:
            print(f"{user} cannot force log off {self.admin_panel.user} due to access level restrictions")
            return

        self.admin_panel.switch_user(user)

    def log_out(self) -> None:
        self.admin_panel.log_out()

    def perform_admin_action(self) -> None:
        if self.admin_panel.user.access_level < AccessLevels.ADMIN:
            print(f"{self.admin_panel.user} doesn't have required access level to perform this operation")
            return

        self.admin_panel.perform_admin_action()
