import smtplib
from email.message import EmailMessage

class EmailSender:
    def __init__(self):
        self.sender_email = "suganyaanandram@gmail.com"
        self.sender_password = "idkv cmce vouw xjfo"

    def send_email(self, to_email, subject, content):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = to_email
        msg.set_content(content)

        # For Gmail, use 'smtp.gmail.com' and port 587
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(self.sender_email, self.sender_password)
                smtp.send_message(msg)
                print("Email sent successfully.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

def send_confirmation_email(sender, to_email, employee_name):
    subject = 'Employee Enrollment Confirmation'
    content = f"Dear {employee_name},\n\nWelcome! Your enrollment is confirmed.\n\nRegards,\nHR Team"
    sender.send_email(to_email, subject, content)

if __name__ == "__main__":
    try:
        sender = EmailSender()
        send_confirmation_email(sender, "suganya.sg.net@gmail.com", "Alice")
    except Exception as e:
        print(f"Error: {e}")

# Example usage after adding an employee:
# sender = EmailSender()
# send_confirmation_email(sender, "employee@mail.com", "Alice")