from controllers.app_controller import AppController
from views.main_window import MainWindow


def main() -> None:
    controller: AppController = AppController()
    app: MainWindow = MainWindow(controller)
    controller.set_view(app)

    app.mainloop()


if __name__ == "__main__":
    main()