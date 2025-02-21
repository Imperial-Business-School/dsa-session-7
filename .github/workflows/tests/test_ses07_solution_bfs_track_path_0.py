test = {
  'name': 'test_ses07_solution_bfs_track_path_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ex_graph = create_bfs_graph()
          >>> bfs_dists, prev_nodes = bfs_track_path(ex_graph, 'John')
          >>> [prev_nodes['Donald'], prev_nodes['Helena'], prev_nodes['John']]
          ['Jared', 'John', None]
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
