class Panda:

    def __init__(self, name, email, gender):
        self.panda_name = name
        if '@' not in email:
            raise AttributeError
        self.panda_email = email
        self.panda_gender = gender

    def name(self):
        return self.panda_name

    def email(self):
        return self.panda_email

    def gender(self):
        return self.panda_gender

    def isMale(self):
        return self.panda_gender == 'male'

    def isFemale(self):
        return self.panda_gender == 'female'

    def __str__(self):
        return self.panda_name

    def __hash__(self):
        return hash(self.panda_name + self.panda_email)

    def __eq__(self, other):
        return self.panda_name == other.panda_name and self.panda_email == other.panda_email and self.panda_gender == other.panda_gender


class PandaSocialNetwork:

    def __init__(self):
        self.pandas = []
        self.friends = {}

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise PandasAlreadyThere
        self.pandas.append(panda)
        self.friends[panda] = []

    def has_panda(self, panda):
        return panda in self.pandas

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends

        self.friends[panda1].append(panda2)
        self.friends[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda1 in self.friends[panda2]

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False

        return self.friends[panda]

    def connection_level(self, panda1, panda2):
        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False

        if self.are_friends(panda1, panda2):
            return 1

        return self.check_friend_pandas_for_connection(panda1, panda2, already_checked=[])

    def check_friend_pandas_for_connection(self, panda, search_for, level=1, already_checked=[]):
        level += 1

        # panda hasn't any friends
        if not self.friends[panda]:
            return -1

        for friend_panda in self.friends[panda]:

            # friend_panda has any friends?
            if not self.friends[friend_panda]:
                continue

            # prevent loop between friends
            if friend_panda in already_checked:
                continue

            already_checked.append(friend_panda)

            if search_for in self.friends[friend_panda]:
                return level

            new_level = self.check_friend_pandas_for_connection(friend_panda, search_for, level, already_checked)
            if new_level > level:
                return new_level

        return -1

    def are_connected(self, panda1, panda2):
        return True if self.check_friend_pandas_for_connection(panda1, panda2) > 0 else False

    def how_many_gender_in_network(self, level, panda, gender):
        if level < 2:
            return len([friend_panda for friend_panda in self.friends[panda] if friend_panda.gender() == gender])
        return self.iterate_my_friends(panda, gender)

    def iterate_my_friends(self, panda, gender):
        count = 0
        for panda_member in self.pandas:
            if panda_member == panda:
                continue

            if self.connection_level(panda, panda_member) > 0 and panda_member.gender() == gender:
                count += 1

        return count


class PandasAlreadyThere(AttributeError):
    pass


class PandasAlreadyFriends(AttributeError):
    pass

