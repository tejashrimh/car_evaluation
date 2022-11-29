import numpy as np
import json
import config
import pickle


class CarPrice():
    def __init__(self,symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,
        engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,
        fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg):

        self.symboling=symboling
        self.normalized_losses = normalized_losses
        self.make = make
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.body_style = body_style
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.engine_type = engine_type
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.fuel_system = fuel_system
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg


        
    def load_model(self):

        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def Predict_price(self):

        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.symboling
        test_array[1] = self.normalized_losses
        test_array[2] = self.make
        test_array[3] = self.json_data['fuel_type'][self.fuel_type]
        test_array[4] = self.json_data['aspiration'][self.aspiration]
        test_array[5] = self.json_data['num_of_doors'][self.num_of_doors]
        test_array[6] = self.json_data['body_style'][self.body_style]
        test_array[7] = self.json_data['drive_wheels'][self.drive_wheels]
        test_array[8] = self.json_data['engine_location'][self.engine_location]
        test_array[9] = self.wheel_base
        test_array[10] = self.length
        test_array[11] = self.width
        test_array[12] = self.height
        test_array[13] = self.curb_weight
        test_array[14] = self.json_data['engine_type'][self.engine_type]
        test_array[15] = self.json_data['num_of_cylinders'][self.num_of_cylinders]
        test_array[16] = self.engine_size
        test_array[17] = self.fuel_system
        test_array[18] = self.bore
        test_array[19] = self.stroke
        test_array[20] = self.compression_ratio
        test_array[21] = self.horsepower
        test_array[22] = self.peak_rpm
        test_array[23] = self.city_mpg
        test_array[24] = self.highway_mpg


        print("Test array",test_array)

        predict_price = np.around(self.model.predict([test_array])[0],2)
        return predict_price

# if __name__ == '__main__' :



#         symboling = 3.00
#         normalized_losses = 127.00
#         make = 0.00
#         fuel_type='gas'
#         aspiration='std'
#         num_of_doors='two'
#         body_style='convertible'
#         drive_wheels='rwd'
#         engine_location='front'
#         wheel_base=88.60
#         length=168.80
#         width=64.10
#         height=48.80
#         curb_weight=2548.00
#         engine_type='dohc'
#         num_of_cylinders='four'
#         engine_size=130.00
#         fuel_system=1.00
#         bore=3.47
#         stroke=2.68
#         compression_ratio=9.00
#         horsepower=111.00
#         peak_rpm=5000.00
#         city_mpg=21.00
#         highway_mpg=27.00


#         Car_price = CarPrice(symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,
#         engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,
#         fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg)

#         Car_price.Predict_price()

