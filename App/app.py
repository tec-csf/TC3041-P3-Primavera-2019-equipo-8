#Our database is formed from all the users of wikipedia whose relationships represent which user edited the page of another user

from neo4j import GraphDatabase

#Function for the first querie
#It returns the number of edits that the specified user has done
#(We added the value() function at the end so that it only returns the number of edits)
def count_edits(session, id_):
	return session.run("MATCH (u:User{Id:$id})-[r:Edito_la_pagina_de]->() "
					   "RETURN count(r)", id=id_).value(0) 

#Function for the second querie
#It returns the id of the users that have more edits than the quantity specified
#(We added the values() function at the end so that it returns all the users' id)
def count_edits_greater_than(session, quantity_):
	return session.run("MATCH (u:User)-[r]->() "
					   "WITH u, count(r) as c "
					   "WHERE c > $quantity "
					   "RETURN u.Id", quantity=quantity_).values()

#Function for the third querie
#It returns the id of all the users that have edited the page of the specified user
def who_edited(session, id_):
	return session.run("MATCH (u1:User) <-[:Edito_la_pagina_de]-(u2:User) "
					   "WHERE u1.Id = $id "
					   "RETURN u2.Id", id=id_).values()

uri = "bolt://localhost:7687" #Port of the database
username = "neo4j" #Username for the database
password = "Practica 3" #Password for the database

#Connection to the database
driver = GraphDatabase.driver(uri, auth=(username, password))

with driver.session() as session:

	#Example of the first querie
	result = count_edits(session,0)
	print(result)

	#Example of the second querie
	result = count_edits_greater_than(session,5)
	print(result)

	#Example of the third querie
	result = who_edited(session,1)
	print(result)

