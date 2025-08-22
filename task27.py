pul = 38500

num_integer = pul // 10000          # 3 ta 10000
num_remainder = pul % 10000         # 8500 qoldiq

num_integer2 = num_remainder // 5000   # 1 ta 5000
num_remainder2 = num_remainder % 5000  # 3500 qoldiq

num_integer3 = num_remainder2 // 2000  # 1 ta 2000
num_remainder3 = num_remainder2 % 2000 # 1500 qoldiq

num_integer4 = num_remainder3 // 500   # 3 ta 500

print(f"{num_integer} dona 10000 so‘mlik, {num_integer2} dona 5000 so‘mlik, {num_integer3} dona 2000 so‘mlik, {num_integer4} dona 500 so‘mlik")
