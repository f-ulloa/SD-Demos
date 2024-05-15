import nodemailer from 'nodemailer';
import dotenv from 'dotenv'
import Mail from 'nodemailer/lib/mailer';

dotenv.config();

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS
  }
});

const mailOptions: Mail.Options = {
  from: process.env.EMAIL_USER,
  to:'felipe.ulloa1@mail.udp.cl',
  subject: 'subject',
};

transporter.sendMail(mailOptions, (error, info) =>{
  if(error){
    console.error('error');
  }else{
    console.log('Correo enviado')
  }
})
