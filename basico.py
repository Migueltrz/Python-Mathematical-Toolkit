import matplotlib as mp 
import pandas as pd
import numpy as np 


class basicos():

    def suma(s,l,i):
       if l[0] == 0:
         l[0] = float(s)     
       else:
         v = l[i] + float(s)
         l.append(v)
         print("%s + %s = %s" % (l[i], float(s), v)) 


    def resta(s,l,i):
      if l[0] == 0:
         l[0] = float(s)     
      else:
         v = l[i] - float(s)
         l.append(v)
         print("%s - %s = %s" % (l[i], float(s), v))


    def mult(s,l,i):
      if l[0] == 0:
         l[0] = float(s)     
      else:
         v = l[i] * float(s)
         l.append(v)
         print("%s * %s = %s" % (l[i], float(s), v))

    
    def div(s,l,i):
       if l[0] == 0:
         l[0] = float(s)     
       else:
         v = l[i] / float(s)
         l.append(v)
         print("%s / %s = %s" % (l[i], float(s), v))


    def rc(s,l):
       rc = float(s) ** (1/2)
       l.append(rc)
       print("rc =", rc)

    
    def pot(s,l):
       pt = float(input("potencia: "))
       pot = float(s) ** (pt)
       l.append(pot)
       print("pot =", pot)

    def por(s,l):
       por = float(input("porcentaje: "))
       pc = float(s)*(por)* 0.01
       l.append(pc)
       print("pc =", pc)


def func_b(b):
   print("Si desea dejar de introducir valores poner (p)")
   ls = [0]
   i = -1
   dic = {}
   while True:
     s=input("valor: ")

     if s == "p":
      return dic

     
     elif b == "s":  
       try:         
        basicos.suma(s,ls,i)
        i += 1
        dic["sumas"] = ls[1:]
       except:
        print("Introduzca un valor valido")

     elif b == "r":  
       try:
         basicos.resta(s,ls,i)
         i += 1
         dic["restas"] = ls[1:]
       except:
        print("Introduzca un valor valido")

     elif b == "m":  
       try:
        basicos.mult(s,ls,i)
        i += 1
        dic["multiplicación"] = ls[1:]
       except:
         print("Introduzca un valor valido") 

     elif b == "d":  
       try:
        basicos.div(s,ls,i)
        i += 1
        dic["división"] = ls[1:]
       except:
         print("Introduzca un valor valido")

     elif b == "rc":
        try:
            basicos.rc(s,ls)
            dic["Raíz cuadrada"] = ls[1:]
        except:
            print("Introduzca un valor valido")

     elif b == "pt":
       try:
         basicos.pot(s,ls)
         dic["Potencia"] = ls[1:]
       except:
         print("Introduzca un valor valido")

     elif b == "pc":
       try:
         basicos.por(s,ls)
         dic["Porcentaje"] = ls[1:]
       except:
         print("Introduzca un valor valido")
    
         
         
   

          
   
       
       
   
   
    