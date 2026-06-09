import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

print("\n=== GENERADOR VECTORIAL FORZADO A SVG (CYBERPUPPETS) ===")
print("Modelando siluetas limpias para el ensamble instrumental...")

# 1. Configuración de la paleta de colores del Dashboard
color_fondo = "#FFFFFF"       # Fondo de la tarjeta blanca
color_principal = "#D97736"   # Terracota corporativo
color_secundario = "#1E293B"  # Gris pizarra oscuro
color_lineas = "#94A3B8"      # Gris suave para cuerdas

# 2. Inicializar el lienzo de dibujo
fig, ax = plt.subplots(figsize=(8, 3), facecolor=color_fondo)
ax.set_facecolor(color_fondo)

# --- DIBUJO DEL ARPA LLANERA (Izquierda) ---
ax.add_patch(patches.Rectangle((-2.5, 0.2), 0.15, 2.2, color=color_secundario, zorder=3))
ax.plot([-2.5, -0.8], [2.4, 2.0], color=color_secundario, lw=8, solid_capstyle='round', zorder=3)
caja_x = [-2.5, -0.8, -1.1, -2.5]
caja_y = [0.2, 0.2, 2.0, 0.2]
ax.fill(caja_x, caja_y, color=color_principal, alpha=0.9, zorder=2)
for i in range(1, 8):
    factor = i / 8.0
    x_cuerda = -2.5 + (1.7 * factor)
    y_top = 2.4 - (0.4 * factor)
    ax.plot([x_cuerda, x_cuerda], [0.2, y_top], color=color_lineas, lw=0.7, alpha=0.7, zorder=1)
ax.text(-1.6, -0.2, "Arpa Llanera", ha="center", va="top", fontsize=10, fontweight="bold", color=color_secundario)

# --- DIBUJO DEL CUATRO (Centro) ---
ax.add_patch(patches.Circle((0.5, 0.8), 0.4, color=color_principal, zorder=2))
ax.add_patch(patches.Circle((0.5, 1.4), 0.3, color=color_principal, zorder=2))
ax.add_patch(patches.Circle((0.5, 1.3), 0.08, color=color_fondo, zorder=3))
ax.add_patch(patches.Rectangle((0.44, 1.6), 0.12, 0.8, color=color_secundario, zorder=2))
ax.add_patch(patches.Rectangle((0.41, 2.4), 0.18, 0.2, color=color_principal, zorder=3))
for dx in [-0.04, -0.01, 0.02, 0.05]:
    ax.plot([0.5 + dx, 0.5 + dx], [0.5, 2.4], color="#FFFFFF", lw=0.8, zorder=4)
ax.text(0.5, -0.2, "Cuatro", ha="center", va="top", fontsize=10, fontweight="bold", color=color_secundario)

# --- DIBUJO DE LAS MARACAS (Derecha) ---
ax.add_patch(patches.Ellipse((2.2, 1.5), 0.4, 0.6, angle=20, color=color_principal, zorder=2))
ax.plot([2.2, 1.9], [1.3, 0.5], color=color_secundario, lw=6, solid_capstyle='round', zorder=1)
ax.add_patch(patches.Ellipse((2.2, 1.5), 0.4, 0.1, angle=20, color=color_fondo, zorder=3))
ax.add_patch(patches.Ellipse((2.6, 1.4), 0.4, 0.6, angle=-20, color=color_secundario, zorder=2))
ax.plot([2.6, 2.9], [1.2, 0.4], color=color_principal, lw=6, solid_capstyle='round', zorder=1)
ax.add_patch(patches.Ellipse((2.6, 1.4), 0.4, 0.1, angle=-20, color=color_fondo, zorder=3))
ax.text(2.4, -0.2, "Maracas", ha="center", va="top", fontsize=10, fontweight="bold", color=color_secundario)

# 3. Ajustes finales del lienzo
ax.set_xlim(-3.0, 3.5)
ax.set_ylim(-0.5, 2.8)
ax.set_axis_off()
plt.tight_layout()

# 4. RUTAS DE DESTINO CON EXPRESIÓN RESTRITA A SVG
# Nota: En tu mensaje mencionas "Joropo-ppal". Si en tu base de datos o HTML llamaste
# a la imagen "Joropo-ppal.svg" en lugar de "inst_joropo.svg", cambia el nombre aquí abajo:
nombre_archivo = "inst_joropo.svg"  # O cámbialo a "Joropo-ppal.svg" según tu plantilla HTML

ruta_destino = os.path.join(r"D:\proyecto\WRO1\danceapp\static\danceapp\images", nombre_archivo)
os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)

# 5. GUARDADO SEGURO DE FORMATO VECTORIAL ORIGINAL (.svg)
# Aquí obligamos explícitamente a Matplotlib a compilar en código de vectores xml
plt.savefig(
    ruta_destino, 
    format='svg',           # <--- ESTO OBLIGA A QUE NO SEA JPG
    bbox_inches='tight', 
    facecolor=fig.get_facecolor(), 
    edgecolor='none'
)
plt.close(fig)

print(f"\n¡Verificado! Se ha forzado y creado con éxito el archivo VECTORIAL en:")
print(f"-> {ruta_destino}")