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

def select(id):
    member =None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    
    if results is not None:
        member = Member(results[0]['first_name'], results['last_name'], results['age'], results['sex'], results['id'])
    return member

# update member
def update(member):
    sql = "UPDATE me SET (first_name, last_name, age, sex) = (%s, %s, %s, %s,) WHERE id = %s"
    values = [member.first_name, member.last_name, member.age, member.sex, member.id]


# delete all members

# delete specific



# get member by booking