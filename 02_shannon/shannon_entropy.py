import math
s= input("ad soyad giriniz:")

s=s.replace(" ","")

liste= []

for i in s :
     liste.append(i)

print(liste)
k= set(liste)
print(k)

d = {}

for i in k:
     adet = liste.count(i)
     oran=adet/len(liste)
     d.update({i:oran})
print(d)

shannon =0
for i in d:
     v = d[i]
     shannon += v*math.log(v,2)


shannon *=-1;
print("shannon eğer : " , shannon)



bs =math.ceil(shannon)#yukarı yuvarlama
print("bit sayısı:", bs)

dk  =list(k) #kümemizi liste haline tekrar ceviriyoruz



b = []
for i in range(int(math.pow(2,bs))):
    a = bin(i)[2:]
    b.append(a)
dk.sort()# dk kümemizi sıraladık
print(dk)
print(b)



for i in range(len(b)): #bite kaç sıfır eklenecek onu tamamlıyoruz
    #4-1=3 3 sıfır eklenecek 4-4=0  hiç eklenmeyecek döngü çalışmaz
    for j in range(bs-len(b[i])):
        b[i]= "0"+b[i]

print("0 eklenmiş hali:",b)




codec= ""    #ilgili harfin kodalaması için yazdık a için 000 vs.
for i in liste:
    codec += b[dk.index(i)]
print(codec)



