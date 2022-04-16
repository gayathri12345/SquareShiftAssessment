import json
import os
from sys import path
from typing import OrderedDict
path.append(os.getcwd())
from flask import request,jsonify
from configfiles.config import Shipping_Charge
from DatabaseConnectivity.DatabaseConnection import add_items,check_item_in_cart,update_quantity,get_all_items,delete_cart_items,get_distance,get_pricing_details
from . import app
ship=Shipping_Charge()

@app.route('/cart/item',methods=['POST'])
def add_items_to_cart():
	try:
		response=OrderedDict()
		try:
			data=request.get_json()
			product_id=data['product_id']
			quantity=data['quantity']
		except Exception as error:
			print(f"Invalid request parameters: {str(error)}")
		if product_id<100 or product_id>110:
			response['status']='error'
			response['message']='Invalid product id'
			return jsonify(response),400
		else:
			records=check_item_in_cart(product_id)
			if records is not None:
				update_quantity(product_id,quantity)
			else:
				add_items(product_id,quantity)
			response['status']='success'
			response['message']='Item has been added to cart'
		return jsonify(response),200
	except Exception as error:
		print(error)


@app.route('/cart/items',methods=['GET','POST'])
def cart_items():
	try:
		response=OrderedDict()
		if request.method=='POST':
			data=request.get_json()
			if data['action']=='empty_cart':
				delete_cart_items()
				response['status']='success'
				response['message']='All items have been removed from the cart'
			else:
				response['status']='error'
		elif request.method=='GET':
			records=get_all_items()
			if len(records)>0:
				items=[]
				for item in records:
					{'product_id':item[0],
					'description':item[1],
					'quantity':item[2]
					}
					items.append(item)

				response['status']='success'
				response['message']='Item available in the cart'
				response['items']=items
			else:
				response['message']='cart is empty'
				return jsonify(response),400
		return jsonify(response),200
	except Exception as error:
		print(error)


@app.route('/cart/checkout-value',methods=['GET'])
def checkout_value():
	try:
		response=OrderedDict()
		data=request.get_json()
		postal_code=data['shipping_postal_code']
		if postal_code<465535 and postal_code>465545:
			response['status']='error'
			response['message']='Invalid postal code'
			return jsonify(response),400
		distance=get_distance(postal_code)
		if distance is not None:
			distance=distance[0]
		else:
			response['status']='error'
			return jsonify(response),400
		cart_items=get_all_items()
		if len(cart_items)==0:
			response['message']='Cart is empty'
			return jsonify(response),200
		cost=[]
		weights=[]
		product_ids=[(item[0],item[2]) for item in cart_items]
		for id,quantity in product_ids:
			record=get_pricing_details(id)
			if record:
				price,weight,discount=record
				price=price-price*discount/100
				price=price*quantity
				weight=weight/1000
				cost.append(price)
				weights.append(weight)
			else:
				response['status']='error'
				return jsonify(response),400
		total_weight=sum(weights)
		shipping_charge=ship.get_shipping_charge(distance,total_weight)
		total_cost=sum(cost)+shipping_charge
		response['status']='success'
		response['message']=f'Total value of your shopping cart is - ${total_cost}'
		return jsonify(response),200
	except Exception as error:
		print(error)