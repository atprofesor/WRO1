function initVoiceRecognition() {
    const statusElement = document.getElementById('voice-status');
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        if (statusElement) {
            statusElement.textContent = 'Tu navegador no soporta Web Speech API.';
        }
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = 'es-ES';
    recognition.continuous = true;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onstart = function () {
        if (statusElement) {
            statusElement.textContent = 'Escuchando comandos de voz...';
        }
    };

    recognition.onresult = function (event) {
        const lastResult = event.results[event.results.length - 1];
        const transcript = lastResult[0].transcript.toLowerCase().trim();
        const command = parseCommand(transcript);
        if (command) {
            const targetUrl = buildNavigationUrl(command);
            if (targetUrl) {
                window.location.href = targetUrl;
            }
        }
    };

    recognition.onerror = function (event) {
        if (statusElement) {
            statusElement.textContent = 'Error en reconocimiento de voz: ' + (event.error || 'desconocido');
        }
    };

    recognition.onend = function () {
        if (statusElement) {
            statusElement.textContent = 'Reconocimiento detenido. Reiniciando...';
        }
        recognition.start();
    };

    recognition.start();
}

function parseCommand(text) {
    if (!text) {
        return null;
    }

    if (text.includes('tango')) {
        return 'tango';
    }
    if (text.includes('joropo')) {
        return 'joropo';
    }
    if (text.includes('volver')) {
        return 'volver';
    }
    if (text.includes('siguiente')) {
        return 'siguiente';
    }
    if (text.includes('home') || text.includes('inicio') || text.includes('finalizar')) {
        return 'home';
    }
    return null;
}

function buildNavigationUrl(command) {
    const body = document.body;
    const currentDance = body.dataset.dance || '';
    const currentStage = body.dataset.stage || '';

    if (command === 'tango' || command === 'joropo') {
        return '/dance/' + command + '/principal/';
    }

    if (command === 'home') {
        return '/';
    }

    if (command === 'volver') {
        if (currentStage === 'principal') {
            return '/';
        }
        if (currentStage === 'fotos') {
            return '/dance/' + currentDance + '/principal/';
        }
        if (currentStage === 'video') {
            return '/dance/' + currentDance + '/fotos/';
        }
    }

    if (command === 'siguiente') {
        if (currentStage === 'principal') {
            return '/dance/' + currentDance + '/fotos/';
        }
        if (currentStage === 'fotos') {
            return '/dance/' + currentDance + '/video/';
        }
    }

    return null;
}
