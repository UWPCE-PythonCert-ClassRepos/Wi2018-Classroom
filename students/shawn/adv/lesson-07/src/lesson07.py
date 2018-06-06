from peewee import *
from src.lesson07_schema import Person, Dept, Job

def seed():
    """
        add job data to database
    """
    people = [
        ('Andrew', 'Sumner', 'Andy'),
        ('Peter', 'Seattle', None),
        ('Susan', 'Boston', 'Beannie'),
        ('Pam', 'Coventry', 'PJ'),
        ('Steven', 'Colchester', None),
    ]

    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30', 65500, 'Andrew'),
        ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Peter'),
        ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Susan'),
        ('Admin supervisor', '2012-10-01', '2014-11,10', 45900, 'Pam'),
        ('Admin manager', '2014-11-14', '2018-01,05', 45900, 'Steven')
    ]

    depts = [
        ('Analyst','B001', 'Biostats' ),
        ('Admin manager','C003', 'Biomarkers' ),
        ('Senior analyst', 'I001', 'IT'),
        ('Senior business analyst','I001', 'IT'),
        ('Admin supervisor','N001','Pre-Clinical')
    ]

    try:

        database = SqliteDatabase('../src/data/personjob.db')
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')  # needed for sqlite only

        for i in Dept.select():
            i.delete_instance()
        for i in Job.select():
            i.delete_instance()
        for i in Person.select():
            i.delete_instance()


        for person in people:
            with database.transaction():
                new_person = Person.create(
                    person_name=person[0],
                    lives_in_town=person[1],
                    nickname=person[2]
                )
                new_person.save()

        for job in jobs:
            p=Person.get(Person.person_name==job[4])

            with database.transaction():
                new_job = Job.create(
                    job_name=job[0],
                    start_date=job[1],
                    end_date=job[2],
                    salary=job[3],
                    person=p
                )
                new_job.save()

        for dept in depts:
            j=Job.get(Job.job_name==dept[0])

            with database.transaction():
                new_dept = Dept.create(
                    dept_num=dept[1],
                    dept_name=dept[2],
                    job=j
                )
                new_dept.save()



        # display the db
        display()

        # update a record
        andrew=Person.get(Person.person_name=="Andrew")
        andrew.lives_in_town="Somerville"
        andrew.save()
        display()

        # delete a record
        pam=Person.get(Person.person_name=="Pam")
        pam.delete_instance()
        display()

        # remove a range
        recs=Person.delete().where(Person.person_name.startswith("S"))
        recs.execute()
        display()

    except Exception as e:
        print(e.args)

    finally:
        database.close()

def display():
    print("====================================================")
    qry = (Person.select(Person.person_name, Person.lives_in_town,
                         Job.job_name,
                         Dept.dept_name)
           .join(Job)
           .join(Dept)
           .order_by(Person.person_name)
           )

    [print(f"{i.person_name} lives in  {i.lives_in_town} "
           f"as a {i.job.job_name} "
           f"in {i.job.dept.dept_name}") for i in qry]

if __name__ == '__main__':
    seed()


