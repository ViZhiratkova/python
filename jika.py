def average(students):  #расчёт среднего арифметического для учеников
    result = {}
    for key, value in students.items():
        total = 0
        count = 0
        for i in value.values():
            if type(i) is int or type(i) is float:
                total = total + i
                count = count + 1
        if count == 0:
            result[key] = None
        else:
            result[key] = round(total / count, 2)
    return result

def mediana(students):  #расчёт медианы для учеников
    result = {}
    for key, value in students.items():
        grades = []
        for v in value.values():
            if v is not None:
                grades.append(v)
        if not grades:
            result[key] = None
        else:
            grades_sorted = sorted(grades)
            n = len(grades_sorted)
            mid = n // 2
            if n % 2 == 1:
                result[key] = grades_sorted[mid]
            else:
                result[key] = (grades_sorted[mid - 1] + grades_sorted[mid]) / 2
    return result

def count(students):  #расчёт кол-ва оценок для учеников
    result = {}
    for key, value in students.items():
        count = 0
        for v in value.values():
            if v is not None:
                count = count + 1
        result[key] = count
    return result

def grade(students): #перевод среднего по всем предметам в пятибальную шкалу
    result = {}
    ave = average(students)
    for key, value in ave.items():
        if value is None:
            result[key] = None
            continue
        elif 90 <= value <= 100:
            result[key] = 5
        elif 75 <= value <= 89:
            result[key] = 4
        elif 60 <= value <= 74:
            result[key] = 3
        elif 0 <= value <= 59:
            result[key] = 2
    return result

def all_students(students):  #вывод всех данных по ученикам
    ave = average(students)
    medi = mediana(students)
    cnt = count(students)
    grd = grade(students)
    for name, grades in students.items():
        print(f"name: {name}")
        print(f"grades: {grades}")
        print(f"average: {ave[name]}")
        print(f"median: {medi[name]}")
        print(f"count: {cnt[name]}")
        print(f"grade: {grd[name]}")
        print()
    return



def subject_grades(students):  #вычисление всех оценок по предмету
    result = {}
    for grades_dict in students.values():
        for subject, grade in grades_dict.items():
            if subject not in result:
                result[subject] = []
            result[subject].append(grade)
    return result

def subject_average(grades):  #расчёт среднего арифметического для оценок предметов
    total = 0
    count = 0
    for i in grades:
        if type(i) is int or type(i) is float:
            total = total + i
            count = count + 1
    if count == 0:
        return None
    return round(total / count, 2)

def subject_median(students): #расчёт медианы для оценок предметов
    result = {}
    for value in students.values():
        for k, v in value.items():
            if v is None:
                continue
            if k in result:
                result[k].append(v)
                continue
            else:
                result[k] = [v]
    medians = {}
    for subject, grades in result.items():
        grades_sorted = sorted(grades)
        n = len(grades_sorted)
        mid = n // 2
        if n % 2 == 1:
            median = grades_sorted[mid]
        else:
            median = (grades_sorted[mid - 1] + grades_sorted[mid]) / 2
        medians[subject] = median
    return medians

def subject_count(grades):  #расчёт кол-ва оценок предмета
    count = 0
    for i in grades:
        if type(i) is int or type(i) is float:
            count = count + 1
    return count

def subject_grade(average):  #перевод среднего предмета в пятибальную шкалу
    if average is None:
        return None
    if average >= 90:
        grade = 5
    elif average >= 75:
        grade = 4
    elif average >= 60:
        grade = 3
    elif average >= 0:
        grade = 2
    return grade


def all_subjects(students):  #вывод всех данных по предметам
    grades = subject_grades(students)
    medians = subject_median(students)
    for subject, grades in grades.items():
        print(subject)
        print(f"grades: {grades}")
        average = subject_average(grades)
        count = subject_count(grades)
        grade = subject_grade(average)
        median = medians.get(subject, None)
        print(f"average: {average}")
        print(f"median: {median}")
        print(f"count: {count}")
        print(f"grade: {grade}")
        print()
    return

