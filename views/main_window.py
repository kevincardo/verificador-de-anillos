import customtkinter as ctk


class MainWindow(ctk.CTk):


    content_frame: ctk.CTkFrame
    title_label: ctk.CTkLabel
    input_label: ctk.CTkLabel
    verify_button: ctk.CTkButton
    n_entry: ctk.CTkEntry
    error_label: ctk.CTkLabel


    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

        self._configure_window()
        self._create_widgets()
        self._place_widgets()


    def get_n(self) -> str:
        return self.n_entry.get()


    def show_error(self, message: str) -> None:
        pass


    def clean_error(self) -> None:
        pass


    def _configure_window(self) -> None:
        self.title("Verificador de Anillos")
        self.geometry("600x400")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)


    def _create_widgets(self) -> None:
        self.content_frame = ctk.CTkFrame(master = self)
        self.title_label = ctk.CTkLabel(
            master = self.content_frame,
            text = "Verificador de Anillos",
            font = ("Segoe UI", 46, "bold")
        )
        self.input_label = ctk.CTkLabel(
            master = self.content_frame,
            text = "Ingrese el valor de n: ",
            font = ("Segoe UI", 16, "bold")
        )
        self.n_entry = ctk.CTkEntry(
            master = self.content_frame,
            font = ("Segoe UI", 16),
        )
        self.verify_button = ctk.CTkButton(
            master = self.content_frame,
            text = "Verificar",
            font = ("Segoe UI", 16, "bold"),
            command = self.controller.verify_ring
        )
        self.error_label = ctk.CTkLabel(
            master = self.content_frame,
            text = "",
            text_color = "red",
        )


    def _place_widgets(self) -> None:
        self.content_frame.grid(
            row = 0,
            column = 0,
            padx = 20,
            pady = 20,
            sticky = "nsew"
        )
        self.title_label.grid(
            row = 0,
            column = 0,
            padx = 35,
            sticky = "nsew"
        )
        self.input_label.grid(
            row = 1,
            column = 0,
            padx = 50,
            pady = 30,
            sticky = "nsew"
        )
        self.n_entry.grid(
            row = 2,
            column = 0,
            padx = 50,
            pady = 10,
            sticky = "nsew"
        )
        self.error_label.grid(
            row = 3,
            column = 0,
            padx = 50,
            pady = 10,
            sticky = "nsew"
        )
        self.verify_button.grid(
            row = 4,
            column = 0,
            padx = 50,
            pady = 10,
            sticky = "nsew"
        )