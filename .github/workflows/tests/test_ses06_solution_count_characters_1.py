test = {
  'name': 'test_ses06_solution_count_characters_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = count_characters('test')
          >>> print(x['t'])
          2
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ses06 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
