from unittest import TestCase, main 

import os
import pathlib

from src.sqlite_manager_package.sqlite_manager import SqliteManager
from example.example_query import ExampleQuery
from example.example_data import teachers


class SqliteManagerTest(TestCase):
    db_path = pathlib.Path("./data/temp.db") 

    def verify_cwd(self) -> None:
        if pathlib.Path().cwd().name != "sqlite_manager":
            raise ValueError("Error, you are in the wrong cwd.")

    def setUp(self) -> None:
        self.verify_cwd()
        try:
            self.db_file = open(self.db_path, "x")
            assert self.db_path.exists()
            print(f"Successfully created file {self.db_path.name}.")
        except OSError as os_error:
            print(f"Error: {os_error}")
    
    def tearDown(self) -> None:
        try:
            self.db_file.close()
            print(f"Successfully closed file {self.db_path.name}.")
            os.remove(self.db_path)
            assert self.db_path.exists() == False
            print(f"Successfully removed file {self.db_path.name}.")
        except OSError as os_error:
            print(f"Error: {os_error}")

    def test_execute_query(self):
        manager = SqliteManager(self.db_path.as_posix())
        manager.execute_query(
            ExampleQuery.create_teacher_table)
        self.assertTrue(manager.is_table_exist('teacher'))

    def test_excecute_many_queries(self):
        manager = SqliteManager(self.db_path.as_posix())

        manager.execute_query(
            ExampleQuery.create_teacher_table)

        manager.excecute_many_queries(
            ExampleQuery.populate_teacher_table, teachers)

        self.assertTrue(manager.is_table_exist('teacher'))

        teacher_list = manager.select_query("SELECT * FROM teacher")
        for teacher in teacher_list:
            print(teacher)
        
        self.assertRaises(AssertionError, manager.select_query, ("CREATE XXXXX"))


if __name__ == '__main__':
    main()
