// دالة التحقق من صحة البيانات
function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // تحقق من أن المستخدم أدخل بيانات
    if (username == "" || password == "") {
        alert("الرجاء ملء جميع الحقول!");
        return false;  // إلغاء الإرسال إذا كانت الحقول فارغة
    }

    // تحقق من بيانات المستخدم
    if (username === "admin" && password === "1234") {
        alert("تم تسجيل الدخول بنجاح!");
        return true;
    } else {
        alert("اسم المستخدم أو كلمة السر غير صحيحة.");
        return false;
    }
} 

 // دالة لتحويل المستخدم إلى الرابط المحدد 
 function button_subnit(button) {
    window.location.href = url;
 }