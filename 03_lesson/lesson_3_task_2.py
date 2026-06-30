from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79123456789"),
    Smartphone("Samsung", "Galaxy S24", "+79223456789"),
    Smartphone("Xiaomi", "Mi 14", "+79323456789"),
    Smartphone("Google", "Pixel 8", "+79423456789"),
    Smartphone("OnePlus", "12", "+79523456789")
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
