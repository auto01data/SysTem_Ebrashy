from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hall_world():
  return render_template('home.html')
@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

