#!/usr/bin/env python3
import ipdb

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
    def __init__(self, name="Jim", job="Admin"):
        self.name = name
        self.job = job
    
    #!Name property stuff
    def get_name (self):
        return self._name
    
    def set_name (self,name):
        if (type(name)==str) and (0<len(name)<=25):
            title_name = name.title()
            self._name = title_name
        else:
            print("Name must be string between 1 and 25 characters.")
           
    name = property(get_name,set_name)
    
    #!Job Property
    def get_job(self):
        return self._job
    
    def set_job(self,job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
    
    job = property(get_job, set_job)
