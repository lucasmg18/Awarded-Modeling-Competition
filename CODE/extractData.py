import os
import glob
import cv2
import numpy as np


# Extraer vectores de píxeles a color de cada imágen de cada clase
totalX = []
totalY = []
for folder_path in glob.glob("./Datos/train/train/*"):
    # Obtener etiqueta del nombre de la carpeta
    classLabel = folder_path.split("/")[-1].split("\\")[-1]
    print(folder_path.split("/")[-1].split("\\")[-1])
    # Para cada imagen de la carpeta obtener la ruta y añadir ".jpg"
    for path in glob.glob(os.path.join(folder_path, "*.jpg")):
        # Leer cada imagen como un vector de píxeles a color
        # El campo cv2.IMREAD_COLOR sirve para indicar que se trata de imagenes a color
        # (la salida de cv2.imread() tiene formato BGR y no RGB)
        img = cv2.imread(path, cv2.IMREAD_COLOR)  
        # transformar píxeles de BGR a RGB    
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        # Guardar valores de cada imagen (Datos Input)
        totalX.append(img)
        # Guardar las etiquetas (Objetivo)
        totalY.append(classLabel)

# Transformar listas en numpy arrays
totalX = np.array(totalX)
totalY = np.array(totalY)



#Separar datos en test y train

np.random.seed(0)
trainPortion = 0.6 #porcentaje de train, el porcentaje de test será la resta de 1 menos el porcentaje de train
#-------------Obtener índices
indexesData = np.arange(len(totalY)) #Indices del conjunto de muestras
#-------------Desordenar indices y separar en rain y test
np.random.shuffle(indexesData) #Desordenar indices de las muestras
numberTrain = round(len(indexesData)*trainPortion) #numero de muestras para train
trainIndexes = indexesData[:numberTrain]
testIndexes = indexesData[numberTrain:]
#-------------Datos desorden:ados para train y test
trainX = totalX[trainIndexes]
testX = totalX[testIndexes]
trainY = totalY[trainIndexes]
testY = totalY[testIndexes]

path = "./Datos/total_data.npz"
# Guardar los arrays en un archivo .npz 
np.savez(path, trainX=trainX, testX=testX,trainY=trainY,testY=testY)





