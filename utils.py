import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import networkx as nx
import plotly.express as px

def visualize_node_data(node_data):
    df = node_data
    
    # Get the unique nodes
    nodes = df['node'].unique()

    selected_node = 0
    
    if len(nodes) > 1:
        # Add a slider to select the node
        selected_node = st.select_slider('Select a node', options=nodes)

    # Filter the dataframe based on the selected node
    filtered_df = df[df['node'] == selected_node]
    
    st.dataframe(filtered_df)

    # Create a line plot for each feature
    fig = px.line(filtered_df, x='timestamp', y='value', color='feature', title=f'Features over Time for Node {selected_node}', width=650, height=500)

    st.plotly_chart(fig)
    
def visualize_edge_data(edge_data):
    df = edge_data
    
    features = df['feature'].unique()
    timestamps = df['timestamp'].unique()
    
    selected_feature = features[0]
    selected_timestamp = timestamps[0]
    
    if len(features) > 1:
        selected_feature = st.select_slider('Select a feature', options=features)

    if len(timestamps) > 1:
        selected_timestamp = st.select_slider('Select a timestamp', options=timestamps)

    # Filter the dataframe based on selected feature and timestamp
    filtered_df = df[(df['feature'] == selected_feature) & (df['timestamp'] == selected_timestamp)]
    
    st.dataframe(filtered_df)

    # Create a directed graph
    G = nx.DiGraph()

    # Add edges with value as weight if the value is not None
    for _, row in filtered_df.iterrows():
        if pd.notnull(row['value']):
            G.add_edge(row['source'], row['target'], weight=row['value'], label=row['value'])

    # Draw the graph using NetworkX and Matplotlib
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)  # Fixing the layout to make it reproducible

    # Draw nodes with custom settings
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', edgecolors='black')

    # Draw edges with custom settings
    edges = nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='->', arrowsize=20, edge_color='grey', width=2)

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

    # Draw edge labels (weights) with custom settings
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

    # Title and axes
    plt.title(f'Directed Graph for Feature: {selected_feature} at Timestamp: {selected_timestamp}', fontsize=16)
    plt.axis('off')

    # Display the plot
    st.pyplot(plt)
