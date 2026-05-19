function handleLogin(event) {
    event.preventDefault();

    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            // Redirect to dashboard (you'll make this later)
            window.location.href = "/dashboard";
        } else {
            alert("Invalid credentials. Please try again.");
        }
    })
    .catch(err => {
        console.error("Error:", err);
        alert("Server error. Please try again later.");
    });
}

