"""Data file- this holds all the data access objects and methods required by the application"""


class UserDAO:
    """Data access object for users. Holds data for all users"""
    def __init__(self):
        self.users = []

    def add_user(self, user):
        """Add a single user to the db"""
        if user.is_valid():
            return False
        if self.user_exists(user):
            return False
        self.users.append(user)
        return True

    def update_user(self, updated_user):
        """Update a user"""
        for index, user in enumerate(self.users):
            if user.username == updated_user.username:
                self.users[index] = updated_user
                return True
        return False

    def get_users(self):
        """Get all users"""
        return self.users

    def get_user_by_username(self, username):
        """Get a user by a username"""
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_users_by_lfa(self, lfa):
        """Get all users supervised by this lfa"""
        return [user for user in self.users if user.lfa == lfa.username]

    def user_exists(self, user):
        """Check if a particular user exists"""
        return True if self.get_user_by_username(user.username) else False

    def get_lfas(self):
        """Get all lfas"""
        return [user for user in self.users if user.type == 'lfa']


class ScoreDAO:
    """Holds data on all scores"""
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        """Add a score to the db"""
        self.scores.append(score)

    def update_score(self, updated_score):
        """Update a particular score"""
        for index, score in enumerate(self.scores):
            if score.user == updated_score.user:
                self.scores[index] = updated_score
                return True
        return False

    def get_scores(self):
        """Get all scores"""
        return self.scores

    def get_score_for_user(self, user):
        """Get a score by user"""
        for score in self.scores:
            if score.user == user.username:
                return score
        return None

    def get_scores_supervised_by_lfa(self, lfa, user_data):
        """Get user scores supervised by this lfa"""
        return [score for score in self.scores if user_data.get_user_by_username(score.user).lfa == lfa.username]
