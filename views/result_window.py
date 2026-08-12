from itertools import product
import tkinter as tk
import customtkinter as ctk
from models.verification_result import VerificationResult
from models.property_result import PropertyResult


class ResultWindow(ctk.CTkToplevel):


    result: VerificationResult
    title_label: ctk.CTkLabel
    addition_frame: ctk.CTkFrame
    multiplication_frame: ctk.CTkFrame
    addition_title: ctk.CTkLabel
    multiplication_title: ctk.CTkLabel
    addition_table_frame: ctk.CTkFrame
    multiplication_table_frame: ctk.CTkFrame
    elements_frame: ctk.CTkFrame
    elements_title: ctk.CTkLabel
    additive_identity_label: ctk.CTkLabel
    multiplicative_identity_label: ctk.CTkLabel
    additive_inverses_label: ctk.CTkLabel
    multiplicative_inverses_label: ctk.CTkLabel
    verification_frame: ctk.CTkFrame
    verification_title: ctk.CTkLabel


    def __init__(self, result: VerificationResult) -> None:
        super().__init__()

        self.result = result

        self._configure_window()
        self._create_widgets()
        self._place_widgets()
        self._create_tables()
        self._show_elements()
        self._show_verifications()


    def _configure_window(self) -> None:
        self.title(f"Resultados para Z{self.result.n}")
        self.geometry("1000x850")
        self.minsize(900, 700)
        self.resizable(True, True)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)

        self.grid_rowconfigure(1, weight = 1)


    def _create_widgets(self) -> None:

        self.title_label = ctk.CTkLabel(
            master = self,
            text = f"Resultados para Z{self.result.n}",
            font = ctk.CTkFont(
                size = 30,
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
            text = "Tabla de la suma",
            font = ctk.CTkFont(
                size = 22,
                weight = "bold",
            )
        )

        self.multiplication_title = ctk.CTkLabel(
            master = self.multiplication_frame,
            text = "Tabla de la multiplicacion",
            font = ctk.CTkFont(
                size = 22,
                weight = "bold",
            )
        )


        self.addition_table_frame = ctk.CTkFrame(
            master = self.addition_frame,
        )

        self.multiplication_table_frame = ctk.CTkFrame(
            master = self.multiplication_frame,
        )


        self.elements_frame = ctk.CTkFrame(
            master = self,
        )

        self.elements_title = ctk.CTkLabel(
            master = self.elements_frame,
            text = "Elementos destacados",
            font = ctk.CTkFont(
                size = 22,
                weight = "bold",
            )
        )

        self.additive_identity_label = ctk.CTkLabel(
            master = self.elements_frame,
            text = "",
            font = ctk.CTkFont(
                size = 17,
            ),
        )

        self.multiplicative_identity_label = ctk.CTkLabel(
            master = self.elements_frame,
            text = "",
            font = ctk.CTkFont(
                size = 17,
            ),
        )

        self.additive_inverses_label = ctk.CTkLabel(
            master = self.elements_frame,
            text = "",
            justify = "left",
            anchor = "w",
            font = ctk.CTkFont(
                size = 17,
            ),
        )

        self.multiplicative_inverses_label = ctk.CTkLabel(
            master = self.elements_frame,
            text = "",
            justify = "left",
            anchor = "w",
            font = ctk.CTkFont(
                size = 17,
            ),
        )


        self.verification_frame = ctk.CTkFrame(
            master = self,
        )

        self.verification_title = ctk.CTkLabel(
            master = self.verification_frame,
            text = "Verificaciones",
            font = ctk.CTkFont(
                size = 22,
                weight = "bold",
            )
        )


    def _place_widgets(self) -> None:

        self.title_label.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            padx = 20,
            pady = (20, 15),
        )


        self.addition_frame.grid(
            row = 1,
            column = 0,
            padx = (20, 10),
            pady = 10,
            sticky = "nsew",
        )

        self.multiplication_frame.grid(
            row = 1,
            column = 1,
            padx = (10, 20),
            pady = 10,
            sticky = "nsew",
        )


        self.addition_frame.grid_columnconfigure(
            0,
            weight = 1,
        )

        self.addition_frame.grid_rowconfigure(
            1,
            weight = 1,
        )

        self.multiplication_frame.grid_columnconfigure(
            0,
            weight = 1,
        )

        self.multiplication_frame.grid_rowconfigure(
            1,
            weight = 1,
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
            pady = (15, 10),
        )


        self.addition_table_frame.grid(
            row = 1,
            column = 0,
            padx = 10,
            pady = (0, 10),
            sticky = "nsew",
        )

        self.multiplication_table_frame.grid(
            row = 1,
            column = 0,
            padx = 10,
            pady = (0, 10),
            sticky = "nsew",
        )


        self.elements_frame.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            padx = 20,
            pady = 10,
            sticky = "ew",
        )


        self.elements_title.grid(
            row = 0,
            column = 0,
            columnspan = 2,
            padx = 10,
            pady = (15, 10),
        )

        self.additive_identity_label.grid(
            row = 1,
            column = 0,
            padx = 15,
            pady = 5,
            sticky = "w",
        )

        self.multiplicative_identity_label.grid(
            row = 1,
            column = 1,
            padx = 15,
            pady = 5,
            sticky = "w",
        )

        self.additive_inverses_label.grid(
            row = 2,
            column = 0,
            padx = 15,
            pady = 5,
            sticky = "nw",
        )

        self.multiplicative_inverses_label.grid(
            row = 2,
            column = 1,
            padx = 15,
            pady = 5,
            sticky = "nw",
        )


        self.verification_frame.grid(
            row = 3,
            column = 0,
            columnspan = 2,
            padx = 20,
            pady = (0, 20),
            sticky = "ew",
        )

        self.verification_title.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = (15, 10),
        )


    def _create_tables(self) -> None:

        self._create_scrollable_table(
            parent = self.addition_table_frame,
            table = self.result.addition_table,
            operation = "+",
        )

        self._create_scrollable_table(
            parent = self.multiplication_table_frame,
            table = self.result.multiplication_table,
            operation = "*",
        )


    def _create_scrollable_table(
        self,
        parent: ctk.CTkFrame,
        table: list[list[int]],
        operation: str,
    ) -> None:

        canvas = tk.Canvas(
            master = parent,
            highlightthickness = 0,
        )

        vertical_scrollbar = ctk.CTkScrollbar(
            master = parent,
            orientation = "vertical",
            command = canvas.yview,
        )

        horizontal_scrollbar = ctk.CTkScrollbar(
            master = parent,
            orientation = "horizontal",
            command = canvas.xview,
        )

        canvas.configure(
            yscrollcommand = vertical_scrollbar.set,
            xscrollcommand = horizontal_scrollbar.set,
        )


        table_frame = ctk.CTkFrame(
            master = canvas,
        )

        canvas.create_window(
            (0, 0),
            window = table_frame,
            anchor = "nw",
        )


        table_frame.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion = canvas.bbox("all")
            )
        )


        canvas.grid(
            row = 0,
            column = 0,
            sticky = "nsew",
        )

        vertical_scrollbar.grid(
            row = 0,
            column = 1,
            sticky = "ns",
        )

        horizontal_scrollbar.grid(
            row = 1,
            column = 0,
            sticky = "ew",
        )


        parent.grid_columnconfigure(
            0,
            weight = 1,
        )

        parent.grid_rowconfigure(
            0,
            weight = 1,
        )


        self._create_table(
            parent = table_frame,
            table = table,
            operation = operation,
        )


    def _create_table(
        self,
        parent: ctk.CTkFrame,
        table: list[list[int]],
        operation: str,
    ) -> None:

        n: int = len(table)


        corner_label: ctk.CTkLabel = ctk.CTkLabel(
            master = parent,
            text = operation,
            width = 40,
            height = 34,
            font = ctk.CTkFont(
                family = "Segoe UI",
                size = 16,
                weight = "bold",
            )
        )

        corner_label.grid(
            row = 0,
            column = 0,
            padx = 1,
            pady = 1,
        )


        for column in range(n):

            label: ctk.CTkLabel = ctk.CTkLabel(
                master = parent,
                text = str(column),
                width = 40,
                height = 34,
                font = ctk.CTkFont(
                    family = "Segoe UI",
                    size = 16,
                    weight = "bold",
                )
            )

            label.grid(
                row = 0,
                column = column + 1,
                padx = 1,
                pady = 1,
            )


        for row in range(n):

            label: ctk.CTkLabel = ctk.CTkLabel(
                master = parent,
                text = str(row),
                width = 40,
                height = 34,
                font = ctk.CTkFont(
                    family = "Segoe UI",
                    size = 16,
                    weight = "bold",
                )
            )

            label.grid(
                row = row + 1,
                column = 0,
                padx = 1,
                pady = 1,
            )


        for row, column in product(range(n), range(n)):

            value: int = table[row][column]

            label: ctk.CTkLabel = ctk.CTkLabel(
                master = parent,
                text = str(value),
                width = 40,
                height = 34,
                font = ctk.CTkFont(
                    family = "Segoe UI",
                    size = 15,
                )
            )

            label.grid(
                row = row + 1,
                column = column + 1,
                padx = 1,
                pady = 1,
            )


    def _show_elements(self) -> None:

        if self.result.additive_identity is None:

            self.additive_identity_label.configure(
                text = "Elemento neutro de la suma: No existe",
            )

        else:

            self.additive_identity_label.configure(
                text = f"Elemento neutro de la suma: {self.result.additive_identity}",
            )


        if self.result.multiplicative_identity is None:

            self.multiplicative_identity_label.configure(
                text = "Elemento identidad del producto: No existe",
            )

        else:

            self.multiplicative_identity_label.configure(
                text = f"Elemento identidad del producto: {self.result.multiplicative_identity}",
            )


        self.additive_inverses_label.configure(
            text = self._format_inverses(
                "Inversos aditivos",
                self.result.additive_inverses,
            )
        )

        self.multiplicative_inverses_label.configure(
            text = self._format_inverses(
                "Inversos multiplicativos",
                self.result.multiplicative_inverses,
            )
        )


    def _format_inverses(
        self,
        title: str,
        inverses: dict[int, int],
    ) -> str:

        if not inverses:

            return f"{title}: No existen"


        inverse_text: str = f"{title}:\n"

        for element, inverse in inverses.items():

            inverse_text += f"    {element} → {inverse}\n"

        return inverse_text.rstrip()


    def _show_verifications(self) -> None:

        self._show_property(
            self.result.additive_group,
            1,
        )

        self._show_property(
            self.result.multiplicative_semigroup,
            2,
        )

        self._show_property(
            self.result.additive_abelian_group,
            3,
        )

        self._show_property(
            self.result.ring,
            4,
        )

        self._show_property(
            self.result.commutative_ring,
            5,
        )

        self._show_property(
            self.result.field,
            6,
        )


    def _show_property(self, property_result: PropertyResult, row: int) -> None:
        symbol: str

        if property_result.is_valid:
            symbol = "✓"
        else:
            symbol = "✗"


        label: ctk.CTkLabel = ctk.CTkLabel(
            master = self.verification_frame,
            text = f"{symbol}  {property_result.name}",
            font = ctk.CTkFont(
                size = 17,
            ),
        )

        label.grid(
            row = row,
            column = 0,
            padx = 20,
            pady = 2,
            sticky = "w",
        )