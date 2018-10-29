"""module bootcamper"""

class Bootcamper(User):
    """Class for bootcampers inheriting from user class"""

    def __init__(self, username, email, password):
        User.__init__(self, username, email, password)

    def view_score(self, username):
        """method for viewing scores"""
        score = score_data.get_score_for_user(self.username)
        if score is None:
            return "No candidate results"
        return score

class LF(User):
    """class for LFs"""

    def __init__(self, username, email, password):
        User.__init__(self, username, email, password)

    def view_all_scores(self, username, score_data, user_data):
        """method for getting all scores"""
        scores = score_data.get_scores_supervised_by_lfa(self.username, user_data)
        if not scores:
            return "No scores added"
        return scores


