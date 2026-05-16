// PWA Service Worker регистрация
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/static/sw.js')
            .then(function(reg) {
                console.log('SW зарегистрирован:', reg.scope);
            })
            .catch(function(err) {
                console.log('SW ошибка:', err);
            });
    });
}