import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
def mailer(nnm,mail):
    sender_email = '71762131004@cit.edu.in'
    sender_password = 'klbp xcpi suol mkyb'
    recipient_email = mail
    subject = 'Congratulations on Your Snake and Ladder Victory! 🏆 Certificate Inside!'

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the image
    image_path = 'output.png'  # Replace with the actual path to your image file
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        image = MIMEImage(image_data, name='image.jpg')
        msg.attach(image)

    # Add a text message if needed
    message = f"Dear {nnm},\n\nCongratulations! 🎉 You're the Snake and Ladder champion! Attached is your official certificate—proof of your awesome victory. Well played!"
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Success: Email sent")
    except Exception as e:
        print("An error occurred:", str(e))