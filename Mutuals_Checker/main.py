# Imports
import requests
import json

ids_to_check = [[126166576, 88228901], [126166576, 417506429]]

class Mutuals:
    friends_1 = []
    friends_2 = []

    @staticmethod
    def get_user_friends(user_id):
        get = json.loads(requests.get("https://friends.roblox.com/v1/users/" + str(user_id) + "/friends").content)["data"]

        return get

    @staticmethod
    def calculateAmount(tbl):
        amount = 0

        for i in tbl:
            amount += 1

        return amount

    def __init__(self, user_id_1, user_id_2):
        self.friends_1 = self.get_user_friends(user_id_1)
        self.friends_2 = self.get_user_friends(user_id_2)

    def get_mutuals(self):
        mutuals = []

        for friend in self.friends_1:
            for other_friend in self.friends_2:
                if friend["id"] == other_friend["id"]:
                    mutuals.append(friend["name"])

                    break

        return mutuals

    def print_users_info(self):
        user_1_friend_count = 0
        user_2_friend_count = 0
        
        user_1_friend_count = self.calculateAmount(self.friends_1)
        user_2_friend_count = self.calculateAmount(self.friends_2)

        print("\nDATA\n")
        print("===========")

        print("User 1 Friend Count: " + str(user_1_friend_count) + "\n")
        print("User 2 Friend Count: " + str(user_2_friend_count) + "\n")

        print("\nMutual Friends\n")
        print("=====================\n")

        mutuals = self.get_mutuals()

        for mutual in mutuals:
            print(mutual)

# Main Method
if __name__ == "__main__":
    for ids in ids_to_check:
        mutuals = Mutuals(ids[0], ids[1])
        mutuals.print_users_info()
