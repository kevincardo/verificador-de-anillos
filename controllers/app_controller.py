from views.main_window import MainWindow


class AppController:


    INFERIOR_LIMIT: int = 2
    SUPERIOR_LIMIT: int = 50

    view: MainWindow
    n: int


    def __init__(self) -> None:
        self.view = None


    def verify_ring(self) -> None:
        self.view.clean_error()

        try:
            n = int(self.view.get_n())
        except ValueError:
            self.view.show_error("Debe ingresar un numero entero")
            return

        if not self.INFERIOR_LIMIT <= n <= self.SUPERIOR_LIMIT:
            self.view.show_error("Debe ingresar un numero entero entre 2 y 50")
            return

        print(f"n = {n}")


    def set_view(self, view: MainWindow) -> None:
        self.view = view
