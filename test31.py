import pandas as pd

# تحميل البيانات
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# تحليل البيانات
def analyze_data(data):
    try:
        print("\nBasic Info:")
        print(data.info())
        
        print("\nTop 5 Records:")
        print(data.head())
        
        # الإيرادات الإجمالية
        data['Revenue'] = data['Quantity'] * data['Price']
        total_revenue = data['Revenue'].sum()
        print(f"\nTotal Revenue: ${total_revenue:,.2f}")
        
        # المنتج الأكثر مبيعًا
        top_product = data.groupby('Product')['Quantity'].sum().idxmax()
        print(f"Top Selling Product: {top_product}")
        
        # الإيرادات حسب الأشهر
        data['Order Date'] = pd.to_datetime(data['Order Date'])
        data['Month'] = data['Order Date'].dt.month
        monthly_revenue = data.groupby('Month')['Revenue'].sum()
        print("\nMonthly Revenue:")
        print(monthly_revenue)
        
        return {
            'total_revenue': total_revenue,
            'top_product': top_product,
            'monthly_revenue': monthly_revenue
        }
    except Exception as e:
        print(f"Error analyzing data: {e}")
        return None

# حفظ النتائج
def save_results(results, file_path):
    try:
        results['monthly_revenue'].to_csv(file_path, header=True)
        print(f"Results saved to {file_path}")
    except Exception as e:
        print(f"Error saving results: {e}")

if __name__ == "__main__":
    # مسار ملف البيانات
    input_file = 'sales_data.csv'
    output_file = 'monthly_revenue.csv'

    # خطوات التحليل
    sales_data = load_data(input_file)
    if sales_data is not None:
        results = analyze_data(sales_data)
        if results:
            save_results(results, output_file)
