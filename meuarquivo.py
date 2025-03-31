from flask import Flask, render_template 
 
app = Flask(__name__)

@app.route("/")

def indix():
    return render_template("index.html")

@app.route("/image")

def serve_image():

 messagem = "image route"

 return render_template("imagem.html", massagem=messagem)


@app.route("/tmb")

def tmb():
  return render_template("tmb.html")


@app.route("/sobre")

def sobre():

  return render_template("sobre.html")

if __name__ == "__main__":

 app.run(debug=True)


 