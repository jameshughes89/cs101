# NAME:
# ST-NUMBER:
# StFX EMAIL:
import copy
import random

import matplotlib.pyplot as plt
import networkx as nx


def make_city(name: str, neighbours: list) -> list:
    """
    Creates and returns a city, encoded as a list containing the city's name, state (if it is infected or not), and
    list of neighbours, i.e. [name, infection state, [list of neighbours]]. Upon creation, all cities have their
    infection status set to False.

    :param name: The name of the city.
    :type name: String
    :param neighbours: A list of integers representing the indices of adjacent cities.
    :type neighbours: A list of integers (indices).
    :return: An encoding of a city
    :rtype: A list of the form [string, bool, [integers]]
    """
    return [name, False, neighbours]


assert "Name" == make_city("Name", [0, 10, 100])[0]
assert False == make_city("Name", [0, 10, 100])[1]
assert [0, 10, 100] == make_city("Name", [0, 10, 100])[2]


def make_edges(number_of_vertices: int, connected_neighbours: int = 4, rewire_probability: float = 0.33) -> dict:
    """
    Generate an adjacency list representing the edges for a graph/network of a specified size. The graph/network is
    undirected and unweighted. The resulting adjacency list is guaranteed to encode a graph/network that is connected.
    connected_neighbours is expected to be an even number; however, if an odd number is provided, then the resulting
    graph/network will have each vertex connect to the (connected_neighbours - 1) closest neighbours.
    :raises networkx.NetworkXError: If a connected graph cannot be generated after 1000 tries, raise an exception
    :param number_of_vertices: The number of vertices/nodes in the graph.
    :type number_of_vertices: Integer
    :param connected_neighbours: Number of closest neighbours to connect to upon creation.
    :type connected_neighbours: Integer
    :param rewire_probability: Likelihood of an edge being rewired after creation.
    :type rewire_probability: Float
    :return: An adjacency list for a connected, undirected, and unweighted graph/network.
    :rtype: Dictionary of lists of integers (integers represent vertices).
    """
    try:
        network = nx.connected_watts_strogatz_graph(
            number_of_vertices, connected_neighbours, rewire_probability, tries=1000
        )
    except nx.NetworkXError:
        raise nx.NetworkXError("Connected graph was unable to be created after 1000 tries --- please run again")
    return nx.to_dict_of_lists(network)


assert 10 == len(make_edges(10, 4, 0.33))
assert 40 == sum(len(current_list) for current_list in make_edges(10, 4, 0.33).values())


def make_world(number_of_cities: int, connected_neighbours: int = 4, rewire_probability: float = 0.33) -> list:
    """
    Returns a world consisting of multiple cities with some amount of connectivity between the cities. The world is
    a list of cities. Each city maintains its list of neighbouring cities.

    :param number_of_cities: The number of vertices/nodes in the graph.
    :type number_of_cities: Integer
    :param connected_neighbours: Number of closest neighbours to connect to upon creation.
    :type connected_neighbours: Integer
    :param rewire_probability: Likelihood of an edge being rewired after creation.
    :type rewire_probability: Float
    :return: A list of n cities.
    :return: A list of lists of the form [[string, bool, [integers]], [string, bool, [integers]], ... ]
    """
    world = []
    connections = make_edges(number_of_cities, connected_neighbours, rewire_probability)
    for i in range(number_of_cities):
        world.append(make_city(f"City {i}", connections[i]))
    return world


world_test = make_world(10)
assert 10 == len(world_test)


def copy_world(world: list) -> list:
    """
    Create and return a copy of the world.

    :param world: A list of cities representing the world to be copied.
    :type world: A list of cities, of the form [[city 0, status, [neighbours]], [[city 1, status, [neighbours]] ... ]
    :return: A copy of the list of cities.
    :return: A list of lists of the form [[string, bool, [integers]], [string, bool, [integers]], ... ]
    """
    return copy.deepcopy(world)


