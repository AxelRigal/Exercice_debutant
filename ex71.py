import random

list = [str(random.randint(0,1)) for octet in range(8)]
print("".join(list))
