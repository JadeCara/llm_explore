import networkx as nx
import matplotlib.pyplot as plt

def build_knowledge_graph(relationships):
    G = nx.Graph()

    # Add edges based on relationships
    for keyword, related_keywords in relationships.items():
        for related_keyword in related_keywords:
            G.add_edge(keyword, related_keyword)

    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_color='black', font_weight='bold')
    plt.show()

# Example usage
build_knowledge_graph(relationships)
