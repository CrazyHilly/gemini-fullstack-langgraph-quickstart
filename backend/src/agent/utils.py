import os
from pathlib import Path
from typing import List, Dict

from langchain_core.messages import AnyMessage, AIMessage, HumanMessage


def get_research_topic(messages: List[AnyMessage]) -> str:
    """
    Get the research topic from the messages.
    """
    # check if request has a history and combine the messages into a single string
    if len(messages) == 1:
        research_topic = messages[-1].content
    else:
        research_topic = ""
        for message in messages:
            if isinstance(message, HumanMessage):
                research_topic += f"User: {message.content}\n"
            elif isinstance(message, AIMessage):
                research_topic += f"Assistant: {message.content}\n"
    return research_topic


def search_files(
        directory: str, 
        query: str, 
        max_results: int = 5
        ) -> List[Dict[str, str]]:
    """
    Get research results from file search.
    """
    results = []
    query_terms = query.lower().split()
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".txt", ".md", ".py", ".json", ".csv")):
                file_path = Path(root) / file
                try:
                    content = file_path.read_text(encoding="utf-8", errors="ignore")
                    
                    matches = sum(1 for term in query_terms if term in content.lower())
                    if matches > 0:
                        results.append({
                            "label": file,
                            "short_url": file,
                            "value": str(file_path.absolute()),
                            "snippet": content[:1000],
                            "match_score": matches
                        })
                except Exception:
                    continue
                    
                if len(results) >= max_results:
                    break
                
        if len(results) >= max_results:
            break
    
    return sorted(results, key=lambda x: x["match_score"], reverse=True)[:max_results]
