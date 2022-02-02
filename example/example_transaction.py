from src.sqlite_manager import SqliteManager
from example.example_data import teachers
from example.example_query import ExampleQuery

def do_some_transactions() -> None:
    manager = SqliteManager(sqlite_db_path='./data/teacher.db')

    manager.execute_query(ExampleQuery.create_teacher_table) 
    assert manager.is_table_exist('teacher')
    
    # manager.excecute_many_queries(ExampleQuery.populate_teacher_table, teachers)
    query_result = manager.select_query(ExampleQuery.select_count_row_in_teacher_table)
    assert query_result[0][0] == len(teachers)

if __name__ == '__main__':
    do_some_transactions()
