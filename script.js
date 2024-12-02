document.addEventListener("DOMContentLoaded", function() {
    const turnOnButton = document.getElementById("turnOnButton");
    const turnOffButton = document.getElementById("turnOffButton");
    const statusMessage = document.getElementById("statusMessage");

    // Define the API endpoint (replace <your_pi_ip> with the IP address of your Raspberry Pi)
    const RELAY_API_URL = "http://<192.168.19.100>:5000";

    // Function to control the relay
    async function controlRelay(action) {
        try {
            const response = await fetch(`${RELAY_API_URL}/relay`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ action: action })
            });
            const result = await response.json();
            statusMessage.textContent = result.status; // Update the status message
        } catch (error) {
            console.error("Error controlling relay:", error);
            statusMessage.textContent = "Error controlling relay";
        }
    }

    // Function to get the relay status
    async function getRelayStatus() {
        try {
            const response = await fetch(`${RELAY_API_URL}/status`);
            if (!response.ok) throw new Error("Network response was not ok");
            const result = await response.json();
            statusMessage.textContent = `Relay Status: ${result.relay_status}`; // Display the relay status
        } catch (error) {
            console.error("Error getting relay status:", error);
            statusMessage.textContent = "Error fetching status";
        }
    }

    // Add event listeners for buttons
    turnOnButton.addEventListener("click", function() {
        controlRelay("on_akm"); // Send request to turn relay ON (AKM)
        console.log("Relay turned ON - AKM");
    });

    turnOffButton.addEventListener("click", function() {
        controlRelay("on_nio"); // Send request to turn relay OFF (NIO)
        console.log("Relay turned OFF - NIO");
    });

    // Check relay status on load
    getRelayStatus();
});
