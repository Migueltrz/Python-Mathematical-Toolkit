import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import seaborn as sns


class avanzado():
    

    def graf():
        exp = input("Ingrese la función usando 'x' como variable y 'np.' si es trigonométrica u otro tipo de función que lo requiera: ")
        
        
        r_i = eval(input("Inicio del rango (puede usar np.pi): ")) 
        r_f = eval(input("Ingrese el fin del rango (puede usar np.pi): ")) 
        n_p = int(input("Cantidad de puntos a graficar: "))
        x = np.linspace(r_i, r_f, n_p)

        y = eval(exp)
        sns.set_style("dark")

        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
        
    

    def inte():
        exp = input("¿Quieres hacer una integral definida (d) o indefinida (i)? ")
        if exp == 'd':

            func = input("Ingrese la función con respecto a 'x' : ")
            l_i = float(input("Límite inferior de integración: "))
            l_s = float(input("Límite superior de integración: "))
            x = sp.Symbol('x')
            f = sp.sympify(func)
            integral = sp.integrate(f, (x, l_i, l_s))
            print("Resultado:", integral)

        elif exp == 'i':

            func = input("Ingrese la función con respecto a 'x': ")
            x = sp.Symbol('x')
            f = sp.sympify(func)
            integral = sp.integrate(f, x)
            print("Resultado:", integral)


def func_a(v):
     while True:
        if v == "g":
            try:
                avanzado.graf()
                break
            except:
                print("Introduzca un valor adecuado")
        elif v == "i":
            try:
                avanzado.inte()
                break
            except:
                print("Introduzca un valor adecuado")


