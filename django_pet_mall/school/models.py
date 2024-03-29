from pyexpat import model
from django.db import models

from django.utils import timezone as datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名")
    age = models.SmallIntegerField(verbose_name="年龄")
    sex = models.BooleanField(default=False)
    class Meta:
        db_table = "sch_student"

    def __str__(self) -> str:
        return self.name
    """
    自己处理信息
    """
    @property
    def achievement(self):
        """拿到对象"""
        queryset = self.s_achievement.values("course__teacher__name","course__name","score")
        print(self.s_achievement.values())
        return queryset

class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="课程名称")
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING,
    related_name = "course", db_constraint=False)
    class Meta:
        db_table = "sch_couse"
    
    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名")
    sex = models.BooleanField(default=False)
    class Meta:
        db_table = "sch_teacher"

    def __str__(self) -> str:
        return self.name

class Achievement(models.Model):
    score = models.DecimalField(default=0, max_digits=4, decimal_places=1, verbose_name="成绩")
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name="s_achievement",
    db_constraint=False)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name="c_achievement",
    db_constraint=False)
    create_dtime = models.DateTimeField(auto_created=datetime.now)
    class Meta:
        db_table = "sch_achievement"

    def __str__(self) -> str:
        return self.name






    