
class Jumper:

    def __init__(self):
        self.max_tries = 0

    def _parachute(self, tries):
        self.parachute = [ 
"""
        
        _____
       /_____\
       \     /
        \   /
          0
        / | \
         / \
        
    ^^^^^^^^^^^^^
""",
"""
        
       /_____\
       \     /
        \   /
          0
        / | \
         / \
        
    ^^^^^^^^^^^^^

""",
"""
        
        _____\
       \     /
        \   /
          0
        / | \
         / \
        
    ^^^^^^^^^^^^^

""",
"""
        
        _____ 
       \     /
        \   /
          0
        / | \
         / \
        
    ^^^^^^^^^^^^^

""", 
"""
        
       \     /
        \   /
          0
        / | \
         / \
        
    ^^^^^^^^^^^^^

""",
"""
        
             /
        \   /
          0
        / | \
         / \
        
    ^^^^^^^^^^^^^

""",
"""
        
        \   /
          0
        / | \
         / \
        
    ^^^^^^^^^^^^^

""",
"""
        
            /
          0
        / | \
         / \
        
    ^^^^^^^^^^^^^

""",
"""
        
          X
        / | \
    ^^^^^^^^^^^^^
        /   \
"""
        ]
        self.max_tries = len(self.parachute)
        
        return