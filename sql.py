from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

Literature = Table('literature', Base.metadata,
                Column('authors_id', Integer, ForeignKey('authors.id')),
                Column('books_id', Integer, ForeignKey('books.id'))
)
	
	
class Books(Base):
	__tablename__ = "books"
	id = Column(Integer, primary_key=True)
	title = Column(String) 
	
	def __init__(self,id,title):
		self.id = id
		self.title = title
       

class Authors(Base):
	__tablename__ = "authors"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	
	def __init__(self,id,name):
		self.id = id
		self.name = name

		
engine = create_engine('sqlite:///prom.db')	
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Authors.name,Books.title).join(Literature).join(Books)
query1 = session.query(Authors)
query2 = session.query(Books)




	
	

def new_record(table,id,name):
	if table =="Authors":
		
		if session.query(Authors).filter(Authors.id == id).first() == None:
			session.add(Authors(id,name))
			session.commit()
			return 'Success'
		else:
			return 'Record is defined in table'
		
	elif table == "Books":
		if session.query(Books).filter(Books.id == id) == None:
			session.add(Books(id,name))
			session.commit()
			return 'Success'
		else:
			return 'Record is defined in table'
	

	

def modify_record(table,id,name):
	if table =="Authors":
	
		modify_query = session.query(Authors).filter(Authors.id == id).first()
		if modify_query == None:
			return 'Record is not defined in table'
		else:	
			modify_query.name = name;
			session.commit()
			return "Success"
		
	elif table == "Books":
		modify_query = session.query(Books).filter(Books.id == id).first()
		if modify_query == None:
			return 'Record is not defined in table'
		else:
			modify_query.title = name;
			session.commit()
			return "Success"
	
	
		
	
	
	
def delete_record(table,id,name):
	if table =="Authors":
		delete_query = session.query(Authors).filter(Authors.id == id).first()
		if delete_query == None:	
			return 'Record is not defined in table'
		else:
			session.delete(delete_query)
			session.commit()			
			return "Success"			
	
	elif table == "Books":
		delete_query = session.query(Books).filter(Books.id == id).first()
		if delete_query == None:
			return 'Record is not defined in table'
		else:
			session.delete(delete_query)
			session.commit()	
			return 'Success'
		
		
	
	