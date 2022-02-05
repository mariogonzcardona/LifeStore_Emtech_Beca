from lifestore_file import lifestore_products, lifestore_searches, lifestore_sales
import pprint
import pandas as pd
 
# 1.1.- Generar un listado de los 5 productos con mayores ventas y un listado con los 10 productos con mayor búsquedas.
# 1.2.- Por categoría, generar un listado con los 5 productos con menores ventas y uno con los 10 productos con menores búsquedas.
# 2.0.- Mostrar dos listados de 5 productos cada una, un listado para productos con las mejores reseñas y otro para las peores, considerando los productos con devolución.
# Nota: No considerar productos sin reseñas.
# 3.1.- Total de ingresos y ventas promedio mensuales.
# 3.2.- 3.2.- Total anual y meses con más ventas al año.
# Nota: Numero de ventas, total de ingresos.

# Generacion de dataframes con respecto a las tres listas de lifestore_file
def generate_dfs():
    df_searches=pd.DataFrame(lifestore_searches, columns=['id_search', 'id_product'])
    df_sales=pd.DataFrame(lifestore_sales, columns=['id_sale', 'id_product','score','date','refund'])
    df_products=pd.DataFrame(lifestore_products, columns=['id_product', 'name', 'price', 'category', 'stock'])
    return df_searches, df_sales, df_products

# Funcion para reducir y contar la frecuencia de un df de acuerdo a la columna de id_product
def reduce_df(df, col_name,count,ascending=False):
    df_res=df['id_product'].value_counts(ascending = ascending)[0:count]
    return pd.DataFrame({'id_product':df_res.index, col_name:df_res.values})

# Mezcla de dataframes de reduce_df y df_products
def filter_products_searches_higher(df,df_products,col_name,count):
    df_result=reduce_df(df,col_name, count)
    list_result = pd.merge(df_result, df_products, on="id_product")
    print(list_result)

# Mostrar reporte de productos con mayores ventas y busquedas
def show_report_higher(df_searches,df_sales,df_products):
    print("-"*110)
    print("Listado de los 5 productos con mayores ventas")
    filter_products_searches_higher(df_sales,df_products,'sales',5)
    print("-"*110)
    print("Listado de los 10 productos con mayores busquedas")
    filter_products_searches_higher(df_searches,df_products,'searches',10)

# Generar un diccionario con las categorias y sus respectivos df
def generate_dict_categories(df_products):
    categories=df_products['category'].unique()
    dict_categories={}
    for category in categories:
        dict_categories[category]=df_products.loc[df_products['category'] == category]
    return dict_categories

# Mostrar reporte de productos con menores ventas y busquedas por categorias en total son 8
def show_report_lowler(df_low, df_products, col_name, count, message):
    dict_dfs=generate_dict_categories(df_products)
    print("-"*110)
    print(message)
    for category in dict_dfs:
        print("La categoria es: ", category)
        df=dict_dfs[category]
        df_categories_res = pd.merge(df, df_low, on="id_product")
        print(df_categories_res.sort_values(by=[col_name],ascending=True)[0:count])
        print("*"*110)

# Generar dataframe de productos con el promedio de reseñas
def score_avg_min_max(df_sales,df_products,count):
    data=[]
    for i in range(1,len(df_products)+1):
        data.append([i, df_sales.loc[df_sales['id_product'] == i]['score'].mean()])
    df_score=pd.DataFrame(data,columns=['id_product','score_svg'])
    df_score = df_score[df_score['score_svg'].notna()]
    
    df_score_max=df_score.sort_values('score_svg',ascending=False)[0:count]
    df_score_min=df_score.sort_values('score_svg',ascending=True )[0:count]
    
    return df_score_max, df_score_min



# Funcion para ejecutar el punto 1.1 del proyecto del curso
def process_report_1_1():
    dfs=generate_dfs() # df_searches, df_sales, df_products
    show_report_higher(dfs[0],dfs[1],dfs[2])
    
# Funcion para ejecutar el punto 1.2 del proyecto del curso
def process_report_1_2():
    dfs=generate_dfs() # df_searches, df_sales, df_products
    ms_sales="Reporte de productos con menores ventas por categorias"
    ms_searches="Reporte de productos con menores busquedas por categorias"
    
    df_low_sales=reduce_df(dfs[1],'sales',300,True)
    df_low_searches=reduce_df(dfs[0],'searches',300,True)
    show_report_lowler(df_low_sales, dfs[2], 'sales',5,ms_sales)
    show_report_lowler(df_low_searches, dfs[2],'searches',10,ms_searches)

# Funcion para ejecutar el punto 2 del proyecto del curso
def process_report_2():
    dfs=generate_dfs() # df_searches, df_sales, df_products
    df_min_max=score_avg_min_max(dfs[1],dfs[2],5)
    
    print("-"*110)
    print("Listado de los 5 productos con mayores reseñas")
    print(df_min_max[0])
    print("-"*110)
    print("Listado de los 5 productos con peores reseñas")
    print(df_min_max[1])
    
# Funcion para ejecutar el punto 3 del proyecto del curso
def process_report_3():
    pass

def main():
    # process_report_1_1()
    # process_report_1_2()
    process_report_2()
    process_report_3()

if __name__ == "__main__":
    main()
