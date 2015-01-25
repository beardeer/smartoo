"""
Module for calculating performance and providing feedback to components
"""


class Feedback(object):
    """
    Record of user feedback after an exercise
    """
    pass


class ComponentsFeedbackAccumulator(object):
    """
    Class for accumulating and providing feedback to session components
    """
    def __init__(self, components):
        """
        Args:
            components (SessionComponentsQuadruple): components to
                provide feedback
        """
        self._components = components

    def accumulate_feedback(feedback):
        """
        Accumulated feedback -- should be called after each user answer.

        Args:
            feedback (Feedback): user feedback after an exercise
        """
        pass

    def provide_feedback():
        """
        Updates components' performance record using accumulated feedback.
        """
        pass


class ComponentPerformanceMeter(object):
    """
    Measures performance of a given component
    """
    pass
