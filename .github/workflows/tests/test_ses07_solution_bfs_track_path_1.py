test = {
  'name': 'test_ses07_solution_bfs_track_path_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ex_graph = create_bfs_graph()
          >>> bfs_dists, bfs_paths = bfs_track_path(ex_graph, 'John')
          >>> [bfs_dists['Donald'], bfs_dists['Jared']]
          [4, 3]
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
