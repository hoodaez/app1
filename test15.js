// دالة لمعالجة عملية الشراء
function buyProduct(productName) {
    alert("Thank you for purchasing " + productName + "!"); // رسالة تأكيد
}

// التعريف وا��تخدام المتغيرات

let userName = "محمود"; // متغير نصي يحتوي على ا��م المستخدم
let userAge = 25; // متغير عددي يحتوي على عمر المستخدم

// ��با��ة رسالة في وحدة التحكم

console.log(`مرحب��ا ${userName}, عمرك هو ${userAge} عام��ا.`);

// التحقق من الصحة للرقم العمر

if (typeof userAge !== "number" || userAge <= 0) {
    console.error("عمر المستخدم يجب أن يكون رقم ��حيح وبالتالي يكون أكبر من 0.");
} else {
    console.log("عمر المستخدم ��حيح.");
    // ��ذا كان العمر ��حيح، يمكنك التحقق من الشرط با��تخدام if
    if (userAge >= 18) {
        console.log("أنت بالغ.");
    } else {
        console.log("أنت قا��ر.");
    }
}