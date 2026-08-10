import customtkinter as ctk
from models.verification_result import VerificationResult



class ResultWindow(ctk.CTkToplevel):


    result: VerificationResult
    title_label: ctk.CTkLabel
    addition_frame: ctk.CTkFrame
    multiplication_frame: ctk.CTkFrame
    addition_title: ctk.CTkLabel
    multiplication_title: ctk.CTkLabel


    def __init__(self, result: VerificationResult) -> None:
        super().__init__()
        self.result = result

        self._configure_window()
        self._create_widgets()
        self._place_widgets()


    def _configure_window(self) -> None:
        self.title(f"Resultados para Z{self.result.n}")
        self.geometry("900x700")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(1, weight = 1)


    def _create_widgets(self) -> None:
        self.title_label = ctk.CTkLabel(
            master = self,
            text = f"Resultados para Z{self.result.n}",
            font = ctk.CTkFont(
                size = 24,
                weight = "bold",
            )
        )
        self.addition_frame = ctk.CTkFrame(
            master = self,
        )
        self.multiplication_frame = ctk.CTkFrame(
            master = self,
        )
        self.addition_title = ctk.CTkLabel(
            master = self.addition_frame,
            text = f"Tabla de la suma",
            font = ctk.CTkFont(
                size = 18,
                weight = "bold",
            )
        )
        self.multiplication_title = ctk.CTkLabel(
            master = self.multiplication_frame,
            text = f"Tabla de la multiplicacion",
            font = ctk.CTkFont(
                size = 18,
                weight = "bold",
            )
        )


    def _place_widgets(self) -> None:
        self.title_label.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            padx = 20,
            pady = (20, 15)
        )
        self.addition_frame.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            padx = (20, 10),
            pady = 10,
            sticky = "nsew"
        )
        self.multiplication_frame.grid(
            row = 1,
            column = 1,
            padx = (10, 20),
            pady = 10,
            sticky = "nsew"
        )
        self.addition_title.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = (15, 10),
        )
        self.multiplication_title.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = (15, 10)
        )


