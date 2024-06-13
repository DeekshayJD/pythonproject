import  re
def ip_check(ip):
    #ip = input("enter ip address :-")
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"

    if re.match(pattern,ip):
        octets = ip.split(".")
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                return False
        return True
    return False

while True:
    ip_adresss=input("enter ip address :-")
    if ip_check(ip_adresss):
        print("valid ip")
        break
    else:
        print("not valid ip")



