sayilar = []

print("Lutfen sayilari girin (islem bitince -1 giriniz)")
while True:
    girdi = int(input('Sayi: '))
    if girdi != -1:
        sayilar.append(girdi)
    else:
        break

print(f"Listenin ilk hali: {sayilar}")
for i in range(len(sayilar)):
    if sayilar[i] == 0:
        sayilar.insert(0, sayilar.pop(i))
print(f"Listenin son hali: {sayilar}")