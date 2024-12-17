# استيراد المكتبات اللازمة
import RPi.GPIO as GPIO  # مكتبة للتحكم بدبابيس GPIO
import time             # مكتبة للتعامل مع الزمن

# إعداد دبابيس GPIO
motor_pin = 18  # دبوس التحكم بالمحرك
button_pin = 17 # دبوس الزر

# إعدادات GPIO
GPIO.setmode(GPIO.BCM)  # استخدام الترقيم وفقًا لـ Broadcom
GPIO.setup(motor_pin, GPIO.OUT)  # ضبط دبوس المحرك كمخرج
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # ضبط دبوس الزر كمدخل مع مقاومة Pull-Up

# متغير لتتبع حالة المحرك
motor_state = False

# وظيفة لتبديل حالة المحرك
def toggle_motor(channel):
    global motor_state
    motor_state = not motor_state  # تبديل الحالة (ON/OFF)
    if motor_state:
        GPIO.output(motor_pin, GPIO.HIGH)  # تشغيل المحرك
        print("Motor ON")
    else:
        GPIO.output(motor_pin, GPIO.LOW)  # إيقاف المحرك
        print("Motor OFF")

# إعداد الزر لالتقاط التغيرات في حالته (Interrupt)
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=toggle_motor, bouncetime=300)

# حلقة رئيسية للحفاظ على البرنامج قيد التشغيل
try:
    print("Press the button to toggle the motor.")
    while True:
        time.sleep(1)  # انتظر لتوفير الموارد
except KeyboardInterrupt:
    print("Exiting program...")

# تنظيف إعدادات GPIO عند الانتهاء
finally:
    GPIO.cleanup()
