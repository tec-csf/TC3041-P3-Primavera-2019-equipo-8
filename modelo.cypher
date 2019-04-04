USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM 'file:///WikiTalkNodes.csv' AS row 
WITH toInteger(row.nodeId) AS nodeId
MERGE (u:User {nodeId: nodeId})
RETURN count(u)