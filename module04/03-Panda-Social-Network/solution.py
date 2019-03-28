class Panda:

    def __init__(self, name, email, gender):
        self.panda_name = name
        if '@' not in email:
            raise AttributeError
        self.panda_email = email
        self.panda_gender = gender
        self.friends = []

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

    def getFriends(self):
        return self.friends

    def __str__(self):
        return self.panda_name

    def __hash__(self):
        return hash(self.panda_name + self.panda_email)

    def __eq__(self, other):
        name = self.panda_name == other.panda_name
        email = self.panda_email == other.panda_email
        gender = self.panda_gender == other.panda_gender
        return (name and email and gender)


class PandaSocialNetwork:

    def __init__(self):
        self.pandas = []
        self.friends = {}
        self.already_counted = []

    def add_panda(self, panda):
        if panda in self.pandas:
            raise PandasAlreadyThere
        self.pandas.append(panda)
        self.friends[panda] = []

    def has_panda(self, panda):
        return panda in self.pandas

    def make_friends(self, panda1, panda2):
        if panda1 not in self.pandas:
            self.add_panda(panda1)
        if panda2 not in self.pandas:
            self.add_panda(panda2)

        if panda2 in self.friends and panda1 in self.friends[panda2]:
            raise PandasAlreadyFriends

        self.friends[panda1].append(panda2)
        self.friends[panda2].append(panda1)

        panda1.friends.append(panda2)
        panda2.friends.append(panda1)

    def are_friends(self, panda1, panda2):
        return panda1 in self.friends[panda2]

    def friends_of(self, panda):
        if panda not in self.pandas:
            return False

        return self.friends[panda]

    def connection_level(self, panda1, panda2):
        if panda1 not in self.pandas or panda2 not in self.pandas:
            return False

        if panda1 in self.friends and panda2 in self.friends[panda1]:
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
        self.already_counted = []
        if level < 2:
            return len([friend_panda for friend_panda in self.friends[panda] if friend_panda.gender() == gender])
        else:
            return self.iterate_my_friends(panda, gender)

    def iterate_my_friends(self, panda, gender):
        count = 0
        for panda_member in self.pandas:
            if panda_member == panda:
                continue

            if self.connection_level(panda, panda_member) > 0 and panda_member.gender() == gender:
                count += 1

        return count



            # self.already_counted.append(friend_panda)
            # count += self.iterate_my_friends(friend_panda, gender)
class PandasAlreadyThere(AttributeError):
    pass

class PandasAlreadyFriends(AttributeError):
    pass

