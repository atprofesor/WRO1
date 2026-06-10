# 🎭 CYBERPUPPETS

## !Luces, cámara, acción! Y que empiece el show

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Vosk](https://img.shields.io/badge/Vosk-Offline%20STT-purple.svg)](https://alphacephei.com/vosk/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![WRO](https://img.shields.io/badge/WRO-2026-Futuros%20Innovadores-red.svg)](https://wro-association.org/)

> **"Preservando la tradición a través de la innovación: danzas latinoamericanas controladas por voz"**

---

## 📖 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Problema que Resuelve](#-problema-que-resuelve)
- [Innovación Tecnológica](#-innovación-tecnológica)
- [Características Principales](#-características-principales)
- [Comandos de Voz](#-comandos-de-voz)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Guía de Uso](#-guía-de-uso)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Equipo de Desarrollo](#-equipo-de-desarrollo)
- [Criterios WRO 2026](#-criterios-wro-2026)
- [Roadmap](#-roadmap)
- [Reconocimientos](#-reconocimientos)
- [Licencia](#-licencia)

---

## 🎯 Descripción del Proyecto

**CyberPuppets** es una plataforma web educativa interactiva que combina tecnología de reconocimiento de voz con contenido cultural para enseñar danzas tradicionales de Latinoamérica, comenzando con el **Joropo venezolano** y el **Tango argentino**.

A través de una interfaz amigable y controlable completamente por voz, los usuarios pueden explorar:

| Sección | Contenido |
|---------|-----------|
| 📖 **Reseñas históricas** | Detalles completos del origen y evolución de cada danza |
| 🗺️ **Mapas geográficos** | Visualización de las regiones de origen |
| 🎵 **Instrumentos típicos** | Representaciones visuales del ensamble instrumental |
| 📸 **Galerías fotográficas** | Carrusel automático con imágenes representativas |
| 🎬 **Videos a pantalla completa** | Demostraciones coreográficas con sonido envolvente |
| 🔊 **Guías de audio** | Narraciones educativas (disponible para Joropo) |

El proyecto está diseñado para ser **accesible, inclusivo y educativo**, permitiendo que niños, personas con movilidad reducida o dificultades de lectura puedan aprender sobre su patrimonio cultural usando solo su voz.

---

## 🌍 Problema que Resuelve

### Contexto Cultural

Las danzas tradicionales latinoamericanas están **perdiendo relevancia** entre las nuevas generaciones debido a:

- Falta de acceso a materiales educativos interactivos
- Predominio de contenido digital extranjero
- Barreras de alfabetización y discapacidades motoras
- Ausencia de tecnologías accesibles en zonas rurales

### Nuestra Solución

| Problema | Solución CyberPuppets |
|----------|----------------------|
| Falta de interés juvenil | Experiencia gamificada e interactiva |
| Barreras de acceso físico | Control por voz (sin mouse/teclado) |
| Dificultades de lectura | Audio guía y narraciones |
| Desconexión geográfica | Mapas interactivos y contenido localizado |
| Privacidad en zonas rurales | Reconocimiento de voz OFFLINE (Vosk) |

### 🌟 Alineación con ODS

| ODS | Contribución |
|-----|---------------|
| **ODS 4 - Educación de Calidad** | Aprendizaje interactivo y accesible sobre patrimonio cultural |
| **ODS 10 - Reducción de Desigualdades** | Acceso universal mediante control por voz |
| **ODS 11 - Ciudades y Comunidades Sostenibles** | Preservación del patrimonio cultural inmaterial |

---

## 💡 Innovación Tecnológica

### 🎤 Reconocimiento de Voz Híbrido

CyberPuppets implementa **dos capas de reconocimiento de voz** que trabajan en conjunto:

| Capa | Tecnología | Ventaja |
|------|------------|---------|
| **Frontend** | Web Speech API | Rápida, sin latencia, funciona en cualquier navegador moderno |
| **Backend Offline** | Vosk + SoundDevice | Privada, no requiere internet, funciona en zonas rurales |

### 🔄 Integración Unificada

Ambos sistemas convergen en la misma lógica de navegación, permitiendo:
- Mismos comandos de voz en ambos modos
- Fallback automático si uno falla
- Experiencia consistente para el usuario

### 🎨 Características Técnicas Destacadas

- **Animaciones CSS puras** (sin JavaScript para el carrusel, mejor rendimiento)
- **Fullscreen API** para experiencia inmersiva de video
- **Responsive Design** adaptable a tablets, computadoras y dispositivos móviles
- **Audio autoplay inteligente** con manejo de políticas de navegador
- **Interceptor de comandos** que evita conflictos entre sistemas de voz

---

## ✨ Características Principales

### 🏠 Página de Inicio (home.html)
- Mapa mundi interactivo con países destacados (Venezuela y Argentina)
- Botones de acceso directo por danza con badges identificativos
- Footer con créditos del equipo y proyecto WRO 2026
- Indicador de comandos de voz disponibles

### 📖 Página Principal de Danza (principal_danza.html)
- Tarjeta lateral izquierda con mapa geográfico del país
- Visualización de instrumentos típicos (disponible para Joropo)
- Tarjeta lateral derecha con reseña histórica completa
- Especificaciones técnicas: métrica musical, instrumentación, pasos clave
- Audio guía narrada con control de reproducción (play/pausa)
- Etiquetas de regiones o focos culturales
- Botones de navegación "Volver" (Home) y "Siguiente" (Fotos)

### 📸 Galería de Fotos (fotos_danza.html)
- Carrusel automático con 4 imágenes representativas
- Animación CSS cíclica (sin JavaScript, rendimiento optimizado)
- Comandos de voz "siguiente", "adelante", "continuar" para avanzar
- Comandos de voz "volver", "atrás", "regresar" para retroceder
- Feedback visual en el footer al detectar comandos
- Viewport fijo y controlado sin scroll accidental

### 🎬 Video a Pantalla Completa (video_danza.html)
- Reproducción automática con sonido (cuando el navegador lo permite)
- Overlay de bienvenida si el navegador bloquea el autoplay
- Entrada automática a pantalla completa al iniciar
- Salida automática al finalizar el video
- Comando de voz "volver"/"atrás"/"regresar" para salir manualmente
- Ocultamiento automático de header y footer para experiencia inmersiva

---

## 🎤 Comandos de Voz

### Comandos Globales (funcionan en cualquier página)

| Comando Principal | Alternativas | Acción |
|------------------|--------------|--------|
| `joropo` | - | Ir a la página del Joropo |
| `tango` | - | Ir a la página del Tango |
| `inicio` | `home`, `finalizar` | Regresar al inicio |

### Comandos por Sección

#### 📖 Página Principal (principal_danza.html)

| Comando | Alternativas | Acción |
|---------|--------------|--------|
| `siguiente` | `adelante`, `continuar` | Ir a Galería de Fotos |
| `volver` | `atrás`, `regresar` | Regresar al Inicio |

#### 📸 Galería de Fotos (fotos_danza.html)

| Comando | Alternativas | Acción |
|---------|--------------|--------|
| `siguiente` | `adelante`, `continuar` | Ir a Video |
| `volver` | `atrás`, `regresar` | Regresar a Página Principal |

#### 🎬 Video (video_danza.html)

| Comando | Alternativas | Acción |
|---------|--------------|--------|
| `volver` | `atrás`, `regresar` | Salir del video y regresar a Galería |
| `siguiente` | `adelante`, `continuar` | Muestra mensaje informativo (el video debe terminar) |

> 💡 **Consejos para mejor reconocimiento:**
> - Hablar claro y en español neutro
> - Mantener volumen normal, no gritar
> - Evitar ruido de fondo
> - Decir un comando a la vez
> - Esperar confirmación visual en el footer

---

## 🛠️ Tecnologías Utilizadas

### Backend

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.10+ | Lenguaje principal del backend |
| **Django** | 4.2 | Framework web MVC |
| **Vosk** | 0.3.45 | Reconocimiento de voz offline |
| **SoundDevice** | 0.4.6 | Captura de audio desde micrófono |
| **SQLite** | 3.x | Base de datos ligera (sin configuración adicional) |

### Frontend

| Tecnología | Propósito |
|------------|-----------|
| **HTML5** | Estructura semántica del sitio |
| **CSS3** | Estilos visuales, animaciones, diseño responsive |
| **JavaScript (ES6+)** | Interactividad, eventos, lógica de voz |
| **Web Speech API** | Reconocimiento de voz en navegador |
| **Fullscreen API** | Control de pantalla completa para videos |

### Assets Multimedia

| Tipo | Formato | Cantidad | Contenido |
|------|---------|----------|-----------|
| Imágenes | SVG | 7+ | Mapas, instrumentos, fotos de danza |
| Audio | MP3 | 1 | Narración guía del Joropo |
| Video | MP4 (H.264) | 1 | Demostración coreográfica del Joropo |

---

## 🏗️ Arquitectura del Sistema

### Diagrama de Componentes

```mermaid
graph TB
    subgraph "Frontend"
        A[HTML/CSS/JS]
        B[Web Speech API]
        C[voice.js]
    end
    
    subgraph "Backend Django"
        D[views.py]
        E[urls.py]
        F[Templates]
        G[Static Files]
    end
    
    subgraph "Motor Vosk Offline"
        H[motor_voz.py]
        I[Modelo Vosk]
        J[SoundDevice]
    end
    

graph LR
    A[Home] -->|"voz: joropo/tango"| B[Principal]
    B -->|"siguiente/adelante"| C[Fotos]
    C -->|"siguiente/adelante"| D[Video]
    D -->|"volver/atrás"| C
    C -->|"volver/atrás"| B
    B -->|"volver/atrás"| A


sequenceDiagram
    participant U as Usuario
    participant N as Navegador
    participant W as Web Speech API
    participant V as voice.js
    participant D as Django
    
    U->>N: Dice "siguiente"
    N->>W: Captura audio
    W->>V: Transcribe texto
    V->>V: Procesa comando
    V->>D: Navega a URL
    D-->>N: Nueva página
    N-->>U: Muestra contenido

CyberPuppets/
│
├── WRO1/                          # Proyecto Django principal
│   ├── manage.py                  # CLI de Django
│   ├── db.sqlite3                 # Base de datos (autogenerada)
│   ├── requirements.txt           # Dependencias Python
│   │
│   ├── cyberpuppets/              # Configuración del proyecto
│   │   ├── __init__.py
│   │   ├── settings.py            # Configuración global
│   │   ├── urls.py                # URLs principales
│   │   └── wsgi.py                # Punto de entrada para producción
│   │
│   ├── danceapp/                  # Aplicación principal
│   │   ├── __init__.py
│   │   ├── admin.py               # Configuración admin
│   │   ├── apps.py                # Configuración app
│   │   ├── views.py               # Lógica de negocio
│   │   ├── models.py              # Modelos de datos
│   │   ├── urls.py                # URLs de la app
│   │   │
│   │   ├── templates/danceapp/    # Plantillas HTML
│   │   │   ├── base.html          # Plantilla base (header, footer, voice.js)
│   │   │   ├── home.html          # Página de inicio con mapa
│   │   │   ├── principal_danza.html  # Información principal de danza
│   │   │   ├── fotos_danza.html      # Galería de fotos con carrusel
│   │   │   └── video_danza.html      # Video a pantalla completa
│   │   │
│   │   └── static/danceapp/       # Archivos estáticos
│   │       ├── css/
│   │       │   └── styles.css     # Estilos globales
│   │       ├── js/
│   │       │   └── voice.js       # Control por voz frontal (Web Speech API)
│   │       ├── images/
│   │       │   ├── map-mundi.svg
│   │       │   ├── venezuela.svg
│   │       │   ├── argentina.svg
│   │       │   ├── Joropo1.svg
│   │       │   ├── Joropo2.svg
│   │       │   ├── Joropo3.svg
│   │       │   ├── Joropo4.svg
│   │       │   └── inst_joropo.svg
│   │       ├── audio/
│   │       │   └── joropo_speech.mp3
│   │       └── videos/
│   │           └── video_joropo.mp4
│   │
│   └── modelos/                   # Modelos de Vosk (offline STT)
│       └── vosk-model-small-es-0.42/  # Modelo español (280MB)
│           ├── am/
│           ├── conf/
│           ├── ivector/
│           ├── README
│           └── final.mdl
│
├── WRO2/                          # Copia de respaldo (opcional)
│
├── motor_voz.py                   # Motor offline Vosk + SoundDevice
│
└── README.md                      # Este archivo


