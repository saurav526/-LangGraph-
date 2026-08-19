# checkpointer = InMemorySaver()

# workflow = graph.compile(checkpointer=checkpointer)


# persistance is implemented in langraph as a checkpointer. The checkpointer is responsible for saving the state of the workflow at certain points, allowing for recovery in case of failure or interruption. In this example, we are using an InMemorySaver as our checkpointer, which saves the state in memory.


