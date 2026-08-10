from controllers.app_controller import AppController
from views.main_window import MainWindow
from models.zn import  Zn
from models.ring_verifier import  RingVerifier


def main() -> None:
    controller: AppController = AppController()
    app: MainWindow = MainWindow(controller)

    app.mainloop()


if __name__ == "__main__":
    main()