import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Gmail SMTP sunucusu ayarları
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"  # Gönderen e-posta adresi
    sender_password = "your_password"  # Gönderen e-posta şifresi

    # E-posta içeriği
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # SMTP sunucusuna bağlan
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # TLS bağlantısını başlat
        server.login(sender_email, sender_password)  # Giriş yap
        server.send_message(msg)  # E-postayı gönder
        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        server.quit()  # Bağlantıyı kapat

# E-posta gönderme örneği
send_email("Test Konusu", "Bu bir test e-postasıdır.", "recipient_email@example.com")

