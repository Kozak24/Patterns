from structural.proxy.logic import AdminPanel, AdminPanelProxy
from structural.proxy.data import User, AccessLevels


def main() -> None:
    default_user = User("Jotaro Kujo", AccessLevels.USER)
    admin_user = User("Giorno Giovanna", AccessLevels.ADMIN)

    print("Before Proxy")
    admin_panel = AdminPanel(admin_user)
    admin_panel.perform_admin_action()
    admin_panel.switch_user(default_user)
    admin_panel.perform_admin_action()

    print("\nAfter Proxy")
    admin_panel = AdminPanelProxy(admin_user)
    admin_panel.perform_admin_action()
    admin_panel.switch_user(default_user)
    admin_panel.log_out()
    admin_panel.switch_user(default_user)
    admin_panel.perform_admin_action()


if __name__ == "__main__":
    main()
