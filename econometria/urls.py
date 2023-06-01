from django.contrib import admin
from django.urls import path, include
from econometria import views

from .views import AppRegressionLineal

urlpatterns = [
    path('', views.home, name="econometria-home"),
    path('problemas-aplicacion', views.problemas_aplicacion, name="problemas-aplicacion"),
    path('regresion-lineal', views.regresion_lineal, name="regresion-lineal"),
    path('aclaracion-regresion-lineal', views.aclaracion_regresion_lineal, name="aclaracion-regresion-lineal"),
    path('parametro-estadistico', views.parametro_estadistico, name="parametro-estadistico"),
    path('anova', views.anova, name="anova"),
    path('varianza', views.varianza, name="varianza"),
    path('intervalos-confianza', views.intervalos_confianza, name="intervalos-confianza"),
    path('calidad', views.calidad, name="calidad"),
    path('supuestos', views.supuestos, name="regresion-supuestos"),
    path('regresion-lineal-multiple', views.regresion_multiple, name="regresion-multiple"),
    path('matrices', views.matrices, name="matrices"),
    path('supuesto-adicional', views.supuesto_adicional, name="supuesto-adicional"),
    path('anova-mrlm', views.anova_mrlm, name="anova-mrlm"),
    path('r-cuadrado-ajustado', views.r_cuadrado_ajustado, name="r-cuadrado-ajustado"),

    #Software
    path('instrucciones', views.instrucciones, name="instrucciones"),
    path('regresion-r', views.regresion_r, name="regresion-r"),
    path('regresion-python', views.regresion_python, name="regresion-python"),

    #app
    #path('applicacion', views.app_regresion_lineal, name="app"),
    path('applicacion', AppRegressionLineal.as_view(), name="app"),
    path('search_col/', views.search_columns, name="search_col"),

    #extra
    path('libros-y-recursos', views.libros, name="libros"),
]
