from flask import Flask	
app = Flask(__name__)

@app.route("/")	
def index():  	
  return """	
  <h1>Python Flask in Docker!</h1>	
  <p>A sample web-app for running Flask inside Docker.</p>	
  """

  def hello(username):
        page_html="""
        <h1>python flask in docker<h1>
        """

if __name__ == "__main__":  	
    app.run(debug=True, host='0.0.0.0')	
