# Refactored Groq LangGraph

This is a refactored version of [google-gemini/gemini-fullstack-langgraph-quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart), modified to use **Groq model** instead of Google Gemini and **local search** instead of Google Search API.

## Key Modifications

- Replaced Google Gemini with Groq models
- Replaced Google Search API with local search implementation
- Updated configuration to use `GROQ_API_KEY` instead of `GEMINI_API_KEY`

## Quick Start

Refer to the [original README](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart#readme) for detailed setup instructions, architecture overview, and deployment guide. The setup process is identical except for using `GROQ_API_KEY` in your `.env` file:

```
GROQ_API_KEY="YOUR_API_KEY"
```

## License

Apache License 2.0 - See [LICENSE](LICENSE) file for details.
