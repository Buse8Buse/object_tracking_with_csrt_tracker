#Video karelerini ayıklayıp kaydediyorum.

import cv2
goruntu = cv2.VideoCapture('Test_2.mp4')

#Şimdi bir CSRT Tracker yaratıyorum.
tracker = cv2.TrackerCSRT_create()
#Görüntüyü ekranda göstermek için aşağıdaki kodu çalıştırıyorum.
success, foto = goruntu.read()

#BBOX parametresi, çıktı verinin içinde bulunduğu çerçeveyi ifade eder.(Bounding box)

#selectROI() işlevi, bize görüntüyü otomatik olarak gösterir ve görüntüdeki ROI'yi manuel olarak seçmemize izin verir.

#!!!!!!!!!!!!!!! ROI'yi seçtikten sonra, seçilen alana ilerlemek için boşluk düğmesine basmamız veya girmemiz gerekiyor !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#tek bir bounding box oluşturmada cv2.selectROI'nin son parametresinin False olması önemlidi.
bbox = cv2.selectROI("Takip ediliyor.",foto,False)
tracker.init(foto,bbox)

#Dörtgen şeklinde bir kutu belirlenir ve sunucudan bu kutu içerine düşen veriler istenir.Çerçeve sınırları minX, minyY maxX, MaxY şeklinde belirlenir.
def drawBox(foto,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(foto,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(foto, "Takip ediliyor.", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),3)

while True:
    #cv2.getTickCount(),bir referans olaydan sonra (makinenin açıldığı an gibi) bu işlevin çağrıldığı ana kadar saat çevrimlerinin sayısıdır.
    #cv2.getTickFrequency(),saat çevrimlerinin sıklığını veya saniyedeki saat çevrimlerinin sayısını döndürür .

    #burada zamanlayıcı ayarlaması yapıldı.
    timer = cv2.getTickCount()

    #burada tracker algılanması için
    success, foto = goruntu.read()

    success,bbox = tracker.update(foto)
    #print(type(bbox))
    print(bbox)

    if success:
        drawBox(foto,bbox)
    else:
        cv2.putText(foto,"Nesne Kayboldu.",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    #saniye başına düşen görüntü sayısını hesaplamak için gerekli ayarlamaları yapıyorum.
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)

    #putText ile görüntü üzerine yazı yazılır.
    #Bu fonksiyona parametre olarak yazdırılacak yazı, yazının başlayacağı koordinat, font bilgisi, renk ve kalınlık değerleri aşağıdadır.

    #Burada görüntü boyut-font-RGB uzayı vs. ayarlamaları ve en son parametrede de yazı kalınlığı ayarlaması yapılır.
    cv2.putText(foto,str(int(fps)),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    #Burada video kestinde çerçeve içine aldığımız görüntünün video oynatıldığında takip edilip "Takipçi" yazısıyla gösterilmesini gerçekleştireceğiz.
    cv2.imshow("Takipçi",foto)

    #cv2.waitKey(1)o anda basılan tuşun karakter kodunu ve herhangi bir tuşa basılmazsa -1'i döndürür.
    #tek bayt olmayan bir kod döndüreceğinden & 0xFF,anahtarın yalnızca tek baytlık (ASCII) temsilinin kalmasını sağlamak için ikili bir VE işlemidir .
        # her zaman 'q'nun 113 olan (onaltılık olarak 0x71) ASCII temsilini döndürür
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
