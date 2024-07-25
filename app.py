import streamlit as st
import pandas as pd

from utils import visualize_node_data, visualize_edge_data

def main():
    st.title("Generic Data Visualizer")
    
    node_data_file = st.file_uploader(
        label="Upload Node Data File",
        type=["csv"]
    )
    
    edge_data_file = st.file_uploader(
        label="Upload Edge Data File",
        type=["csv"]
    )
    
    if node_data_file:
        st.header("Visualize Node Data")
        
        node_data = pd.read_csv(node_data_file, index_col=0)
        
        visualize_node_data(node_data=node_data)
        
    if edge_data_file:
        st.header("Visualize Edge Data")
        
        edge_data = pd.read_csv(edge_data_file, index_col=0)
        
        visualize_edge_data(edge_data=edge_data)
    

if __name__=="__main__":
    main()