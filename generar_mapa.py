import geopandas as gpd
import matplotlib.pyplot as plt

print("Cargando base de datos geoespacial interna...")

# 1. Descargar/Cargar el mapa mundial con dimensiones políticas reales
url_geojson = "https://raw.githubusercontent.com/datasets/geo-boundaries-world-110m/master/countries.geojson"
mundo = gpd.read_file(url_geojson)

# 2. Configurar la paleta de colores mate (Códigos HEX)
color_oceanos = "#ECEFF1"
color_resto_mundo = "#CFD8DC"
color_venezuela = "#D97736" # Terracota Mate
color_argentina = "#537895"  # Azul Acero Mate
color_lineas_fronteras = "#FFFFFF" # Fronteras blancas para limpieza visual

# 3. Inicializar el lienzo de dibujo (Alta definición)
fig, ax = plt.subplots(figsize=(16, 9), facecolor=color_oceanos)
ax.set_facecolor(color_oceanos)

# 4. Dibujar todos los países con el color base mate
mundo.plot(ax=ax, color=color_resto_mundo, edgecolor=color_lineas_fronteras, linewidth=0.5)

# 5. Filtrar y pintar los países del proyecto CyberPuppets
# Buscamos por el nombre oficial en el GeoJSON
venezuela = mundo[mundo['name'] == 'Venezuela']
argentina = mundo[mundo['name'] == 'Argentina']

# Superponer los países destacados con su color correspondiente
venezuela.plot(ax=ax, color=color_venezuela, edgecolor=color_lineas_fronteras, linewidth=0.8)
argentina.plot(ax=ax, color=color_argentina, edgecolor=color_lineas_fronteras, linewidth=0.8)

# 6. Limpieza estética (Quitar los ejes de coordenadas latitud/longitud)
ax.set_axis_off()

# Ajustar los márgenes de forma estricta
plt.tight_layout()

# 7. Guardar el archivo DIRECTAMENTE en la ruta estática de tu app de Django
# Usamos una 'r' al principio de la ruta para que Windows no se confunda con las barras invertidas (\)
ruta_destino = r"D:\proyecto\WRO1\danceapp\static\danceapp\images\map-mundi.svg"

# Cambiamos la extensión a .svg y Matplotlib se encargará del resto de forma vectorial
plt.savefig(ruta_destino, format='svg', bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')

print(f"¡Éxito absoluto! El mapa vectorial ha sido integrado en: {ruta_destino}")