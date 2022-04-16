import requests
from DatabaseConnectivity.DatabaseConnection import add_products,add_warehouse

SERVER_URL='https://e-commerce-api-recruitment.herokuapp.com/'

def add_all_product_details():
	for id in range(100,111):
		resp=requests.get(f'{SERVER_URL}product/{id}')
		resp=resp.json()['product']
		add_products(
		resp['id'],
		resp['name'],
		resp['price'],
		resp['description'],
		resp['category'],
		resp['image'],
		resp['discount_percentage'],
		resp['weight_in_grams'])

def add_warhouse_details():
	for pincode in range(465535,465546):
		resp=requests.get(f'{SERVER_URL}warehouse/distance',params={'postal_code':pincode})
		resp=resp.json()
		add_warehouse(pincode,resp['distance_in_kilometers'])

add_all_product_details()
add_warhouse_details()