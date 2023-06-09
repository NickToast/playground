from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def test_template():
    return render_template('index.html', welcome=True)

#Level 1: Render 3 blue boxes

@app.route('/play')
def play():
    return render_template('index.html', level=1, num=3, color='lightblue')

#Level 2: Have it display blue boxes x times

@app.route('/play/<int:num>')
def box_multiplied(num):
    return render_template('index.html', level=2, num=num, color='lightblue')

#Level 3: Display x boxes with an color depending on the route name

@app.route('/play/<int:num>/<string:color>')
def boxes_num_color(num, color):
    return render_template('index.html', level=3, num=num, color=color)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.