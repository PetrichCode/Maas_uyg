maaslar = {}
menu = """
Maaş Programı
1- Maaş Ekle
2- Maaş Sil
3- Maaşlara Toplu Zam Yap
4- Maaşa Tekli Zam Yap
5- Maaşları Listele
6- Çıkış
"""
while True:
  print(menu)
  secim = input("Seçiminiz: ")
  if secim == "1":
    isim = input("İsim: ")
    maas = float(input("Maaş: "))
    maaslar[isim] = maas
    print(f"{isim} isimli kişinin {maas} TL maaşı eklendi.")
  elif secim == "2":
    isim = input("İsim: ")
    try:
      silinen_maas = maaslar.pop(isim)
      print(f"{isim} isimli kişinin {silinen_maas} TL maaşı silindi.")
    except KeyError:
      print(f"{isim} isimli kişi bulunamadı.")
  elif secim == "3":
    zam = float(input("Zam yüzdesi: "))
    for isim in maaslar:
      yeni_maas = maaslar[isim] * (1 + zam / 100)
      maaslar[isim] = yeni_maas
    print(f"Tüm maaşlara %{zam} zam yapıldı.")
  elif secim == "4":
    isim = input("İsim: ")
    zam = float(input("Zam yüzdesi: "))
    try:
      eski_maas = maaslar[isim]
      yeni_maas = eski_maas * (1 + zam / 100)
      maaslar[isim] = yeni_maas
      print(f"{isim} isimli kişinin {eski_maas} TL olan maaşı %{zam} zam ile {yeni_maas} TL oldu.")
    except KeyError:
      print(f"{isim} isimli kişi bulunamadı.")
  elif secim == "5":
    for isim, maas in maaslar.items():
      print(f"{isim}: {maas} TL")
  elif secim == "6":
    print("Programdan çıkılıyor...")
    break
  else:
    print("Geçersiz seçim. Lütfen 1-6 arasında bir sayı girin.")
