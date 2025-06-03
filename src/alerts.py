import os
from twilio.rest import Client

def send_sms_alert(phone, message):
    # Twilio credentials from environment variables
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
    if not all([account_sid, auth_token, twilio_number]):
        raise ValueError("Twilio credentials not set in environment variables.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=phone
    )
    return message.sid

def send_email_alert(email, subject, body):
    # Placeholder for email alert logic (e.g., using SendGrid, SMTP, etc.)
    print(f"Email to {email}: {subject}\n{body}")

# Example usage:
# send_sms_alert("+1234567890", "Poaching alert detected in Sector 4!")
# send_email_alert("user@example.com", "Deforestation Alert", "Satellite detected new forest loss.")
