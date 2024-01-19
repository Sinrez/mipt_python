from schema import schema

query = """
    query {
        hello
    }
"""
 
result = schema.execute(query)
print(result.data)