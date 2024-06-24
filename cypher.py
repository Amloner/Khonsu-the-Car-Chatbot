from langchain.chains import GraphCypherQAChain
from langchain.prompts.prompt import PromptTemplate

from llm import llm
from graph import graph

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about car and provide recommendations.
Convert the user's question based on the schema.

Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.

If details of a specific car is asked, provide its model, horsepower, year, and msrp.
Example Cypher Statements:

1. To find CarID:
```
MATCH (c:Car)-[:MADE_BY]->(m:Make)
RETURN c.model, c.carID
```

2. Gives details of a carID:
```
MATCH (c:Car)
WHERE c.carID = 123
return c.carID, c.horsepower, c.msrp
```
3. detials of car by year
```
MATCH (c:Car)-[:MADE_IN]->(y:Year)
WHERE y.Year = 2016
RETURN c.carID, c.horsepower, c.msrp , y.Year
```

3. detials of a car give its carID (Transmisison can be replaced by stlye or size based on question)
```
MATCH (y:Year)<-[Y:MADE_IN]-(c:Car)-[:HAS]->(t:Transmission)
WHERE c.carID=123
RETURN c.carID, c.horsepower, c.msrp , y.Year, t.type
```


Schema:
{schema}

Question:
{question}
"""

cypher_prompt = PromptTemplate.from_template(CYPHER_GENERATION_TEMPLATE)

cypher_qa = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    verbose=True,
    cypher_prompt=cypher_prompt
)
