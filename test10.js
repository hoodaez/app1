// التعامل مع العمليات الحسابية
let display = document.getElementById('display');

function appendToDisplay(value) {
    display.value += value;
}

function calculate() {
    try {
        display.value = eval(display.value);  // حساب النتيجة باستخدام eval
    } catch (e) {
        display.value = 'خطأ';
    }
}

// التعامل مع محول العملات
async function convertCurrency() {
    const amount = document.getElementById('currency-input').value;
    const fromCurrency = document.getElementById('currency-from').value;
    const toCurrency = document.getElementById('currency-to').value;
    
    if (!amount || isNaN(amount)) {
        alert('الرجاء إدخال مبلغ صحيح');
        return;
    }

    const apiKey = 'YOUR_API_KEY'; // استبدل هذا بـ API Key الخاص بك من ExchangeRate-API أو أي API آخر
    const url = `https://v6.exchangerate-api.com/v6/${apiKey}/latest/${fromCurrency}`;
    
    const response = await fetch(url);
    const data = await response.json();
    
    if (data.result === 'success') {
        const rate = data.conversion_rates[toCurrency];
        const convertedAmount = amount * rate;
        document.getElementById('conversion-result').innerText = `${amount} ${fromCurrency} = ${convertedAmount.toFixed(2)} ${toCurrency}`;
    } else {
        alert('حدث خطأ أثناء الحصول على البيانات');
    }
}
