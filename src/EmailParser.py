import email

from .EmailMessage import EmailMessage

def parse_raw_message(raw_msg: dict) -> EmailMessage:
    try:
        content = email.message_from_bytes(raw_msg[b"BODY[]"])
    except Exception as e:
        print(f"Error: {e}")

    #  for key in content.keys():
        #  print(key)
        #  print(content[key]+"\n\n")

    msg = EmailMessage()
    msg.set_date(content["Date"])
    msg.set_sender(content["From"])
    msg.set_subject(content["Subject"])
    msg.set_body(content.get_payload())
    print(msg)

    return msg
