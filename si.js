// scripts.js
document.addEventListener("DOMContentLoaded", function() {
    // Crear confeti
    function createConfetti() {
        const confettiContainer = document.getElementById('confetti');
        for (let i = 0; i < 100; i++) {
            const confetti = document.createElement('div');
            confetti.classList.add('confetti');
            confetti.style.left = Math.random() * 100 + 'vw';
            confetti.style.animationDuration = Math.random() * 3 + 2 + 's';
            confettiContainer.appendChild(confetti);
        }
    }
    createConfetti();

    // Cuenta regresiva
    function countdown() {
        const now = new Date();
        const eventDate = new Date(now.getFullYear(), 11, 31); // Cambia esta fecha a la fecha de cumpleaños

        const currentTime = now.getTime();
        const eventTime = eventDate.getTime();

        const remTime = eventTime - currentTime;

        const s = Math.floor(remTime / 1000);
        const m = Math.floor(s / 60);
        const h = Math.floor(m / 60);
        const d = Math.floor(h / 24);

        const days = d;
        const hours = h % 24;
        const minutes = m % 60;
        const seconds = s % 60;

        document.getElementById('countdown').textContent = 
            days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

        setTimeout(countdown, 1000);
    }

    countdown();
});
