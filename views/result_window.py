import customtkinter as ctk


class ResultWindow(ctk.CTkToplevel):


    n: int


    def __init__(self, n: int) -> None:
        super().__init__()
        self.n = n

        self._configure_window()


    def _configure_window(self) -> None:
        self.title(f"Resultados para Z{self.n}")
        self.geometry("900x700")
        self.resizable(False, False)


