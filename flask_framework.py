from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def anasayfa():
    on = 10
    yirmi = 20

    sozluk = {"TL":"Türkiye", "Dolar":"ABD", "Euro":"AB"}

    return render_template("anasayfa.html", number=on, number2=yirmi, sozluk=sozluk)

@app.route("/hakkimizda")
def hakkimizda():
    return render_template("hakkimizda.html")

@app.route("/inheritence")
def inheritence():
    return render_template("inheritence.html")
    

if __name__ == "__main__":
    app.run(debug=True)