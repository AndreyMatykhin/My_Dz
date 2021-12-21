tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']

tutors_klasses = ((tutor, klass) for tutor, klass in
                  zip(tutors, [klasses[i] if i < len(klasses) else None for i in range(len(tutors))]))

print(*tutors_klasses)
