from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

datos=[{}]

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['GET'])         
def checkoutRender():
    return render_template("checkout.html", data=datos[0])

@app.route('/check', methods=['POST'])         
def checkout():
    data={
        'strawberry':request.form["strawberry"],
        'raspberry':request.form["raspberry"],
        'apple':request.form["apple"],
        'first_name':request.form["first_name"],
        'last_name':request.form["last_name"],
        'student_id':request.form["student_id"]
    }
    print("Cobrando a "+str(data["first_name"])+" por "+ str(int(data["strawberry"])+int(data["raspberry"])+int(data["apple"])))
    datos.clear()
    datos.append(data)
    return redirect("/checkout")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    