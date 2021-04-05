from db.run_sql import run_sql
from models.exclass import Exclass
from models.member import Member

# save new exclass
def save(exclass):
    sql = "INSERT INTO exclasses(name, activity_type, duration, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [exclass.name, exclass.activity_type, exclass.duration, exclass.capacity]
    results = run_sql(sql, values)
    exclass.id = results[0]['id']
    return exclass
    
# select all classes
def select_all():
    exclasses = []
    
    sql = "SELECT * FROM exclasses"
    results = run_sql(sql)
    
    for row in results:
        exclass = Exclass(row['name'], row['activity_type'], row['duration'], row['capacity'], row['id'])
        exclasses.append(exclass)
    return exclasses


# select specific class by id
def select(id):
    exclass = None
    sql = 'SELECT * FROM exclasses WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)[0]
    
    if results is not None:
        exclass = Exclass(results['name'], results['activity_type'], results['duration'], results['capacity'], results['id'])
    return exclass

# delete all exclassess
def delete_all():
    sql = "DELETE FROM exclasses"
    run_sql(sql)

# delete specific exclass by id
def delete(id):
    sql = "DELETE FROM exclasses WHERE id = %s"
    values = [id]
    run_sql(sql, values)[0]
    
# update specific exclass
def update(exclass):
    sql = "UPDATE exclasses SET (name, activity_type, duration, capacity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [exclass.name, exclass.activity_type, exclass.duration, exclass.capacity, exclass.id]
    run_sql(sql, values)