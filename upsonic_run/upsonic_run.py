#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time
import traceback
import copy
import multiprocessing
from cryptography.fernet import Fernet

class Upsonic_Run:
    def __init__(self, cloud, encryption_key, interval=5, try_number = 0) -> None:
        self.encryption_key = encryption_key
        self.connection = cloud
        self.interval = interval
        self.threads = {}
        self.uniq = (((Fernet.generate_key()).decode()).replace("-", "").replace("_", ""))[
                :10
            ]
        self.try_number = try_number
    



    def add_task(self, name, endless=False, thread=False, args_for_func=(), kwargs_for_func={}):
        try_number = 0
        while try_number <= self.try_number or self.try_number == 0:
            all_records = self.connection.get_all(encryption_key=self.encryption_key)
            runners = [runner for runner in all_records if runner.startswith("RUNNER-") and (time.time() - all_records[runner]) <= self.interval*2]
            old_runners = [runner for runner in all_records if runner.startswith("RUNNER-") and (time.time() - all_records[runner]) > self.interval*2]
            for i in old_runners:
                self.connection.delete(i)
            if len(runners) == 0:
                try_number += 1
                time.sleep(self.interval)
            else:
                self.connection.set(f"TASK-{name}", [name, args_for_func, kwargs_for_func, endless, thread, random.choice(runners)], encryption_key=self.encryption_key)
                return


    def delete_task(self, name):

        self.connection.delete(f"TASK-{name}")

    

    def result(self, name,):
        return self.connection.get(f"RESULT-{name}",encryption_key=self.encryption_key)


    def run(self,name, args_for_func=(), kwargs_for_func={}):
        self.add_task(name, args_for_func=args_for_func, kwargs_for_func=kwargs_for_func)
        time.sleep(self.interval*2)
        while True:
            the_result = self.result(name)
            if the_result is not None:
                return the_result
            time.sleep(self.interval)
