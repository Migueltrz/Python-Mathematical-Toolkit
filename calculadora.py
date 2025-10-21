from avanzado import func_a
from basico import func_b
from estadistica import func_e
from optimizar import opt
import pandas as pd



while True:
    op=input("¿Qué tipo de operación deseas hacer?: Básica (B) o Avanzada (A) ")
    if op == "A" or op == "B":
        break 
    else:
        print("Pon un valor valido")
    

if op == "B":
    dic = {}
    while True:
        b = input('''¿Qué operación deseas hacer?, suma(s), resta(r), multiplicación(m), división(d), 
raíz cuadrada(rc), potencia(pt) o porcentaje(pc) o salir(e) ''')
        la = ["s","r","m","d","rc","pt","pc"]  
        if b == "e":
            break   
        elif b in la: 
            dic.update(func_b(b))
        else:
            print("Introduzca un valor adecuado")
    try:
        max_l = max(len(v) for v in dic.values())
        for k, v in dic.items():
            if len(v) < max_l:
                dic[k] += [None] * (max_l - len(v))


        dc = pd.DataFrame(dic)
        dc.to_csv('Básicos.csv', index=False)
    except:
        print("Intente hacer una operación la siguiente ocasión")

elif op == "A":
    while True:
        b = input("¿Qué quieres hacer?, Estadística (s), operaciones Avanzadas(o) o salir(e) ")
        if b == "e":
            break
        elif b == "s":
            while True:
                v = input("Histograma de datos(h), filtro de datos(f) o regresar(r) ")
                if v == "r":
                    break
                elif v in ["h","f"]:
                    func_e(v)
        elif b == "o":
            while True:
                v = input("Optimización de funciones(op), graficar(g), integrar(i) o regresar(r) ")
                if v == "r":
                    break
                elif v == "op": 
                    while True: 
                        try:
                            opt()
                            break
                        except:
                            print("Introduce operaciones validas.")

                elif v in ["g","i"]:
                   func_a(v)
                else:
                    print("Introduzca un valor adecuado.")
        
        else:
            print("Introduzca un valor adecuado")


        

        

     
                
            
                



