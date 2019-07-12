from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    print('running the html page')
    return render_template("index.html")

@app.route('/<num>')
def enter_row_num(num):
    print('running the num route function')
    return render_template("num_change.html", num=int(int(num)/2))

@app.route('/<num_x>/<num_y>')
def enter_row_and_column(num_x, num_y):
    print('running the row and column function')
    return render_template("row_and_column_change.html", num_x=int(int(num_x)/2), num_y=int(int(num_y)/2))

@app.route('/<num_x>/<num_y>/<color1>/<color2>')
def four_var(num_x, num_y, color1, color2):
    print('running the four var function')
    return render_template("x_y_color1_color2.html", num_x=int(int(num_x)/2), num_y=int(int(num_y)/2), color1=str(color1), color2=str(color2))

if __name__=="__main__":
    app.run(debug=True)