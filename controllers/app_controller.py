from controllers.utils import Utils


class AppController:


    n: int


    def verify_ring(self, n_text: str) -> tuple[bool, str]:
        try:
            n = int(n_text)
        except ValueError:
            return False, "Debe ingresar un numero entero"

        if not Utils.INFERIOR_LIMIT <= n <= Utils.SUPERIOR_LIMIT:
            return False, f"El valor debe estar entre {Utils.INFERIOR_LIMIT} y {Utils.SUPERIOR_LIMIT}"

        return True, ""
