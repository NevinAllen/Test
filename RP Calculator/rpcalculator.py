from flask import Flask, render_template, url_for, redirect, request, send_from_directory
import os.path

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index/')
def indexB():
    return render_template("index.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/rpcal/')
def rpcal():
    return render_template("rpcal.html")


@app.route('/rpcal2/')
def rpcal2():
    return render_template("rpcal2.html")


@app.route('/rpcal/', methods=["GET", "POST"])
def form():
    print("Entering form function")
    if request.method == "POST":  # POST
        # upon user submission
        print("Entering form function")
        pw = request.form['pw']
        mt = request.form['mt']
        return render_template("rpcal2.html", pw=pw, mt=mt)
    else:  # GET
        return render_template('rpcal.html')


@app.route('/rpcal2/', methods=["GET", "POST"])
def rpform():
    print("Entering RP form function")

    if request.method == "POST":
        print("Entering form function")
        h21 = request.form['h21']
        h22 = request.form['h22']
        h23 = request.form['h23']
        h11 = request.form['h11']
        gp = request.form['gp']
        h2 = [h21, h22, h23]
        h1 = [h11, gp]
        pw = request.form.get('pw')
        mt = request.form.get('mt')
        h1.append(pw)
        h1.append(mt)

        for i in range(len(h2)):
            if h2[i] == "20.00":
                h2[i] = "A"
            elif h2[i] == "17.50":
                h2[i] = "B"
            elif h2[i] == "15.00":
                h2[i] = "C"
            elif h2[i] == "12.50":
                h2[i] = "D"
            elif h2[i] == "10.00":
                h2[i] = "E"
            elif h2[i] == "5.00":
                h2[i] = "S"
            else:
                h2[i] = "U"

        for i in range(len(h1)):
            if h1[i] == "10.00":
                h1[i] = "A"
            elif h1[i] == "8.75":
                h1[i] = "B"
            elif h1[i] == "7.50":
                h1[i] = "C"
            elif h1[i] == "6.25":
                h1[i] = "D"
            elif h1[i] == "5.00":
                h1[i] = "E"
            elif h1[i] == "2.50":
                h1[i] = "S"
            else:
                h1[i] = "U"

        def calculate(one, two, three, four, five, six=None, seven=None):
            rp = 0
            subs = [one, two, three, four, five]
            max_score = "80.00"

            if six != None:
                subs.append(six)
                max_score = "90.00"
            if seven != None:
                subs.append(seven)

            for i in range(len(subs)):
                rp += float(subs[i])
            if seven != None and six != None:
                rp = rp/100 * 90
            elif mt != None and pw == None:
                rp = rp/90 * 80
            rp = round(rp, 2)
            return str(rp) + " / " + max_score

    final = calculate(h21, h22, h23, h11, gp, pw, mt)
    return render_template('calresult.html', h21=h21, h22=h22, h23=h23, h11=h11, gp=gp, mt=mt, pw=pw, final=final, h2=h2, h1=h1)


if __name__ == '__main__':
    app.run(debug=True)
