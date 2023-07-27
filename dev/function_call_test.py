from langchain import (
    LLMMathChain,
    OpenAI,
    SerpAPIWrapper,
    SQLDatabase,
    SQLDatabaseChain,
)
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from nft_tools import NFT_info
from langchain.chat_models import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = '''2fe60ccdc0e2687d086f79ba1a82cbc9f3c55f35bb2f77c0e983edf820f416b9'''

nft = NFT_info('cpu')
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
# db = SQLDatabase.from_uri("sqlite:///../../../../../notebooks/Chinook.db")
# db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions",
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
    ),
]
# tools = tools.append(nft.get_nft_metrics)
# print(tools)
mrkl = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

mrkl.run(
    "谁是鹿晗的女朋友的年龄是多少，再乘积0.5等于多少"
)