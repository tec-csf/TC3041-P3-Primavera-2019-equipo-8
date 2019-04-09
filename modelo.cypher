
#Nodos de los usuarios

USING PERIODIC COMMIT 2000
LOAD CSV WITH HEADERS FROM 'file:///WikiTalkNodes.csv' AS row 
WITH toInteger(row.nodeId) AS nodeId
MERGE (u:User {Id: nodeId})
RETURN count(u)


#Relaciones

USING PERIODIC COMMIT 2000
LOAD CSV WITH HEADERS FROM 'file:///WikiTalkRelationships.csv' AS row 
WITH row.FromNodeId as FromNodeId, row.ToNodeId as ToNodeId
MATCH (u1:User {Id: FromNodeId})
MATCH (u2:User {Id: ToNodeId})
MERGE (u1)-[r:Edito_la_pagina_de]->(u2)
RETURN count(r)
