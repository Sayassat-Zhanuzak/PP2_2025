import re
import csv

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

BINPattern = r"\nБИН\s(?P<BIN>[0-9]+)"
BINResult = re.search(BINPattern, text).group("BIN")
print(BINResult)

CheckPattern = r"\nЧек\s(?P<Check>№[0-9]+)"
CheckResult = re.search(CheckPattern, text).group("Check")
print(CheckResult)

ItemPattern = r"(?P<ItemRowNumber>\d+\.)\n(?P<ItemName>.*?)\n(?P<ItemsCount>.*?)\s*x\s*(?P<ItemPrice>.*?)\n(?P<TotalItemPrice1>.*?)\nСтоимость\n(?P<TotalItemPrice2>.*?)(?=\n\d+\.|\Z)"
prog = re.compile(ItemPattern, re.S)
items = prog.finditer(text)

with open('data.csv', 'w', newline='', encoding="utf8") as csvfile:
    fieldnames = ['ItemRowNumber', 'ItemName', 'ItemsCount', 'ItemPrice', 'TotalItemPrice1', 'TotalItemPrice2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in items:
        writer.writerow({
            "ItemRowNumber": item.group("ItemRowNumber").strip(),
            "ItemName": item.group("ItemName").strip(),
            "ItemsCount": item.group("ItemsCount").strip(),
            "ItemPrice": item.group("ItemPrice").strip(),
            "TotalItemPrice1": item.group("TotalItemPrice1").strip(),
            "TotalItemPrice2": item.group("TotalItemPrice2").strip()
        })

print("CSV file 'data.csv' created successfully!")

for item in prog.finditer(text):
    print(item.group("ItemRowNumber"), item.group("ItemName"))
