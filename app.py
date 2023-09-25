import math
import uuid

num = math.factorial(52)

print(f"{num=:e}")

num = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print(f"{num=}")
