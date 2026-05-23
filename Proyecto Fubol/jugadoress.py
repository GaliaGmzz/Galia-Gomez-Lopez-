import numpy as np

# LEER CSV
datosJugadores = np.genfromtxt(
    r"c:\Users\gomez\OneDrive\Documentos\Programación\Programacion 2\Proyecto futbol (Pandas)\Futbol\jugadores_futbol.csv",  
    delimiter=",",
    dtype=None,
    encoding="utf-8",
    names=True         
)

jugadoresOrdenados = np.sort(
    datosJugadores, order = "Goles")

top5 = jugadoresOrdenados[-5:]

top5 = top5[::-1]

print(f"Top 5 goleadores: {top5}")

#Promedio de edad

promedioEdad=np.mean(datosJugadores["Edad"])
print(f"Promedio de edad {promedioEdad}")

#10 mas caros

topCaros=np.sort(datosJugadores, order="ValorMercado")

top10 = topCaros[-10:]
top10[::-1]
print(f"Top 10 caros: {top10}")

np.savetxt(
    r"c:\Users\gomez\OneDrive\Documentos\Programación\Programacion 2\Proyecto futbol (Pandas)\Futbol\jugadores_futbol.csv",
    top10,
    delimiter=",",
    fmt="%s",               
    header="ID, JUGADOR, EQUIPO, POSICION, EDAD, PARTIDOS, GOLES, ASISTENCIA, VALORMERCADO"   
)
#total de goles
totalGol=np.sum(datosJugadores ["Goles"])
print(f"total: {totalGol}")
#promedio de goles
promedioGol=np.mean(datosJugadores ["Goles"])
print(f"Promedio: {promedioGol}")
#maxima 
maxima=np.max(datosJugadores["Goles"])
print(f"Maximo: {maxima}")
