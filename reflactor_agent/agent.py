from typing import List, Tuple,Sequence
from dotenv import load_dotenv
from langchain.chains.question_answering.map_reduce_prompt import messages
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph import  END, MessageGraph
from chain  import reflector_chain,generator_chain
import os
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
graph = MessageGraph()
GENERATE = 'generate'
REFLECTOR = 'reflector'

def generator_node(state):
    last_human_msg = ""
    for msg in reversed(state):
        if isinstance(msg, HumanMessage):
            last_human_msg = msg.content
            break
    return generator_chain.invoke({
        "messages": state,
        "user_input": last_human_msg
    })

def reflector_node(state):
    last_human_msg = ""
    for msg in reversed(state):
        if isinstance(msg, HumanMessage):
            last_human_msg = msg.content
            break
    reflection = reflector_chain.invoke({
        "messages": state,
        "user_input": last_human_msg
    })
    return [HumanMessage(content=reflection.content)]

graph.add_node(REFLECTOR, reflector_node)
graph.add_node(GENERATE, generator_node)
graph.set_entry_point(GENERATE)


from langgraph.graph import END

def should_continue(state):
    if len(state) > 5:
        return "end"      # label in mapping
    return "reflect"      # label in mapping

graph.add_conditional_edges(
    GENERATE,
    should_continue,
    {
        "reflect": REFLECTOR,
        "end": END
    }
)

graph.add_edge(REFLECTOR,GENERATE)

app = graph.compile()
print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()
response = app.invoke(HumanMessage(content='Ai agent taking control over Humans'))
print(response)