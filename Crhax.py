import requests

def create_account(username, password, email):
    url = "https://craftrise.com/register"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
    }
    data = {
        "username": username,
        "password": password,
        "email": email
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        print("Hesap başarıyla oluşturuldu!")
    else:
        print("Hesap oluşturulurken bir hata oluştu.")

# Hesap bilgilerini gir
username = "azerbaijan_termux"
password = "sifre123"
email = "azerbaijan.termux@example.com"

# Hesap oluşturma işlemini başlat
create_account(username, password, email)
