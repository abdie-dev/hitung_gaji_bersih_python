"""VERSI MANDIRI"""

# """Aplikasi CLI hitung gaji bersih karyawan"""
#
# # Karyawan :
# # 1. Kasir
# # 2. Non Kasir
#
#
# def jobdesc():
#     """input Jobdesc karyawan, gaji kotor, potongan, potongan kasir"""
#     jobdesc = input(
#         "Apakah kamu kasir (y/n) : "
#     ).lower()  # .lower untuk mengubah input menjadi huruf kecil
#
#     """berupa float karna mata uang"""
#     gaji_kotor = float(input("Masukkan gaji kotor: "))
#     potongan = float(input("Masukkan potongan: "))
#     ks = input("Masukkan potongan kasir (jika ada, masukkan 0 jika non kasir): ")
#
#     if ks == "":
#         ks = 0
#     else:
#         ks = float(ks)
#
#     """ logika / rumus pengurangan gaji karyawan berdasarkan Jobdesc.
#     gunakan ini menggunakan format jutaan jadi misal kamu input 3100, maka outputnya 3,100,000"""
#
#     if jobdesc == "y":
#         # gaji_kotor, potongan, ks = gaji_kotor, potongan, ks * 1000
#         gaji_bersih = gaji_kotor - (potongan + ks)
#         format_rupiah_bersih = "Rp {:,.2f}".format(gaji_bersih * 1000)
#         print("gaji bersih kasir adalah :", format_rupiah_bersih)
#     elif jobdesc == "n":
#         # gaji_kotor, potongan, ks = gaji_kotor, potongan, ks * 1000
#         gaji_bersih = gaji_kotor - potongan
#         format_rupiah_bersih = "Rp {:,.2f}".format(gaji_bersih * 1000)
#         print("gaji bersih non kasir adalah :", format_rupiah_bersih)
#     else:
#         print("Jobdesc tidak valid. Silakan masukkan 'kasir' atau 'non kasir'.")
#
#
# jobdesc()

"""Versi QWEN.AI"""

#
# """Aplikasi CLI hitung gaji bersih karyawan"""
#
#
# def hitung_gaji():
#     """Hitung gaji bersih berdasarkan jabatan (kasir/non-kasir)."""
#     jabatan = input("Apakah kamu kasir? (y/n): ").strip().lower()
#
#     if jabatan not in ("y", "n"):
#         print("Input tidak valid. Harap masukkan 'y' atau 'n'.")
#         return
#
#     try:
#         gaji_kotor = float(input("Masukkan gaji kotor (dalam ribuan): "))
#         potongan = float(input("Masukkan potongan (dalam ribuan): "))
#
#         if jabatan == "y":
#             potongan_kasir = input(
#                 "Masukkan potongan khusus kasir (dalam ribuan, tekan Enter jika 0): "
#             ).strip()
#             potongan_kasir = float(potongan_kasir) if potongan_kasir else 0.0
#             total_potongan = potongan + potongan_kasir  # <-- ini logika yang benar!
#         else:
#             total_potongan = potongan
#
#         gaji_bersih = gaji_kotor - total_potongan
#         if gaji_bersih < 0:
#             print("⚠️  Peringatan: Gaji bersih negatif! Cek ulang data.")
#             gaji_bersih = 0
#
#         # Format ke Rupiah (dalam satuan penuh, bukan ribuan)
#         format_rupiah = f"Rp {gaji_bersih * 1_000:,.0f}"
#         jabatan_str = "kasir" if jabatan == "y" else "non-kasir"
#         print(f"Gaji bersih {jabatan_str}: {format_rupiah}")
#
#     except ValueError:
#         print(
#             "❌ Error: Pastikan angka yang dimasukkan valid (gunakan titik untuk desimal)."
#         )
#
#
# # Jalankan
# if __name__ == "__main__":
#     hitung_gaji()

