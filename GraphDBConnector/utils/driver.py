from dse.cluster import Cluster, GraphExecutionProfile, EXEC_PROFILE_GRAPH_DEFAULT, EXEC_PROFILE_GRAPH_SYSTEM_DEFAULT
from dse.graph import GraphOptions


def get_result():
    # create the default execution profile pointing at a specific graph
    graph_name = 'test'
    ep = GraphExecutionProfile(graph_options=GraphOptions(graph_name=graph_name))
    cluster = Cluster(execution_profiles={EXEC_PROFILE_GRAPH_DEFAULT: ep})
    session = cluster.connect()

    # use the system execution profile (or one with no graph_options.graph_name set) when accessing the system API
    session.execute_graph("system.graph(name).ifNotExists().create()", {'name': graph_name},
                          execution_profile=EXEC_PROFILE_GRAPH_SYSTEM_DEFAULT)

    # ... set dev mode or configure graph schema ...

    # // Property Labels
    result = session.execute_graph('schema.propertyKey("genreId").Text().create()')
    result = session.execute_graph('schema.propertyKey("name").Text().create()')

    # // Vertex labels
    # schema.vertexLabel("movie").properties("movieId","title","year").create()
    # schema.vertexLabel("person").properties("personId","name").create()
    result = session.execute_graph('schema.vertexLabel("genre").properties("genreId","name").create()')

    # // Edge labels
    # schema.edgeLabel("director").single().connection("movie","person").create()
    # schema.edgeLabel("belongsTo").single().connection("movie","genre").create()
    #
    # // Vertex indexes
    # schema.vertexLabel("movie").index("moviesById").materialized().by("movieId").add()
    # schema.vertexLabel("person").index("personsById").materialized().by("personId").add()
    # schema.vertexLabel("genre").index("genresByName").materialized().by("name").add()

    result = session.execute_graph('graph.addVertex(label,"genre","genreId","g2","name","Adventure")')
    data = ''
    for r in result:
        data = r

    # Drop the graph database
    session.execute_graph("system.graph(name).drop()", {'name': graph_name},
                          execution_profile=EXEC_PROFILE_GRAPH_SYSTEM_DEFAULT)
    #Test
    return str(data)

if __name__=='__main__':
    result = get_result()
    print result

