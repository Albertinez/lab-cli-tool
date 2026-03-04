import argparse
from lib.models import Task, User

users = {}

def add_task(args):
    user = users.get(args.username) or User(args.username)
    users[args.username] = user
    task = Task(args.task_description)
    user.add_task(task)

def complete_task(args):
    user = users.get(args.username)
    if user:
        for task in user.tasks:
            if task.description == args.task_description:
                task.complete()
                return
        print("❌ Task not found.")
    else:
        print("❌ User not found.")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("username")
    add_parser.add_argument("task_description")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
    complete_parser.add_argument("username")
    complete_parser.add_argument("task_description")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()