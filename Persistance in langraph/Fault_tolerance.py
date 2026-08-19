from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict
import time

# 1. Define the state
class CrashState(TypedDict):
    input: str
    step1: str
    step2: str


# 2. Define steps
def step_1(state: CrashState) -> CrashState:
    print("✅ Step 1 executed")
    return {"step1": "done", "input": state["input"]}

def step_2(state: CrashState) -> CrashState:
    print("⏳ Step 2 hanging... now manually interrupt from the notebook toolbar (STOP button)")
    time.sleep(1000)  # Simulate long-running hang
    return {"step2": "done"}

def step_3(state: CrashState) -> CrashState:
    print("✅ Step 3 executed")
    return {"done": True}


# 3. Build the graph
builder = StateGraph(CrashState)
builder.add_node("step_1", step_1)
builder.add_node("step_2", step_2)
builder.add_node("step_3", step_3)

builder.set_entry_point("step_1")
builder.add_edge("step_1", "step_2")
builder.add_edge("step_2", "step_3")
builder.add_edge("step_3", END)

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# from the previous snippet, we can see that the checkpointer is responsible for saving the state of the workflow at certain points, allowing for recovery in case of failure or interruption. In this example, we are using an InMemorySaver as our checkpointer, which saves the state in memory.


# these are the steps that will be executed in the workflow. Step 1 and Step 3 are simple steps that print a message and return a state. Step 2 simulates a long-running hang by sleeping for 1000 seconds, which allows us to manually interrupt the execution to simulate a crash.

# these can be used for debugging and monitoring the workflow's progress. The checkpointer allows us to resume execution from the last saved state, which can save time and resources in case of unexpected interruptions.
try:
    print("▶️ Running graph: Please manually interrupt during Step 2...")
    graph.invoke({"input": "start"}, config={"configurable": {"thread_id": 'thread-1'}})
except KeyboardInterrupt:
    print("❌ Kernel manually interrupted (crash simulated).")



# 6. Re-run to show fault-tolerant resume
print("\n🔁 Re-running the graph to demonstrate fault tolerance...")
final_state = graph.invoke(None, config={"configurable": {"thread_id": 'thread-1'}})
print("\n✅ Final State:", final_state)


list(graph.get_state_history({"configurable": {"thread_id": 'thread-1'}}))


# The above code demonstrates a fault-tolerant workflow using a state graph. It defines a series of steps that can be executed in sequence, with the ability to save the state at each step using an in-memory checkpointer.