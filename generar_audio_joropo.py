from gtts import gTTS
import os

print("\n=== GENERADOR DE AUDIO-GUÍA TEXT-TO-SPEECH (CYBERPUPPETS) ===")
print("Compilando el libreto cultural del Joropo...")

# 1. Construcción del guion auditivo unificado
libreto = (
    "Bienvenidos a la sección del Joropo. "
    "El Joropo es la máxima expresión del mestizaje cultural venezolano, consolidado en el siglo dieciocho "
    "a partir de la fusión del fandango español, las melodías indígenas y los polirritmos africanos. "
    "Originalmente, la palabra significaba fiesta o jolgorio campesino, evolucionando hasta convertirse "
    "en la identidad dancística nacional. Su coreografía representa un elegante juego de cortejo donde "
    "el hombre ejecuta un zapateo recio y enérgico para asombrar a la mujer, mientras ella responde "
    "con un sutil y coordinado escobillao. "
    "Esta manifestación trasciende las fronteras llaneras para diversificarse en variantes como el joropo "
    "central y el oriental, cada uno con variantes instrumentales y dancísticas únicas. Debido a su "
    "incalculable valor identitario, fue declarado Patrimonio Cultural de la Nación, consolidándose como "
    "el latido artístico de Venezuela ante el mundo. "
    "Dentro de sus especificaciones tradicionales, destaca una métrica musical de tres cuartos y seis octavos "
    "alternados. Su ensamble instrumental típico está compuesto por el Arpa Llanera, el Cuatro y las Maracas. "
    "Y sus focos culturales principales se localizan en Los Llanos, la Región Central y el Eje Oriental."
)

print("Sintetizando voz artificial con acento en español nativo...")

# 2. Configurar gTTS (Idioma español 'es', tld 'es' o 'com' para acento limpio)
tts = gTTS(text=libreto, lang='es', tld='com', slow=False)

# 3. Definir ruta y crear directorio de audios si no existe
carpeta_destino = r"D:\proyecto\WRO1\danceapp\static\danceapp\audio"
os.makedirs(carpeta_destino, exist_ok=True)

ruta_archivo = os.path.join(carpeta_destino, "joropo_speech.mp3")

# 4. Guardar archivo final
tts.save(ruta_archivo)

print(f"\n¡Éxito rotundo! Archivo de audio-guía generado en:\n-> {ruta_archivo}")