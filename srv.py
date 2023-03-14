 
"""
 ~~ Raspberry Pi Pico W servo kütüphanesi projesi v0.1
                                                        by Ali Haydar Kilic ~~ 
      
        """


from machine import Pin, PWM

 
class Servo:
    
    def __init__ (self, pin:int, fre:int, aciMin:int, aciMax:int, servoMinDeg:int, servoMaxDeg:int,durum=False):  
            
            """
            PWM nesnesini başlattığımız bölüm. 

            #argüman açıklaması
            #pin: Servoyu süreceğimiz gpio pin numarasını yazacağımız argüman.
            #fre: frekans ayarı yapabilmemizi sağlayan argüman.
            #aciMin: Servo motorun minimum açısı.(Genellikle servolar 0-180 derece arasında olurlar ama 120 veya 360 derecelik servolar da bulunmakta)
            #aciMax: Servo motorun maksimum açısı.
            #servoMinDeg: Servonun minimum açı değerinin karşılığı olan değer.
            #servoMinDeg: Servonun maksimum açı değerinin karşılığı olan değer.(Genelde 1350-7500 arasıdır servodan servoya değişkenlik gösterebilir!!)
            #durum: Hata yakalamak için konulmuş argüman. (Henüz çokta efektif bir hata yakalama performansı göstermiyor.)
             """
            
            if isinstance(pin, int):
                pin = Pin(pin, Pin.OUT)
            if isinstance(pin, Pin):
                self.__pwm = PWM(pin)
                self.durum=True
            if self.durum==True:
                self.__pwm.freq(fre)   
                self.aciMin=aciMin      
                self.aciMax=aciMax   
                self.servoMinDeg=servoMinDeg     
                self.servoMaxDeg=servoMaxDeg
            else:  
                self.deinit()
    def deinit(self):
        """ PWM nesnesini iptal etmek için kullandığımız fonksiyon
 
         """
        self.__pwm.deinit()

    def aciGit(self, hedefAci:int):
        """ Servoyu belirlenen açıya götürür

        args:
        #hedefAci(int): Minimum açı ile Maksimum açı (dahil) arasında bir açı değerine taşınacak konum.
        
         """
        
        if hedefAci<self.aciMin:
            hedefAci=self.aciMin
        if hedefAci>self.aciMax:
            hedefAci=self.aciMax
        
        hedefDeg=int(self.servoMinDeg+((hedefAci*self.servoMaxDeg)/self.aciMax))
        self.__pwm.duty_u16(hedefDeg)

    def orta(self):
        """ Servoyu ortaya taşır.
         """
        self.aciGit(90)    
    
    def dutyFree(self):
        """ Servonun serbestçe hareket etmesine izin verir.
         """
        self.__pwm.duty_u16(0)
