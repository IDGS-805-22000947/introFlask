from flask import Flask, render_template, request, jsonify
app=Flask(__name__)



@app.route("/")
def index():
    titulo="IDGS805"
    lista=["Pedro", "Juan", "Mario"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/Hola")
def hola():
    return "Hola Mundo!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}!"

@app.route("/form1/")
def form1():
    return '''
            <form>
            <label for="nombre">Nombre:</lable>
            <input type="text" id="nombre" name="nombre"> </input>
            </form>

            '''

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2))) 


# -----------------------------------------
class CompraBoletos:
    def __init__(self, num_boletos=0, nombre_persona="", num_personas=0, usa_tarjeta_cineco=False):
        self.num_boletos = num_boletos
        self.nombre_persona = nombre_persona
        self.num_personas = num_personas
        self.usa_tarjeta_cineco = usa_tarjeta_cineco

    def calcular_costo(self):
        valor_base = 12
        costo_total = self.num_boletos * valor_base

        # Descuentos por cantidad de boletos
        if self.num_boletos > 5:
            costo_total *= 0.85  # 15% de descuento
        elif 3 <= self.num_boletos <= 5:
            costo_total *= 0.90  # 10% de descuento

        # Descuento adicional por usar tarjeta CINECO
        if self.usa_tarjeta_cineco:
            costo_total *= 0.90  # 10% adicional de descuento

        return costo_total

@app.route("/Cinepolis")
def compra():
    return render_template("Cinepolis.html")

@app.route("/resultado_compra", methods=["POST"])
def resultado_compra():
    nombre_persona = request.form.get("nombre_persona")
    num_personas = int(request.form.get("num_personas"))
    num_boletos = int(request.form.get("num_boletos"))
    usa_tarjeta_cineco = request.form.get("usa_tarjeta_cineco") == "si"

    max_boletos = num_personas * 7
    if num_boletos > max_boletos:
        return jsonify({"error": f"Supera el límite de boletos permitidos ({max_boletos})."})

    compra = CompraBoletos(num_boletos, nombre_persona, num_personas, usa_tarjeta_cineco)
    costo_total = compra.calcular_costo()

    return jsonify({"costo_total": f"${costo_total:.2f}"})

#-------------------------------------------




if __name__ == "__main__":
    app.run(debug=True, port=3000)