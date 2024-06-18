document.getElementById('message-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const messageInput = document.getElementById('message-input').value;

    fetch('/process_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: messageInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('processed-message').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
