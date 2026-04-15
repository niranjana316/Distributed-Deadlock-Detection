import streamlit as st
import simpy
from deadlock import WaitForGraph

st.title("Distributed Deadlock Detection (WFG)")

num_processes = st.slider("Number of Processes", 2, 10, 4)

wfg = WaitForGraph()

st.write("Define dependencies (Who waits for whom)")

edges = []

for i in range(num_processes):
    wait_for = st.number_input(f"P{i} waits for:", min_value=0, max_value=num_processes-1, key=i)
    if i != wait_for:
        edges.append((f"P{i}", f"P{wait_for}"))

if st.button("Run Detection"):
    for e in edges:
        wfg.add_edge(e[0], e[1])

    deadlock, cycle = wfg.detect_deadlock()

    if deadlock:
        st.error(f"Deadlock Detected! Cycle: {cycle}")
    else:
        st.success("No Deadlock Detected")
