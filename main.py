#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sql

insert_propt = \
    ['building, room_number, capacity', 'dept_name, building, budget(budget > 0)',
     'course_id, title, dept_name, credits(credits > 0)', 'ID, name, dept_name, salary(salary > 29000',
     'course_id, sec_id, semester(Spring, Summer, Winter, Fall), year, building, room_number,time_slot_id'
        , 'ID, course_id, sec_id, year', 'ID, name, dept_name, tot_cred(tot_cred >= 0)',
     'ID, course_id, sec_id, semester, year, grade', 's_ID, i_ID',
     'time_slot_id, day, start_hr[0,24), start_min[0,60), end_hr[0,24), end_min[0,60', 'course_id, prerea_id']
delete_propt = \
    ['building, room_number', 'dept_name', 'course_id', 'ID', 'course_id, sec_id, semester, year',
     'ID, cpirse_id, sec_id, semester, year'
        , 'ID', 'ID, course_id, sec_id, semester, year', 's_ID', 'time_slot_id, day, start_hr, start_min',
     'course_id, prereq_id']

ask = \
    ['normal_query1', 'normal_query2', 'join_query1', 'join_query2', 'nested_query1', 'nested_query2', 'group_query1',
     'group_query2','auto_sql']

query_info = \
    ['查找所有教师的名字', '查找所有在Computer Science系中且工资大于70000的教师姓名',
     '对于大学中所有讲授课程的教师，找出他们的姓名以及所讲述的所有课程标识',
     '找出所有教师的姓名，他们工资至少比Biology系某一个教师的工资高',
     '找出所有在2009年秋季和2010年春季学期同时开课的所有课程',
     '找出不同的学生总数，他们选修了ID为10101的教师所讲授的课程',
     '平均工资超过42000的系的系名和平均工资', '找出每个系在2010年春季学期坚守一门课程的教师人数','请自行输入合法的sql语句']

query_sql = \
['''select name from instructor;''',
 '''select name from instructor where dept_name='Comp.Sci' and salary > 700000;''',
 '''select name, course_id from instructor, teaches where instructor.ID = teaches.ID;''',
 '''select distinct T.name from instructor as T , instructor as S 
where T.salary > S.salary and S.dept_name = 'Biology'; ''',
 '''select distinct course_id from section where semester = 'Fall' and year = 2009 and 
    course_id in (select course_id from section where semester = 'Spring' and year = 2010);''',
 '''select count (distinct ID) from takes where (course_id, sec_id, semester, year) in (select course_id, sec_id, semester, year
 from teaches where teaches.ID = 10101);''',
 '''select dept_name, avg(salary) as avg_salary from instructor group by dept_name having avg(salary) > 42000;''',
 '''select dept_name, count(distinct ID) as instr_count from instructor natural join teaches
 where semester = 'Spring' and year = 2010 group by dept_name'''
 ]


class INSERT(QWidget):
    def __init__(self, x):
        super().__init__()

        self.cb = QComboBox()
        self.db = x
        layout = QVBoxLayout()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('q')
        self.cb.addItems(
            ['classroom', 'department', 'course', 'instructor', 'section', 'teaches', 'student', 'takes', 'advisor'
                , 'time_slot', 'prereq'])
        self.btn = QPushButton('Done')
        self.text = QTextEdit()
        self.text.setToolTip('building, room_number, capacity')
        self.cb.currentIndexChanged.connect(self.selectionchange)
        self.btn.clicked.connect(self.insert)
        layout.addWidget(self.btn)
        layout.addWidget(self.cb)
        layout.addWidget(self.text)

        self.setLayout(layout)

    def selectionchange(self):
        self.text.setToolTip(insert_propt[self.cb.currentIndex()])

    def insert(self):
        text_string = self.text.toPlainText()
        text_string = text_string.strip('\n')
        x = text_string.split(',')
        sql_string = 'insert into ' + self.cb.currentText() + 'values' + '('
        le = len(x)
        sql_string = sql_string + '\'' + x[0] + '\''
        for id in range(1, le):
            sql_string = sql_string + ', \'' + x[id] + '\''
        sql_string = sql_string + ')'
        self.db.insert(sql_string)

    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()


class DELETE(QWidget):

    def __init__(self, x):
        super().__init__()
        self.db = x
        self.cb = QComboBox()
        layout = QVBoxLayout()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('q')
        self.cb.addItems(
            ['classroom', 'department', 'course', 'instructor', 'section', 'teaches', 'student', 'takes', 'advisor'
                , 'time_slot', 'prereq'])
        self.btn = QPushButton('Done')
        self.text = QTextEdit()
        self.cb.currentIndexChanged.connect(self.selectionchange)
        self.btn.clicked.connect(self.delete)
        layout.addWidget(self.btn)
        layout.addWidget(self.cb)
        layout.addWidget(self.text)
        self.setLayout(layout)

    def selectionchange(self):
        self.text.setToolTip(delete_propt[self.cb.currentIndex()])

    def delete(self):
        text_string = self.text.toPlainText()
        text_string = text_string.strip('\n')
        sql_string = 'delete from ' + self.cb.currentText() + 'where' + text_string
        self.db.delete(sql_string)


    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()


class ASK(QWidget):
    def __init__(self, x):
        super().__init__()
        self.db = x
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('query')
        self.cb = QComboBox()
        self.btn = QPushButton('Done')
        self.text = QTextEdit()
        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setText(query_info[0])
        self.cb.addItems(ask)
        self.cb.currentIndexChanged.connect(self.selectchange)
        self.btn.clicked.connect(self.query)
        layout.addWidget(self.text)
        layout.addWidget(self.btn)
        layout.addWidget(self.cb)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def selectchange(self):
        self.label.setText(query_info[self.cb.currentIndex()])

    def query(self):
        if self.cb.currentIndex() < 8 :
            sql_string = query_sql[self.cb.currentIndex()]
            self.db.query(sql_string)
        else :
            sql_string = self.text.toPlainText()
            self.db.query(sql_string)

    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()


class Example(QWidget):
    close_signal = pyqtSignal()

    def __init__(self, insert, ask, delete):
        super().__init__()

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        self.btn = QPushButton('插入', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn1 = QPushButton('删除', self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn3 = QPushButton('查询', self)
        self.btn3.resize(self.btn3.sizeHint())
        self.btn.move(0, 60)
        self.btn1.move(0, 120)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.btn.setToolTip("插入操作")
        self.btn1.setToolTip("删除操作")
        self.btn3.setToolTip("查询操作")
        self.btn.clicked.connect(insert.handle_click)
        self.btn1.clicked.connect(delete.handle_click)
        self.btn3.clicked.connect(ask.handle_click)


if __name__ == '__main__':
    mysql = sql.Mysql()
    app = QApplication(sys.argv)
    ask = ASK(mysql)
    insert = INSERT(mysql)
    delete = DELETE(mysql)
    ex = Example(insert, ask, delete)
    ex.show()
    sys.exit(app.exec_())
