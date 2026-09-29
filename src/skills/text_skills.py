"""Module containing string processing and analytical tools for AI agents."""

import re
from typing import Dict, List, Any

def analyze_and_summarize_text(text: str, max_keywords: int = 3) -> Dict[str, Any]:
    """Analyze a block of text, extract key phrases, and calculate metadata metrics.
    
    Args:
        text (str): The body of text to process.
        max_keywords (int): Maximum number of top keywords to return.
        
    Returns:
        Dict[str, Any]: Analytical breakdown including word count and keywords.
    """
    if not text.strip():
        return {"word_count": 0, "keywords": [], "preview": ""}

    # 1. Clean and count words
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)

    # 2. Filter out basic filler stop words manually to extract unique keywords
    stop_words = {
        'the', 'a', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 'in', 
        'on', 'at', 'to', 'for', 'of', 'with', 'by', 'an', 'this', 'that', 'i', 'you'
    }
    filtered_words = [w for w in words if w not in stop_words and len(w) > 2]

    # 3. Calculate frequencies
    frequency_map = {}
    for word in filtered_words:
        frequency_map[word] = frequency_map.get(word, 0) + 1

    # 4. Sort and isolate top keywords
    sorted_keywords = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)
    top_keywords = [word for word, count in sorted_keywords[:max_keywords]]

    # 5. Extract a quick 60-character human snippet preview
    preview = text[:60] + "..." if len(text) > 60 else text

    return {
        "word_count": word_count,
        "keywords": top_keywords,
        "preview": preview
    }
