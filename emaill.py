import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
def mailer(nnm,mail):
    sender_email = 'abcdefgh@gmail.com'
    sender_password = 'abcd efgh ijkl'
    recipient_email = mail
    subject = 'Congratulations on Your Snake and Ladder Victory! 🏆 Certificate Inside!'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    image_path = 'output.png'  # Replace with the actual path to your image file
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        image = MIMEImage(image_data, name='image.jpg')
        msg.attach(image)

    message = f"Dear {nnm},\n\nCongratulations! 🎉 You're the Snake and Ladder champion! Attached is your official certificate—proof of your awesome victory. Well played!"
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Success: Email sent")
    except Exception as e:
        print("An error occurred:", str(e))
