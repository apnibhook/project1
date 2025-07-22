from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/our_services')
def our_services():
    return render_template('our_services.html')

@app.route('/trades')
def trades():
    return render_template('trades.html')

@app.route('/our_projects')
def our_projects():
    return render_template('our_projects.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)