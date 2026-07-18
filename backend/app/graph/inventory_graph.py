from langgraph.graph import StateGraph, END

from app.graph.state import InventoryState


workflow = StateGraph(InventoryState)