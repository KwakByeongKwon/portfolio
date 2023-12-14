from django.db import models
from django.utils import timezone
# Create your models here.


class PlayerInfo(models.Model):
    schoolname = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    playername = models.CharField(max_length=50)
    age = models.IntegerField(null=False)
    pitchingtype = models.CharField(max_length=20)
    intro = models.TextField(max_length=2000)
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return f'소속 : {self.schoolname}, 학년 : {self.grade} 이름 : {self.playername}, 유형 : {self.pitchingtype}'
    
class Opponent(models.Model):
    gamename = models.CharField(max_length=50)
    opponent_name = models.CharField(max_length=20)
    opponent_date = models.DateTimeField(default='')
    playerinfo_reference = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    

class Record(models.Model):
    opponent_reference = models.ForeignKey(Opponent, on_delete=models.CASCADE)
    record = models.CharField(default='',max_length=100)
    position = models.CharField(default='',max_length=100)
    speed = models.IntegerField(default=135)
    ballcourse = models.IntegerField(default=0)
    strike_ball = models.CharField(default='',max_length=10)
    hitter_num = models.IntegerField(default=0)

class BallData(models.Model):
    opponent = models.ForeignKey(Opponent, on_delete=models.CASCADE)
    total_pitches = models.IntegerField(default=0)
    total_fast_ball = models.IntegerField(default=0)
    total_breaking_ball= models.IntegerField(default=0)
    total_speed_off_ball= models.IntegerField(default=0)

    foursim_ball = models.IntegerField(default=0)
    twosim_ball = models.IntegerField(default=0)
    cutfast_ball = models.IntegerField(default=0)

    curve_ball = models.IntegerField(default=0)
    slider_ball = models.IntegerField(default=0)
    sinker_ball = models.IntegerField(default=0)

    circlechan_ball = models.IntegerField(default=0)
    splitter_ball = models.IntegerField(default=0)
    fork_ball = models.IntegerField(default=0)
    
    left_hitter_total_pitches = models.IntegerField(default=0)
    left_hitter_total_fast_ball = models.IntegerField(default=0)
    left_hitter_total_breaking_ball = models.IntegerField(default=0)
    left_hitter_total_speed_off_ball = models.IntegerField(default=0)
    
    right_hitter_total_pitches = models.IntegerField(default=0)
    right_hitter_total_fast_ball = models.IntegerField(default=0)
    right_hitter_total_breaking_ball = models.IntegerField(default=0)
    right_hitter_total_speed_off_ball = models.IntegerField(default=0)


    