from client import CallGraphExtractor

src = """
def authenticate():
    check_token()

def api_endpoint():
    authenticate()
    fetch_payload()
"""

graph = CallGraphExtractor.extract_graph(src)
print("Extracted Static Call Graph:", graph)
