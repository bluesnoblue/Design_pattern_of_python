"""
Factory Method 工厂方法
意图：
定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

适用性：
当一个类不知道它所必须创建的对象的类的时候。
当一个类希望由它的子类来指定它所创建的对象的时候。
当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。
"""
class ChinaGetter(object):

    def __init__(self):
        self.trans = {'dog': '小狗', 'cat': '小猫'}

    def get(self,msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglishGetter(object):

    def get(self,msgid):
        return str(msgid)

def get_localizer(language='English'):
    """the factory method"""

    languages = {'English':EnglishGetter,'China':ChinaGetter}
    return languages[language]()

e,g = get_localizer(),get_localizer('China')

for msg_id in ['dog', 'parrot', 'cat' ,'bear']:
    print(e.get(msg_id),g.get(msg_id))