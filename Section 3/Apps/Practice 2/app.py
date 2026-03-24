from flask import Flask, render_template,request

app=Flask(__name__,)



jobs = [
        {
            "title": "Software Engineer",
            "location": "San Francisco, USA",
            "type": "Full Time",
            "salary": "$80k - $120k",
            "logo": "img/com-logo-1.jpg",
            "deadline": "15 Mar, 2026"
        },
        {
            "title": "Data Analyst",
            "location": "London, UK",
            "type": "Part Time",
            "salary": "£30k - £45k",
            "logo": "img/com-logo-2.jpg",
            "deadline": "01 Apr, 2026"
        },
        {
            "title": "UX Designer",
            "location": "Berlin, Germany",
            "type": "Contract",
            "salary": "€50 - €70/hour",
            "logo": "img/com-logo-3.jpg",
            "deadline": "20 Feb, 2026"
        }
    ]


@app.route('/')
def hello():
    # return "<h1>hello world</h1>"
    return home()

@app.route('/home')
def home():
    return render_template('home.html')





@app.route('/jobs')
def jobs_list():
    return render_template('jop-list.html',jobs=jobs)



# @app.route('/form')
# def form():
#     return render_template('form.html')
# @app.route("/item")
# def item_view():
#     # Path parameter
#     # id_value = item_id

#     # Query parameters
#     color = request.args.get("color", "unknown")
#     size = request.args.get("size", "unspecified")

#     # Pass values into the template
#     return render_template("item.html",  color=color, size=size)

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=int("4000"))