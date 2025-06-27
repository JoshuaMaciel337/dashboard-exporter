from flask import Flask, render_template, request, send_file, abort, flash
from config import DEBUG, SECRET_KEY
import pandas as pd
import io

app = Flask(__name__)
app.config['DEBUG'] = DEBUG
app.config['SECRET_KEY'] = SECRET_KEY

# Sample data (in production, this would come from a database)
def get_dashboard_data():
    return {
        'filters': {
            'timeframe': '7 days',
            'gender': 'All',
            'category': 'Select a value'
        },
        'statistics': {
            'total_products': 0,
            'critical_stock': 0,
            'need_production': 0,
            'excess_stock': 0
        },
        'table_data': [],
        'charts': {
            'top': [],
            'bottom': []
        }
    }

@app.route('/')
def index():
    dashboard_data = get_dashboard_data()
    return render_template('index.html', data=dashboard_data)

@app.route('/export')
def export_excel():
    try:
        # Dummy dataframe; replace with real data in production
        df = pd.DataFrame({
            'Product': ['Product A', 'Product B'],
            'Stock': [10, 20]
        })
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        output.seek(0)
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name='export.xlsx'
        )
    except Exception as e:
        print("Error generating Excel export:", e)
        abort(500)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', message="Page not found (404)"), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html', message="Server error (500)"), 500

if __name__ == '__main__':
    app.run()
