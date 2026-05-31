import sys

ko_file = sys.argv[1]
new_vermagic = sys.argv[2].encode()

with open(ko_file, 'rb') as f:
    data = f.read()

# 找到vermagic字段
import re
match = re.search(b'vermagic=([^\x00]+)\x00', data)
if match:
    old = match.group(0)
    old_ver = match.group(1)
    print(f"Found vermagic: {old_ver}")
    # 构造等长新字符串（不足补零）
    new = b'vermagic=' + new_vermagic + b'\x00' * (len(old) - len(b'vermagic=') - len(new_vermagic))
    if len(new) != len(old):
        print(f"Length mismatch: old={len(old)} new={len(new)}")
        sys.exit(1)
    data = data[:match.start()] + new + data[match.start()+len(old):]
    with open(ko_file, 'wb') as f:
        f.write(data)
    print(f"Done! New vermagic: {new_vermagic.decode()}")
else:
    print("vermagic not found!")
    sys.exit(1)
