# Shopping List CLI

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A simple command-line **shopping list** app written in Python, with a Persian (Farsi) interface. Products are saved to a local JSON file, so the list survives between runs.

> Persian version of this file: [README.fa.md](README.fa.md)

## Features

- Add products with their stock (count)
- Remove products (with a friendly message if the item does not exist)
- View the whole list
- Show a contact phone number (customizable via a variable)
- The list is saved to `shopping_list.json` automatically after every change
- Colored output with [colorama](https://pypi.org/project/colorama/) (the app still works if colorama is not installed)
- The menu loops until you choose `exit`
- Safe input handling (no crash on invalid input)

## Demo

```
برای شروع برنامه کلمه‌ی open رو بنویس: open
سلام! به برنامه لیست خرید خوش اومدی😊
─────────────────────────────
  Shopping List | لیست خرید
─────────────────────────────
1.add➕
2.remove➖
3.view all👁️‍🗨️
4.tel📞
5.exit
چه کاری برات انجام بدم؟: 1
نام محصول رو وارد کن💠: milk
موجودی محصول رو وارد کن💠: 2
«milk» با موجودی 2 اضافه شد😊
⌛
```

## Getting Started

```bash
git clone https://github.com/<username>/shopping-list-app.git
cd shopping-list-app
pip install -r requirements.txt
python shopping.py
```

Type `open` to start the menu, then choose an option between 1 and 5.

## Menu Options

| Option | Action |
| --- | --- |
| 1 | Add a product (name + stock) |
| 2 | Remove a product |
| 3 | View all products |
| 4 | Show contact phone number |
| 5 | Exit |

## Data Storage

The list is stored in `shopping_list.json` next to the script. The file is created automatically and is ignored by git (see `.gitignore`), so your personal data never gets committed.

## Customization

Set your own contact number in the `PHONE` variable at the top of `shopping.py`.

## License

Released under the [MIT License](LICENSE).
