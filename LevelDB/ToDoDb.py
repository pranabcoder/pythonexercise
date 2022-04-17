import DbHelper


def main():
    run = 1
    DbHelper.create_table()

    while run:
        print("\n")
        print("1. Insert new task in todo list")
        print("2. View the todo list")
        print("3. Delete the task list")
        print("4. exit")
        x = input("Choose any of above option:")
        if x == "1":
            task = str(input("Enter your task:"))
            DbHelper.data_entry(task)
        elif x == "2":
            DbHelper.print_data()
        elif x == "3":
            index_to_delete = int(input("Enter the index of the task to delete:"))
            DbHelper.delete_task(index_to_delete)
        elif x == "4":
            run = 0
        else:
            print("Please choose valid option")

    DbHelper.close_cursor()


if __name__ == '__main__':
    main()
