import quopri
import email

from .EmailMessage import EmailMessage

def parse_raw_message(UID: int, raw_msg: dict) -> EmailMessage:
    try:
        content = email.message_from_bytes(raw_msg[b"BODY[]"])
        charset = content.get_charsets()
        i = 0
        for part in content.walk():
            part.set_charset(charset[i])
            i += 1
    except Exception as e:
        print(f"Error: {e}")

    msg = EmailMessage()
    msg.set_uid(UID)
    msg.set_date(content["Date"])
    msg.set_sender(content["From"])
    msg.set_subject(content["Subject"])
    body = ""
    if content.is_multipart():
        for part in content.get_payload():
            charset = part.get_charset().__str__()
            if charset == "None":
                charset = "utf-8"
            body += quopri.decodestring(part.as_string()).decode(charset)
    else:
        charset = part.get_charset().__str__()
        if charset == "None":
            charset = "utf-8"
        body = quopri.decodestring(content.get_payload()).decode(charset)
    msg.set_body(body)

    return msg
