// تعريف رسالة ترحيبية تظهر عند تحميل الصفحة
window.onload = function() {
    alert("مرحبًا بك في موقعنا!");
    // نافذة منبثقة ترحيبية تظهر عند تحميل الصفحة
};

// تعريف متغيرات واستخدامها
let userName = "محمود"; // متغير نصي يحتوي على اسم المستخدم
let userAge = 25; // متغير عددي يحتوي على عمر المستخدم

// طباعة رسالة في وحدة التحكم
console.log(`مرحبًا ${userName}, عمرك هو ${userAge} عامًا.`);
// دمج النصوص مع المتغيرات باستخدام القالب النصي (template literals)

// تعريف دالة بسيطة
function greetUser(name) {
    return `مرحبًا، ${name}!`;
    // دالة تُرجع رسالة ترحيبية مخصصة بناءً على الاسم المدخل
}

// استدعاء الدالة وطباعة النتيجة
console.log(greetUser(userName));

// التعامل مع الأحداث (Event Handling)
document.getElementById("myButton").addEventListener("click", function() {
    alert("لقد ضغطت على الزر!");
    // رسالة تظهر عند الضغط على الزر
});

// التعامل مع المصفوفات
let items = ["تفاح", "موز", "برتقال"]; // مصفوفة تحتوي على عناصر
items.push("عنب"); // إضافة عنصر جديد إلى المصفوفة
items.forEach(function(item, index) {
    console.log(`العنصر ${index + 1}: ${item}`);
    // طباعة كل عنصر في المصفوفة مع ترتيبه
});

// التعامل مع الكائنات
let user = {
    name: "محمود",
    age: 25,
    email: "mahmoud@example.com",
    greet: function() {
        console.log(`مرحبًا، أنا ${this.name}.`);
        // دالة داخل الكائن تستخدم خاصية "this" للوصول إلى البيانات
    }
};

user.greet(); // استدعاء الدالة داخل الكائن

// التحقق من الشرط باستخدام if
if (userAge > 18) {
    console.log("أنت بالغ.");
    // رسالة تظهر إذا كان العمر أكبر من 18
} else {
    console.log("أنت قاصر.");
    // رسالة تظهر إذا كان العمر أقل أو يساوي 18
}

// حلقة for لطباعة الأرقام من 1 إلى 5
for (let i = 1; i <= 5; i++) {
    console.log(`الرقم الحالي هو: ${i}`);
    // طباعة الرقم الحالي في كل تكرار
}

// حلقة while لطباعة الأرقام من 5 إلى 1
let count = 5; // متغير عددي يبدأ من 5
while (count > 0) {
    console.log(`الرقم التنازلي: ${count}`);
    count--; // تقليل قيمة المتغير في كل دورة
}

// استخدام setTimeout لتأخير تنفيذ الكود
setTimeout(function() {
    console.log("تم تنفيذ هذا الكود بعد 3 ثوانٍ.");
    // رسالة تظهر بعد 3 ثوانٍ
}, 3000);

// استخدام setInterval لتكرار تنفيذ الكود
let intervalId = setInterval(function() {
    console.log("تنفيذ متكرر كل 2 ثانية.");
    // رسالة تظهر كل 2 ثانية
}, 2000);

// إيقاف setInterval بعد 6 ثوانٍ
setTimeout(function() {
    clearInterval(intervalId);
    console.log("تم إيقاف التكرار.");
    // إيقاف تنفيذ setInterval
}, 6000);

// إنشاء عنصر HTML جديد باستخدام DOM
let newElement = document.createElement("p");
newElement.textContent = "هذا نص تمت إضافته باستخدام JavaScript.";
// إنشاء عنصر <p> جديد وإضافة نص داخله

document.body.appendChild(newElement);
// إضافة العنصر الجديد إلى الصفحة

// استخدام try...catch للتعامل مع الأخطاء
try {
    let result = someUndefinedFunction(); // دالة غير معرّفة
} catch (error) {
    console.error("حدث خطأ:", error.message);
    // طباعة رسالة الخطأ في وحدة التحكم
} finally {
    console.log("تمت محاولة تنفيذ الكود.");
    // كود يتم تنفيذه سواء حدث خطأ أم لا
}

// استيراد وتصدير الوحدات (Modules) - ES6
// ملاحظة: يجب أن تكون في ملفين منفصلين
// في ملف module.js
export function sayHello(name) {
    return `مرحبًا، ${name}!`;
    // دالة تقوم بتصدير رسالة ترحيبية
}

// في ملف main.js
// import { sayHello } from './module.js';
// console.log(sayHello("محمود"));

// التعرف على الأحداث الديناميكية
document.addEventListener("mousemove", function(event) {
    console.log(`حركة الفأرة: X=${event.clientX}, Y=${event.clientY}`);
    // طباعة إحداثيات الفأرة أثناء الحركة
});

// استخدام التاريخ والوقت
let currentDate = new Date(); // الحصول على التاريخ الحالي
console.log(`التاريخ الحالي: ${currentDate.toLocaleDateString()}`);
console.log(`الوقت الحالي: ${currentDate.toLocaleTimeString()}`);

// دوال رياضية باستخدام Math
console.log(`القيمة العشوائية: ${Math.random()}`); // قيمة عشوائية بين 0 و 1
console.log(`الجذر التربيعي لـ 16: ${Math.sqrt(16)}`); // الجذر التربيعي
console.log(`أكبر قيمة: ${Math.max(5, 10, 15)}`); // أكبر قيمة

// تخزين واسترجاع البيانات باستخدام LocalStorage
localStorage.setItem("username", userName); // تخزين البيانات
console.log(`اسم المستخدم من LocalStorage: ${localStorage.getItem("username")}`); // استرجاع البيانات
