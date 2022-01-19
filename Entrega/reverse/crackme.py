cc_secret = "TG9yZW1pcHN1bWRvbG9yc2l0YW1ldCxjb25zZWN0ZXR1cmFkaXBpc2NpbmdlbGl0UGhhc2VsbHVzZQ=="

cc_secret1 = "Loremipsumdolorsitamet,consecteturadipiscingelitPhaselluse"

import base64


def codificar():
    message = cc_secret1
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(base64_message)


def decodificar():
    base64_message = cc_secret
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    print(message)


def choose_greatest():
    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1  # need a value to return if 1 & 2 are equal

    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2

    print("El numero con valor The number with largest positive magnitude is "
          + str(greatest_value))

choose_greatest()

codificar(cc_secret1)
""" ¡¡ What you need !! """
decodificar()

print("FIN DE PROGRAMA CTF")
