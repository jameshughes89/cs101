## CSCS 161 Assignment #2 -- Zombie Apocalypse
## Name: PLEASE FILL THIS IN
## Student number: SERIOUSLY

import string

import matplotlib.pyplot as plt
import networkx
import numpy

#### This stuff you just have to use, you're not expected to know how it works.
#### You just need to read the plain English function headers.
#### If you want to learn more, by all means follow along (and ask questions if
#### you're curious). But you certainly don't have to.


def make_city(name, neighbours):
    """
    Create a city (implemented as a list).

    :param name: String containing the city name
    :param neighbours: The city's row from an adjacency matrix.

    :return: [name, Infection status (defailt value of False), List of neighbours]
    """

    return [name, False, list(numpy.where(neighbours == 1)[0])]


def make_connections(n, density=0.35):
    """
    This function will return a random adjacency matrix of size
    n x n. You read the matrix like this:

    if matrix[2,7] = 1, then cities '2' and '7' are connected.
    if matrix[2,7] = 0, then the cities are _not_ connected.

    :param n: number of cities
    :param density: controls the ratio of 1s to 0s in the matrix

    :returns: an n x n adjacency matrix
    """

    # Generate a random adjacency matrix and use it to build a networkx graph
    a = numpy.int32(numpy.triu((numpy.random.random_sample(size=(n, n)) < density)))
    G = networkx.from_numpy_matrix(a)

    # If the network is 'not connected' (i.e., there are isolated nodes)
    # generate a new one. Keep doing this until we get a connected one.
    # Yes, there are more elegant ways to do this, but I'm demonstrating
    # while loops!
    while not networkx.is_connected(G):
        a = numpy.int32(numpy.triu((numpy.random.random_sample(size=(n, n)) < density)))
        G = networkx.from_numpy_matrix(a)

    # Cities should be connected to themselves.
    numpy.fill_diagonal(a, 1)

    return a + numpy.triu(a, 1).T


def set_up_cities(
    names=[
        "City 0",
        "City 1",
        "City 2",
        "City 3",
        "City 4",
        "City 5",
        "City 6",
        "City 7",
        "City 8",
        "City 9",
        "City 10",
        "City 11",
        "City 12",
        "City 13",
        "City 14",
        "City 15",
    ]
):
    """
    Set up a collection of cities (world) for our simulator.
    Each city is a 3 element list, and our world will be a list of cities.

    :param names: A list with the names of the cities in the world.

    :return: a list of cities
    """

    # Make an adjacency matrix describing how all the cities are connected.
    con = make_connections(len(names))

    # Add each city to the list
    city_list = []
    for n in enumerate(names):
        city_list += [make_city(n[1], con[n[0]])]

    return city_list


def draw_world(world):
    """
    Given a list of cities, produces a nice graph visualization. Infected
    cities are drawn as red nodes, clean cities as blue. Edges are drawn
    between neighbouring cities.

    :param world: a list of cities
    """

    G = networkx.Graph()

    bluelist = []
    redlist = []

    plt.clf()

    # For each city, add a node to the graph and figure out if
    # the node should be red (infected) or blue (not infected)
    for city in enumerate(world):
        if city[1][1] == False:
            G.add_node(city[0])
            bluelist.append(city[0])
        else:
            G.add_node(city[0], node_color="r")
            redlist.append(city[0])

        for neighbour in city[1][2]:
            G.add_edge(city[0], neighbour)

    # Lay out the nodes of the graph
    position = networkx.circular_layout(G)

    # Draw the nodes
    networkx.draw_networkx_nodes(G, position, nodelist=bluelist, node_color="b")
    networkx.draw_networkx_nodes(G, position, nodelist=redlist, node_color="r")

    # Draw the edges and labels
    networkx.draw_networkx_edges(G, position)
    networkx.draw_networkx_labels(G, position)

    # Force Python to display the updated graph
    plt.show()
    plt.draw()


def print_world(world):
    """
    In case the graphics don't work for you, this function will print
    out the current state of the world as text.

    :param world: a list of cities
    """

    print("{:15}{:15}".format("City", "Infected?"))
    print("------------------------")
    for city in world:
        print("{:15}{}".format(city[0], city[1]))


def draw_pretty_histogram(times):
    """
    Create a pretty histogram showing a distribution of the number of times it
    took to get to the end of the world over the provided times.
    :param times: a list of the time to end of worlds. The distribution of
        these values will be created.
    """

    plt.hist(times)
    plt.xlabel("Time to End of World")
    plt.ylabel("Count")
    plt.title("Distribution of End of the World Times")
    plt.show()


#### That's the end of the stuff provided for you.
#### Put *your* code after this comment.
