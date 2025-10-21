import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sp
import seaborn as sns


class estadistica():

    def hist():
       
        a = input("Ingrese el nombre del archivo CSV (incluya la extensión .csv): ")

        try:
            df = pd.read_csv(a)
        except FileNotFoundError:
            print("El archivo especificado no se encontró.")
            return
        except Exception as e:
            print("Ocurrió un error al leer el archivo CSV:", e)
            return
        
        print("Columnas disponibles en el archivo CSV:")
        for col in df.columns:
            print(col)


       
        filt = input("¿Desea filtrar por valores numéricos (n), por año 'si es formato valido' (a) o de manera normal 'str' (m) o usar toda la columna (c)? ").lower()

        if filt == 'n':
           
            columna = input("Ingrese el nombre de la columna para filtrar: ")

           
            if columna not in df.columns:
                print(f"La columna '{columna}' no existe en el archivo CSV.")
                return
           
            try:
                df[columna] = df[columna].astype(float)
            except ValueError:
                try:
                    df['average_rating'] = pd.to_numeric(df['average_rating'], errors='coerce')
                    df.dropna(subset=['average_rating'], inplace=True)
                except Exception as e:
                    print("Ocurrió un error al limpiar los valores de la columna 'average_rating':", e)
        

           
            f_min = float(input(f"Ingrese el valor mínimo de los renglones de la columna '{columna}' que desea filtrar: "))
            f_max = float(input(f"Ingrese el valor máximo de los renglones de la columna '{columna}' que desea filtrar: "))

           
            d_filt = df[(df[columna] >= f_min) & (df[columna] <= f_max)]

        elif filt == 'a':
           
            columna = input("Ingrese el nombre de la columna con las fechas: ")

           
            if columna not in df.columns:
                print(f"La columna '{columna}' no existe en el archivo CSV.")
                return
           
    

           
            try:
                df[columna] = pd.to_datetime(df[columna])
            except Exception as e:
                print("Ocurrió un error al convertir la columna a fecha:", e)
                return

           
            v_func = input(f"Ingrese el valor del año de que desea filtrar: ")

           
            d_filt = df[df[columna].dt.year == float(v_func)]

        elif filt == 'm':
           
            columna = input("Ingrese el nombre de la columna para filtrar: ")

           
            if columna not in df.columns:
                print(f"La columna '{columna}' no existe en el archivo CSV.")
                return
           
            v_func = input(f"Ingrese el valor de los renglones de la columna '{columna}' que desea filtrar: ")

           
            d_filt = df[df[columna] == v_func]
        elif filt == "c":
            c_hist = input("Ingrese el nombre de la columna para hacer el histograma: ")
            d_hist = df[c_hist]

           
            plt.hist(d_hist, bins=10, alpha=0.5)
            plt.xlabel(c_hist)
            plt.ylabel('Frecuencia')
            plt.title(f'Histograma de los datos de la columna {c_hist}')
            plt.grid(True)
            plt.show()
            return

        else:
            print("Opción no válida.")
            return

        
        c_hist = input("Ingrese el nombre de la columna para hacer el histograma: ")

        
        if c_hist not in d_filt.columns:
            print(f"La columna '{c_hist}' no existe en los datos filtrados.")
            return

        
        d_hist = d_filt[c_hist]

        
        plt.hist(d_hist, bins=10, alpha=0.5)
        plt.xlabel(c_hist)
        plt.ylabel('Frecuencia')
        plt.title(f'Histograma de los datos de la columna {c_hist} filtrados por {columna}')
        plt.grid(True)
        plt.show()



    def filt():
        
        a = input("Ingrese el nombre del archivo CSV (incluya la extensión .csv): ")

        
        try:
            df = pd.read_csv(a)
        except FileNotFoundError:
            print("El archivo especificado no se encontró.")
            return
        except Exception as e:
            print("Ocurrió un error al leer el archivo CSV:", e)
            return

        
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    
        for columna in df.select_dtypes(include=['object']):
            df[columna] = pd.to_numeric(df[columna], errors='coerce')

    
        desc_df = df.describe()

      
        print("Estadísticas descriptivas del DataFrame:")
        print(desc_df)

        print("\nOpciones posibles para guardar (todos los renglones):")
        print(desc_df.index)

        dat_g = input("Ingrese los datos que desea guardar (separe con comas, por ejemplo, mean,std,min,max): ").split(',')

      
        df_filt = desc_df.loc[dat_g]

        nuevo_csv = input("Ingrese el nombre del archivo CSV para guardar los datos filtrados (incluya la extensión .csv): ")
        df_filt.to_csv(nuevo_csv, index=True)
        print(f"Los datos filtrados se han guardado en '{nuevo_csv}'.")


def func_e(v):
    while True:
        if v == "h":
            try:
                estadistica.hist()
                break
            except:
                print("Revisa que los valores sean adecuados.")
        if v == "f":
            try:
                estadistica.filt()
                break
            except:
                print("Revisa que los valores sean adecuados.")

#estadistica.filt()
#estadistica.hist()   
