from neo4j import GraphDatabase

class KnowledgeGraphNeo4j:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_node_and_relationships(self, keyword, related_keywords):
        with self.driver.session() as session:
            session.write_transaction(self._create_node_tx, keyword, related_keywords)

    @staticmethod
    def _create_node_tx(tx, keyword, related_keywords):
        # Create nodes for keyword and related keywords and relationships between them
        tx.run("MERGE (a:Keyword {name: $keyword})", keyword=keyword)
        for related_keyword in related_keywords:
            tx.run("""
            MATCH (a:Keyword {name: $keyword}), (b:Keyword {name: $related_keyword})
            MERGE (a)-[:RELATED_TO]->(b)
            """, keyword=keyword, related_keyword=related_keyword)

# Example usage
kg = KnowledgeGraphNeo4j("bolt://localhost:7687", "neo4j", "password")

for keyword, related_keywords in relationships.items():
    kg.create_node_and_relationships(keyword, related_keywords)

kg.close()
