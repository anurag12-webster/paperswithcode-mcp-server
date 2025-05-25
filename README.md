# paperswithcode-mcp-server

Claude Desktop Config
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "papers-with-code": {
      "command": "uv",
      "args": ["run", "python", "server.py"],
      "cwd": "/path/to/paperswithcode-mcp"
    }
  }
}
```

Available Tools

`search_papers(query, items_per_page, page)` - Search papers by keywords

`get_paper_details(paper_id)` - Get full paper information

`get_paper_datasets(paper_id, limit)` - List datasets used in paper

`get_paper_methods(paper_id, limit)` - List methods used in paper

`get_paper_repositories(paper_id, limit)` - Find code repositories for paper

`get_paper_tasks(paper_id, limit)` - List ML tasks addressed by paper