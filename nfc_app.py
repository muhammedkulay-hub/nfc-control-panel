import json
import os
import time

class NFCControlPanel:
    def __init__(self):
        self.cards_file = "nfc_cards.json"
        self.cards = self.load_cards()
    
    def load_cards(self):
        if os.path.exists(self.cards_file):
            with open(self.cards_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_cards(self):
        with open(self.cards_file, 'w') as f:
            json.dump(self.cards, f, indent=4)
    
    def add_card(self):
        name = input("Kart Adı: ")
        card_type = input("Kart Türü (Ev/Araç/Banka): ")
        uid = input("Kart ID: ")
        
        card = {
            "name": name,
            "type": card_type,
            "uid": uid,
            "active": True
        }
        self.cards.append(card)
        self.save_cards()
        print("✅ Kart eklendi!")
    
    def list_cards(self):
        print("\n📋 KART LİSTESİ:")
        for i, card in enumerate(self.cards, 1):
            status = "🟢" if card["active"] else "🔴"
            print(f"{i}. {card['name']} ({card['type']}) {status}")
    
    def show_menu(self):
        print("\n🔷 NFC CONTROL PANEL 🔷")
        print("1. Kart Ekle")
        print("2. Kartları Listele") 
        print("3. Çıkış")
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Seçim: ")
            
            if choice == "1":
                self.add_card()
            elif choice == "2":
                self.list_cards()
            elif choice == "3":
                print("👋 Güle güle!")
                break
            else:
                print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    app = NFCControlPanel()
    app.run()
