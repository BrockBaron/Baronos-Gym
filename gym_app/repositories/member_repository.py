from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member

# add / save new member 

def save(member):
    sql = "INSERT INTO members (first_name, second_name, age, sex) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.second_name, member.age, member.sex]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member
    
# select all members

def select_all():
    members = []
    
    sql = "SELECT * FROM members ORDER BY id"
    results = run_sql(sql,)
    
    for row in results:
        member = Member(row['first_name'], row['second_name'], row['age'], row['sex'], row['id'])
        members.append(member)
    return members

# selct by specific member by id

def select(id):
    member =None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    
    if results is not None:
        member = Member(results['first_name'], results['second_name'], results['age'], results['sex'], results['id'])
    return member

# update member
def update(member):
    sql = "UPDATE members SET (first_name, second_name, age, sex) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.second_name, member.age, member.sex, member.id]
    run_sql(sql, values)

# delete all members
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


# delete specific
def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)[0]
    
    
# get member by booking
def get_by_exclass(exclass):
    sql = "SELECT members.* FROM members INNER JOIN bookings ON members.id = bookings.member_id WHERE bookings.exclass_id = %s"
    values = [exclass.id]
    results = run_sql(sql, values)
    
    members = []
    for row in results:
        member = Member(row['first_name'], row['second_name'], row['age'], row['sex'], row['id'])
        members.append(member)
    
    return members
