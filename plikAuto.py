class Auto:

    rocznik = 0

    def ustawRocznik(self, jakiRok):
        self.rocznik = jakiRok

    def powiedzDzienDobry(self):
        print(f"dzien dobry jestem auto z roku {self.rocznik}")

