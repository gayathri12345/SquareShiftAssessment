from DatabaseConnectivity import *

def connect_to_database():
	try:
		conn=None
		conn = psycopg2.connect(
			host=config.host,
			database=config.database,
			user=credentials.username,
			password=credentials.password
			)
		return conn,conn.cursor()
	except Exception as error:
		print(error)

def add_products(id,name,price,description,category,image,discount_percentage,weight_in_grams):
	try:
		query = '''
				INSERT INTO product (id,name,price,description,category,image,discount_percentage,weight_in_grams)
				VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
				'''
		conn,cursor=connect_to_database()
		cursor.execute(query,(id,name,price,description,category,image,discount_percentage,weight_in_grams))
		conn.commit()
		print(f"Product {id} added to database")
	except Exception as error:
		print(error)
	finally:
		if conn:
			conn.close()

def add_warehouse(pincode,distance):
	try:
		query='''
				INSERT INTO warehouse (postal_code,distance_in_kilometers)
				VALUES (%s,%s)
			'''
		conn,cursor=connect_to_database()
		cursor.execute(query,(pincode,distance))
		conn.commit()
		print(f'pincode {pincode} added to databse')
	except Exception as error:
		print(error)
	finally:
		if conn:
			conn.close()

def add_items(product_id,quantity):
	try:
		query='''
		INSERT INTO items (product_id,quantity)
		VALUES (%s,%s)
		'''
		conn,cursor=connect_to_database()
		cursor.execute(query,(product_id,quantity))
		conn.commit()
	except Exception as error:
		print(error)
	finally:
		if conn:
			conn.close()
	

def update_quantity(product_id,quantity):
	try:
		query='''
		UPDATE items SET quantity=%s WHERE product_id=%s
		'''
		conn,cursor=connect_to_database()
		cursor.execute(query,(quantity,product_id))
		conn.commit()
	except Exception as error:
		print(error)

def check_item_in_cart(product_id):
	try:
		query='''SELECT product_id from items WHERE product_id=%s'''
		conn,cursor=connect_to_database()
		cursor.execute(query,(product_id,))
		records=cursor.fetchone()
		return records

	except Exception as error:
		print(error)

def get_all_items():
	try:
		query='''SELECT items.product_id, product.name, items.quantity 
				FROM items
				INNER JOIN product on items.product_id=product.id'''
		conn,cursor=connect_to_database()
		cursor.execute(query)
		records=cursor.fetchall()
		return records
	except Exception as error:
		print(error)
	finally:
		if conn:
			conn.close()

def delete_cart_items():
	try:
		query='''TRUNCATE TABLE items;'''
		conn,cursor=connect_to_database()
		cursor.execute(query)
		conn.commit()

	except Exception as error:
		print(error)
	finally:
		if conn:
			conn.close()

def get_distance(pincode):
	try:
		query='''SELECT distance_in_kilometers FROM warehouse WHERE postal_code=%s'''
		conn,cursor=connect_to_database()
		cursor.execute(query,(pincode,))
		records=cursor.fetchone()
		return records
	except Exception as error:
		print(error)
	finally:
		if conn:
			conn.close()

def get_pricing_details(product_id):
	try:
		query='''SELECT price, weight_in_grams, discount_percentage FROM product WHERE id=%s'''
		conn,cursor=connect_to_database()
		cursor.execute(query,(product_id,))
		records=cursor.fetchone()
		return records
	except Exception as error:
		print(error)


