import geopandas as gpd
import matplotlib.pyplot as plt
import os

print("\n=== GENERADOR CARTOGRÁFICO REAL DE VENEZUELA (CYBERPUPPETS) ===")
print("Extrayendo fronteras geográficas oficiales de la base de datos mundial...")

# 1. Intentar cargar el mapa mundial integrado o usar el fallback oficial
try:
    path = gpd.datasets.get_path('naturalearth_lowres')
    world = gpd.read_file(path)
except Exception:
    # Soporte resiliente por si la versión local de datasets está deprecada
    url = "https://raw.githubusercontent.com/datasets/geo-boundaries-world-110m/master/countries.geojson"
    world = gpd.read_file(url)

# 2. Estandarizar columnas a minúsculas para prevenir KeyErrors (ej. 'ISO_A3' vs 'iso_a3')
world.columns = [col.lower() for col in world.columns]

# Detectar dinámicamente cómo se llaman las columnas de nombres y códigos en esta base de datos
col_nombre = 'name' if 'name' in world.columns else (
    'name_long' if 'name_long' in world.columns else None
)
col_iso = 'iso_a3' if 'iso_a3' in world.columns else (
    'iso3' if 'iso3' in world.columns else None
)

# 3. Filtrar a Venezuela de forma segura e independiente de las columnas existentes
if col_nombre:
    condicion = world[col_nombre].str.lower() == 'venezuela'
else:
    # Fallback si no hay columnas reconocibles de nombre (usar la primera columna por defecto)
    condicion = world.iloc[:, 0].str.lower() == 'venezuela'

if col_iso:
    condicion |= (world[col_iso].str.upper() == 'VEN')

# Extraer el objeto geométrico oficial de Venezuela
venezuela = world[condicion]

if venezuela.empty:
    print("Error crítico: No se pudo localizar la geometría oficial de Venezuela en el dataset.")
    exit()

# 4. Configurar paleta de colores corporativa estilo Mapamundi plano
color_mar = "#ECEFF1"          # Gris tiza suave (Fondo de tu Dashboard)
color_vecinos = "#F1F5F9"      # Gris neutral muy claro para países limítrofes
color_venezuela = "#D97736"    # Terracota Mate unificado para resaltar el país completo
color_lineas = "#CBD5E1"       # Gris suave para fronteras limpias

# 5. Preparar el lienzo de visualización (Single Viewport optimizado)
fig, ax = plt.subplots(figsize=(10, 7), facecolor=color_mar)
ax.set_facecolor(color_mar)

# 6. Dibujar todos los países de la región como contexto de fondo real
world.plot(ax=ax, color=color_vecinos, edgecolor=color_lineas, linewidth=0.8)

# 7. Sobrepintar a Venezuela de forma limpia y uniforme (Sin divisiones internas)
venezuela.plot(ax=ax, color=color_venezuela, edgecolor=color_lineas, linewidth=1.2)

# 8. ENCUADRE DE PRECISIÓN (Coordenadas geográficas exactas de la región de Venezuela)
# Esto garantiza que el zoom apunte perfectamente al país manteniendo sus proporciones reales
ax.set_xlim(-74.5, -59.5)
ax.set_ylim(-1.5, 13.5)

# 9. Limpieza estética total de ejes numéricos
ax.set_axis_off()
plt.tight_layout()

# 10. Guardar directamente en el directorio de estáticos de tu Django
ruta_destino = r"D:\proyecto\WRO1\danceapp\static\danceapp\images\venezuela-map.svg"
os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)

plt.savefig(ruta_destino, format='svg', bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)

print(f"\n¡Éxito rotundo! El mapa geográficamente real ha sido guardado en:\n-> {ruta_destino}")