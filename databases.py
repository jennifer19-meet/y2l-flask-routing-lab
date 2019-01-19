from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(type_of_item, price, rating,color,year_designed, designer):
	product_object= Products(
		type_of_item = type_of_item,
		price = price,
		rating = rating,
		color = color,
		year_designed = year_designed,
		designer = designer
		)
	session.add(product_object)
	session.commit()
  #TODO: complete the functions (you will need to change the function's inputs)
# create_product("dresss", 199,9,"blue",2009,"kimmy")

def update_product(id, price, rating):
  #TODO: complete the functions (you will need to change the function's inputs)
	product_object = session.query(Products).filter_by(id=id).first()
	if price <300:		
		product_object.price = price
		product_object.rating = rating
		session.commit()
	else:
		print("The number you entered is too high")
update_product(1,300,8)
def delete_product(id):
	session.query(Products).filter_by(id= id).delete()
	session.commit()
# delete_product(1)
def get_product(type_of_item):
	a=session.query(Products).filter_by(type_of_item=type_of_item).first()
	return(a)

print(get_product("top"))