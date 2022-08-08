# http://www.pythonchallenge.com/pc/def/channel.html
# 压缩包里有readme.txt
#!/usr/bin/env/ python3

#!/usr/bin/env/ python3

import zipfile
import re

infile = "L06/channel.zip"

# 使用 zipfile 包解压并读取文件内容到 files
files = {}
fzip = zipfile.ZipFile(infile)
for name in fzip.namelist():
    with fzip.open(name) as f:
        files[name] = f.read().decode("utf-8")

# readme.txt 中 nothing 初始值
nothing = "90052"

while True:
    f = nothing + ".txt"
    # 获取 comment 并输出结果
    print(fzip.getinfo(f).comment.decode("utf-8"), end="")
    if f in files:
        # print(files[f])
        result = re.search(r"Next nothing is (\d+)", files[f])
        try:
            nothing = result.group(1)
        except:
            break
