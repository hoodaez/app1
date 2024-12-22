// استهداف شاشة العرض
const display = document.getElementById("display");

// دالة لإضافة القيم إلى شاشة العرض
function appendValue(value) {
  if (display.innerText === "0") {
    display.innerText = value;
  } else {
    display.innerText += value;
  }
}

// دالة لمسح شاشة العرض
function clearDisplay() {
  display.innerText = "0";
}

// دالة لحذف آخر مدخل
function deleteLast() {
  display.innerText = display.innerText.slice(0, -1) || "0";
}

// دالة لحساب النتيجة
function calculateResult() {
  try {
    display.innerText = eval(display.innerText.replace("×", "*").replace("÷", "/"));
  } catch {
    display.innerText = "Error";
  }
}

