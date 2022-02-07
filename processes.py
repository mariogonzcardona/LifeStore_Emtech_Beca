from lifestore_file import lifestore_products, lifestore_searches, lifestore_sales
import calendar
import pandas as pd
 
# 1.1.- Generar un listado de los 5 productos con mayores ventas y un listado con los 10 productos con mayor búsquedas.
# 1.2.- Por categoría, generar un listado con los 5 productos con menores ventas y uno con los 10 productos con menores búsquedas.
# 2.0.- Mostrar dos listados de 5 productos cada una, un listado para productos con las mejores reseñas y otro para las peores, considerando los productos con devolución.
# Nota: No considerar productos sin reseñas.
# 3.1.- Total de ingresos y ventas promedio mensuales.
# 3.2.- Total anual y meses con más ventas al año.
# Nota: Numero de ventas, total de ingresos.

# Funcion para ejecutar el punto 1 del proyecto del curso    
def process_report_1(option):
    dfs=generate_dfs() # df_searches, df_sales, df_products
    if option == 1:
        # Mostrar reporte de productos con mayores ventas y busquedas
        print("-"*50)
        print("List of the 5 products with the highest sales")
        df_sales=filter_products_searches(dfs[1],dfs[2],'sales',5)
        print(df_sales.to_markdown())
        
        print("-"*50)
        print("List of the 10 most searched products")
        df_searches=filter_products_searches(dfs[0],dfs[2],'searches',10)
        print(df_searches.to_markdown())
    elif option == 2:
        # Mostrar reporte de productos con menores ventas y busquedas por categoria
        print("-"*50)
        show_menu_categories(dfs[0],dfs[1],dfs[2]) #category_list,dict_categories

# Funcion para ejecutar el punto 2 del proyecto del curso
def process_report_2(option):
    dfs=generate_dfs() # df_searches, df_sales, df_products
    df_min_max=score_avg_min_max(dfs[1],dfs[2],5)
    if option == 1:
        print("List of the 5 products with the most reviews")
        print(df_min_max[0].round(decimals = 2).to_markdown())
    elif option == 2:
        print("List of the 5 products with the worst reviews")
        print(df_min_max[1].round(decimals = 2).to_markdown())
    
# Funcion para ejecutar el punto 3 del proyecto del curso
def process_report_3(option):
    dfs=generate_dfs() # df_searches, df_sales, df_products
    df_month=show_report_total_monthly_income(dfs[1],dfs[2])
    if option == 1:
        print("Listing of total income, average sales, total sales per month")
        print(df_month.to_markdown())
    elif option == 2:
        # Para obtener el total de ventas anual para 2020
        total_anual='${:,.2f}'.format(df_month['total_revenue'].sum())
        print(f'Total annual sales for the year 2020 is: {total_anual}')
    elif option == 3:
        # Meses con mayores ventas en el año
        print("Months with the highest sales in 2020")
        print(df_month[['month','total_sales']].sort_values(by=['total_sales'],ascending=False)[:5].to_markdown())

# Muestra un menu con las categorias y sus respectivos df
def show_menu_categories(df_searches,df_sales,df_products):
    category_list, dict_categories= generate_dict_categories(df_products)
    while True:
        print("-"*50)
        print("Select a category to see the products with the lowest sales and searches.")
        for cat in category_list:
            index=category_list.index(cat)
            print(f'{index+1}. {cat}')
        exit_option=len(category_list)+1
        print(f'{exit_option}. Exit')
        try:
            option = int(input("Select an option: "))
            if option != exit_option:
                print("-"*50)
                opt_selected=category_list[option-1]
                df_low_sales=reduce_df(df_sales,'sales',300,True)
                df_low_searches=reduce_df(df_searches,'searches',300,True)
                print(f'List of the 5 products with the lowest sales in {opt_selected}')
                show_report_lowler(dict_categories[opt_selected],df_low_sales,'sales',5)
                print(f'List of the 10 products with the lowest searches in {opt_selected}')
                show_report_lowler(dict_categories[opt_selected],df_low_searches,'searches',10)
            elif option == exit_option:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")
        
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
def filter_products_searches(df,df_products,col_name,count):
    df_result=reduce_df(df,col_name, count)
    df_res=pd.merge(df_result, df_products, on="id_product")
    return df_res[['id_product',col_name,'price','category','stock']]

# Generar un diccionario con las categorias y sus respectivos df
def generate_dict_categories(df_products):
    categories=df_products['category'].unique()
    dict_categories={}
    for category in categories:
        dict_categories[category]=df_products.loc[df_products['category'] == category]
    return categories.tolist(),dict_categories

# Mostrar reporte de productos con menores ventas y busquedas por categorias en total son 8
def show_report_lowler(df_category,df_reduce, col_name, count):
    print("-"*50)
    df_categories_res = pd.merge(df_category, df_reduce, on="id_product")
    if df_categories_res.empty:
        print(f'There are no products in the category')
    else:
        df_cat_res=df_categories_res.sort_values(by=[col_name],ascending=True)[0:count]
        print(df_cat_res[['id_product',col_name,'price','category','stock']].to_markdown())

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

# Generar dataframe para ventas totales, promedio, mensuales y anuales.
def show_report_total_monthly_income(df_sales,df_products):
    # Dentro del dataframe de df_sales aseguramos que la columna de date sea de tipo datetime
    df_sales['date'] = pd.to_datetime(df_sales['date'],format='%d/%m/%Y') 
    # Quitamos los productos que fueron devueltos es decir refund == 1
    monthly_sales = df_sales.drop(df_sales[df_sales.refund == 1].index)
    dict_sales_monthly={}
    months_list=[]
    total_revenue=[]
    total_sales=[]
    avg_list=[]
    for x in range(1,13):
        by_monthly_sales= monthly_sales[monthly_sales['date'].dt.month == x]
        df_res=reduce_df(by_monthly_sales,'sale_count',300,ascending = True)
        df_res=df_res.sort_values(by=['id_product'],ascending=True)
        
        id_products_list=list(df_res.id_product)
        # Total de ventas por mes
        counter_sales=sum(list(df_res.sale_count))
        
        list_sales_monthly=[]

        for m in id_products_list:
            price_value = df_products.loc[df_products.id_product==m, 'price'].values[0]
            sale_count = df_res.loc[df_res.id_product==m, 'sale_count'].values[0]
            list_sales_monthly.append(price_value*sale_count)
        months_list.append(calendar.month_name[x])
        total_revenue.append(sum(list_sales_monthly))
        avg_list.append(0 if counter_sales==0 else sum(list_sales_monthly)/counter_sales)
        total_sales.append(counter_sales)
    dict_sales_monthly={
        "month":months_list,
        "total_revenue":total_revenue,
        "avg_sales":avg_list,
        "total_sales":total_sales
    }
    df_month=pd.DataFrame.from_dict(dict_sales_monthly)
    df_month['avg_sales']=df_month['avg_sales'].round(decimals = 2)
    return df_month


