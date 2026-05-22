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
