# Beca Santander EmTech
![santander](https://emtech.digital/santanderskills/landing/img/santander_1.png)

![EmTech](https://emtech.digital/santanderskills/landing/img/logo_emtech.png)
## _Proyecto LifeStore_

Este proyecto está desarrollado en Python 3.9

LifeStore es una tienda virtual que maneja una amplia gama de artículos, recientemente, la Gerencia de ventas, se percató que la empresa tiene una importante acumulación de inventario. Asimismo, se ha identificado una reducción en las búsquedas de un grupo importante de productos, lo que ha redundado en una disminución sustancial de sus ventas del último trimestre.

## Consigna

- Productos más vendidos y productos rezagados a partir del análisis de las categorías con menores ventas y categorías con menores búsquedas.
- Productos por reseña en el servicio a partir del análisis de categorías con mayores ventas y categorías con mayores búsquedas.
- Sugerir una estrategia de productos a retirar del mercado, así como sugerencia de cómo reducir la acumulación de inventario considerando los datos de ingresos y ventas mensuales.

## Tecnología

En este proyecto se enlistan las siguientes librerías para poder desarrollar los puntos solicitados.
| Plugin | Versión |
| ------ | ------ |
| asgiref | 3.5.0 |
| Django | 4.0.1 |
| numpy | 1.22.1 |
| pandas | 1.4.0 |
| python-dateutil | 2.8.2 |
| pytz | 2021.3 |
| six | 1.16.0 |
| sqlparse | 0.4.2 |
| tabulate | 0.8.9 |
| tzdata | 2021.5 |


## Instalación

Para poder ejecutar el programa es neceario crear un ambiente virtual e instalar las dependencias en el archivo requirements.txt, ejecute main.py.

```sh
virtualenv env
source env/Scripts/activate
pip install -r requirements.txt
python main.py
```

## Ejecucion
Este programa cuenta con un login y un register a traves de un menu interactivo por consola

#### _Primera sección Login, Register y Exit:_
```sh
--------------------------------------------------
1. Login
2. Register
3. Exit
--------------------------------------------------
Select an option: 1
Enter your email: mario@hotmail.com
Enter your password: Test01.
Login successful
```

#### _Para la sección del Menu:_
```sh
--------------------------------------------------
1. Show report 1
2. Show report 2
3. Show report 3
4. Exit
--------------------------------------------------
Select an option: 1
```

#### _Para la sección del Punto 1:_
```sh
--------------------------------------------------
1. Show products with the highest sales and searches
2. Show products with lower sales and searches by category
3. Exit
--------------------------------------------------
```

#### _Para la sección del Punto 2:_
```sh
--------------------------------------------------
1. Show Top Reviewed Products
2. Show Worst Reviewed Products
3. Exit
--------------------------------------------------
```

#### _Para la sección del Punto 3:_
```sh
--------------------------------------------------
1. Show Total Revenues
2. Show Total Annual Sales
3. Months With Higher Sales
4. Exit
--------------------------------------------------
```

## Licencia

Apache License

**Free Software, Hell Yeah!**
