from controllers.app_controller import AppController
from views.main_window import MainWindow
from models.zn import  Zn
from models.ring_verifier import  RingVerifier


def main() -> None:
    controller: AppController = AppController()
    app: MainWindow = MainWindow(controller)

    z5 = Zn(5)
    ring_verifier = RingVerifier(z5)
    print(ring_verifier.verify_additive_associativity())
    #for row in z5.multiplication_table():
        #print(row)

    app.mainloop()


if __name__ == "__main__":
    main()