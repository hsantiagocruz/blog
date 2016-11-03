import os
import shutil

print "****Generador de blogs***"

agregados="<!--ref-->"
from os import listdir
for post in listdir("_post"):
    htmlEntrada='post/'+ post+'.html'
    titulo=""
    archivo=open("_post/"+post,"r")
    i=0
    contenido=""
    for linea in archivo.readlines():
        if i==0:
            contenido+="<h1>"+linea+"</h1>"
            titulo=linea
            i+=1
            continue
        contenido+=linea+"<br>"
    agregados+="<li><a href="+htmlEntrada+">"+titulo+"</a></li>>"
    plantilla=open("_temp.html","r")
    contenidoP=plantilla.read()
    plantilla.close()
    contenidoP=contenidoP.replace('<!--contenido><-->',contenido)
    entrada=open(htmlEntrada,'w')
    entrada.write(contenidoP)
    entrada.close()
    archivo.close()
    print agregados
index=open('index.html','r')
lee=index.read()
lee.replace('<!---->',"agregados")
index.close()
index2=open('index3.html','w')
index2.write(lee)
print lee
index2.close
