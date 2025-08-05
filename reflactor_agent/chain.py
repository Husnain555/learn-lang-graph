from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# -------------------- GENERATOR (Posty) --------------------
generator_template = ChatPromptTemplate.from_messages([
    ("system",
     "You are Posty, an AI assistant who transforms raw ideas or drafts "
     "into high-performing LinkedIn posts. "
     "Your style is engaging, professional, and story-driven, optimized "
     "to encourage interaction (likes, comments, shares). "
     "Always end with a call-to-action."),
    ("human",
     "Here’s the content idea or draft:\n\n{user_input}\n\n"
     "Rewrite this as a polished LinkedIn post."),
    MessagesPlaceholder(variable_name="messages"),
])

# -------------------- REFLECTOR --------------------
reflector_template = ChatPromptTemplate.from_messages([
    ("system",
     "You are Reflector, an AI agent that reviews LinkedIn posts with a critical eye. "
     "Your job is to identify weaknesses, improve clarity, and make the content "
     "more engaging, persuasive, and impactful. "
     "Always maintain the original intent while improving flow, grammar, and engagement potential."),
    ("human",
     "Review the following LinkedIn post and provide:\n"
     "1. Key weaknesses\n"
     "2. Suggested improvements\n"
     "3. A fully improved version\n\n"
     "Post:\n{user_input}"),
    MessagesPlaceholder(variable_name="messages"),
])

# -------------------- LLM & CHAINS --------------------
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

generator_chain = generator_template | llm
reflector_chain = reflector_template | llm
