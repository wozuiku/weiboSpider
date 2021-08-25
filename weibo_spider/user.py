class User:
    def __init__(self):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""

        self.id = ''
        self.nickname = ''
        self.gender = ''
        self.location = ''
        self.birthday = ''
        self.description = ''
        self.verified_reason = ''
        self.talent = ''
        self.education = ''
        self.work = ''

        self.weibo_num = 0
        self.following = 0
        self.followers = 0

        print('User init')

    def __str__(self):
        """返回一个对象的描述信息print(user)的时候调用"""
        result = ''
        result += u'用户昵称: %s\n' % self.nickname
        result += u'用户id: %s\n' % self.id
        result += u'微博数: %d\n' % self.weibo_num
        result += u'关注数: %d\n' % self.following
        result += u'粉丝数: %d\n' % self.followers
        print('User str')
        return result




user = User()
print(user)