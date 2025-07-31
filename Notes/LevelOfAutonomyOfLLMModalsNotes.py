# Levels of Autonomy
# 1. Code (Manual Programming)
# Autonomy Level: 0
# Nature: Fully deterministic
#
# Disadvantages:
#
# Requires writing explicit code for every possible scenario.
#
# Becomes complex and harder to maintain as the number of scenarios increases.
#
# 2. LLM Models
# Autonomy Level: Low to Medium
# Nature: Intelligent but single-task focused
#
# Advantages:
#
# Great at performing specific tasks when prompted correctly.
#
# Disadvantages:
#
# A single model can typically handle only one task at a time.
#
# You can’t easily execute multiple tasks in one go.
#
# Becomes a bottleneck when scalability or multitasking is required.
#
# 3. Chains
# Autonomy Level: Medium
# Nature: Rule-based LLM chaining
#
# Explanation:
#
# Chains allow structuring multiple LLM calls in a sequence.
#
# Each step can process part of a task and pass the output to the next.
#
# Disadvantages:
#
# Rigid in behavior – always follow the same flow.
#
# Not easily adaptable to dynamic scenarios or user inputs.
#
# 4. Routers
# Autonomy Level: Medium to High
# Nature: Smart task delegation system
#
# Explanation:
#
# Routers act like intelligent AI buddies.
#
# They decide which prompt goes to which specific LLM or function based on the input.
#
# Reduces the need for writing extensive if-else logic.
#
# Disadvantages:
#
# Lack memory – they don't retain information from previous tasks or context.
#
# 5. State Machines / Agents
# Autonomy Level: High
# Nature: Context-aware, memory-enabled AI agents
#
# Explanation:
#
# Agents act like smart state machines.
#
# There's typically a central controller (agent head) that receives the user's prompt.
#
# This controller assigns the task to a relevant LLM agent.
#
# Each LLM agent has its own memory and context, allowing it to track previous interactions.
#
# How it works:
#
# The user sends a prompt.
#
# The agent assigns it to a suitable LLM with memory.
#
# The LLM performs the task and responds back to the agent.
#
# The agent may confirm the result with the user (e.g., “Do you approve or want changes?”).
#
# If approved, the agent can pass the task to another agent responsible for real-world actions (e.g., generating UI, calling APIs, saving data).
#
# Advantages:
#
# Supports complex, multi-step workflows.
#
# Can maintain memory and improve responses based on past interactions.
#
# Much closer to human-like task handling.
#
# Stateful Agents (Memory-enabled) – Agents with context, memory, and human-like task flow.
# They retain past interactions, adapt over time,
# and manage multi-step tasks by remembering what the
# user said or requested earlier. These agents simulate
# conversations and workflows in a way that feels
# natural and continuous, making them ideal for complex, dynamic tasks.