import time
import datetime

# Engellenecek siteler
blocked_sites = ["www.facebook.com", "www.youtube.com"]
# Engelleme saatleri
start_time = "9:00"  # Engellemeye başlayacak saat
end_time = "17:00"  # Engellemeyi bitirecek saat
# Hosts dosyasının yolu
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

while True:
    # Şu anki zaman
    current_time = datetime.datetime.now().strftime("%H:%M")

    # Engelleme zamanları arasında mı?
    if start_time < current_time < end_time:
        # Hosts dosyasına ekleme
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in blocked_sites:
                if site not in content:
                    file.write(redirect + " " + site + "\n")
    else:
        # Hosts dosyasından kaldırma
        with open(hosts_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(site in line for site in blocked_sites):
                    file.write(line)
            file.truncate()  # Dosyanın sonunu kes

    time.sleep(60)  # 1 dakika bekle

