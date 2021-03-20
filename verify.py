from authy.api import AuthyApiClient
from flask import Flask, render_template, request, redirect, url_for




@app.route("/phone_verification", methods=["GET", "POST"])
def phone_verification():
    return render_template("phone_verification.html")

app = Flask(__name__)
app.config.from_object('config')

api = AuthyApiClient(app.config['AUTHY_API_KEY'])


@app.route("/phone_verification", methods=["GET", "POST"])
def phone_verification():
    pass

@app.route("/phone_verification", methods=["GET", "POST"])
def phone_verification():
    if request.method == "POST":
        country_code = request.form.get("country_code")
        phone_number = request.form.get("phone_number")
        method = request.form.get("method")
        
        api.phones.verification_start(phone_number, country_code, via=method)
        
        return redirect(url_for("verify"))


    return render_template("phone_verification.html")


if __name__ == '__main__':
    app.run(debug=True)