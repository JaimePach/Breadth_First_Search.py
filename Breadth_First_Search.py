import csv
import os
import time
from os import system

folder = 'C:\\Users\\jg823\\OneDrive\\Documentos\\Pia IA\\'    #   DIRECCION DEL FOLDER "\\low-dimensional"
datos = []

system("cls")   #   LIMPIA LA TERMINAL

#LEE LAS INSTANCIAS DEL ARCHIVO
def asignar_Instancias(Archivo):
   print('____________________________________________________'+Archivo+' ____________________________________________________')
   
   subtema = []
   tarea = []
   duracion = []
   valor = []
   obligatorio = []
   requerimiento1 = []
   requerimiento2 = []
   
   with open(folder+ 'low-dimensional\\' + Archivo, 'rt') as t:
      reader = csv.reader(t)
      for row in reader:
         if(len(row)>0):
            if(row[0] != ''):
               
               subtema.append(int(row[2]))
               tarea.append(int(row[3]))
               duracion.append(int(row[4]))
               valor.append(int(row[5]))
               requerimiento1.append(int(row[7]))
               requerimiento2.append(int(row[8]))
               obligatorio.append(int(row[9]))
   return(list([subtema, tarea, duracion, valor, obligatorio, requerimiento1, requerimiento2]))

def Breadth_First_Search(Datos):

   tareasCompletadas = [] # lista de las tareas que se ejecutaran
   califSubtema = [0,0,0,0,0,0,0,0] # Aqui se almacenara la calificacion de cada subtema mientras hacemos tarea
   duracionSubtema = [0,0,0,0,0,0,0,0] #Aqui se guardara lo que durara haciendo tareas
   # Primero buscamos en cada subtema todas lasa tarea obligatorias
   for subtemaActual in range(0,8,1):
      for tareaActual in range(0, 11, 1):

         if(Datos[4][subtemaActual*11 + tareaActual ] == 1): # Pregunta si la tarea es obligatoria
           
           tareasCompletadas.append(subtemaActual*11 + tareaActual) #Pos agregamos esa tarea
           califSubtema[subtemaActual] += Datos[3][subtemaActual*11 + tareaActual ] #Incrementar calif del subtema
           duracionSubtema[subtemaActual] += Datos[2][subtemaActual*11 + tareaActual] #Incrementar duracion del subtema

           if(Datos[5][subtemaActual*11 + tareaActual] != 0): # pregunta si hay requisito 1
              #si hay lo agregamos
              tareasCompletadas.append(Datos[5][subtemaActual*11 + tareaActual]) #Agregar requisito 1 en tareas
              califSubtema[Datos[0][Datos[5][subtemaActual*11 + tareaActual ]] - 1] += Datos[3][Datos[5][subtemaActual*11 + tareaActual]] # aumentar el valor del requerimiento 1
              duracionSubtema[Datos[0][Datos[5][subtemaActual*11 + tareaActual]] - 1] += Datos[2][Datos[5][subtemaActual*11 + tareaActual]] # aumerntar la duracion del requirimiento 1

           if(Datos[6][subtemaActual*11 + tareaActual] != 0):# pregunta si hay requisito 2
              #si hay lo agregamos
              tareasCompletadas.append(Datos[6][subtemaActual*11 + tareaActual]) #Agregar requisito 1 en tareas
              califSubtema[Datos[0][Datos[6][subtemaActual*11 + tareaActual ]] - 1] += Datos[3][Datos[6][subtemaActual*11 + tareaActual]] # aumentar el valor del requerimiento 2
              duracionSubtema[Datos[0][Datos[6][subtemaActual*11 + tareaActual]] - 1] += Datos[2][Datos[6][subtemaActual*11 + tareaActual]] # aumerntar la duracion del requirimiento 2
       # Aqui se empieza con el algortimo de busqueda del menor valor
      while(califSubtema[subtemaActual]< 70):
        menorDuracion = 10000000000000
        for task in range(0,11,1):
            if((task + subtemaActual*11) not in tareasCompletadas): #Preguntamos si la tarea ya la habiamos hecho
               if(Datos[2][task + subtemaActual*11] <= menorDuracion): # Preguntamos si es la tarea con menor duracion
                 menorDuracion = Datos[2][task + subtemaActual*11]
                 menorValor = Datos[3][task + subtemaActual*11]  
                 menorTarea = task + subtemaActual*11

                 if(Datos[5][task + subtemaActual*11] == 0 and Datos[6][task  + subtemaActual*11] == 0): # si no tiene requirimientos no los suma
                   menorReq1 = 0
                   menorReq2 = 0
                 elif(Datos[5][task  + subtemaActual*11] == 1 and Datos[6][task + subtemaActual*11] == 1):    
                    menorReq1 = Datos[5][task + subtemaActual*11]
                    menorReq2 = Datos[6][task + subtemaActual*11]
                 elif(Datos[5][task + subtemaActual*11] == 0 and Datos[6][task + subtemaActual*11] == 1):    
                    menorReq1 = 0
                    menorReq2 = Datos[6][task + subtemaActual*11]
                 elif(Datos[5][task + subtemaActual*11] == 1 and Datos[6][task + subtemaActual*11] == 0):
                    menorReq1 = Datos[5][task + subtemaActual*11]
                    menorReq2 = 0        
         #Aqui agregamos la tarea con menor duracion           
        tareasCompletadas.append(menorTarea)
        califSubtema[subtemaActual] += menorValor
        duracionSubtema[subtemaActual] += menorDuracion
        #Despues agregamos los requisitos de esa tarea
        if(menorReq1 != 0): # si existe el requisito 1 se agrega
           tareasCompletadas.append(menorReq1)
           califSubtema[Datos[0][menorReq1 - 1]] += Datos[3][menorReq1 - 1]
           duracionSubtema[Datos[0][menorReq1 - 1]] += Datos[2][menorReq1 - 1]
        if(menorReq2 != 0):  # si existe el requisito 2 se agrega 
           tareasCompletadas.append(menorReq2)
           califSubtema[Datos[0][menorReq2 - 1]] += Datos[3][menorReq2 - 1]
           duracionSubtema[Datos[0][menorReq2 - 1]] += Datos[2][menorReq2 - 1]       
   print("\n Las Tareas a completar son las siguientes \n",tareasCompletadas)
   print("\n Las Calificaciones de cada subtema son: \n",califSubtema)
   print("\n La Duracion de cada subtema son: \n",duracionSubtema)

Start = time.time()

for archivo in os.listdir(folder + 'low-dimensional\\'): #Iterar todos los archivos del low-dimensional
   if(archivo.endswith(".csv")):
      separador = archivo.split('_')
      datos = asignar_Instancias(archivo) # Aqui almacenas todos los de datos de un archivo
      resultadoFinal = Breadth_First_Search(datos)

      datos = []

runtime = time.time() - Start
print("Runtime: " + str("{:.15f}".format(runtime)) + "\n")