// استهداف العناصر
const calculator = document.getElementById("calculator");
const sun = document.getElementById("sun");
const moon = document.getElementById("moon");
const background = document.getElementById("background");
const toggleButton = document.getElementById("toggleButton");

// دالة لتشغيل/إيقاف الآلة الحاسبة
function toggleCalculator() {
  if (calculator.style.display === "none") {
    // تشغيل الآلة
    calculator.style.display = "block";
    sun.style.display = "block";
    moon.style.display = "none";
    background.style.background = "linear-gradient(135deg, #87ceeb, #f6d365)";
    toggleButton.innerText = "Turn Off";
  } else {
    // إيقاف الآلة
    calculator.style.display = "none";
    sun.style.display = "none";
    moon.style.display = "block";
    background.style.background = "linear-gradient(135deg, #2c3e50, #1c1c1c)";
    toggleButton.innerText = "Turn On";
  }
}

// دالة لإضافة القيم إلى شاشة العرض
function appendValue(value) {
  const display = document.getElementById("display");
  if (display.innerText === "0") {
    display.innerText = value;
  } else {
    display.innerText += value;
  }
}

// دالة لمسح شاشة العرض
function clearDisplay() {
  const display = document.getElementById("display");
  display.innerText = "0";
}

// دالة لحذف آخر مدخل
function deleteLast() {
  const display = document.getElementById("display");
  display.innerText = display.innerText.slice(0, -1) || "0";
}

// دالة لحساب النتيجة
function calculateResult() {
  const display = document.getElementById("display");
  try {
    display.innerText = eval(display.innerText.replace("×", "*").replace("÷", "/"));
  } catch {
    display.innerText = "Error";
  }
}