world_test = make_world(10)
copied_world_test = copy_world(world_test)
assert world_test == copied_world_test
assert not (world_test is copied_world_test)
assert not (world_test[0] is copied_world_test[0])
assert not (world_test[0][2] is copied_world_test[0][2])


def draw_world(world: list) -> None:
    """
    Calling this function will display an image representing the world in its current state.
    Draw the cities with their names, their connections, and represent the city's infection status with the vertex's
    colour (cyan --- not infected, red --- infected).
    :param world: A list of cities representing the world.
    :type world: A list of cities, of the form [[city 0, status, [neighbours]], [[city 1, status, [neighbours]] ... ]
    """
    network = nx.Graph()
    city_infection_state_colours = []
    plt.clf()

    # Create all the city nodes and set colours
    for i, city in enumerate(world):
        network.add_node(i)
        if city[1]:
            city_infection_state_colours.append("r")
        else:
            city_infection_state_colours.append("c")

    # Add edges between nodes (cities) _after_ all nodes are created to
    # eliminate issues with networkx's automatic node numbering and labels
    for i, city in enumerate(world):
        for neighbour in city[2]:
            network.add_edge(i, neighbour)

    layout = nx.circular_layout(network)
    nx.draw_networkx(network, pos=layout, with_labels=True, node_color=city_infection_state_colours, node_size=500)
    plt.show()

# Eyeball test required --- uncomment to view test
"""
draw_world(
    [
        ["City 0", False, [4, 1]],
        ["City 1", True, [0, 2]],
        ["City 2", False, [1, 3]],
        ["City 3", True, [2, 4]],
        ["City 5", False, [3, 0]],
    ]
)"""


def draw_number_of_cities_infected(number_of_cities_infected_list: list) -> None:
    """
    Draw a line plot of the number of cities infected in the world over time. The parameter provided will be a list of
    the number of cities infected at each time step of the simulation, with index 0 being the first observation of the
    number of cities infected, and the last index will be the last observation.

    :param number_of_cities_infected_list: A list of the number of cities infected at each step of a simulation.
    :type number_of_cities_infected_list: List of Integers.
    """
    plt.clf()
    plt.plot(number_of_cities_infected_list)
    plt.title("The Number of Cities Infected In The World Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Number of Cities Infected")
    plt.show()


# Eyeball test required --- uncomment to view test
# draw_number_of_cities_infected([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1])


def draw_distribution(simulation_steps_list: list) -> None:
    """
    Creates a histogram of the distribution of simulation runtimes (in total steps).

    :param simulation_steps_list: Collection of simulation runtimes (in total steps)
    :type simulation_steps_list: List of integers
    """
    plt.clf()
    plt.hist(simulation_steps_list)
    plt.title("Distribution of Simulation Runtimes in Total Steps")
    plt.xlabel("Total Simulation Steps")
    plt.ylabel("Count")
    plt.show()


# Eyeball test required --- uncomment to view test
# draw_distribution([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])


def is_infected(city: list) -> bool:
    """
    Return the infection state of the provided city. True if the city is infected, False otherwise.

    :param city: City to retrieve state from
    :type city: A list of the form [string, bool, [integers]]
    :return: True if the city is infected, False otherwise
    :rtype: Boolean
    """


# city_is_infected_test = make_city("", [])
# city_is_infected_test[1] = False
# assert False == is_infected(city_is_infected_test)
# city_is_infected_test[1] = True
# assert True == is_infected(city_is_infected_test)


def get_neighbours(city: list) -> list:
    """
    Return the provided city's list of neighbours indices. Note, the list of neighbours are indices of the neighbours,
    not cities themselves.

    :param city: An encoding of a city.
    :type city: A list of the form [string, bool, [integers]].
    :return: The city's list of neighbour indices.
    :rtype: A list of integers.
    """


