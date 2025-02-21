test = {
  'name': 'test_ses06_solution_divide_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> divide(10, 0)
          No division by 0.
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
