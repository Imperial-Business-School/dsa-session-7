test = {
  'name': 'test_ses06_solution_count_words_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = count_words('it is what it is')
          >>> print(x['it'])
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
