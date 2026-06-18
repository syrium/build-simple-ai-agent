from dotenv import load_dotenv
from pydantic import BaseModel
#from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool


load_dotenv()

class ResearchResponse(BaseModel): #from pydantic
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

#llm = ChatOpenAI(model="gpt-4o-mini")
#llm2 = ChatAnthropic(model_name="claude-3-5-sonnet-20241022")
llm = ChatAnthropic(model_name="claude-haiku-4-5-20251001", timeout= 30, stop=None)

#Test response
#response = llm.invoke("What is the meaning of life?")
#print(response)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """, 
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]

).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can I help you research?")
raw_response = agent_executor.invoke({"query": query})
raw_text = None
if isinstance(raw_response, dict):
    output = raw_response.get("output")
    if isinstance(output, list) and len(output) > 0:
        first_output = output[0]
        if isinstance(first_output, dict):
            raw_text = first_output.get("text")
#print(raw_response)

try:
    if raw_text is None:
        raise ValueError("No text output found in response")
    structured_response = parser.parse(raw_text)
    #structured_response = parser.parse(raw_response["output"][0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)
