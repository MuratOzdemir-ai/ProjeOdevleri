import random
import tkinter as tk
from tkinter import messagebox, font
import time

english_questions = {
    "DO": "yapmak",
    "GO": "gitmek",
    "COME": "gelmek",
    "SEE": "görmek",
    "HEAR": "duymak",
    "SPEAK": "konuşmak",
    "WRITE": "yazmak",
    "READ": "okumak",
    "WORK": "çalışmak",
    "PLAY": "oynamak",
    "DRINK": "içmek",
    "EAT": "yemek",
    "TAKE": "almak",
    "GIVE": "vermek",
    "WAIT": "beklemek",
    "FIND": "bulmak",
    "SELL": "satmak",
    "CLOSE": "kapatmak",
    "OPEN": "açmak",
    "START": "başlamak",
    "FINISH": "bitirmek",
    "CHOOSE": "seçmek",
    "LEARN": "öğrenmek",
    "TEACH": "öğretmek",
    "ENTER": "girmek",
    "EXIT": "çıkmak",
    "MOVE": "hareket etmek",
    "WALK": "yürümek",
    "RUN": "koşmak",
    "FLY": "uçmak",
    "JUMP": "atlamak",
    "SWIM": "yüzmek",
    "SLEEP": "uyumak",
    "WAKE UP": "uyandırmak",
    "LAUGH": "gülmek",
    "CRY": "ağlamak",
    "LOVE": "sevmek",
    "HATE": "nefret etmek",
    "JOIN": "katılmak",
    "DRAW": "çizmek",
    "DESIGN": "tasarlamak",
    "DEVELOP": "geliştirmek",
    "SENSE": "sezmek",
    "RECOGNIZE": "tanımak",
    "CHANGE": "değişmek",
    "COMPLETE": "tamamlamak",
    "CONDITION": "şart etmek",
    "MEET": "görüşmek",
    "TALK": "konuşmak",
    "REPEAT": "tekrar etmek",
    "IMAGINE": "hayal etmek",
    "CREATE": "yaratmak",
    "TASTE": "tatmak",
    "FEEL": "hissetmek",
    "INDICATE": "belirtmek",
    "SHARE": "paylaşmak",
    "TRUST": "güvenmek",
    "RUN AWAY": "kaçmak",
    "RISE": "yükselmek",
    "DECREASE": "azalmak",
    "INCREASE": "artmak",
    "SOLVE": "çözmek",
    "TRY": "denemek",
    "SUCCEED": "başarmak",
    "ENDURE": "katlanmak",
    "MISS": "özlemek",
    "UNDERSTAND": "anlamak",
    "REMEMBER": "hatırlamak",
    "FORGET": "unutmak",
    "JOKE": "şaka yapmak",
    "STRENGTHEN": "güçlendirmek",
    "WEAKEN": "zayıflatmak",
    "CONNECT": "bağlamak",
    "CUT OFF": "koparmak",
    "ACCUMULATE": "biriktirmek",
    "LIE DOWN": "yatmak",
    "SELECT": "seçmek",
    "RUN (A PROGRAM)": "çalıştırmak",
    "CONDUCT": "yürütmek",
    "SET UP": "kurmak",
    "GUESS": "tahmin etmek",
    "DETERMINE": "belirlemek",
    "SUGGEST": "önermek",
    "CALM": "yatıştırmak",
    "PRIORITIZE": "öncelik vermek",
    "DISTRIBUTE": "dağıtmak",
    "IDENTIFY": "belirlemek",
    "CLEAN": "temizlemek",
    "EMPOWER": "güçlendirmek",
    "ENCOURAGE": "teşvik etmek",
    "ESTABLISH": "temel oluşturmak",
    "SUPERVISE": "denetlemek",
    "IMPROVE": "geliştirmek",
    "REPAIR": "onarmak",
    "PROTECT": "korumak",
    "CONTRIBUTE": "katkıda bulunmak",
    "PLAN": "planlamak",
    "PROJECT": "proje yapmak",
    "INFLUENCE": "etkileyebilmek"
}

# Soruları karıştır
word_items = list(english_questions.items())
random.shuffle(word_items)

# Sadece ilk 15 soruyu al
word_items = word_items[:15]

# Puanlar
score_player1 = 0
score_player2 = 0
question_index = 0
time_limit = 15  # Her soru için süre (saniye)
current_player = 1  # Hangi oyuncunun sırada olduğunu takip et
timer = time_limit  # Timer değişkenini burada tanımladık

# Tkinter penceresi oluştur
root = tk.Tk()
root.title("Çiftli Quiz Oyunu")
root.configure(bg="#2E2E2E")

# Modern yazı tipleri
header_font = font.Font(family="Helvetica", size=20, weight="bold")
question_font = font.Font(family="Helvetica", size=16)
entry_font = font.Font(family="Helvetica", size=14)

# Oyuncu penceresini oluştur
question_label = tk.Label(root, text="", font=header_font, fg="white", bg="#2E2E2E")
question_label.pack(pady=20)

