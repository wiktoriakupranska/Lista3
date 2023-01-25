import base64

def encrypt_base64(text: str) -> str:
    zaszyfrowany_tekst = base64.b64encode(text.encode())
    return zaszyfrowany_tekst.decode()

def decrypt_base64(zaszyfrowany_tekst: str) -> str:
    odszyfrowany_tekst = base64.b64decode(zaszyfrowany_tekst.encode()).decode()
    return odszyfrowany_tekst

oryginalny_tekst = "Jeszcze troche i licencjat bede miala w kieszeni"
zaszyfrowany_tekst = encrypt_base64(oryginalny_tekst)
odszyfrowany_tekst = decrypt_base64(zaszyfrowany_tekst)

print("Oryginalny tekst:", oryginalny_tekst)
print("Zaszyfrowany tekst:", zaszyfrowany_tekst)
print("Odszyfrowany tekst:", odszyfrowany_tekst)

#kod pisany w Visual Studio Code; działanie sprawdzone również na stronie https://replit.com/languages/python3
