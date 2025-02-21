test = {
  'name': 'test_ses06_solution_print_dict_values_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print_dict_values({'banana': 'yellow', 'apple': 'green', 'berry': 'blue'})
          apple green
          banana yellow
          berry blue
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
