from django.core.mail import mail_admins

MIN_TEXT_LENGTH = 3


def process_message_feedback(text, email, session_pk):
    # check message
    if len(text) < MIN_TEXT_LENGTH:
        raise ValueError("Message text is too short")

    print session_pk
    print text
    print email

    # render message (email body)
    message = """
    text:
    {text}

    email:
    {email}

    session:
    {session}
    """.format(text=text, email=email, session=session_pk)

    # TODO: mail_admins('Smartoo: Message Feedback', message)