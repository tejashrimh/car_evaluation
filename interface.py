from flask import Flask,jsonify,request,render_template,redirect,url_for
from Project_app.utils import CarPrice
import os
import config

app = Flask(__name__)

picfloder = os.path.join("static",'img')

app.config['UPLOAD_FOLDER'] =picfloder


    
@app.route('/',methods =["POST","GET"])
def test():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'back.jpeg')
    return render_template("home.html",user_img = pic1) 


@app.route("/result",methods =["POST","GET"])
def Predict_price():

     if request.method == 'POST':
        data = request.form 
        print("Data is :",data)

        symboling  = eval(data["symboling"])
        normalized_losses  = eval(data["normalized_losses"])
        make  = eval(data["make"])
        fuel_type  = (data["fuel_type"])
        aspiration  = (data["aspiration"])
        num_of_doors  = (data["num_of_doors"])
        body_style  = (data["body_style"])
        drive_wheels  = (data["drive_wheels"])
        engine_location  = (data["engine_location"])
        wheel_base  = eval(data["wheel_base"])
        length  = eval(data["length"])
        width  = eval(data["width"])
        height  = eval(data["height"])
        curb_weight  = eval(data["curb_weight"]) 
        engine_type  = (data["engine_type"])
        num_of_cylinders  = (data["num_of_cylinders"])
        engine_size  = eval(data["engine_size"])
        fuel_system  = eval(data["fuel_system"])
        bore  = eval(data["bore"])
        stroke  = eval(data["stroke"])
        compression_ratio  = eval(data["compression_ratio"])
        horsepower  = eval(data["horsepower"])
        peak_rpm  = eval(data["peak_rpm"])
        city_mpg  = eval(data["city_mpg"])
        highway_mpg  = eval(data["highway_mpg"])

    
    # symboling = 3.00
    # normalized_losses = 127.00
    # make = 0.00
    # fuel_type='gas'
    # aspiration='std'
    # num_of_doors='two'
    # body_style='convertible'
    # drive_wheels='rwd'
    # engine_location='front'
    # wheel_base=88.60
    # length=168.80
    # width=64.10
    # height=48.80
    # curb_weight=2548.00
    # engine_type='dohc'
    # num_of_cylinders='four'
    # engine_size=130.00
    # fuel_system=1.00
    # bore=3.47
    # stroke=2.68
    # compression_ratio=9.00
    # horsepower=111.00
    # peak_rpm=5000.00
    # city_mpg=21.00
    # highway_mpg=27.00    

    
        
        Car_price = CarPrice(symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,
        engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,
        fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg)

        price = Car_price.Predict_price() 
    

        return render_template("result1.html", price= price)



if __name__ == "__main__":
    app.run(port = 5200)  # server start