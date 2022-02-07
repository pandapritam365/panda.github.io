from flask import Flask, render_template,url_for,request,redirect

app = Flask(__name__)
# print(app)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/works.html")
def works_page():
    return render_template('works.html')


@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about_me():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')



# @app.route("/blog/<int:post_id>")
# def blog(post_id):
#     return f'post id is {post_id}'


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('data.txt', mode='a') as database:
        name=data["name"]
        email=data["email"]
        subject=data["subtext"]
        message=data["message"]
        file = database.write(f'\n{name},{email},{subject},{message}')
        print(file)
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
       data=request.form.to_dict()
       write_to_file(data)
       return redirect('/thankyou.html')
  
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return f'hey you have submitted successfully!!'
    # if __name__=='__main__':
    #     app.run(debug=True)
