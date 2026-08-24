import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings



async def send_email(
    to_email: str,
    subject: str,
    html_content: str,
):

    message = MIMEMultipart("alternative")

    message["From"] = (
        f"{settings.brevo_from_name} "
        f"<{settings.brevo_from_email}>"
    )

    message["To"] = to_email

    message["Subject"] = subject


    html_part = MIMEText(
        html_content,
        "html"
    )


    message.attach(html_part)


    try:

        server = smtplib.SMTP(
            settings.brevo_host,
            settings.brevo_port
        )


        server.starttls()


        server.login(
            settings.brevo_user,
            settings.brevo_pass
        )


        server.sendmail(
            settings.brevo_from_email,
            to_email,
            message.as_string()
        )


        server.quit()


        return True


    except Exception as error:

        raise Exception(
            f"Email sending failed: {str(error)}"
        )