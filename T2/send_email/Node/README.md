1. Inicializar el Proyecto

mkdir proyecto-nodemailer
cd proyecto-nodemailer
npm init -y

2. Instalar Dependencias

npm install nodemailer
npm install dotenv
npm install --save-dev typescript @types/node @types/nodemailer

3. Inicializar TypeScript

npx tsc --init

4. Crear la Estructura del Proyecto

mkdir src
touch src/index.ts
touch .env

5. Configurar TypeScript (tsconfig.json)

Asegúrate de que tu tsconfig.json tenga las siguientes configuraciones mínimas:

{
    "compilerOptions": {
        "target": "ES6",
        "module": "commonjs",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true,
        "outDir": "./dist"
    },
    "include": ["src"]
}

6. Configurar el Archivo .env

Primero, crea una contraseña de aplicación en tu cuenta de Gmail:

    - Ve a tu cuenta de Google.
    - Dirígete a "Seguridad".
    - En la sección "Acceso de Google", selecciona "Contraseñas de aplicaciones".
    - Sigue los pasos para generar una contraseña de aplicación.

Luego, crea un archivo .env en la raíz de tu proyecto con las siguientes variables (ajusta según tus datos):

EMAIL_USER=tu-email@gmail.com
EMAIL_PASS=tu-contraseña-de-aplicacion

7. Escribir el Código en TypeScript (src/index.ts)

import nodemailer from 'nodemailer';
import dotenv from 'dotenv';

// Cargar las variables de entorno desde el archivo .env
dotenv.config();

// Configurar el transportador con los datos de tu cuenta de correo
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS
    }
});

// Configurar el correo
const mailOptions = {
    from: process.env.EMAIL_USER,
    to: 'destinatario@example.com',
    subject: 'Asunto del correo',
    text: 'Cuerpo del correo'
};

// Enviar el correo
transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
        console.error('Error al enviar el correo:', error);
    } else {
        console.log('Correo enviado:', info.response);
    }
});

8. Configurar Scripts en package.json

Agrega los siguientes scripts en tu package.json para compilar y ejecutar tu proyecto:

"scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
}

9. Asegurar el Archivo .env

Asegúrate de no subir tu archivo .env a ningún repositorio público. Puedes agregarlo al .gitignore:

echo .env >> .gitignore

Cómo Levantar el Proyecto

1. Compilar el Proyecto

npm run build

2. Ejecutar el Proyecto

npm start
