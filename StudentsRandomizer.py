#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import random

SOURCE_FILENAME = "students.csv"
RESULT_FILENAME = "randomly_sorted_students.txt"


def get_students_names_to_list():
    students_file = pd.read_csv(SOURCE_FILENAME)
    return students_file['NAME'].tolist()


def randomize_students_list(students_list):
    return random.sample(students_list, len(students_list))


def export_randomly_sorted_students_to_txt(students_list):
    txt_file = open(RESULT_FILENAME, "w")
    i = 1
    for student in students_list:
        numbered_randomly_sorted_student = str(i) + ". " + student
        txt_file.write(numbered_randomly_sorted_student + "\n")
        i = i+1
    txt_file.close()


def print_randomly_sorted_students():
    txt_file = open(RESULT_FILENAME, "r")
    txt_file_lines = txt_file.read().splitlines()
    for line in txt_file_lines:
        print(line)
    txt_file.close()


if __name__ == "__main__":
    students_list = get_students_names_to_list()
    randomized_students_list = randomize_students_list(students_list)
    export_randomly_sorted_students_to_txt(randomized_students_list)
    print_randomly_sorted_students()
