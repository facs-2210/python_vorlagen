
def anonymizeName(name):
    # take first character and fill to 10 with *
    return name[0] + "*" * 9

print(anonymizeName("Sandro")) # S*********


def anonymizeZip(zip):
    # take the first two and add two zeros
    return zip[:2] + "00"

print(anonymizeZip("1234")) # 1200

def anonymizePhone(phone):
    # replace the last 4 digits with 0 (Beware whitespace)
    return phone[:-5] + "00 00"

print(anonymizePhone("078 123 12 12")) # 078 123 00 00

def anonymizeEmail(email):
    # take the first char and fill 9 with *, then add the domain
    return email[0] + "*" * 9 + email[email.index("@"):]

print(anonymizeEmail("test@domain.ch")) # t*******@domain.ch


def anonymizeCreditCard(creditCard):
    # take the last 4 digits, replace the rest with *
    return "*" * 12 + creditCard[-4:]

print(anonymizeCreditCard("1234 5678 9012 3456")) # ************3456

def anonymizeIp(ipAddress):
    # replace the last octet with 0
    return ".".join(ipAddress.split('.')[:-1] + ["0"])

print(anonymizeIp("127.120.121.34")) # 127.120.121.0