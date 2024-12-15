# استيراد المكتبات اللازمة
import pandas as pd  # لتحليل البيانات
from sklearn.metrics.pairwise import cosine_similarity  # لحساب التشابه بين الأفلام
from sklearn.feature_extraction.text import TfidfVectorizer  # لتحويل النصوص إلى أرقام

# بيانات افتراضية تمثل الأفلام ووصفها
movies = {
    'Movie_ID': [1, 2, 3, 4, 5],
    'Title': ['Inception', 'Titanic', 'Avatar', 'The Matrix', 'Interstellar'],
    'Genre': ['Sci-Fi, Thriller', 'Romance, Drama', 'Sci-Fi, Adventure', 'Sci-Fi, Action', 'Sci-Fi, Drama']
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(movies)

# عرض البيانات الأصلية
print("البيانات الأصلية:")
print(df)

# تحويل الأنواع (Genre) إلى تمثيل رقمي باستخدام TF-IDF
tfidf = TfidfVectorizer(stop_words='english')  # إزالة الكلمات الشائعة مثل (the, is, etc.)
tfidf_matrix = tfidf.fit_transform(df['Genre'])  # تحويل العمود 'Genre' إلى مصفوفة رقمية

# حساب التشابه بين الأفلام باستخدام التشابه الكوني (Cosine Similarity)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# دالة للحصول على توصيات
def get_recommendations(title, df, cosine_sim):
    # العثور على مؤشر الفيلم بناءً على العنوان
    idx = df[df['Title'] == title].index[0]

    # الحصول على درجات التشابه للفيلم المطلوب
    sim_scores = list(enumerate(cosine_sim[idx]))

    # ترتيب الأفلام بناءً على التشابه (من الأعلى إلى الأقل)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # الحصول على أفضل 3 أفلام (باستثناء الفيلم المطلوب)
    sim_scores = sim_scores[1:4]

    # استخراج عناوين الأفلام الموصى بها
    movie_indices = [i[0] for i in sim_scores]
    return df['Title'].iloc[movie_indices]

# تجربة التوصية لفيلم "Inception"
print("\nتوصيات بناءً على الفيلم 'Inception':")
recommendations = get_recommendations('Inception', df, cosine_sim)
print(recommendations)
