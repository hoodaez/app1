// الحصول على الزر من خلال معرّفه
const colorButton = document.getElementById("colorButton");

// إنشاء مصفوفة تحتوي على ألوان متعددة
const colors = ["#ff6347", "#ffeb3b", "#4caf50", "#2196f3", "#9c27b0"];

// وظيفة لتغيير لون الخلفية عند الضغط على الزر
colorButton.addEventListener("click", function() {
    // اختيار لون عشوائي من المصفوفة
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    
    // تغيير لون خلفية الصفحة
    document.body.style.backgroundColor = randomColor;
});
