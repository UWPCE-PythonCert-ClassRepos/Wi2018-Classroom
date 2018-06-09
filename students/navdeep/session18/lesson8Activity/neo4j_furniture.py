"""
    neo4j example
"""
from neo4j.v1 import GraphDatabase, basic_auth
import logging

logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)
def main():
    log.info('Here is where we use the connect to neo4j.')
    log.info('')
    graphenedb_user = input("Username: ") 
    graphenedb_pass = input("Password: ") 
    graphenedb_url = input("URL: ") 
    driver = GraphDatabase.driver(graphenedb_url.strip(),
                                  auth=basic_auth(graphenedb_user.strip(), graphenedb_pass.strip()))
    with driver.session() as session:
        log.info('Adding a few Person nodes')
        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Cooper'),
                            ('Fred', 'Barnes'),
                            ('Mary', 'Evans'),
                            ('Marie', 'Curie'),
                            ]:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (
                first, last)
            session.run(cyph)
        
        log.info("Get all of people in the DB:")
        cyph = """MATCH (p:Person)
                  RETURN p.first_name as first_name, p.last_name as last_name
                """
        result = session.run(cyph)
        print("People in database:")
        for record in result:
            print(record['first_name'], record['last_name'])

        favorite_colors = ['blue', 'orange', 'green', 'purple', 'gold']
        for color in favorite_colors:
            cyph = "CREATE (n:Color {color: '%s'})" % (color)
            session.run(cyph)
        cypher = """
        MATCH (p1:Person {first_name: 'Alice', last_name: 'Cooper'}), (c1:Color {color: 'orange'})
        CREATE (p1)-[c:FAVORITE_COLOR]->(c1)
        return p1
        """
        session.run(cypher)

        cypher = """
        MATCH (p1:Person {first_name: 'Bob', last_name: 'Jones'}), (c1:Color {color: 'blue'})
        CREATE (p1)-[c:FAVORITE_COLOR]->(c1)
        return p1
        """
        session.run(cypher)
        cypher = """
        MATCH (p1:Person {first_name: 'Fred', last_name: 'Barnes'}), (c1:Color {color: 'gold'})
        CREATE (p1)-[c:FAVORITE_COLOR]->(c1)
        return p1
        """
        session.run(cypher)
        session.close()

main()