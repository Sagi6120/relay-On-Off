document.addEventListener("DOMContentLoaded", function() {
    const turnOnButton = document.getElementById("turnOnButton");
    const turnOffButton = document.getElementById("turnOffButton");
    const statusMessage = document.getElementById("statusMessage");

    turnOnButton.addEventListener("click", function() {
        // Simulate turning the relay ON
        statusMessage.textContent = "Relay TURNED ON"; // Update the status message
        console.log("Relay turned ON"); // For debugging
    });

    turnOffButton.addEventListener("click", function() {
        // Simulate turning the relay OFF
        statusMessage.textContent = "Relay TURNED OFF"; // Update the status message
        console.log("Relay turned OFF"); // For debugging
    });
});
