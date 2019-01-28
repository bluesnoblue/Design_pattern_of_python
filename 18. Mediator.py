"""
18. Mediator（中介者）

意图：
用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。

适用性：
一组对象以定义良好但是复杂的方式进行通信。产生的相互依赖关系结构混乱且难以理解。
一个对象引用其他很多对象并且直接与这些对象通信,导致难以复用该对象。
想定制一个分布在多个类中的行为，而又不想生成太多的子类。
"""

import time


class TC:
    def __init__(self):
        self._tm = tm
        self._bProblem = 0

    def setup(self):
        print('Setting up the Test')
        time.sleep(1)

    def execute(self):
        if not self._bProblem:
            print('Executing the test')
        else:
            print('Problem in setup,Test not excuted')

    def tearDown(self):
        if not self._bProblem:
            print("Tearing down")
            time.sleep(1)
            self._tm.publishReport()
        else:
            print("Test not executed. No tear down required.")

    def setTM(self, TM):
        self._tm = TM

    def setProblem(self, value):
        self._bProblem = value


class Reporter:
    def __init__(self):
        self._tm = None

    def prepare(self):
        print('Reporter Class is preparing to report the result')
        time.sleep(1)

    def report(self):
        print('Reporting the result of Test')
        time.sleep(1)

    def setTM(self, TM):
        self._tm = tm


class DB:
    def __init__(self):
        self._tm = None

    def insert(self):
        print('DB:Insertign the executing begin status in the Databse')
        time.sleep(1)
        #Follwing code is simulate a comunicaiton from DB to TC
        import random
        if random.randrange(1,4) == 3 :
            return -1

    def update(self):
        print("DB:Updating the test results in Database")
        time.sleep(1)

    def setTM(self, TM):
        self._tm = tm

class TestManager:
    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepareReporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.setProblem()

    def setReporter(self, reporter):
        self._reporter = reporter

    def setDB(self, db):
        self._db = db

    def publishReport(self):
        self._db.update()
        rvalue = self._reporter.report()

    def setTC(self, tc):
        self._tc = tc


if __name__ == '__main__':
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.setReporter(reporter)
    tm.setDB(db)
    db.setTM(tm)

    while True:
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()
