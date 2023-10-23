import time
from homework.tasks import longtime_add, task_two


def test_example():
    result = longtime_add.delay(1, 2)
    result2 = task_two.delay(3, 3)
    # at this time, our task is not finished, so it will return False
    print("Task finished? ", result.ready())
    print("Task result: ", result.result)
    print("Task2 finished? ", result2.ready())
    print("Task2 result: ", result2.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print("Task finished? ", result.ready())
    print("Task result: ", result.result)
    print("Task2 finished? ", result2.ready())
    print("Task2 result: ", result2.result)
    assert result == 3
