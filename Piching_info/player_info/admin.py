from django.contrib import admin

# Register your models here.
from player_info.models import PlayerInfo
from player_info.models import BallData,Record,Opponent

admin.site.register(PlayerInfo)
admin.site.register(BallData)
admin.site.register(Record)
admin.site.register(Opponent)