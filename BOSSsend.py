import threading
from concurrent.futures.thread import ThreadPoolExecutor
from .BOSSluojike import boss_gogo, get_of
def run(i):
    get_c = get_of().boss(i)
    boss_gogo(*get_c)
if __name__ == '__main__':
    student_list=["run"]
    for i in student_list:
        print("====================={}=====================".format(i))
        run(i)
        print("---------------------------------{}---------------------------------".format(i))
