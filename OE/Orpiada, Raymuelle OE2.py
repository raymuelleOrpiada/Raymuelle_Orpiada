class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand}, {self.model}, {self.price}"

def add_phone(phone_list):
    phone_list.append(Phone(input("Brand: "), input("Model: "), input("Price: ")))

def modify_phone(phone_list):
    list_phones(phone_list)
    i = int(input("Select phone (number): ")) - 1
    if 0 <= i < sum(1 for _ in phone_list):
        phone = phone_list[i]
        phone.brand = input(f"Brand ({phone.brand}): ") or phone.brand
        phone.model = input(f"Model ({phone.model}): ") or phone.model
        phone.price = input(f"Price ({phone.price}): ") or phone.price

def delete_phone(phone_list):
    list_phones(phone_list)
    i = int(input("Select phone (number): ")) - 1
    if 0 <= i < sum(1 for _ in phone_list):
        phone_list.pop(i)

def list_phones(phone_list):
    for i, phone in enumerate(phone_list, 1):
        print(f"{i}. {phone}")

def main():
    phone_list = []
    while True:
        choice = input("\n1. Add\n2. Modify\n3. Delete\n4. List\n5. Exit\nChoice: ")
        if choice == "1": add_phone(phone_list)
        elif choice == "2": modify_phone(phone_list)
        elif choice == "3": delete_phone(phone_list)
        elif choice == "4": list_phones(phone_list)
        elif choice == "5": break
if __name__ == "__main__": main()
