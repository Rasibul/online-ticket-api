def verification_email_template(token:str):


    verification_url = (
        "http://localhost:5173/"
        f"verify-email?token={token}"
    )


    return f"""

    <h2>
    Welcome to Online Ticket Booking
    </h2>


    <p>
    Please verify your email.
    </p>


    <a href="{verification_url}">
    Verify Email
    </a>


    <p>
    Link expires after 24 hours.
    </p>

    """