from workers import task

@task(schedule=10)
def do_something():
    print('I run every 10 seconds')