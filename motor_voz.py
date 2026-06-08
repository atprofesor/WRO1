import queue
import sys
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# 1. Crear una cola (Queue) para almacenar los fragmentos de audio en tiempo real
cola_audio = queue.Queue()

def callback_microfono(indata, frames, time, status):
    """Esta función es llamada automáticamente por sounddevice por cada bloque de audio"""
    if status:
        print(f"Estado del micrófono: {status}", file=sys.stderr)
    # Metemos los datos binarios del audio en nuestra cola
    cola_audio.put(bytes(indata))

# 2. Carga del Modelo Acústico Local de Vosk
# (Asegúrate de haber descargado el modelo "vosk-model-small-es-0.42" y extraerlo en esta carpeta)
modelo_path = "modelos/vosk-model-small-es-0.42"
try:
    model = Model(modelo_path)
except Exception:
    print(f"Error: No se encontró el modelo de Vosk en la ruta '{modelo_path}'.")
    print("Descárgalo de alphacephei.com/vosk/models e insértalo en esa carpeta.")
    sys.exit(1)

# 3. Configuración del Diccionario de Comando y Control
comandos_permitidos = '["tango", "joropo", "siguiente", "volver", "inicio", "[unk]"]'
rec = KaldiRecognizer(model, 16000, comandos_permitidos)

print("\n=== MOTOR DE VOZ CYBERPUPPETS ===")
print("Escuchando comandos locales de voz con SoundDevice...")

# 4. Abrir el flujo del micrófono de forma segura
try:
    # Abrimos el micrófono a 16000Hz (frecuencia óptima para Vosk), en Mono (1 canal), formato int16
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback_microfono):
        
        while True:
            # Sacamos el audio de la cola (se bloquea aquí hasta que haya datos disponibles)
            data = cola_audio.get()
            
            # Pasamos el audio a la IA para el análisis fonético
            if rec.AcceptWaveform(data):
                resultado = json.loads(rec.Result())
                texto_detectado = resultado.get("text", "")
                
                if texto_detectado:
                    print(f"¡Comando detectado!: {texto_detectado}")
                    
                    # AQUÍ IRÁ LA FUTURA COMUNICACIÓN CON DJANGO MEDIANTE WEBSOCKETS
                    if texto_detectado == "tango":
                        print("-> Orden: Ir a la sección de Tango")
                    elif texto_detectado == "joropo":
                        print("-> Orden: Ir a la sección de Joropo")
                        
except KeyboardInterrupt:
    print("\nMotor de voz detenido por el usuario.")
except Exception as e:
    print(f"\nError crítico en el hardware de audio: {e}")