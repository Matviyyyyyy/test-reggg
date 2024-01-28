from flask import Flask, render_template, request, flash, redirect, url_for,session
from SQLAgent import SQLAgent

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DB_NAME = 'logo-cars-table.db'
DB_NAME2 = 'brand_cars_table.db'
DB_NAME3 = 'news_table.db'
DB_NAME4 = 'users_table.db'

@app.route("/")
def p_auto_main():
    return render_template('autogura_main.html')

@app.route("/auto_cars")
def p_auto_cars():
    return render_template('auto_cars.html')

@app.route("/horeca")
def p_horeca():
    return render_template("horeca.html")

@app.route("/history")
def p_history():
    return render_template("history.html")

@app.route("/ac-agura")
def p_ac_agura():
    return render_template("ac-agura.html")

@app.route("/azs")
def p_azs():
    return render_template("azs.html")

@app.route("/ins")
def p_ins():
    return render_template("ins.html")

@app.route("/do-auto")
def p_do_auto():
    return render_template("do-auto.html")


@app.route("/sln-cars-main")
def cars_show():
    sql_agent = SQLAgent(DB_NAME)
    all_logo_cars = sql_agent.get_all()
    return render_template('sln-cars-main.html', all_logo_cars=all_logo_cars)

@app.route("/cont")
def p_cont():
    return render_template("cont.html")

@app.route("/eks-van")
def p_eks_van():
    return render_template("eks-van.html")

@app.route("/about-comp")
def p_about_comp():
    return render_template("about_comp.html")

@app.route("/au-ser")
def p_our_can():
    return render_template("au-ser.html")

@app.route("/offer")
def p_offer():
    return render_template("offer.html")

@app.route("/chose-auto")
def p_chose_auto():
    sql_agent2 = SQLAgent(DB_NAME2)
    all_brand_cars = sql_agent2.get_all_cars()
    return render_template('chose-auto.html', all_brand_cars=all_brand_cars)

@app.route("/news")
def p_news():
    sql_agent3 = SQLAgent(DB_NAME3)
    all_news = sql_agent3.get_news()
    return render_template('news.html', all_news=all_news)
@app.route("/we-can")
def p_we_can():
    return render_template("we-can.html")
@app.route("/car/<car_id>")
def p_car(car_id):
    sql_agent2 = SQLAgent(DB_NAME2)
    all_brand_cars = sql_agent2.get_all_cars()
    car = all_brand_cars[int(car_id) - 1]
    return render_template("car.html", car=car)


@app.route("/filtred", methods=["POST"])
def filtr():
    sql_agent2 = SQLAgent(DB_NAME2)

    one_type_drive = request.form.get("name_ra3")
    two_type_drive = request.form.get("name_ra4")
    year_2021 = request.form.get("name_ra1")
    two_year = request.form.get("name_ra2")

    filter_car = sql_agent2.get_filtred_cars(two_year)
    return render_template('chose-auto.html', all_brand_cars=filter_car)

@app.route("/sig_page")
def p_sign():
    return render_template('sign_page.html')
@app.route("/reg_page")
def p_reg():
    return render_template('registr_page.html')

@app.route("/registration", methods=["POST"])
def registration_func():
    name_user = request.form.get("user_name_reg_page")
    pri_user = request.form.get("user_pri_reg_page")
    email_user = request.form.get("user_email_reg_page")
    tel_user = request.form.get("user_tel_reg_page")
    password_user = request.form.get("user_password_reg_page")

    sql_agent_for_reg = SQLAgent(DB_NAME4)
    sql_agent_for_reg.add_user(name_user, pri_user, tel_user, email_user, password_user)
    return render_template('sign_page.html')

@app.route("/sign_in", methods=["POST"])
def sign_in_func():
    name_user_sign = request.form.get("user_name_sign_page")
    email_user_sign = request.form.get("user_email_sign_page")
    password_user_sign = request.form.get("user_password_sign_page")

    sql_agent_for_reg = SQLAgent(DB_NAME4)
    user_verify = sql_agent_for_reg.get_correct_user(name_user_sign, email_user_sign, password_user_sign)
    user_verify_not = sql_agent_for_reg.get_uncorrect_user(name_user_sign, email_user_sign, password_user_sign)


    if user_verify:
        user_data = sql_agent_for_reg.get_user_dani(name_user_sign, email_user_sign, password_user_sign)
        user_data = dict(zip(sql_agent_for_reg.get_user_columns(), user_data))
        session['user_id'] = user_data['id_user']
        return render_template('user_page.html', user_data=user_data)
    else:
        return redirect(url_for("p_uncorrect_page"))

@app.route("/uncorrect_page")
def p_uncorrect_page():
    return render_template('uncorrect_page.html')

@app.route("/user_page")
def p_user_page():
    return render_template('user_page.html')



if __name__ == '__main__':
    app.run(debug=True)

"""
vanv/Scripts\activate
python app.py
"""

#return redirect(url_for("p_user_page", user_data=user_data))
#return redirect(url_for("p_uncorrect_page"))