# city_neighbours_test = make_city("", [])
# assert [] == get_neighbours(city_neighbours_test)
# city_neighbours_test = make_city("", [0, 1, 2])
# assert [0, 1, 2] == get_neighbours(city_neighbours_test)


def infect(city: list) -> list:
    """
    Return a copy of the city as infected; return a copy of the city with the infection status set to True.

    :param city: City to be infected
    :type city: A list of the form [string, bool, [integers]]
    :return: A copy of the provided city with the infected status set to True
    :rtype: A list of the form [string, bool, [integers]]
    """


# city_infect_test_a = make_city("", [])
# city_infect_test_b = infect(city_infect_test_a)
# assert True == city_infect_test_b[1]
# city_infect_test_c = infect(city_infect_test_b)
# assert True == city_infect_test_c[1]
# assert not (city_infect_test_a is city_infect_test_b)
# assert not (city_infect_test_b is city_infect_test_c)


def cure(city: list) -> list:
    """
    Return a copy of the city as not infected; return a copy with the infection status set to False.

    :param city: City to be cured
    :type city: A list of the form [string, bool, [integers]]
    :return: A copy of the provided city with the infected status set to False
    :rtype: A list of the form [string, bool, [integers]]
    """


# city_cure_test_a = make_city("", [])
# city_cure_test_a[1] = True
# city_cure_test_b = cure(city_cure_test_a)
# assert False == city_cure_test_b[1]
# city_cure_test_c = cure(city_cure_test_b)
# assert False == city_cure_test_c[1]
# assert not (city_cure_test_a is city_cure_test_b)
# assert not (city_cure_test_b is city_cure_test_c)


def number_of_cities_infected(world: list) -> int:
    """
    Count the number of cities that are currently infected in the world.

    :param world: A list of cities representing the world.
    :type world: A list of cities, of the form [[city 0, status, [neighbours]], [[city 1, status, [neighbours]] ... ].
    :return: The number of cities currently infected in the world.
    :rtype: Integer.
    """


# assert 0 == number_of_cities_infected([])
# assert 0 == number_of_cities_infected([["", False, []], ["", False, []], ["", False, []]])
# assert 3 == number_of_cities_infected([["", True, []], ["", True, []], ["", True, []]])
# assert 2 == number_of_cities_infected([["", True, []], ["", False, []], ["", True, []]])
# assert 1 == number_of_cities_infected([["", True, []], ["", False, []], ["", False, []]])
# assert 1 == number_of_cities_infected([["", False, []], ["", True, []], ["", False, []]])
# assert 1 == number_of_cities_infected([["", False, []], ["", False, []], ["", True, []]])


def is_world_completely_infected(world: list) -> bool:
    """
    Check if the world is completely infected. The world is determined to be completely infected if all cities in the
    world have their infection status as True. This function returns True if the world is completely infected and False
    otherwise.

    :param world: A list of cities representing the world.
    :type world: A list of cities, of the form [[city 0, status, [neighbours]], [[city 1, status, [neighbours]] ... ].
    :return: True if the world is completely infected (all cities infected), False otherwise.
    :rtype: Boolean.
    """


# assert True == is_world_completely_infected([])
# assert True == is_world_completely_infected([["", True, []], ["", True, []], ["", True, []]])
# assert False == is_world_completely_infected([["", False, []], ["", False, []], ["", False, []]])
# assert False == is_world_completely_infected([["", True, []], ["", False, []], ["", False, []]])
# assert False == is_world_completely_infected([["", False, []], ["", True, []], ["", False, []]])
# assert False == is_world_completely_infected([["", False, []], ["", False, []], ["", True, []]])


