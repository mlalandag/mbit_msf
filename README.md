# Médicos sin Fronteras 


## Predicción de aumento de cuotas de socios

El presente repositorio contiene los notebooks, reports, modelos y código de aplicación elaborados durante el proyecto de predicción de aumento de cuotas de socios de MSF.

## Notebooks
En el repositorio hay distintos notebooks, aunque muchos de ellos corresponden a experimentos realizados en las distintas fases del proyecto. Los notebooks correspondientes al modelo que mejores resultados dió son los siguientes:

**MSF_Definitivo_Preprocessing_Spark** : Que contiene el preprocesamiento de la información contenida en las tablas originales de MSF almacenadas en S3.

**MSF_Definitivo_MLOps** : Contiene los últimos ajustes del conjunto de datos resultante del preprocesamiento, la preparación del conjunto de entrenamiento, el propio entrenamiento y el registro del modelo en MLFLow. Concluye con la obtención del Feature Store y un fichero únicamente con las predicciones por ID

## Streamlit
La carpeta **streamlit** contiene el prototipo de la aplicación implementada con dicho framework así como sus dependencias.

## Sweetviz
En la carpeta **sweetviz_reports** tenemos los profilings realizados sobre las tablas originales de MSF con la herramienta Sweetviz

## Quality Rules
En la carpeta **quality_rules** tan sólo hay unos ficheros de texto conteniendo unos conjuntos de reglas de calidad generados con la herramienta de calidad de AWS GLue.

## Descripción de Tablas
Contiene el Excel proporcionado por MSF en el que se describe cada atributo dentro de las tablas de MSF