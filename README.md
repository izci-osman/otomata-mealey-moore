# 💡 Mealy ve Moore Makinesi Simülasyonu

Bu proje, klasik otomata teorisinde yer alan **Mealy** ve **Moore** makinelerinin çalışma prensiplerini simüle etmek amacıyla geliştirilmiştir. Python ile yazılmıştır ve kullanıcıdan alınan giriş dizisine göre durum geçişlerini ve çıktıları hesaplar.

## 🚀 Özellikler

- Mealy makinesi simülasyonu (durum + giriş → çıkış)
- Moore makinesi simülasyonu (yalnızca durum → çıkış)
- Dosya üzerinden durumlar, alfabe ve geçiş tabloları okuma
- Komut satırından giriş alarak çalıştırma

## 📂 Dosya Yapısı

- `mealy_machine_simulation.py`: Mealy makinesi simülasyon kodu
- `moore_machine_simulation.py`: Moore makinesi simülasyon kodu 
- `INPUT.TXT`: Durum kümesi, giriş ve çıkış alfabesi
- `GECISDIYAGRAMI.TXT`: Geçiş ve çıkış tablosu

## 🛠️ Kullanım

```bash
# Proje klasörüne geç
cd proje-klasoru

# Python scriptini çalıştır
python mealy_machine_simulation.py
