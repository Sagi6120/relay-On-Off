document.addEventListener("DOMContentLoaded", function() {
    const turnOnButton = document.getElementById("turnOnButton");
    const turnOffButton = document.getElementById("turnOffButton");
    const statusMessage = document.getElementById("statusMessage");

    turnOnButton.addEventListener("click", function() {
        // Simulate turning the relay ON - AKM
        statusMessage.textContent = "Relay TURNED ON - AKM"; // Update the status message
        console.log("Relay turned ON - AKM"); // For debugging
    });

    turnOffButton.addEventListener("click", function() {
        // Simulate turning the relay OFF - NIO
        statusMessage.textContent = "Relay TURNED OFF - NIO"; // Update the status message
        console.log("Relay turned OFF - NIO"); // For debugging
    });
});
