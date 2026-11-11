#!/usr/bin/env python3
"""
Shopping List — برنامه‌ی لیست خرید تحت خط فرمان (CLI)
A simple command-line shopping list app written in Python.

اجرا / Run:  python shopping.py
برای شروع، کلمه‌ی open را وارد کن.
"""

import json
from pathlib import Path
from time import sleep

# ---------- رنگ‌ها (colorama) ----------
try:
    from colorama import Fore, Style, init as _colorama_init
    _colorama_init(autoreset=True)
except ImportError:  # اگر colorama نصب نبود، برنامه بدون رنگ کار می‌کند
    class _NoColor:
        def __getattr__(self, name):
            return ""
    Fore = _NoColor()
    Style = _NoColor()

GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
BRIGHT = Style.BRIGHT

# ---------- تنظیمات ----------
PHONE = "09923296030"  # شماره‌ای که در گزینه‌ی ۴ نمایش داده می‌شود
DATA_FILE = Path(__file__).with_name("shopping_list.json")  # محل ذخیره‌ی لیست

shopping_dict = {}  # لیست خرید: {نام محصول: موجودی}


def load_list():
    """خواندن لیست خرید از فایل (اگر از قبل وجود داشته باشد)."""
    global shopping_dict
    if DATA_FILE.exists():
        try:
            shopping_dict = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            shopping_dict = {}
            print(RED + "فایل ذخیره‌سازی خراب بود؛ لیست خالی ساخته شد🤔")


def save_list():
    """ذخیره‌ی لیست خرید در فایل JSON."""
    try:
        DATA_FILE.write_text(
            json.dumps(shopping_dict, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError:
        print(RED + "ذخیره‌سازی انجام نشد🤔")


def show_menu():
    print(CYAN + "─────────────────────────────")
    print(BRIGHT + "  Shopping List | لیست خرید")
    print(CYAN + "─────────────────────────────")
    print("1.add➕")
    print("2.remove➖")
    print("3.view all👁️‍🗨️")
    print("4.tel📞")
    print("5.exit")


def get_choice():
    """خواندن انتخاب کاربر؛ فقط عدد ۱ تا ۵ قبول است."""
    raw = input("چه کاری برات انجام بدم؟: ").strip()
    if not raw.isdigit() or not 1 <= int(raw) <= 5:
        print(RED + "عدد رو اشتباه وارد کردی🤔")
        return None
    return int(raw)


def add_product():
    name = input("نام محصول رو وارد کن💠: ").strip()
    if not name:
        print(RED + "اسم محصول نمی‌تونه خالی باشه🤔")
        return
    stock = input("موجودی محصول رو وارد کن💠: ").strip()
    if not stock.isdigit():
        print(RED + "موجودی باید یک عدد باشه🤔")
        return
    shopping_dict[name] = int(stock)
    save_list()
    print(GREEN + f"«{name}» با موجودی {stock} اضافه شد😊")


def remove_product():
    name = input("نام محصول رو وارد کن💠: ").strip()
    if name not in shopping_dict:
        print(RED + "کالا وجود نداشت🤔")
    else:
        del shopping_dict[name]
        save_list()
        print(GREEN + "انجام شد😊")


def view_products():
    if not shopping_dict:
        print(YELLOW + "لیست خرید خالیه🤔")
        return
    print(BRIGHT + "لیست خریدت:")
    for name, stock in shopping_dict.items():
        print(f"  • {name}: {stock}")


def show_tel():
    print(GREEN + f"شماره تماس: {PHONE}")


def shopping():
    """حلقه‌ی اصلی برنامه."""
    load_list()
    print(BRIGHT + "سلام! به برنامه لیست خرید خوش اومدی😊")
    while True:
        show_menu()
        num = get_choice()
        if num is None:
            continue
        if num == 1:
            add_product()
        elif num == 2:
            remove_product()
        elif num == 3:
            view_products()
        elif num == 4:
            show_tel()
        else:  # خروج
            break
        print(YELLOW + "⌛")
        sleep(2)
    print(BRIGHT + "فعلاً! بدرود😊")


def main():
    word = input("برای شروع برنامه کلمه‌ی open رو بنویس: ").strip().lower()
    if word == "open":
        shopping()
    else:
        print(RED + "برای شروع باید کلمه‌ی open رو بنویسی🤔")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + YELLOW + "برنامه بسته شد😊")
