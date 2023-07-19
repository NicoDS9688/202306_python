class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = {'cuenta1': CuentaBancaria(tasa_interes = 0.02, balance = 0),
                       'cuenta2': CuentaBancaria(tasa_interes = 0.02, balance = 0)}

    def hacer_deposito(self, amount, accountNmbr):
        self.cuenta[accountNmbr].deposito(amount)
        return self

    def hacer_retiro(self, amount, accountNmbr):
        self.cuenta[accountNmbr].retiro(amount)
        return self

    def mostrar_balance(self, accountNmbr):
        self.cuenta[accountNmbr].mostrar_info_cuenta()
        return self

    def hacer_transferencia(self, amount, receiver, sender_accountNmbr, receiver_accountNmbr):
        if self.cuenta[sender_accountNmbr].balance >= amount:
            self.cuenta[sender_accountNmbr].retiro(amount)
            receiver.hacer_deposito(amount, receiver_accountNmbr)
            print(f"{self.name} ha transferido ${amount} a {receiver.name}")
        else:
            print("Fondos insuficientes para realizar transferencia")
        return self



class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interes = 0.01, balance = 0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)


    def deposito(self, amount):
        self.balance += amount
        print(f"Deposito por el valor de ${amount} realizado con exito")
        return self

    def retiro(self, amount):
        self.balance -= amount
        print(f"Retiro por el valor de ${amount} realizado con exito")
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            balance1 = self.balance
            self.balance += self.balance * self.tasa_interes
            print(f"Se ha generado ${self.tasa_interes * balance1}")
        else:
            print("No se ha podido relizar la operacion debido a fondos insuficientes")
        return self

    @classmethod
    def mostrar_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            print("Informacion de cuenta:")
            cuenta.mostrar_info_cuenta()
            print("-"*10)


usuario1 = Usuario("John Shepard", "cmdrshep@alliance.com")
usuario2 = Usuario("Geralt de Rivia", "geraltwitcher@gmail.com")

usuario1.hacer_deposito(200, 'cuenta1')
usuario1.hacer_retiro(100, 'cuenta2')
usuario1.mostrar_balance('cuenta1')
usuario1.mostrar_balance('cuenta2')

usuario1.hacer_transferencia(50, usuario2, 'cuenta1', 'cuenta1')
usuario1.mostrar_balance('cuenta1')
usuario2.mostrar_balance('cuenta1')

CuentaBancaria.mostrar_todas_las_cuentas()
