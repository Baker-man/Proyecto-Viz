# Proyecto Viz

**ÍNDICE**

[1. Objetivos](#0)<br />
[2. Pasos seguidos](#steps)<br />
[3. Visualización](#viz)<br />

------------------------------------------

🎯 **OBJETIVOS**<a name="0"/> 

1) Crear un repo nuevo con files src, img, data, Readme.md y gitignore.

2) Issue con el link pegado de nuestro Repo

3) Generar visualización de los datos obtenidos mediante una ETL con Python, Tableau, Power BI...

------------------------------------------

📋 **PASOS SEGUIDOS**<a name="steps"/> 

Se han generado dos cuadros de mando con Power BI que disponen de selectores/filtros y gráficos similares, y cuya diferencia reside en el mapa central de cada uno.
Para el primero se ha elegido un mapa de calor para visualizar más eficazmente la concentración de accidentes y para el segundo se ha elegido un mapa de puntos por cada accidente con la posibilidad de consultar en el pop-up información adicional de cada uno.

Los widgets comunes presentes en ambos cuadros de mando son:

  - Filtro por distrito de Madrid
  - Filtro de fecha
  - Filtro de rango de edad de los afectados
  - Filtro de estado meteorológico
  - Contador del número de accidentes
  - Gráfico de barras de tipos de accidentes y de tipo de vehículo afectado
  - Gráfico circular de afectados por sexo

Se ha considerado que estos campos eran los más importantes porque ayudaban a tener una visión espacio-temporal de la problemática y aportaban información sobre los potenciales condicionantes y características de los accidentes de tráfico. El objetivo es que sirva como visor tanto como para el público general como para las autoridades locales competentes

Para el mapa de puntos de accidentes se han incluido los siguientes elementos/campos en el pop-up:

  - Distrito
  - Estado meteorológico
  - Fecha
  - Hora
  - Personas involucradas
  - Lesividad
  - Positivo en alcohol


Por otro lado, se ha elaborado un mapa de calor dinámico por meses para el periodo 2019-2022, de esta forma se pueden ver las diferencias en la concentración de accidentes a lo largo del año.

---------------------------------------

💹 **VISUALIZACIÓN**<a name="viz"/> 

1) Dashboard concentración de accidentes de tráfico en Madrid:

![Dashboard1](https://user-images.githubusercontent.com/112175733/203138345-64af7a6b-dbca-4af6-9662-f988f3683a82.png)

2) Dashboard de accidentes de tráfico en Madrid:

![Dashboard2](https://user-images.githubusercontent.com/112175733/203138367-136020f9-b7b3-4941-9d46-6052d52d89a4.png)

3) Mapa de calor dinámico por meses:

https://user-images.githubusercontent.com/112175733/202927977-8a08705f-cc0e-45a1-a5cc-40ce513b6c10.mp4


