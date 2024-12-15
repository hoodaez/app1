# استيراد المكتبات اللازمة
import nltk  # مكتبة معالجة اللغة الطبيعية
from nltk.chat.util import Chat, reflections 

patterns=[
    (r"hi|hey|hello", ["Hello! How can I help you today?",]),
    (r"good morning|good afternoon|good evening", ["Good morning/afternoon/evening! How are you?",]),
    (r"i'm (.*) (.*) ?", ["Nice to meet you, %1. How are you %2?",]),
    (r"how are you ?", ["I'm doing great, thank you. How about you ?",]),
    (r"my name is (.*)", ["Nice to meet you, %1. How can I help you today?",]),
    (r"quit", ["Bye! It was nice talking to you. See you later."]),
    (r"what is the weather today ?", ["The weather is quite nice today. It's a sunny day with a 20% chance of rain.",])
    (r"what is the time now ?", ["The current time is 10:30 AM."]),
    (r"how old are you ?", ["I'm 23 years old."]),
]

chatbot= chat(patterns,reflections)

print("Hi, I'm a simple chatbot. Type 'quit' to exit.")
chatbot.converse()
    
    
    
    
    
    
    
    
    
