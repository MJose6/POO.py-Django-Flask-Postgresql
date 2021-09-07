class Aritmetica:
    """
        Clase aritmetica para realizar operaciones basicas
    """
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        return self.operando1 + self.operando2
    def restar(self):
        return self.operando1 - self.operando2
    def multiplicar(self):
        return self.operando1 * self.operando2
    def dividir(self):
        return self.operando1 / self.operando2

aritmetica1 = Aritmetica(6, 8)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicacion: {aritmetica1.multiplicar()}')
print(f'Division: {aritmetica1.dividir():.2f}')