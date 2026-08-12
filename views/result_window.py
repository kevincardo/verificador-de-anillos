from itertools import product
import customtkinter as ctk
from models.verification_result import VerificationResult


class ResultWindow(ctk.CTkToplevel):


    result: VerificationResult
    title_label: ctk.CTkLabel
    addition_frame: ctk.CTkFrame
    multiplication_frame: ctk.CTkFrame
    addition_table_frame: ctk.CTkScrollableFrame
    multiplication_table_frame: ctk.CTkScrollableFrame
    addition_title: ctk.CTkLabel
    multiplication_title: ctk.CTkLabel
    elements_frame: ctk.CTkFrame
    elements_title: ctk.CTkLabel
    additive_identity_label: ctk.CTkLabel
    multiplicative_identity_label: ctk.CTkLabel
    additive_inverses_label: ctk.CTkLabel
    multiplicative_inverses_label: ctk.CTkLabel


    def __init__(self, result: VerificationResult) -> None:
        super().__init__()
        self.result = result

        self._create_widgets()
        self._configure_window()
        self._place_widgets()
        self._create_tables()
        self._show_elements()


    def _configure_window(self) -> None:
        self.title(f"Resultados para Z{self.result.n}")
        self.geometry("900x700")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.addition_frame.grid_rowconfigure(1, weight=1)
        self.addition_frame.grid_columnconfigure(0, weight=1)

        self.multiplication_frame.grid_rowconfigure(1, weight=1)
        self.multiplication_frame.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)


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
        self.addition_table_frame = ctk.CTkScrollableFrame(
            master = self.addition_frame,
        )
        self.multiplication_table_frame = ctk.CTkScrollableFrame(
            master = self.multiplication_frame,
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
        self.elements_frame = ctk.CTkFrame(
            master = self,
        )
        self.elements_title = ctk.CTkLabel(
            master = self.elements_frame,
            text = "Elementos Destacados",
            font = ctk.CTkFont(
                size = 18,
                family = "Segoe UI",
                weight = "bold",
            )
        )
        self.additive_identity_label = ctk.CTkLabel(
            master = self.elements_frame,
            text = "",
            font = ctk.CTkFont(
                family = "Segoe UI",
                size = 24
            )
        )
        self.multiplicative_identity_label = ctk.CTkLabel(
            master=self.elements_frame,
            text="",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=24
            )
        )
        self.multiplicative_inverses_label = ctk.CTkLabel(
            master=self.elements_frame,
            text="",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=24
            ),
            justify = "left"
        )
        self.additive_inverses_label = ctk.CTkLabel(
            master=self.elements_frame,
            text="",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=24
            ),
            justify="left"
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
        self.addition_table_frame.grid(
            row = 1,
            column = 0,
            padx = 10,
            pady = (0, 10),
            sticky = "nsew"
        )
        self.multiplication_table_frame.grid(
            row = 1,
            column = 0,
            padx = 10,
            pady = (0, 10),
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
        self.elements_frame.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            padx = 20,
            pady = (10, 20),
            sticky = "nsew"
        )
        self.elements_title.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=15,
            pady=(15, 10),
        )

        self.additive_identity_label.grid(
            row=1,
            column=0,
            padx=15,
            pady=5,
            sticky="w",
        )

        self.multiplicative_identity_label.grid(
            row=1,
            column=1,
            padx=15,
            pady=5,
            sticky="w",
        )

        self.additive_inverses_label.grid(
            row=2,
            column=0,
            padx=15,
            pady=5,
            sticky="w",
        )

        self.multiplicative_inverses_label.grid(
            row=2,
            column=1,
            padx=15,
            pady=5,
            sticky="w",
        )


    def _create_tables(self) -> None:
        self._create_table(
            parent = self.addition_table_frame,
            table = self.result.addition_table,
            type = "addition"
        )
        self._create_table(
            parent = self.multiplication_table_frame,
            table = self.result.multiplication_table,
            type = "multiplication"
        )


    def _create_table(self, parent: ctk.CTkScrollableFrame, table: list[list[int]], type: str) -> None:
        n: int = len(table)
        sign: str = ""

        match type:
            case "addition":
                sign = "+"
            case "multiplication":
                sign = "*"


        corner_label: ctk.CTkLabel = ctk.CTkLabel(
            master = parent,
            text = sign,
            width = 35,
            height = 30,
            font = ctk.CTkFont(
                family = "Segoe UI",
                size = 24,
                weight = "bold",
            )
        )
        corner_label.grid(
            row = 0,
            column = 0,
            padx = 1,
            pady = 1
        )

        for column in range(n):
            label: ctk.CTkLabel = ctk.CTkLabel(
                master = parent,
                text = str(column),
                width = 35,
                height = 30,
                font = ctk.CTkFont(
                    family = "Segoe UI",
                    size = 24,
                    weight = "bold",
                )
            )
            label.grid(
                row = 0,
                column = column + 1,
                padx = 1,
                pady = 1
            )

        for row in range(n):
            label: ctk.CTkLabel = ctk.CTkLabel(
                master = parent,
                text = str(row),
                width = 35,
                height = 30,
                font = ctk.CTkFont(
                    family = "Segoe UI",
                    size = 24,
                    weight = "bold",
                )
            )
            label.grid(
                row = row + 1,
                column = 0,
                padx = 1,
                pady = 1
            )

        for row, column in product(range(n), range(n)):
            value: int = table[row][column]

            label: ctk.CTkLabel = ctk.CTkLabel(
                master = parent,
                text = str(value),
                width = 35,
                height = 30,
                font = ctk.CTkFont(
                    family = "Segoe UI",
                    size = 24,
                )
            )
            label.grid(
                row = row + 1,
                column = column + 1,
                padx = 1,
                pady = 1
            )


    def _show_elements(self) -> None:
        additive_identity = self.result.additive_identity
        multiplicative_identity = self.result.multiplicative_identity

        if additive_identity is None:
            self.additive_identity_label.configure(text = "Neutro aditivo: No existe")
        else:
            self.additive_identity_label.configure(text = f"Neutro aditivo: {additive_identity}")

        if multiplicative_identity is None:
            self.multiplicative_identity_label.configure(text = "Neutro multiplicativo: No existe")
        else:
            self.multiplicative_identity_label.configure(text = f"Neutro multiplicativo: {multiplicative_identity}")

        self.additive_inverses_label.configure(
            text = self._format_inverses("Inversos aditivos", self.result.additive_inverses)
        )

        self.multiplicative_inverses_label.configure(
            text = self._format_inverses("Inversos multiplicativos", self.result.multiplicative_inverses)
        )


    def _format_inverses(self, text: str, inverses: dict[int, int]) -> str:
        if not inverses:
            return f"{text}: No existen"

        values = []

        for element, inverse in inverses.items():
            values.append(f"{element} -> {inverse}")

        return f"{text}: \n" + "".join(values)




