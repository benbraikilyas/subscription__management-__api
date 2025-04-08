// Replace this URL with your actual Django API endpoint
const apiUrl = "http://localhost:8001/subscription_management_api/subscriptions/template";  // Adjust with your URL

// Fetch subscription data from the API
fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        const subscriptionList = document.getElementById("subscription-list");

        // Loop through the data and create list items
        data.forEach(subscription => {
            const listItem = document.createElement("li");
            listItem.textContent = `Subscriptions: ${subscription.name}, Status: ${subscription.status}`;
            subscriptionList.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });
