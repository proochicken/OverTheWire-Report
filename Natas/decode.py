import base64
import binascii

ecoded_secret = "3d3d516343746d4d6d6c315669563362"

#Hex to String
hex_decode = binascii.unhexlify(ecoded_secret).decode()
rev_str = hex_decode[::-1]
secret = base64.b64decode(rev_str).decode()

print(secret)
