from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
class Products(Base):
	__tablename__ ="Info about Products"

	id = Column(Integer, primary_key= True)
	type_of_item = Column(String)
	price = Column(Integer)
	rating = Column(Integer)
	color = Column(String)
	year_designed = Column(Integer)
	designer = Column(String)



# Write your classes here :

    # TODO: complete this class
   