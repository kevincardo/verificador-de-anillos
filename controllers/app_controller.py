from controllers.utils import Utils
from models.zn import Zn
from models.ring_verifier import RingVerifier
from models.verification_result import VerificationResult
from views.result_window import ResultWindow



class AppController:


    n: int


    def verify_ring(self, n_text: str) -> tuple[bool, str, VerificationResult | None]:
        try:
            n = int(n_text)
        except ValueError:
            return False, "Debe ingresar un numero entero", None

        if not Utils.INFERIOR_LIMIT <= n <= Utils.SUPERIOR_LIMIT:
            return False, f"El valor debe estar entre {Utils.INFERIOR_LIMIT} y {Utils.SUPERIOR_LIMIT}", None

        zn: Zn = Zn(n)
        verifier: RingVerifier = RingVerifier(zn)
        result: VerificationResult = verifier.verify_all()

        return True, "", result
