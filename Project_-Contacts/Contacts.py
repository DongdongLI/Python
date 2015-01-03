import MySQLdb


#cur=db.cursor()
#cur.execute("select * from contact where first_name='dongdong'")

#for row in cur.fetchall():
#	for i in row:
#		print i

def new_contact():
	db=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="contact")

	name=raw_input("Please input the name of the new contact\n").encode('utf-8').split(' ')
	
	if len(name)==2:
		name.insert(1,"")
	#print name
	number=raw_input("Please input the phone number\n").encode('utf-8')


	cur=db.cursor()
	cur.execute("insert into contact(first_name, middle_name, last_name, phone_number) values ('%s','%s','%s','%s')" %(name[0],name[1],name[2],number))
	db.commit()
	db.close()

def search():
	key=raw_input("Please type in the keyword of the contact you want to search: (only one)\n").encode('utf-8')
	db=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="contact")
	cur=db.cursor()
	cur.execute("select * from contact where first_name='%s' or middle_name='%s' or last_name='%s'"%(key,key,key))
	#use to test if there is any result
	if len(cur.fetchall())==0:
		print "sorry, nothing found\n"
		return
	cur.execute("select * from contact where first_name='%s' or middle_name='%s' or last_name='%s'"%(key,key,key))# if the function is still running then there are uesults. so execute the query again
	print '{:<20}'.format('First Name')+'{:<20}'.format('Middle Name')+'{:<20}'.format('Last Name')+'{:<20}'.format('Phone Number')
	for row in cur.fetchall():
		print '{:<20}'.format(row[0])+'{:<20}'.format(row[1])+'{:<20}'.format(row[2])+'{:<20}'.format(row[3])

def delete():
	keyword=raw_input("Please type in the keyword of the contact you want to delete: first_name and last_name:\n").encode('utf-8').split(' ')
	db=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="contact")
	cur=db.cursor()
	cur.execute("delete from contact where first_name='%s' and last_name='%s'"%(keyword[0],keyword[1]))
	db.commit()
	db.close()

def show_all():
	db=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="contact")
	cur=db.cursor()
	cur.execute("select * from contact")
	print '{:<20}'.format('First Name')+'{:<20}'.format('Middle Name')+'{:<20}'.format('Last Name')+'{:<20}'.format('Phone Number')
	for row in cur.fetchall():
		print '{:<20}'.format(row[0])+'{:<20}'.format(row[1])+'{:<20}'.format(row[2])+'{:<20}'.format(row[3])

def __main__():#for testing purpose
	#delete()
	show_all()
	#new_contact()
	#search()

if __name__=="__main__":
	__main__()