answer_entry = tk.Entry(root, font=entry_font)
answer_entry.pack(pady=10)

result_label = tk.Label(root, text="", font=question_font, fg="white", bg="#2E2E2E")
result_label.pack(pady=10)

score_label = tk.Label(root, text="", font=question_font, fg="white", bg="#2E2E2E")
score_label.pack(pady=10)

timer_label = tk.Label(root, text="", font=question_font, fg="white", bg="#2E2E2E")
timer_label.pack(pady=10)

# Soru sorma ve cevabı kontrol etme fonksiyonları
def update_score():
    score_label.config(text=f"Oyuncu 1: {score_player1} | Oyuncu 2: {score_player2}")

def ask_question():
    global question_index, current_player
    if question_index < len(word_items):
        question_label.config(text=word_items[question_index][0])
        answer_entry.delete(0, tk.END)
        result_label.config(text="")
        global timer
        timer = time_limit
        timer_label.config(text=f"Kalan Süre: {timer} saniye")
        update_timer()
    else:
        if current_player == 1:
            current_player = 2
            question_index = 0  # Soruları sıfırla
            result_label.config(text="Oyuncu 1'in soruları bitti, Oyuncu 2'nin sırası!")
            root.after(2000, ask_question)  # 2 saniye bekleyin
        else:
            end_game()  # Her iki oyuncunun soruları bittiğinde oyunu bitir

def check_answer(event=None):
    global question_index, current_player
    user_answer = answer_entry.get().strip().lower()
    correct_answer = word_items[question_index][1]

    if user_answer == correct_answer.lower():
        if current_player == 1:
            global score_player1
            score_player1 += 1
        else:
            global score_player2
            score_player2 += 1
        result_label.config(text="Tebrikler Doğru!")
    else:
        result_label.config(text=f"!Yanlış! Doğru Cevap: * {correct_answer} *")

    update_score()
    question_index += 1
    ask_question()

def update_timer():
    global timer
    if timer > 0:
        timer -= 1
        timer_label.config(text=f"Kalan Süre: {timer} saniye")
        root.after(1000, update_timer)
    else:
        result_label.config(text="!Süre Doldu!")
        question_index += 1
        ask_question()

# Oyuncu için "Kontrol Et" butonunu oluştur
check_button = tk.Button(root, text="Kontrol Et", command=check_answer, font=entry_font, bg="#4CAF50", fg="white")
check_button.pack(pady=20)

# "Enter" tuşuyla cevap kontrolü
answer_entry.bind("<Return>", check_answer)

# İlk soruyu sor
ask_question()

# Oyun sona erme fonksiyonu
# Oyun sona erme fonksiyonu
# Oyun sona erme fonksiyonu
def end_game():
    global result_label, winner  # Kazananı tutmak için winner değişkenini global yap
    # Kazananı belirleme
    if score_player1 > score_player2:
        winner = "🎉 Oyuncu 1 Kazandı! 🎉"
        result_color = "green"
    elif score_player1 < score_player2:
        winner = "🎉 Oyuncu 2 Kazandı! 🎉"
        result_color = "blue"
    else:
        winner = "🚀 Beraberlik! 🚀"
        result_color = "orange"

    # Sonuçları ekranda göster ve sabit tut
    result_text = f"{winner}\n\n" \
                  f"💡 Toplam Puanlar:\n" \
                  f"🏆 Oyuncu 1: {score_player1}\n" \
                  f"🏆 Oyuncu 2: {score_player2}\n\n" \
                  f"📅 Oyun Bitti! İstersen yeni bir oyun başlatabilirsin."

    result_label.config(text=result_text, fg=result_color, font=("Helvetica", 14, "bold"))
    result_label.pack(pady=20)  # Sonuçları sabit tutmak için tekrar paketi açın

    # Yeniden başlama butonu ekleyelim
    restart_button = tk.Button(root, text="Yeni Oyun Başlat", command=restart_game, font=("Helvetica", 12),
                               bg="#4CAF50", fg="white")
    restart_button.pack(pady=10)

    # Sonucu tekrar gör butonu ekleyelim
    show_result_button = tk.Button(root, text="Sonucu Tekrar Gör", command=show_result, font=("Helvetica", 12),
                                   bg="#2196F3", fg="white")
    show_result_button.pack(pady=10)

# Sonucu gösterme fonksiyonu
def show_result():
    global result_label
    result_text = f"{winner}\n" \
                  f"🏆 Oyuncu 1: {score_player1}\n" \
                  f"🏆 Oyuncu 2: {score_player2}\n" \
                  f"📅 Oyun Bitti!"
    result_label.config(text=result_text, fg="black", font=("Helvetica", 14, "bold"))
    result_label.pack(pady=20)

# Oyun yeniden başlatma fonksiyonu
def restart_game():
    global score_player1, score_player2, question_index, current_player
    score_player1 = 0
    score_player2 = 0
    question_index = 0
    current_player = 1
    result_label.config(text="")
    update_score()
    ask_question()  # İlk soruyu sor

# Tkinter ana döngüsünü başlat
root.mainloop()