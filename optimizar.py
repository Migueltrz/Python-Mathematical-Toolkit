import sympy as sp



def opt():
    x = sp.Symbol("x")
    fun = sp.sympify(input("Función con 'x' como variable esa variable: "))


    d_1 = sp.diff(fun, x)
    d_2 = sp.diff(d_1, x)

    pcr = sp.solve(d_1, x)

    if pcr == []:
        print("La función proporcionada no tiene valores críticos")
    else: 
        print("Valores críticos:", pcr)

        for p in pcr:
            if not sp.im(p):
                d_2_ev = d_2.subs(x, p)
                y = fun.subs(x,p)
                if d_2_ev > 0:
                    print(f"El punto crítico ({p},{y}) es un mínimo")
                elif d_2_ev < 0:
                    print(f"El punto crítico ({p},{y}) es un máximo")
                else:
                    d_1_iz = d_1.subs(x, p - 0.001)
                    d_1_der = d_1.subs(x, p + 0.001)

                    if d_1_iz * d_1_der < 0:
                        
                        if d_1_iz > d_1_der :
                            print(f"En el punto crítico ({p},{y}) hay un máximo")
                        else:
                            print(f"En el punto crítico ({p},{y}) hay un mínimo local")
                    else:
                        print(f"El punto crítico ({p},{y}) es un punto de inflexión")
            else:
                print("Tu función tiene raices negativas, busca otro metodo para encontrar el punto de inflexión")
        
