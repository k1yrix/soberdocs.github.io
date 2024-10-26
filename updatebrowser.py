import os

fileList = os.listdir("docs/")

with open("md/listTemplate.md", "r") as f:
    template = f.read()

with open("md/filelist.md", "w") as f:
    f.write(f"{template}\n")

for i in fileList:
    with open("md/filelist.md", "a") as f:
        f.write(f"# [{i.removesuffix(".html")}](../docs/{i})\n")