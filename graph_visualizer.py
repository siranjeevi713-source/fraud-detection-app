import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(df):

    G = nx.DiGraph()

    for i, row in df.iterrows():
        G.add_edge(row["from_account"], row["to_account"], weight=row["amount"])

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000)

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()
