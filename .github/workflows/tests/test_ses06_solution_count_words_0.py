test = {
  'name': 'test_ses06_solution_count_words_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = count_words('test sentence')
          >>> print(x['test'])
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
