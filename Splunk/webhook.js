// Set your Splunk HEC token and URL here
var splunkToken = "YOUR_SPLUNK_HEC_TOKEN";
var splunkUrl = "https://YOUR_SPLUNK_HEC_URL/services/collector";

// Define the Zabbix webhook function
function sendToSplunk(subject, message) {
  // Build the JSON payload to send to Splunk
  var payload = {
    "event": {
      "severity": "warning",
      "description": message,
      "source": "Zabbix",
      "subject": subject
    }
  };

  // Set the Splunk HEC headers
  var headers = {
    "Authorization": "Splunk " + splunkToken,
    "Content-Type": "application/json"
  };

  // Send the payload to Splunk via HTTP POST
  var response = httpClient.post(splunkUrl, {
    headers: headers,
    body: JSON.stringify(payload)
  });

  // Log the response status code and message
  console.log("Response status code: " + response.statusCode);
  console.log("Response message: " + response.body);
}

// Register the Zabbix webhook function as a media type
registerMediaType({
  "type": "webhook",
  "subtype": "zabbix-splunk-hec",
  "options":{
    "subject": "{$EVENT.NAME}",
    "message": "{$EVENT.VALUE}"
  },
  "send-to": function (data) {
    sendToSplunk(data.subject, data.message);
  }
});