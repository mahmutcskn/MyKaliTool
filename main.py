#!/usr/bin/env python3

import os
import sys

# İşletim sistemi kontrolü ve gerekli kütüphaneleri yükleme
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    print("colorama kütüphanesi kurulu değil. Kurulum için: pip install colorama")
    sys.exit(1)

def clear_screen():
    """Ekranı temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Ana menüyü gösterir."""
    clear_screen()
    print(f"{Fore.CYAN}--- Kali Tool V1.0 ---")
    print(f"{Fore.GREEN}1. Selam ver")
    print(f"{Fore.GREEN}2. Nasılsın diye sor")
    print(f"{Fore.YELLOW}Yardım için 'help' yazın.")
    print(f"{Fore.RED}Çıkmak için 'exit' veya 'quit' yazın. (Veya Ctrl+C)")

def handle_input(choice):
    """Kullanıcı girdisine göre işlem yapar."""
    if choice == '1':
        clear_screen()
        print(f"{Fore.MAGENTA}{Style.BRIGHT}{'Selam Ver' : ^50}")
        print("\n\n")
        print("Merhaba, hoş geldin!")
        input("\nMenüye dönmek için Enter'a basın...")
    elif choice == '2':
        clear_screen()
        print(f"{Fore.MAGENTA}{Style.BRIGHT}{'Nasıl Olduğunu Sor' : ^50}")
        print("\n\n")
        print("Bugün nasılsın? Umarım her şey yolundadır.")
        input("\nMenüye dönmek için Enter'a basın...")
    elif choice.lower() in ['exit', 'quit']:
        print(f"{Fore.RED}Çıkış yapılıyor...")
        sys.exit(0)
    elif choice.lower() == 'help':
        show_menu()
    else:
        print(f"{Fore.RED}Geçersiz komut. Lütfen '1', '2' veya 'help' yazın.")

def main():
    """Programın ana döngüsü."""
    show_menu()
    
    # CTRL+C için sinyal yakalayıcı
    try:
        while True:
            choice = input(f"{Fore.CYAN}Komut > {Style.RESET_ALL}").strip()
            handle_input(choice)
            show_menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Programdan çıkış yapılıyor...")
        sys.exit(0)

if __name__ == "__main__":
    main()