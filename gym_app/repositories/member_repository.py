from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member

# add / save new member 

def save(member):
    sql = "INSERT INTO members (first_name, last_name, age, sex) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_, member.age, member.sex]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member
    
# select all members

def select_all():
    members = []
    
    sql = "SELECT * FROM members"
    results = run_sql(sql,)
    
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['sex'], row['id'])
        members.append(member)
    return members

# selct by specific member by id

# delete members

# get member by booking

# get member by exclass