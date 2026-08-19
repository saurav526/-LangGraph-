# checkpointer = InMemorySaver()

# workflow = graph.compile(checkpointer=checkpointer)


# persistance is implemented in langraph as a checkpointer. The checkpointer is responsible for saving the state of the workflow at certain points, allowing for recovery in case of failure or interruption. In this example, we are using an InMemorySaver as our checkpointer, which saves the state in memory.

# before running the workflow, we compile it with the checkpointer. This means that the workflow will be able to save its state at designated checkpoints during execution.

# Benefits of using a checkpointer include the ability to resume execution from the last saved state, which can save time and resources in case of unexpected interruptions. It also allows for better debugging and monitoring of the workflow's progress.


# Benefits of persistence in langraph include the ability to recover from failures, improved resource management, and enhanced debugging capabilities. By saving the state of the workflow at checkpoints, users can resume execution without losing progress, which is particularly useful for long-running or complex workflows. Additionally, persistence allows for better tracking of the workflow's execution history, making it easier to identify and resolve issues. Overall, implementing persistence through a checkpointer enhances the robustness and reliability of workflows in langraph.
