# -*- coding: utf-8 -*-
import matplotlib.image as mpimg#abrir la imagen
from PIL import Image#abrir la imagen
import os#recorrer carpetas
import csv#generar el archivo
#import math
###############################################################################
    #Variables Globales y creación de la matriz
###############################################################################
a = 0
b = 0
conClase = 0
opcion = 0
matrizDataSet = []
for i in range(2370):
    matrizDataSet.append([0.0]*15)
    
###############################################################################
    #Obtencion de propiedades
###############################################################################

#Obtencion del promedio de columnas entre filas
def OP1(imagen, columnas, filas):
    promedioColFil = columnas/filas
    return promedioColFil

#Contador de unos respecto a la imagen
def OP2(imagen, columnas, filas):
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            uno = (int(imagen[i][j]))
            if(uno != 0):
                contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos

#Contador de unos con respecto a la columa intermedia
def OP3(imagen, columnas, filas):
    colInter = int(columnas/2)
    contUnos = 0
    promedioUnos = 0    
    for i in range(filas):
        for j in range(columnas):
            if(j == colInter):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos

#Contador de unos con respecto a la columna 1/4
def OP4(imagen, columnas, filas):
    colCuarto = int(columnas/4)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(j == colCuarto):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos

#Contador de unos con respecto a la columna 3/4
def OP5(imagen, columnas, filas):
    colTresCuartos = int((columnas/4)*3)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(j == colTresCuartos):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos

#Contador de unos con respecto a la fila intermedia
def OP6(imagen, columnas, filas):
    filInter = int(filas/2)
    contUnos = 0
    promedioUnos = 0    
    for i in range(filas):
        for j in range(columnas):
            if(i == filInter):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos

#Contador de unos con respecto a la fila 1/4
def OP7(imagen, columnas, filas):
    filCuarto = int(filas/4)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(i == filCuarto):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos

#Contador de unos con respecto a la fila 3/4
def OP8(imagen, columnas, filas):
    filTresCuartos = int((filas/4)*3)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(i == filTresCuartos):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos

#Contador de cortes con respecto a las columna intermedia
def OP9(imagen, columnas, filas):
    colInter = int(columnas/2)
    contCortes = 0
    corte = 0
    for j in range(columnas):
        dato = (int(imagen[j][colInter]))
        if dato!=corte:
            contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes

#Contador de cortes con respecto a la columna 1/4
def OP10(imagen, columnas, filas):
    colCuarto = int(columnas/4)
    contCortes = 0
    corte = 0
    for j in range(columnas):
        dato = (int(imagen[j][colCuarto]))
        if dato!=corte:
            contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes

#Contador de cortes con respecto a la columna 3/4
def OP11(imagen, columnas, filas):
    colTresCuartos = int((columnas/4)*3)
    contCortes = 0
    corte = 0
    for j in range(columnas):
        dato = (int(imagen[j][colTresCuartos]))
        if dato!=corte:
            contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes

#Contador de cortes con respecto a la fila intermedia
def OP12(imagen, columnas, filas):
    filInter = int(filas/2)
    contCortes = 0
    corte = 0
    for i in range(filas):
        for j in range(columnas):
            if i==filInter:
                dato = (int(imagen[filInter][j]))
                if dato!=corte:
                    contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes

#Contador de cortes con respecto a la fila 1/4
def OP13(imagen, columnas, filas):
    filCuarto = int(filas/4)
    contCortes = 0
    corte = 0
    for i in range(filas):
        for j in range(columnas):
            if i==filCuarto:
                dato = (int(imagen[filCuarto][j]))
                if dato!=corte:
                    contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes

#Contador de cortes con respecto a la fila 3/4
def OP14(imagen, columnas, filas):
    filTresCuartos = int((filas/4)*3)
    contCortes = 0
    corte = 0
    for i in range(filas):
        for j in range(columnas):
            if i==filTresCuartos:
                dato = (int(imagen[filTresCuartos][j]))
                if dato!=corte:
                    contCortes = contCortes+1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes
    
#Llenado de matris con los datos de las propiedades
###############################################################################
    #Manin del Programa
###############################################################################
print("####Genera dataSet####")

carpeta = str(input("Ingrese Nombre de la Carpeta: "))

for directorio, subDirectorio, listArchivos in os.walk(carpeta):
    for file in listArchivos:
        png = directorio+"/"+file            
        imagen1 = mpimg.imread(png)
        imagen2 = Image.open(png)
        (columnas, filas) = imagen2.size
        matrizDataSet[a][b] = OP1(imagen1, columnas, filas)
        b = b+1
        matrizDataSet[a][b]= OP2(imagen1, columnas, filas)
        b +=1            
        matrizDataSet[a][b] = OP3(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP4(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP5(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP6(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP7(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP8(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP9(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP10(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP11(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP12(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP13(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP14(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = conClase-1
        a +=1
        b = 0
    conClase = conClase+1
datosMatriz = matrizDataSet
csvSalida = open('DataSet.csv','w',newline='')
Salida = csv.writer(csvSalida)
Salida.writerow(["Propiedad1","Propiedad2","Propiedad3","Propiedad4",
                 "Propiedad5","Propiedad6","Propiedad7","Propiedad8",
                 "Propiedad9","Propiedad10","Propiedad11","Propiedad12",
                 "Propiedad13","Propiedad14","Clase"])
Salida.writerows(datosMatriz)
del Salida
csvSalida.close()
print("DataSet Generado: XD")