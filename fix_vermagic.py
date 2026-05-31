import sys

ko_file = sys.argv[1]
old_vermagic = sys.argv[2].encode()
new_vermagic = sys.argv[3].encode()

with open(ko_file, 'rb') as f:
    data = f.read()

if old_vermagic in data:
    data = data.replace(old_vermagic, new_vermagic, 1)
    with open(ko_file, 'wb') as f:
        f.write(data)
    print(f"Replaced: {old_vermagic} -> {new_vermagic}")
else:
    print(f"Not found: {old_vermagic}")
    # 搜索现有vermagic
    import re
    matches = re.findall(b'vermagic=([^\x00]+)', data)
    for m in matches:
        print(f"Found vermagic: {m}")
