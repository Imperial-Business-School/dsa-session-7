test = {
  'name': 'test_ses06_solution_count_characters_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = count_characters('hello')
          >>> print(x['h'])
          1
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
