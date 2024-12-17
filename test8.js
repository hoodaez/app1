// الحصول على شاشة العرض
const display = document.getElementById("display");

// إضافة رقم أو رمز إلى الشاشة
function appendCharacter(character) {
    display.value += character;
}

// مسح كامل للشاشة
function clearDisplay() {
    display.value = "";
}

// حذف آخر إدخال
function deleteLast() {
    display.value = display.value.slice(0, -1);
}

// حساب النتيجة
function calculateResult() {
    try {
        // تقييم التعبير الحسابي
        display.value = eval(display.value);
    } catch (error) {
        // في حالة وجود خطأ
        display.value = "خطأ";
    }
}
