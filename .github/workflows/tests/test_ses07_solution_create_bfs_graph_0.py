test = {
  'name': 'test_ses07_solution_create_bfs_graph_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ex_graph = create_bfs_graph()
          >>> [x in ex_graph.children_of('Jared') for x in ['John', 'Helena', 'Donald', 'Paul']]
          [False, False, True, True]
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ses07 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
