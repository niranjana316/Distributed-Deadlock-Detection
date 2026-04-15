import streamlit as st
import simpy
from deadlock import DistributedSystem

st.title("Distributed Deadlock Detection using WFG")

num_processes = st.slider("Number of Processes", 2, 10, 5)

if st.button("Run Simulation"):
    env = simpy.Environment()
    system = DistributedSystem(env, num_processes)

    system.run()

    st.write("Generated Wait-For Graph Edges:")
    st.write(system.graph.edges())

    deadlock, cycle = system.detect_deadlock()

    if deadlock:
        st.error(f"Deadlock Detected! Cycle: {cycle}")
    else:
        st.success("No Deadlock Detected")
