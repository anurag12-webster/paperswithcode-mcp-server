import requests
import json
from typing import Optional, Dict, Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Papers With Code Enhanced", dependencies=["requests"])

BASE_URL = "https://paperswithcode.com/api/v1"
HEADERS = {"Accept": "application/json"}


def make_request(endpoint: str, params: Optional[Dict[str, Any]] = None) -> str:
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code == 200:
            return json.dumps(response.json(), indent=2)
        else:
            return f"Error: Received status code {response.status_code}\nResponse: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


@mcp.tool()
def search_papers(query: str, items_per_page: int = 20, page: int = 1) -> str:
    params = {
        "q": query,
        "items_per_page": min(items_per_page, 50),
        "page": page
    }
    return make_request("papers/", params)


@mcp.tool()
def get_paper_details(paper_id: str) -> str:
    return make_request(f"papers/{paper_id}/")


@mcp.tool()
def get_paper_datasets(paper_id: str, limit: int = 50) -> str:
    params = {"items_per_page": limit}
    return make_request(f"papers/{paper_id}/datasets/", params)


@mcp.tool()
def get_paper_methods(paper_id: str, limit: int = 50) -> str:
    params = {"items_per_page": limit}
    return make_request(f"papers/{paper_id}/methods/", params)


@mcp.tool()
def get_paper_repositories(paper_id: str, limit: int = 50) -> str:
    params = {"items_per_page": limit}
    return make_request(f"papers/{paper_id}/repositories/", params)


@mcp.tool()
def get_paper_tasks(paper_id: str, limit: int = 50) -> str:
    params = {"items_per_page": limit}
    return make_request(f"papers/{paper_id}/tasks/", params)


if __name__ == "__main__":
    mcp.run()