import quopri

from . import Email

def parse_raw_message(raw_msg: dict) -> Email:
    try:
        #  content = raw_msg[b"BODY[]"].decode("utf-8")
        content = quopri.decodestring(raw_msg[b"BODY[]"])
        content = content.decode("windows-1251")
    except:
        pass

    #  print(content)
    start = content.find("From:")
    end = content.find("Content-Type: text/html")

    content = content[start:end].strip()

    start = content.find("Date:")
    end = content.find('\n', start)
    print(start)
    print(end)
    timestamp = content[start:end]

    #  print(message)
    print(timestamp)
    return None
