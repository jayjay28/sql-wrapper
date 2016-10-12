import psycopg2
a = ["CREATE TABLE uno (id int PRIMARY KEY);","CREATE TABLE dos (id int PRIMARY KEY);"]


class SQ():
	def __init__(self):
		conn = psycopg2.connect('dbname=test user=Athen')
		cur = conn.cursor()	
	def create_table(self,a):
		conn = psycopg2.connect('dbname=test user=Athen')
		cur = conn.cursor()	
		for x in a:
			cur.execute(("CREATE TABLE %s id int serial;") %(x))
			conn.commit()
		cur.close()
		conn.close()
	def create_column(table_name,column_name):
		conn = psycopg2.connect('dbname=test user=Athen')
		cur = conn.cursor()
		cur.execute(("ALTER TABLE %s ADD %s varchar;")%(table_name, column_name))
		conn.commit()
		cur.close()
		conn.close()
	def create_multiple_columns(table_name, colum_names):
		for x in colum_names:
			create_column(table_name, x)
	def update_info(table_name,name, age, city, state,):
		conn = psycopg2.connect('dbname=test user=Athen')
		cur = conn.cursor()
		cur.execute((("INSERT INTO %s (name, age, city, state) VALUES ('%s','%s','%s','%s');")%(table_name, name, age, city, state)))
		conn.commit()
		cur.close()
		conn.close()
	def get_user(self,name):
		conn = psycopg2.connect('dbname=test user=Athen')
		cur = conn.cursor()
		cur.execute((("SELECT * FROM dos WHERE name='%s'")%(name)))
		a = cur.fetchone()
		cur.close()
		conn.close()
		return a

# table_names= ["chronixx","buju","maxwell"]
# SQ().create_table(table_names)


def update_table():
	conn = psycopg2.connect('dbname=test user=Athen')
	cur = conn.cursor()

	cur.execute("UPDATE dos SET city='WestBubafack', state='FL' WHERE id=2;")
	conn.commit()
	cur.close()
	conn.close()

update_table()
