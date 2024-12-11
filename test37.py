from transformers import GPT2LMHeadModel, GPT2Tokenizer

# تحميل النموذج والرمز المميز (Tokenizer)
model_name = "gpt2"  # يمكنك استخدام نماذج أخرى مثل "gpt-3" إذا كانت لديك إمكانية الوصول إليها.
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# وظيفة لإجراء المحادثة
def chat():
    print("مرحبًا! أنا روبوت محادثة. اكتب 'خروج' لإنهاء المحادثة.")
    
    while True:
        user_input = input("أنت: ")
        if user_input.lower() == 'خروج':
            print("وداعًا!")
            break

        # تحويل النص المدخل إلى رموز قابلة للفهم من قبل النموذج
        input_ids = tokenizer.encode(user_input, return_tensors='pt')

        # توليد رد من النموذج
        output = model.generate(input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, pad_token_id=tokenizer.eos_token_id)

        # تحويل الرد إلى نص
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        print("الروبوت: ", response)

chat()

