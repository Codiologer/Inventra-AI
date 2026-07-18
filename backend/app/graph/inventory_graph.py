from langgraph.graph import StateGraph, START, END

from app.graph.state import InventoryState


workflow = StateGraph(InventoryState)


def start_node(state: InventoryState):

    return state


workflow.add_node("start", start_node)

workflow.add_edge(START, "start")

workflow.add_edge("start", END)


inventory_graph = workflow.compile()