
#Query that returns the number of edits a specified user has done

MATCH (u:User{Id:1})-[r:Edito_la_pagina_de]->() 
RETURN count(r)

#Query that returns the id of the users that have more edits than the quantity specified

MATCH (u:User)-[r]->() 
WITH u, count(r) as c 
WHERE c > 5
RETURN u.Id

#Query that returns the id of all the users that have edited the page of the specified user

MATCH (u1:User) <-[:Edito_la_pagina_de]-(u2:User) 
WHERE u1.Id = 1
RETURN u2.Id