from dataclasses import dataclass
from typing import Optional
# from database import DatabaseManager

@dataclass
class Owner:
    first_name: str
    last_name: str
    email: str
    phone: str

    @staticmethod
    def from_database_record(record):
        """Tạo đối tượng Owner từ dữ liệu database."""
        if record:
            return Owner(
                first_name=record[0],
                last_name=record[1],
                email=record[2],
                phone=record[3],
            )
        return None

@dataclass
class User:
    name: str
    email: str
    role: str
    phone: Optional[int] = None
    
    def inTen(self):
        print(self.name)
    
    @staticmethod
    def from_database_record(record):
        """Tạo đối tượng User từ dữ liệu database."""
        if record:
            return User(
                name=record[0],
                email=record[1],
                phone=record[2],
                role=record[3],
            )
        return None

# ownerData = ("Owner", "Society", "owner@society.com", "093545458787")
# userData = ("User", "user@society.com", "023122145646", "5")

# o = Owner.from_database_record(ownerData)
# u = User.from_database_record(userData)

# print(o)
# print(u)


# db_manager = DatabaseManager("test.db")
# db_manager.create_table(
#     table_name='owners',
#     columns=['first_name', 'last_name', 'email', 'phone'],
# )

# db_manager.insert_data_from_csv(
#     csv_file='data/owners.csv',
#     table_name='owners',
# )

# owner_record = db_manager.select_data(table_name='owners')
# owner = Owner.from_database_record(owner_record)

# print(owner)