SELECT si.roll_number, si.name
FROM student_information si
JOIN examination_marks em ON si.roll_number = em.roll_number
WHERE (em.subject_one + em.subject_two + em.subject_three) < 100;