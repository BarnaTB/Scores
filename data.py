"""Data file- this holds all the data access objects and methods required by the application"""


class UserDAO:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if self.user_exists(user):
            return False
        self.users.append(user)
        return True

    def update_user(self, updated_user):
        for index, user in enumerate(self.users):
            if user.username == updated_user.username:
                self.users[index] = updated_user
                return True
        return False

    def get_users(self):
        return self.users

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_users_by_lfa(self, lfa):
        return [user for user in self.users if user.lfa == lfa.username]

    def user_exists(self, user):
        return True if self.get_user_by_username(user.username) else False

    def get_lfas(self):
        return [user for user in self.users if user.type == 'lfa']


class ScoreDAO:
    def __init__(self):
        self.scores = []

    def get_scores(self):
        return self.scores

    def get_score_for_user(self, user):
        for score in self.scores:
            if score.user == user.username:
                return score
        return None
