"""module bootcamper"""

class Bootcamper(User):
    """Class for bootcampers inheriting from user class"""

    def __init__(self, username, email, password):
        User.__init__(self, username, email, password)
        self.username = username
        self.email = email
        self.password = password

    def view_score(self, username):
        """method for viewing scores"""
        if get_score_for user is None:
            return No candidate results

class LF(User):
    """class for LFs"""

    def __init__(self, username, email, password):
        User.__init__(self, username, email, password)
        self.username = username
        self.email = email
        self.password = password

    def view_all_scores(self, username):
        """method for getting all scores"""
        if get_scores is None:
            return No scores added


