class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interes = 0.01, balance = 0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)


    def deposito(self, amount):
        self.balance += amount
        print("Deposito realizado con exito")
        return self

    def retiro(self, amount):
        self.balance -= amount
        print("Retiro realizado con exito")
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



cuentaBancaria1 = CuentaBancaria()
cuentaBancaria2 = CuentaBancaria()

cuentaBancaria1.deposito(250).deposito(910).deposito(27).retiro(469).generar_interes().mostrar_info_cuenta()
cuentaBancaria2.deposito(5).deposito(500).retiro(300).retiro(55).retiro(220).retiro(100).generar_interes().mostrar_info_cuenta()

CuentaBancaria.mostrar_todas_las_cuentas()



