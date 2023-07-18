class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount

    def mostrar_balance(self):
        print(self.balance_cuenta)

    def hacer_transferencia(self, amount, receiver):
        if self.balance_cuenta >= amount:
            self.balance_cuenta -= amount
            receiver.hacer_deposito(amount)
            print(f"{self.name} ha tranferido ${amount} a {receiver.name}")
        else:
            print("Fondos insuficientes para realizar transferencia")




bobby = Usuario("Bobby Lee", "bobbylee@python.com")

john = Usuario("John Shepard", "cmdrshep@alliance.com")

geralt = Usuario("Geralt de Rivia", "geraltwitcher@gmail.com")

bobby.hacer_deposito(250)
bobby.hacer_deposito(550)
bobby.hacer_deposito(755)
bobby.hacer_retiro(500)
bobby.mostrar_balance()

john.hacer_deposito(200)
john.hacer_deposito(150)
john.hacer_retiro(150)
john.hacer_retiro(350)
john.mostrar_balance()

geralt.hacer_deposito(1000)
geralt.hacer_retiro(333)
geralt.hacer_retiro(333)
geralt.hacer_retiro(333)
geralt.mostrar_balance()


bobby.hacer_transferencia(200, geralt)
bobby.mostrar_balance()
geralt.mostrar_balance()


