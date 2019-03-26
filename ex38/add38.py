# -*- coding: utf-8 -*-

students = ['Darin', 'Zek', 'Jack', 'Jane', 'Tom']
print "There are %d students in the classroom A." % len(students)
print "They are ", students

# 1. append()
print "Today, a transfer student, whose name is Juliet, is coming!"
students.append('Juliet')
print "Now, there are %d students in the classroom A." % len(students)

# 2. count()
print "There are %d student(s), whose name is Zek." %  students.count('Zek')

# 3. sort()
print "Let's sort your seats by your name: "
students.sort()
print students

# 4. index()
print "So, the first seat belongs to %s." % students[0]

# 5. insert()
# 6. remove()
print "Zek hopes for the first seat for he is too short."
students.remove('Zek')
students.insert(0, 'Zek')
print "Now, the seats are ", students

# 7. reserve()
print "So, we can sort students by their height by descending order: "
students.reverse()
print students

#8. extend()
print "Today, a course will be processed in class A and B."
studentsB = ['Susan', 'Simth', 'Alex', 'Alice']
print "There are %d students in class B." % len(studentsB)
print "They are ", studentsB
students.extend(studentsB)
print "Today, in the class, there are students as ", students
