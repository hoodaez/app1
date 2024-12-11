from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Flask API</h1>
    <p>Use the endpoint <code>/api/uppercase</code> to convert text to uppercase.</p>
    """

@app.route('/api/uppercase', methods=['POST'])
def uppercase_text():
    # استقبال البيانات كـ JSON
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400  # رد خطأ في حالة غياب البيانات

    input_text = data['text']  # النص المدخل
    uppercase_result = input_text.upper()  # تحويل النص إلى حروف كبيرة
    return jsonify({'result': uppercase_result})  # إرسال الرد كـ JSON

if __name__ == '__main__':
    app.run(debug=True)
