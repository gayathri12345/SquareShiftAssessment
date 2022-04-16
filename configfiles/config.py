database='SquareShift_Test'
port='5432'
host='localhost'


class Shipping_Charge:
    
    def __init__(self):
        pass

    def get_shipping_charge(self,distance,weight):
        if weight<=2:
            if distance<=5:
                shipping_charge=12
            elif distance>5 and distance<20:
                shipping_charge=15
            elif distance>20 and distance<50:
                shipping_charge=20
            elif distance>50 and distance<500:
                shipping_charge=50
            elif distance>500 and distance<800:
                shipping_charge=100
            elif distance>800:
                shipping_charge=220
        elif weight>=2.01 and weight<=5:
            if distance<=5:
                shipping_charge=14
            elif distance>5 and distance<20:
                shipping_charge=18
            elif distance>20 and distance<50:
                shipping_charge=24
            elif distance>50 and distance<500:
                shipping_charge=55
            elif distance>500 and distance<800:
                shipping_charge=110
            elif distance>800:
                shipping_charge=250

        elif weight>=5.01 and weight<=20:
            if distance<=5:
                shipping_charge=16
            elif distance>5 and distance<20:
                shipping_charge=25
            elif distance>20 and distance<50:
                shipping_charge=30
            elif distance>50 and distance<500:
                shipping_charge=80
            elif distance>500 and distance<800:
                shipping_charge=130
            elif distance>800:
                shipping_charge=270

        elif weight>=20.01:
            if distance<=5:
                shipping_charge=21
            elif distance>5 and distance<20:
                shipping_charge=35
            elif distance>20 and distance<50:
                shipping_charge=50
            elif distance>50 and distance<500:
                shipping_charge=90
            elif distance>500 and distance<800:
                shipping_charge=150
            elif distance>800:
                shipping_charge=300
        return shipping_charge