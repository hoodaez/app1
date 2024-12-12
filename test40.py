import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# بيانات مبدئية عن المنتجات والعملاء
data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["T-shirt Red", "T-shirt Blue", "Jeans Black", "Jacket Green", "Dress Yellow"],
    "Product_Description": [
        "Comfortable red T-shirt for casual wear",
        "Blue T-shirt with modern design",
        "Black jeans perfect for daily use",
        "Green jacket for winter warmth",
        "Yellow dress for formal occasions"
    ]
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# استخراج الخصائص من وصف المنتجات باستخدام TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df["Product_Description"])

# حساب التشابه بين المنتجات باستخدام Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# وظيفة لإيجاد المنتجات المشابهة
def recommend_products(product_id, num_recommendations=2):
    # تحديد مؤشر المنتج
    idx = df[df["Product_ID"] == product_id].index[0]
    # استرجاع الدرجات المشابهة
    similarity_scores = list(enumerate(cosine_sim[idx]))
    # ترتيب المنتجات حسب التشابه
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    # اختيار أفضل المنتجات
    top_products = similarity_scores[1:num_recommendations + 1]
    # عرض النتائج
    recommendations = [df.iloc[i[0]]["Product_Name"] for i in top_products]
    return recommendations

# تجربة النظام
product_to_recommend = 1  # اختر منتج البداية
recommended = recommend_products(product_to_recommend)
print(f"Based on product '{df[df['Product_ID'] == product_to_recommend]['Product_Name'].values[0]}', we recommend: {recommended}")
