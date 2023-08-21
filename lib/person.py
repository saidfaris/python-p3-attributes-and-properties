#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    pass
    def __init__(self, name=None, job=None):
        self._name = None
        self._job = None

        if name is not None:
            self.name = name
        if job is not None:
            self.job = job    

    def get_name(self):
        print('Retrieving name...')
        return self._name      

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <=25:
            self._name = name.title()

        else:
            print('Name must be string between 1 and 25 characters.')

    def get_job(self):
        print('Retrieving job...')
        return self._job      

    def set_job(self, job):
        if job.title() in [approved_job.title() for approved_job in APPROVED_JOBS]:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)


person1 = Person()
person1.name = 'mr.titus'
person1.job = 'itc'

print(person1.name)
print(person1.job)