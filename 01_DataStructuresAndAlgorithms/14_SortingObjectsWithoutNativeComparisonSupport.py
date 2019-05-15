from operator import attrgetter


# 기본 비교 기능 없이 객체 정렬


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


user_list = [User(23), User(3), User(99)]
lambda_sorted_user_list = sorted(user_list, key=lambda user: user.user_id)
attr_sorted_user_list = sorted(user_list, key=attrgetter('user_id'))

print(user_list)
print(lambda_sorted_user_list)
print(attr_sorted_user_list)

# attrgetter min(), max() 에도 사용할 수 있다
print(min(user_list, key=attrgetter('user_id')))
print(max(user_list, key=attrgetter('user_id')))
