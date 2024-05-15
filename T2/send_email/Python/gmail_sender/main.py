from gmail_sender.config import load_config
from gmail_sender.email_utils import create_email, send_email

def main():
    config = load_config()
    
    from_addr = config['username']
    to_addr = "felipe.ulloa1@mail.udp.cl"
    subject = "Asunto del correo"
    body = "Cuerpo del correo"
    
    email_msg = create_email(subject, body, from_addr, to_addr)
    send_email(config, email_msg)
    print("Correo enviado con éxito")

if __name__ == "__main__":
    main()
