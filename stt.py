# ==========================================
# 2. State Transition Testing
# ==========================================

print("\n===== State Transition Testing =====")

password_benar = "admin123"
percobaan = 0

while percobaan < 3:
    password = input("Masukkan Password: ")

    if password == password_benar:
        print("Login Berhasil")
        break
    else:
        percobaan += 1
        print(f"Password Salah ({percobaan}x)")

if percobaan == 3:
    print("Akun Terkunci")
