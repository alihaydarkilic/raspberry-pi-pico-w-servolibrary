# Raspberry Pi Pico W için servo kütüphanesi v0.1 (Micropython)
Raspberry Pi Pico W için servo kütüphanesi

**Servo kütüphanesi versiyon 0.2'ye ve Robot kol kütüphanesine sürüm notlarından ulaşabilirsiniz.**
**You can find Servo library v0.2 and Robot arm library in the release notes.**

Thonyy ide ile main.py ve srv.py açarak kullanmaya başlayabilirsiniz. Eğer elinizde kart yoksa https://wokwi.com/projects/359149286284606465 linki bıraktığım simülasyon sitesinden testlerini gerçekleştirebilir, ve kütüphaneyi geliştirebilirsiniz. Umarım yardımcı olmuştur.

DİPNOT!! kütüphaneyi gerçek hayatta test ettiğimde harici +5V güç kaynağı ile servolara güç vererek test ettim. Raspberry Pi Pico W nin gücünün yetmediğini ve yapması gereken işlemleri tam yapamamasına neden oluyor. İmkanınız var iste ekstra bir güç kaynağı ile servoların güç beslemesini yapın.

Servo Library v0.1 for Raspberry Pi Pico W (Micropython)

You can start using the servo library for Raspberry Pi Pico W by opening main.py and srv.py with Thonyy IDE. If you don't have the device, you can perform tests and develop the library on the simulation site I provided at https://wokwi.com/projects/359149286284606465. I hope it helps.

NOTE: When I tested the library in real life, I powered the servos with an external +5V power supply. The Raspberry Pi Pico W's power is not enough and it can cause it to not perform its required operations properly. If possible, use an additional power supply to power the servos.
