import re
import csv

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

ItemPattern = r"(?P<ItemRowNumber>\d+\.)\n(?P<ItemName>.*?)\n(?P<ItemsCount>.*?)\s*x\s*(?P<ItemPrice>.*?)\n(?P<TotalItemPrice1>.*?)\nСтоимость\n(?P<TotalItemPrice2>.*?)(?=\n\d+\.|\nБанковская карта:|\Z)"
prog = re.compile(ItemPattern, re.S)
items = prog.finditer(text)

with open('data.csv', 'w', newline='', encoding="utf8") as csvfile:
    fieldnames = ['Номер', 'Наименование', 'Количество', 'Цена за единицу', 'Стоимость', 'Итого']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in items:
        writer.writerow({
            "Номер": item.group("ItemRowNumber").strip(),
            "Наименование": item.group("ItemName").strip(),
            "Количество": item.group("ItemsCount").strip(),
            "Цена за единицу": item.group("ItemPrice").strip(),
            "Стоимость": item.group("TotalItemPrice1").strip(),
            "Итого": item.group("TotalItemPrice2").strip()
        })

print("CSV file 'data.csv' created successfully!")

for item in prog.finditer(text):
    print(item.group("ItemRowNumber"), item.group("ItemName"))
