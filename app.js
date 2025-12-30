const API_URL = "https://rdmb8ld7pl.execute-api.us-east-1.amazonaws.com/initial";

async function submitFeedback(event) {
    event.preventDefault();

    const btn = document.getElementById("submit-btn");
    btn.disabled = true;
    btn.innerText = "Submitting...";

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const feedback = document.getElementById("feedback").value;

    const data = { name, email, feedback };

    console.log("Sending to API:", API_URL);
    console.log("Data:", data);

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        alert(result.message);

    } catch (error) {
        alert("Error submitting feedback");
        console.error(error);
    }

    btn.disabled = false;
    btn.innerText = "Submit";
}
