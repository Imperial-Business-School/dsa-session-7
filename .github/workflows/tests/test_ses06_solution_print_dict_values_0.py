test = {
  'name': 'test_ses06_solution_print_dict_values_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print_dict_values({'Zoe': 'ICL', 'Mark': 'UCL'})
          Mark UCL
          Zoe ICL
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
