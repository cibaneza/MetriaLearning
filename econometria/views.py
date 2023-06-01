from pickle import TRUE
from django.shortcuts import render
import pandas as pd
import numpy as np
import statsmodels.api as sm
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

#Starting
def home(request):
    return render(request, "inicio.html")

def problemas_aplicacion(request):
    return render(request, "problemas_aplicacion.html")

def regresion_lineal(request):
    return render(request, "regresion_lineal.html")

def aclaracion_regresion_lineal(request):
    return render(request, "aclaracion_regresion_lineal.html")

def parametro_estadistico(request):
    return render(request, "parametro_estadistico.html")

def anova(request):
    return render(request, "anova.html")

def varianza(request):
    return render(request, "varianza.html")

def intervalos_confianza(request):
    return render(request, "intervalos_confianza.html")

def calidad(request):
    return render(request, "calidad.html")

def supuestos(request):
    return render(request, "supuestos.html")

def regresion_multiple(request):
    return render(request, "regresion_lineal_multiple.html")

def matrices(request):
    return render(request, "matrices.html")

def supuesto_adicional(request):
    return render(request, "supuesto_adicional.html")

def anova_mrlm(request):
    return render(request, "anova_mrlm.html") 

def r_cuadrado_ajustado(request):
    return render(request, "r_cuadrado_ajustado.html")

#Software
def instrucciones(request):
    return render(request, "instrucciones.html")

def regresion_r(request):
    return render(request, "regresion_r.html")

def regresion_python(request):
    return render(request, "regresion_python.html")

#app
#@csrf_exempt
#LoginRequiredMixin, View
class AppRegressionLineal(View):
    def get(self, request):
        return render(request, 'app.html')
#def app_regresion_lineal(request):
#    return render(request, "app.html")


@csrf_exempt
def search_columns(request):
    #option_y = request.POST.getlist('output_y')
    #option_x = request.POST.getlist('output_x')
    #s = ''.join(option_y)
    #z = ''.join(option_x)
    #print(s)
    #print(z)

    if bool(request.FILES.get('document', False)) == True:
        uploaded_file = request.FILES['document']
        file_size = uploaded_file.size
        print(file_size)
        global data
        global df
        if uploaded_file:
            if file_size < 3145728:
                filename = uploaded_file.name
                print(filename)
                if filename.endswith('.csv'):
                    print('File is a csv')
                    df = pd.read_csv(uploaded_file).dropna() 
                    print(df.head())
                    columns = df.columns

                    header = df.axes[1].values.tolist()
                    attributes = len(header)
                    rows = len(df.index)
                    types = []
                    maxs = []
                    mins = []
                    means = []
                    # statistic attribut
                    for i in range(len(header)):
                        types.append(df[header[i]].dtypes)
                        if df[header[i]].dtypes != 'object':
                            maxs.append(df[header[i]].max())
                            mins.append(df[header[i]].min())
                            means.append(round(df[header[i]].mean(),2))
                        else:
                            maxs.append(0)
                            mins.append(0)
                            means.append(0)

                    zipped_data = zip(header, types, maxs, mins, means)

                elif filename.endswith('.txt'):
                    print('File is a txt')
                    df = pd.read_table(uploaded_file, delimiter=',').dropna() 
                    print(df.head())
                    columns = df.columns

                    header = df.axes[1].values.tolist()
                    attributes = len(header)
                    rows = len(df.index)
                    types = []
                    maxs = []
                    mins = []
                    means = []
                    # statistic attribut
                    for i in range(len(header)):
                        types.append(df[header[i]].dtypes)
                        if df[header[i]].dtypes != 'object':
                            maxs.append(df[header[i]].max())
                            mins.append(df[header[i]].min())
                            means.append(round(df[header[i]].mean(),2))
                        else:
                            maxs.append(0)
                            mins.append(0)
                            means.append(0)

                    zipped_data = zip(header, types, maxs, mins, means)

                elif filename.endswith('.xls'):
                    print('File is a xls')
                    df = pd.read_excel(uploaded_file).dropna() 
                    print(df.head())
                    columns = df.columns

                    header = df.axes[1].values.tolist()
                    attributes = len(header)
                    rows = len(df.index)
                    types = []
                    maxs = []
                    mins = []
                    means = []
                    # statistic attribut
                    for i in range(len(header)):
                        types.append(df[header[i]].dtypes)
                        if df[header[i]].dtypes != 'object':
                            maxs.append(df[header[i]].max())
                            mins.append(df[header[i]].min())
                            means.append(round(df[header[i]].mean(),2))
                        else:
                            maxs.append(0)
                            mins.append(0)
                            means.append(0)

                    zipped_data = zip(header, types, maxs, mins, means)

                elif filename.endswith('.xlsx'):
                    print('File is a xlsx')
                    df = pd.read_excel(uploaded_file, engine='openpyxl').dropna() 
                    print(df.head())
                    columns = df.columns

                    header = df.axes[1].values.tolist()
                    attributes = len(header)
                    rows = len(df.index)
                    types = []
                    maxs = []
                    mins = []
                    means = []
                    # statistic attribut
                    for i in range(len(header)):
                        types.append(df[header[i]].dtypes)
                        if df[header[i]].dtypes != 'object':
                            maxs.append(df[header[i]].max())
                            mins.append(df[header[i]].min())
                            means.append(round(df[header[i]].mean(),2))
                        else:
                            maxs.append(0)
                            mins.append(0)
                            means.append(0)

                    zipped_data = zip(header, types, maxs, mins, means)

                else:
                    print('File has not .csv, .txt extension')
                    uploaded_file.clean()
                    data = {}
            else:
                raise ValidationError("No puedes subir archivos mayores a 3Mb")
        
        data = {
                "df": df,
                "cols": columns,
                "name": filename,
                "header": header,
                "attributes": attributes,
                "rows": rows,
                "zipped_data": zipped_data,
        }

    if bool(request.POST.getlist('output_y', False)) & bool(request.POST.getlist('output_x', False)) == True:
        
        option_y = request.POST.getlist('output_y')
        option_x = request.POST.getlist('output_x')
        print(option_y, option_x)
        #print(df.head())
        #print(df.loc[:, option_y])
        #print(df.loc[:, option_x])

        y = df.loc[:, option_y]
        x = df.loc[:, option_x]

        x = sm.add_constant(x)
        lm = sm.OLS(y,x).fit()
        #print(lm.summary2())
        lm_result = lm.summary2()
        #print(lm_result.tables[1])
  
        data['lm'] = lm_result
        data['tables'] = lm.summary().as_html()
        #print(data['tables']) 
    

    return render(request, "search_columns.html", context=data) 

#Extra
def libros(request):
    return render(request, "libros.html")