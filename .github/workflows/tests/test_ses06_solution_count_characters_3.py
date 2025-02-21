test = {
  'name': 'test_ses06_solution_count_characters_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = count_characters('hello world')
          >>> print(x['l'])
          3
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
