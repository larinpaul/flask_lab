from flask import Flask, render_template, request # importing the Flask Module and creating a web-server
# we've also just added the render_template function

app = Flask(__name__) # it is going to be main.py

@app.route("/") # creating a default page with /
def home(): # this function is activated when the user opens the default page
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact(): # The function check whether the request is indeed POST
    if request.method == 'POST':
        print(request.form)
    return render_template("contact.html")

app.debug = True
app.config['SECRET_KEY'] = 'my secret key is very nice'

manager = Manager(app)

if __name__ == "__main__": # this condition checks whether the Python script is working
                           # the script gets the name "__main__" by default
    app.run(debug=True) 
    