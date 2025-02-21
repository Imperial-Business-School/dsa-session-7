test = {
  'name': 'test_ses07_solution_create_bfs_graph_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ex_graph = create_bfs_graph()
          >>> [x in ex_graph.children_of('Helena') for x in ['John', 'Helena', 'Donald', 'Paul']]
          [True, False, False, True]
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