def students_distribution(students):
    distribution = {5: 0, 4: 0, 3: 0, 2: 0}
    for name, grades_dict in students.items():
        total = 0
        count = 0
        for value in grades_dict.values():
            if type(value) is int or type(value) is float:
                total = total + value
                count = count + 1
        if count == 0:
            student_grade = None
        else:
            average = total / count
            if average >= 90:
                student_grade = 5
            elif average >= 75:
                student_grade = 4
            elif average >= 60:
                student_grade = 3
            elif average >= 0:
                student_grade = 2
        if student_grade in distribution:
            distribution[student_grade] = distribution[student_grade] + 1
    return distribution

def subject_distribution(students):
    distribution = {5: 0, 4: 0, 3: 0, 2: 0}
    result = {}
    for grades_dict in students.values():
        for subject, grade in grades_dict.items():
            if subject not in result:
                result[subject] = []
            if grade is None:
                continue
            result[subject].append(grade)
    average_distribution = {subject: round(sum(grades) / len(grades), 2) for subject, grades in result.items()}
    for value in average_distribution.values():
        if value >= 90:
            subject_grade = 5
        elif value >= 75:
            subject_grade = 4
        elif value >= 60:
            subject_grade = 3
        elif value >= 0:
            subject_grade = 2
        if subject_grade in distribution:
            distribution[subject_grade] = distribution[subject_grade] + 1
    return distribution

def get_students_data(students):
    ave = average(students)
    medi = mediana(students)
    cnt = count(students)
    grd = grade(students)
    result = []
    for name in students:
        result.append({
            "name": name,
            "grades": students[name],
            "average": ave[name],
            "median": medi[name],
            "count": cnt[name],
            "grade": grd[name]})
    return result


def score_to_grade(score):
    if score is None:
        return None
    if 90 <= score <= 100:
        return 5
    elif 75 <= score <= 89:
        return 4
    elif 60 <= score <= 74:
        return 3
    elif 0 <= score <= 59:
        return 2
    else:
        return None

def get_subjects_data(students):
    subj_grades = subject_grades(students)
    medians = subject_median(students)
    result = []
    for subject, grades_list in subj_grades.items():
        avg = subject_average(grades_list)
        cnt = subject_count(grades_list)
        grd = score_to_grade(avg)
        median = medians.get(subject)
        result.append({
            "subject": subject,
            "grades": grades_list,
            "average": avg,
            "median": median,
            "count": cnt,
            "grade": grd})
    return result


def get_top_students(students, top_n=3):
    student_list = []
    for name, subjects in students.items():
        scores = [v for v in subjects.values() if v is not None and isinstance(v, (int, float))]
        if not scores:
            avg = None
            grd = None
        else:
            avg = round(sum(scores) / len(scores), 2)
            grd = score_to_grade(avg)
        student_list.append({"name": name, "average": avg, "grade": grd})
    student_list.sort(key=lambda x: x["average"] if x["average"] is not None else -float("inf"),reverse=True)
    return student_list[:top_n]

def generate_report(students, top_n=3):
    students_data = get_students_data(students)
    subjects_data = get_subjects_data(students)
    return {
        "num_students": len(students),
        "num_subjects": len(subjects_data),
        "students": students_data,
        "subjects": subjects_data,
        "students_distribution": students_distribution(students),
        "subjects_distribution": subject_distribution(students),
        "top_students": get_top_students(students, top_n)}

def main():
    students = {
        "Иванов": {"Математика": 89, "Физика": 92, "История": 79, "Литература": 85},
        "Петрова": {"Математика": 98, "Физика": None, "История": 93, "Литература": 89},
        "Сидоров": {"Математика": None, "Физика": None, "История": None, "Литература": None},
        "Кузнецова": {"Математика": 90, "Физика": 50, "История": 78.5, "Литература": 74},
        "Морозов": {"Математика": 83, "Физика": 77, "История": 30, "Литература": 80}}

    report = generate_report(students, top_n=3)
    import pprint
    pprint.pprint(report, sort_dicts=False, width=120)
if __name__ == "__main__":
    main()






