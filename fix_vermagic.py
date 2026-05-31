import sys
import re

ko_file = sys.argv[1]
new_ver = sys.argv[2].encode()

with open(ko_file, 'rb') as f:
    data = f.read()

match = re.search(b'vermagic=([^\x00]*)\x00', data)
if not match:
    print("vermagic not found!")
    sys.exit(1)

old_ver = match.group(1)
print(f"Old vermagic: {old_ver}")
print(f"New vermagic: {new_ver}")

if len(new_ver) > len(old_ver):
    print(f"ERROR: new vermagic too long! max={len(old_ver)} got={len(new_ver)}")
    sys.exit(1)

# 用新版本替换，不足部分补零
padded = new_ver + b'\x00' * (len(old_ver) - len(new_ver))
start = match.start(1)
end = match.end(1)
data = data[:start] + padded + data[end:]

with open(ko_file, 'wb') as f:
    f.write(data)
print("Done!")
