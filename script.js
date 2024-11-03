async function getRelayStatus() {
    try {
        const response = await fetch(`${RELAY_API_URL}/status`);
        if (!response.ok) throw new Error("Network response was not ok");
        const result = await response.json();
        document.getElementById("relayStatus").textContent = result.relay_status;
    } catch (error) {
        console.error("Error getting relay status:", error);
        document.getElementById("relayStatus").textContent = "Error fetching status";
    }
}
