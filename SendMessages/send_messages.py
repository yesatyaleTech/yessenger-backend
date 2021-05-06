import vonage

client = vonage.Client(key="8ce7b319", secret="EtT4RhkMj1Odeu43")
sms = vonage.Sms(client)

print(sms)

responseData = sms.send_message(
    {
        "from": "18882895380",
        "to": "16178667928",
        "text": "A text message sent using the Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")