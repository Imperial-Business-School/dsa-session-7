test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> d = {'dog', 'cat', 'bird', 'cow'}
          >>> type(d)
          0b7118a32cccff9b9bd1870b7f9da066
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> 'cat' in d
          a7465ecc0421c9e0085a8a012fce1e93
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> d.add('mouse')
          >>> len(d)
          17676197347896dd77ecff7024cf78ad
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Write Error if there's an error
          >>> x, y = [9,3,1], 1 
          >>> y
          ffa75b1b87165b2ccfd71fdee28914dc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Write Error if there's an error
          >>> x, y = 4, 1 
          >>> y, x = x, y 
          >>> x
          ffa75b1b87165b2ccfd71fdee28914dc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Write Error if there's an error
          >>> def f(x, y):
          ...     a, b = 3*x, 2*y
          ...     return a, b
          >>> x, y = f(2, 2)
          >>> x
          3298fb8a656a2d5ee7c6ca45f9c3d9b7
          # locked
          >>> y
          ef50822dd004a6ebc5cba5a9fddf1767
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> animals = {'eagle': 'bird', 'hawk': 'bird', 'manatee': 'mammal', 'finch': 'bird'}
          >>> bird_count = 0
          >>> for animal in animals:
          ...    if animals[animal] == 'bird':
          ...        bird_count += 1
          >>> bird_count
          453cf288da1dfd386b98842f7679fc94
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
