import customtkinter as ctk


class MainWindow(ctk.CTk):


    content_frame: ctk.CTkFrame
    title_label: ctk.CTkLabel
    n_entry: ctk.CTkEntry


    def __init__(self) -> None:
        super().__init__()

        self._configure_window()
        self._create_widgets()
        self._place_widgets()


    def _configure_window(self) -> None:
        self.title("Verificador de Anillos")
        self.geometry("600x400")
        self.resizable(False, False)


    def _create_widgets(self) -> None:
        self.content_frame = ctk.CTkFrame(master = self)
        self.title_label = ctk.CTkLabel(
            master = self,
            text = "Verificador de Anillos"
        )


    def _place_widgets(self) -> None:
        self.content_frame.grid(
            row = 0,
            column = 0,
            padx = 20,
            pady = 20,
        )
        self.title_label.grid(
            row = 0,
            column = 0
        )