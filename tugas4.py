# ==========================================
# BLACK BOX TESTING
# Boundary Value Analysis
# dan State Transition Testing
# ==========================================

# ==========================================
# 1. Boundary Value Analysis
# ==========================================

def cek_nilai(nilai):
    if nilai < 0 or nilai > 100:
        return "Nilai Tidak Valid"
    elif nilai >= 75:
        return "A"
    elif nilai >= 60:
        return "B"
    elif nilai >= 40:
        return "C"
    else:
        return "D"


print("===== Boundary Value Analysis =====")

data_test = [-1, 0, 1, 99, 100, 101]

for nilai in data_test:
    hasil = cek_nilai(nilai)
    print(f"Input Nilai: {nilai} -> Grade: {hasil}")


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
