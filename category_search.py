from duckduckgo_search import DDGS

search_system_prompt = '''
    You are an expert researching agent. You have access to a search engine. Given a question, you will return a query to search for relevant information. Return only what you want to search.
'''
fallback_search_system_prompt = '''
    You are an expert researching agent. You have access to a search engine. Given a question and an error from a previous search, you will return a corrected query to search for relevant information. Return only what you want to search.
'''

def web_search(query: str) -> tuple(bool, str):
    try:
        results = []

        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                search_title = r['title']
                search_snippet = r['snippet']
                results.append(f"Title: {search_title}\nSnippet: {search_snippet}")

        if not results:
            return False, "No results found."

        return True, "\n\n".join(results)

    except Exception as e:
        return False, str(e)