def simulation_step(world: list, spread_probability: float, cure_probability: float) -> list:
    """
    Simulate a step of the infectious disease scenario and return the resulting world.

    Each city, if infected, has (a) a chance to spread the disease to a neighbouring city and (b) a chance to be cured.
    Infection happens to one of the current city's neighbours and curing happens to the current city.

    The function ensures that city 0 is always infected when completed.

    This function executes such that all decisions on curing and infecting are based on the parameter `world` and the
    final resulting world after the simulation step is returned. This is to treat the simulation step as if all cities
    in the world are infecting/curing at the same time.

    :param world: A list of cities representing the world.
    :type world: A list of cities, of the form [[city 0, status, [neighbours]], [[city 1, status, [neighbours]] ... ].
    :param spread_probability: Probability that a city will spread its infection to another neighbouring city.
    :type spread_probability: Float, between 0 -- 1.
    :param cure_probability: Probability that a city will be cured of its infection.
    :type cure_probability: Float, between 0 -- 1.
    :return: A list of cities representing the state of the world after the simulated step.
    :return: A list of lists of the form [[string, bool, [integers]], [string, bool, [integers]], ... ]
    """


# sim_step_world_test = [
#     ["City 0", True, [1]],
#     ["City 1", False, [2]],
#     ["City 2", True, [3]],
#     ["City 3", False, [4]],
#     ["City 4", False, [0]],
# ]
# next_world = simulation_step(sim_step_world_test, 0, 0)
# assert not (next_world is sim_step_world_test)
# assert True == next_world[0][1]
# assert False == next_world[1][1]
# assert True == next_world[2][1]
# assert False == next_world[3][1]
# assert False == next_world[4][1]
# next_world = simulation_step(sim_step_world_test, 0, 1)
# assert True == next_world[0][1]
# assert False == next_world[1][1]
# assert False == next_world[2][1]
# assert False == next_world[3][1]
# assert False == next_world[4][1]
# next_world = simulation_step(sim_step_world_test, 1, 1)
# assert True == next_world[0][1]
# assert True == next_world[1][1]
# assert False == next_world[2][1]
# assert True == next_world[3][1]
# assert False == next_world[4][1]
# next_world = simulation_step(sim_step_world_test, 1, 0)
# assert True == next_world[0][1]
# assert True == next_world[1][1]
# assert True == next_world[2][1]
# assert True == next_world[3][1]
# assert False == next_world[4][1]


def simulate_infections_disease(
    world: list, spread_probability: float, cure_probability: float, cutoff: int = 100000
) -> list:
    """
    Run a simulation of an infections disease scenario on the provided world with the specified parameters and return a
    list of the number of cities infected for each step of the simulation, with index 0 being the first step. Note that
    index 0 should always be 1 as city 0 always starts as the only infected city. Although the provided world may have
    cities having different infection statuses, this function will automatically set city 0 as infected before the
    simulation starts. This function will run until the whole whole is infected, or the cutoff value is hit. The purpose
    of the cutoff is to ensure that the simulation does not run forever. If the simulation hits the cutoff but you
    expect that the simulation would have finish had it run longer, then increase the value of the cutoff.

    :param world: A list of cities representing the world that the simulation is run on.
    :type world: A list of cities, of the form [[city 0, status, [neighbours]], [[city 1, status, [neighbours]] ... ].
    :param spread_probability: Probability that a city will spread its infection to another neighbouring city.
    :type spread_probability: Float, between 0 -- 1.
    :param cure_probability: Probability that a city will be cured of its infection.
    :type cure_probability: Float, between 0 -- 1.
    :param cutoff: Ensure the simulation runs no longer than this number of steps.
    :type cutoff: Integer
    :return: A list of the number of infected cities at each step of the pandemic
    :rtype: A list of integers
    """


# world = make_world(10, 4, 0.33)
# assert [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] == simulate_infections_disease(world, 0, 0, 10)
# assert [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] == simulate_infections_disease(world, 0, 1, 10)
# Eyeball test required --- uncomment to view test
# draw_number_of_cities_infected(simulate_infections_disease(0.4, 0.25))

# Run a simulation on a new world

# Eyeball test required --- uncomment to view test
# draw_distribution(number_of_iterations)
