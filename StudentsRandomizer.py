#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import random

FILENAME = "students.csv"

def get_students_names_to_list():
    students_file = pd.read_csv(FILENAME)
    return students_file['NAME'].tolist()


def randomize_students_list(students_list):
    return random.sample(students_list, len(students_list))


def print_numbered_list_elements(students_list):
    i = 1
    for student in students_list:
        print(str(i) + ". " + student)
        i = i+1


if __name__ == "__main__":
    students_list = get_students_names_to_list()
    randomized_students_list = randomize_students_list(students_list)
    print_numbered_list_elements(randomized_students_list)
