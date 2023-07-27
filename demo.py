from langchain.document_loaders.base import Document
from langchain.indexes import VectorstoreIndexCreator
from langchain.utilities import ApifyWrapper


# 初始化 Apify API token and OpenAI API key
import os
os.environ["OPENAI_API_KEY"] = "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"
os.environ["APIFY_API_TOKEN"] = "apify_api_NePAHqLJMilGNnnDq73iVoiBQM5BGD2Quiq7"
apify = ApifyWrapper()

# Call the Website Content Crawler Actor to crawl the specified URL
loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={"startUrls": [{"url": "https://branch4-web-app.nftgo.dev/analytics/market-overview"}]},
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
)
print(loader)
# https://release-data-farmer-api.nftgo.dev/api/v1/ranking/trending-collections?sortby=saleNum&asc=-1&offset=0&limit=100&range=6h
# Initialize the vector index from the crawled documents
index = VectorstoreIndexCreator().from_loaders([loader])

# Query the vector index to get answers to your questions
query = "What is the website about?"
result = index.query_with_sources(query)
print(result["answer"])
print(result["sources"])