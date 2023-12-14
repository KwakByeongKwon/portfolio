from django.shortcuts import render, redirect
from .models import PlayerInfo, BallData,Opponent,Record
from django.urls import reverse
# Create your views here.
from django.views import generic
from .forms import PlayerInfoForm,SpeedForm,OpponentForm

# 계산 여기부터

def add(ball_data,pitching_datas,leftright):
    if leftright == 'Left':
        if pitching_datas == 'foursim': 
            ball_data.foursim_ball += 1
            ball_data.total_fast_ball += 1
            ball_data.left_hitter_total_fast_ball += 1
                
        elif pitching_datas == 'twosim':
            ball_data.twosim_ball += 1
            ball_data.total_fast_ball += 1
            ball_data.left_hitter_total_fast_ball += 1
            
        elif pitching_datas == 'cutfast':
            ball_data.cutfast_ball += 1
            ball_data.total_fast_ball += 1
            ball_data.left_hitter_total_fast_ball += 1
            
        elif pitching_datas == 'curve':
            ball_data.curve_ball += 1
            ball_data.total_breaking_ball += 1
            ball_data.left_hitter_total_breaking_ball += 1
            
        elif pitching_datas == 'slider':
            ball_data.slider_ball += 1
            ball_data.total_breaking_ball += 1
            ball_data.left_hitter_total_breaking_ball += 1
            
        elif pitching_datas == 'sinker':
            ball_data.sinker_ball += 1
            ball_data.total_breaking_ball += 1
            ball_data.left_hitter_total_breaking_ball += 1
            
        elif pitching_datas == 'circlechan':
            ball_data.circlechan_ball += 1
            ball_data.total_speed_off_ball += 1
            ball_data.left_hitter_total_speed_off_ball += 1
            
        elif pitching_datas == 'splitter':
            ball_data.splitter_ball += 1
            ball_data.total_speed_off_ball += 1
            ball_data.left_hitter_total_speed_off_ball += 1
            
        elif pitching_datas == 'forkball':
            ball_data.fork_ball += 1
            ball_data.total_speed_off_ball += 1
            ball_data.left_hitter_total_speed_off_ball += 1
            
        ball_data.total_pitches += 1
        ball_data.left_hitter_total_pitches += 1
        ball_data.save()
        
    elif leftright == 'Right':
        if pitching_datas == 'foursim': 
            ball_data.foursim_ball += 1
            ball_data.total_fast_ball += 1
            ball_data.right_hitter_total_fast_ball += 1
                
        elif pitching_datas == 'twosim':
            ball_data.twosim_ball += 1
            ball_data.total_fast_ball += 1
            ball_data.right_hitter_total_fast_ball += 1
            
        elif pitching_datas == 'cutfast':
            ball_data.cutfast_ball += 1
            ball_data.total_fast_ball += 1
            ball_data.right_hitter_total_fast_ball += 1
            
        elif pitching_datas == 'curve':
            ball_data.curve_ball += 1
            ball_data.total_breaking_ball += 1
            ball_data.right_hitter_total_breaking_ball += 1
            
        elif pitching_datas == 'slider':
            ball_data.slider_ball += 1
            ball_data.total_breaking_ball += 1
            ball_data.right_hitter_total_breaking_ball += 1
            
        elif pitching_datas == 'sinker':
            ball_data.sinker_ball += 1
            ball_data.total_breaking_ball += 1
            ball_data.right_hitter_total_breaking_ball += 1
            
        elif pitching_datas == 'circlechan':
            ball_data.circlechan_ball += 1
            ball_data.total_speed_off_ball += 1
            ball_data.right_hitter_total_speed_off_ball += 1
            
        elif pitching_datas == 'splitter':
            ball_data.splitter_ball += 1
            ball_data.total_speed_off_ball += 1
            ball_data.right_hitter_total_speed_off_ball += 1
            
        elif pitching_datas == 'forkball':
            ball_data.fork_ball += 1
            ball_data.total_speed_off_ball += 1
            ball_data.right_hitter_total_speed_off_ball += 1
            
        ball_data.total_pitches += 1
        ball_data.right_hitter_total_pitches += 1
        ball_data.save()
        
def calcul(opponent_start,pitching_datas,leftright):
    ball_data = opponent_start.balldata_set.first()
    
    add(ball_data,pitching_datas,leftright)
    
# 여기까지

class Index(generic.ListView):
    model = PlayerInfo
    template_name = "player_info/index.html"


class Player(generic.CreateView):
    model = PlayerInfo
    form_class = PlayerInfoForm
    template_name= "player_info/player.html"
    success_url = '/info/'

class Detail(generic.DetailView):
    model = PlayerInfo
    template_name= "player_info/detail.html"


def pitching(request, id):
    pitching_data = PlayerInfo.objects.get(pk=id)
    
    form_class = SpeedForm
    
    gamename = request.POST['gamename']                   # 게임이름
    opponent_name = request.POST['opponent_name']         # 상대팀명
    opponent_date = request.POST['opponent_date']         # 경기날짜


    new_opponent = pitching_data.opponent_set.create(gamename=gamename,
                                      opponent_name=opponent_name,
                                      opponent_date=opponent_date) # 데이터 생성
    opponent_data = Opponent.objects.get(id=new_opponent.id)
    record_data = opponent_data.record_set.all()
    
    balldata = opponent_data.balldata_set.create()

    ctx = {'pitching_data':pitching_data,'record_data':record_data,'form_class':form_class,'opponent_data':opponent_data} #####
    
    return render(request, 'player_info/pitching.html', ctx)


def delete(request, id):
    delete_data = PlayerInfo.objects.get(pk=id)
    if request.method == 'POST':
        delete_data.delete()

        return redirect('/info/')
    
    else:
        return render(request, 'player_info/delete.html',{'delete_data':delete_data})
    

def edit(request, id):
    detail_data = PlayerInfo.objects.get(pk=id)
    if request.method == 'POST':
        detail_data.schoolname = request.POST.get('schoolname')
        detail_data.grade = request.POST.get('grade')
        detail_data.playername = request.POST['playername']
        detail_data.age = request.POST.get('age')
        detail_data.pitchingtype = request.POST.get('pitchingtype')
        detail_data.intro = request.POST.get('intro')
        detail_data.save()
        return redirect(f'/info/detail/{id}/')
    
    else:
        return render(request, 'player_info/edit.html',{'detail_data':detail_data})
 

    
def update(request,pk,id):
    pitching_data = PlayerInfo.objects.get(pk=pk)
    opponent_start = pitching_data.opponent_set.order_by('-id').first()
    form_class = SpeedForm
    
    leftright = request.POST['update_leftright']
    hitter_num = int(request.POST['update_hitter_num'])
    record_updates = opponent_start.record_set.get(pk=id)
    record_updates.record = request.POST['update_record']
    record_updates.ballcourse = request.POST['update_course']
    record_updates.speed = request.POST['update_speed']
    record_updates.position = leftright
    record_updates.strike_ball = request.POST['update_strikeball']
    record_updates.hitter_num = hitter_num
    
    record_updates.save()
    ctx = {'leftright':leftright,'pitching_data':pitching_data,'opponent_start':opponent_start,'form_class':form_class,'hitter_num':hitter_num}
    
    return render(request,'player_info/pitching.html',ctx)

def pitching_avg(request, id):
    pitching_data = PlayerInfo.objects.get(pk=id)
    opponent_start = pitching_data.opponent_set.order_by('-id').first()
    form_class = SpeedForm
    leftright = request.POST['leftright']   # 좌타 우타 값 받아오기
    hitter_num = int(request.POST['hitter_num']) # 타순 받아오기
    try:
        pitching_datas = request.POST['pitchinginfo']
        speed = request.POST['speed']           # 스피드 받아오기
        ballcourse = request.POST['ballcourse'] # 코스 받아오기
        strike_ball = request.POST['strikeball'] # 스트라크/볼 받아오기
        
        calcul(opponent_start,pitching_datas,leftright)
        opponent_start.record_set.create(record=pitching_datas,position=leftright,speed=speed,ballcourse=ballcourse,strike_ball=strike_ball,hitter_num=hitter_num)
        ctx = {'pitching_data':pitching_data,'leftright':leftright,'form_class':form_class,'opponent_start':opponent_start,'hitter_num':hitter_num}
        
        return render(request,'player_info/pitching.html',ctx)
    except:
        error_message = '구종/코스 를 선택해주세요.'
        ctx = {'error_message':error_message,'pitching_data':pitching_data,'form_class':form_class,'opponent_start':opponent_start,'hitter_num':hitter_num,'leftright':leftright}
        
        return render(request,'player_info/pitching.html',ctx)

    
from django.utils import timezone

def vsinfo(request,id):
    pitching_data = PlayerInfo.objects.get(pk=id)

    form_class = OpponentForm
    opponent_data = pitching_data.opponent_set.all()
    
    ctx = {'pitching_data':pitching_data,'opponent_data':opponent_data,'form_class':form_class}
    return render(request,'player_info/vsinfo.html',ctx)




def gamedetail(request,id,pk):
    pitching_data = PlayerInfo.objects.get(pk=pk)
    opponent_rec = Opponent.objects.get(pk=id)
    
    ball_data = opponent_rec.balldata_set.all()[0]
    if ball_data.left_hitter_total_pitches == 0:
        left_bk_per = 0
        left_so_per = 0
        left_ft_per = 0
    else:   
        left_ft_per = round(ball_data.left_hitter_total_fast_ball / ball_data.left_hitter_total_pitches * 100,1)
        left_bk_per = round(ball_data.left_hitter_total_breaking_ball / ball_data.left_hitter_total_pitches * 100,1)            
        left_so_per = round(ball_data.left_hitter_total_speed_off_ball / ball_data.left_hitter_total_pitches * 100,1)
    
    if ball_data.right_hitter_total_pitches == 0:
        right_ft_per = 0
        right_bk_per = 0
        right_so_per = 0
    else:
        right_ft_per = round(ball_data.right_hitter_total_fast_ball / ball_data.right_hitter_total_pitches * 100,1)        
        right_bk_per = round(ball_data.right_hitter_total_breaking_ball / ball_data.right_hitter_total_pitches * 100,1)        
        right_so_per = round(ball_data.right_hitter_total_speed_off_ball / ball_data.right_hitter_total_pitches * 100,1)

    
    left_pitch_list = [left_ft_per,left_bk_per,left_so_per]
    right_pitch_list = [right_ft_per,right_bk_per,right_so_per]
    
    #Opponent 모델과 연결된 record_set 쿼리셋 가져옴
    # 해당 쿼리셋에서 ballcourse가 1 인것을 필터링 
    total_courses = [len(opponent_rec.record_set.filter(ballcourse=i)) for i in range(1, 10)]
    total_pitching = len(opponent_rec.record_set.all())
    if total_pitching != 0:
        total_per = [round(course / total_pitching * 100, 1) for course in total_courses]
    else:
        return render(request,'player_info/fail.html')

    # left_hitter_1 = 
    L_lst = []
    for i in range(1,10):
        # 'position'이 'Left'이고 'ballcourse'가 1인 'foursim', 'twosim', 'cutfast'의 개수 가져오기
        total_left_fast_course = opponent_rec.record_set.filter(position='Left', ballcourse=i, record__in=['foursim', 'twosim', 'cutfast']).count()
        # 'position'이 'Left'이고 'ballcourse'가 1인 'curve', 'slider', 'sinker'의 개수 가져오기
        total_left_braking_course = opponent_rec.record_set.filter(position='Left', ballcourse=i, record__in=['curve', 'slider', 'sinker']).count()
        # 'position'이 'Left'이고 'ballcourse'가 1인 ['circlechan', 'splitter', 'forkball']의 개수 가져오기
        total_left_speedoff_course = opponent_rec.record_set.filter(position='Left', ballcourse=i, record__in=['circlechan', 'splitter', 'forkball']).count()

        # 좌타의 1번코스의 총 투구 개수
        total_left = total_left_fast_course + total_left_speedoff_course + total_left_braking_course
        
        # 총 개수의 센트 구하기 
        if total_left == 0:
            left_fast = 0
            left_braking = 0
            left_speed_off = 0
        else:
            left_fast = round(total_left_fast_course / total_left * 100,1)
            left_braking = round(total_left_braking_course / total_left * 100,1)
            left_speed_off = round(total_left_speedoff_course / total_left * 100,1)

        L_lst.append(left_fast)
        L_lst.append(left_braking)
        L_lst.append(left_speed_off)

    # right_hitter =
    R_lst = []
    for i in range(1,10):
        # 'position'이 'Right'이고 'ballcourse'가 1인 'foursim', 'twosim', 'cutfast'의 개수 가져오기
        total_right_fast_course = opponent_rec.record_set.filter(position='Right', ballcourse=i, record__in=['foursim', 'twosim', 'cutfast']).count()
        # 'position'이 'Right'이고 'ballcourse'가 1인 'curve', 'slider', 'sinker'의 개수 가져오기
        total_right_braking_course = opponent_rec.record_set.filter(position='Right', ballcourse=i, record__in=['curve', 'slider', 'sinker']).count()
        # 'position'이 'Right'이고 'ballcourse'가 1인 ['circlechan', 'splitter', 'forkball']의 개수 가져오기
        total_right_speedoff_course = opponent_rec.record_set.filter(position='Right', ballcourse=i, record__in=['circlechan', 'splitter', 'forkball']).count()

        # 좌타의 1번코스의 총 투구 개수
        total_right = total_right_fast_course + total_right_speedoff_course + total_right_braking_course
        
        # 총 개수의 센트 구하기 
        if total_right == 0:
            right_fast = 0
            right_braking = 0
            right_speed_off = 0
        else:
            right_fast = round(total_right_fast_course / total_right * 100,1)
            right_braking = round(total_right_braking_course / total_right * 100,1)
            right_speed_off = round(total_right_speedoff_course / total_right * 100,1)

        R_lst.append(right_fast)
        R_lst.append(right_braking)
        R_lst.append(right_speed_off)

    # 그래프 
    from django.db.models import Avg
    import pandas as pd
    import matplotlib.pyplot as plt
    from io import BytesIO
    import base64
    plt.style.use('default')
    
    #데이터 베이스 가져오기
    data = opponent_rec.record_set.all()

    # 데이터 프레임 생성
    df = pd.DataFrame(data.values('speed', 'record'))
    
    # 각 record 값의 빈도 계산
    value_counts = df['record'].value_counts()

    record_values = ['foursim', 'twosim', 'cutfast']
    fast_ball_mean = df[df['record'].isin(record_values)]['speed'].mean()
    
    record_values2 = ['curve', 'slider', 'sinker']
    breaking_mean = df[df['record'].isin(record_values2)]['speed'].mean()
    
    record_values3 = ['circlechan', 'splitter', 'forkball']
    speed_off_mean = df[df['record'].isin(record_values3)]['speed'].mean()

    fast_ball_mean = round(fast_ball_mean, 1)
    breaking_mean = round(breaking_mean, 1)
    speed_off_mean = round(speed_off_mean, 1)


    # 시각화 - 각 record 값에 대한 그래프 그리기
    plt.figure(figsize=(10, 5))

  # 각 record 값에 대한 그래프 플로팅
    for record_value in df['record'].unique():
        record_data = df[df['record'] == record_value]
        plt.plot(record_data.index, record_data['speed'], marker='o', linestyle='-', label=f'Record {record_value}')

    # 그래프에 데이터 포인트 표시
    for idx, row in df.iterrows():
        plt.text(idx, row['speed'], f"{row['speed']}", ha='right', va='bottom')
    plt.xticks(df.index)
    plt.title('Speed by Record')
    plt.xlabel('Ball Count')
    plt.ylabel('Speed')
    plt.legend()

    # 이미지 파일로 그래프 저장
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    # 이미지를 base64로 인코딩하여 HTML에 삽입할 준비
    graphic = base64.b64encode(image_png).decode('utf-8')
    graphic = f'data:image/png;base64,{graphic}'
    
    # S,B 의 그래프
    df2 = pd.DataFrame(data.values('strike_ball', 'record', 'position'))
    S_counts_fast = []
    B_counts_fast = []
    S_counts_breaking = []
    B_counts_breaking = []
    S_counts_speedoff = []
    B_counts_speedoff = []

    # 각 SB 개수 구하기
    for record_value in record_values:
        record_S_count = df2[(df['record'] == record_value) & (df2['strike_ball'] == 'S')].shape[0]
        record_B_count = df2[(df['record'] == record_value) & (df2['strike_ball'] == 'B')].shape[0]
        S_counts_fast.append(record_S_count)
        B_counts_fast.append(record_B_count)
 
    for record_value in record_values2:
        record_S_count = df2[(df['record'] == record_value) & (df2['strike_ball'] == 'S')].shape[0]
        record_B_count = df2[(df['record'] == record_value) & (df2['strike_ball'] == 'B')].shape[0]
        S_counts_breaking.append(record_S_count)
        B_counts_breaking.append(record_B_count)

    for record_value in record_values3:
        record_S_count = df2[(df['record'] == record_value) & (df2['strike_ball'] == 'S')].shape[0]
        record_B_count = df2[(df['record'] == record_value) & (df2['strike_ball'] == 'B')].shape[0]
        S_counts_speedoff.append(record_S_count)
        B_counts_speedoff.append(record_B_count)

    # SB 퍼센트 구하기
    total_fast = sum(S_counts_fast) + sum(B_counts_fast)
    # 분모가 0인 경우에 대비하여 조건문으로 처리
    fast_S_ratios = [count / total_fast * 100 if total_fast != 0 else 0 for count in S_counts_fast]
    fast_B_ratios = [count / total_fast * 100 if total_fast != 0 else 0 for count in B_counts_fast]

    total_breaking = sum(S_counts_breaking) + sum(B_counts_breaking)
    breaking_S_ratios = [count / total_breaking * 100 if total_breaking != 0 else 0 for count in S_counts_breaking]
    breaking_B_ratios = [count / total_breaking * 100 if total_breaking != 0 else 0 for count in B_counts_breaking]

    total_speedoff = sum(S_counts_speedoff) + sum(B_counts_speedoff)
    speedoff_S_ratios = [count / total_speedoff * 100 if total_speedoff != 0 else 0 for count in S_counts_speedoff]
    speedoff_B_ratios = [count / total_speedoff * 100 if total_speedoff != 0 else 0 for count in B_counts_speedoff]

    #S/B 비율 토탈
    fast_S_total = round(sum(fast_S_ratios),1)
    fast_B_total = round(sum(fast_B_ratios),1)

    breaking_S_total = round(sum(breaking_S_ratios),1)
    breaking_B_total = round(sum(breaking_B_ratios),1)

    speedoff_S_total = round(sum(speedoff_S_ratios),1)
    speedoff_B_total = round(sum(speedoff_B_ratios),1)
    

    # 시각화
    plt.figure(figsize=(13, 5))

    # 각 레코드 라벨 및 S, B 비율
    labels = ['Fast', 'Breaking', 'Speed-Off']
    record_sets = [record_values, record_values2, record_values3]
    SB_ratios = [(fast_S_ratios, fast_B_ratios), (breaking_S_ratios, breaking_B_ratios), (speedoff_S_ratios, speedoff_B_ratios)]

    for i, (S_ratios, B_ratios) in enumerate(SB_ratios):
        plt.subplot(1, 3, i+1)  # 각 레코드 값에 대해 subplot을 생성합니다.
        plt.bar(record_sets[i], S_ratios, label='Strike', color='darkorange', width=0.3)  # S의 비율을 빨간색으로 표시합니다.
        plt.bar(record_sets[i], B_ratios, bottom=S_ratios, label='Ball', color='green', width=0.3)  # B의 비율을 파란색으로 표시하고 S 위에 쌓습니다.
        plt.yticks([0, 20, 40, 60, 80, 100])
        plt.xlabel('Ball Type')
        plt.ylabel('Percentage')
        plt.title(f'S/B Ratios for {labels[i]}')  # 타이틀에 해당하는 값을 표시합니다.
        plt.legend()
    
    plt.subplots_adjust(wspace=1.3) #간격 조정

    # 이미지 파일로 그래프 저장
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    # 이미지를 base64로 인코딩하여 HTML에 삽입할 준비
    graphic2 = base64.b64encode(image_png).decode('utf-8')
    graphic2 = f'data:image/png;base64,{graphic2}'

    
    # hitter_num에 따른 record_values 비율 구하기
    df3 = pd.DataFrame(data.values('record', 'hitter_num'))
    hitter_nums = list(range(1, 10))  # hitter_num 값: 1부터 9까지
    record_ratios = []

    for num in hitter_nums:
        # hitter_num에 해당하는 데이터 필터링
        filtered_df = df3[df3['hitter_num'] == num]

        # record_values, record_values2, record_values3 각각의 비율 계산
        record_counts = []
        for record_set in [record_values, record_values2, record_values3]:
            record_count = 0
            for record_value in record_set:
                record_count += len(filtered_df[filtered_df['record'] == record_value])
            record_counts.append(record_count)

        # 비율 계산
        total_records = sum(record_counts)
        record_ratio = [count / total_records * 100 if total_records != 0 else 0 for count in record_counts]
        record_ratios.append(record_ratio)

    # 시각화 - hitter_num에 따른 record_values 비율 그래프 (색상 변경)
    plt.figure(figsize=(10, 4))
    bar_width = 0.2
    colors = ['royalblue', 'orangered', 'green']  # 원하는 색상 리스트

    for i, label in enumerate(['Fast', 'Breaking', 'Speed-Off']):
        ratios = [ratio[i] for ratio in record_ratios]
        x_values = [num + i * bar_width for num in hitter_nums]
        plt.bar(x_values, ratios, label=label, width=bar_width, color=colors[i])  # 각 레코드 유형에 색상 적용

        # 그래프 끝에 해당하는 값 출력
        for j, val in enumerate(ratios):
            plt.text(x_values[j], val, f'{val:.1f}', ha='center', va='bottom')

    plt.xlabel('Hitter Number')
    plt.ylabel('Percentage')
    plt.title('Record Ratios by Hitter Number')
    plt.xticks([num + bar_width for num in hitter_nums], hitter_nums)
    plt.legend()
    plt.tight_layout()

    # 이미지 파일로 그래프 저장
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 이미지를 base64로 인코딩하여 HTML에 삽입할 준비
    graphic3 = base64.b64encode(image_png).decode('utf-8')
    graphic3 = f'data:image/png;base64,{graphic3}'

    from django.db.models import Avg, F
    from django.db.models.functions import TruncDay
    import matplotlib.pyplot as plt
    from io import BytesIO
    import base64
       
    ctx = {
        'opponent_rec': opponent_rec,
        'pitching_data': pitching_data,
        'total_per': total_per,
        'graphic': graphic,
        'graphic2': graphic2,
        'graphic3': graphic3,
        'fast_ball_mean': fast_ball_mean,
        'breaking_mean': breaking_mean,
        'speed_off_mean': speed_off_mean,
        'left_pitch_list': left_pitch_list,
        'right_pitch_list': right_pitch_list,
        'L_lst': L_lst,
        'R_lst': R_lst,
        'ball_data': ball_data,
        'fast_S_total':fast_S_total,
        'fast_B_total':fast_B_total,
        'breaking_S_total':breaking_S_total,
        'breaking_B_total':breaking_B_total,
        'speedoff_S_total':speedoff_S_total,
        'speedoff_B_total':speedoff_B_total,
    }

    return render(request, 'player_info/gamedetail.html', ctx)


def delete_opponent(request,id,pk):
    pitching_data = PlayerInfo.objects.get(pk=pk)
    opponent_data = pitching_data.opponent_set.all()
    opponent_data_del = pitching_data.opponent_set.get(pk=id)
    now = timezone.now()
    
    ctx = {'pitching_data':pitching_data,'opponent_data':opponent_data,
           'now':now,'opponent_data_del':opponent_data_del}
    
    if request.method == 'POST':
        opponent_data_del.delete()
        return redirect(f'/info/detail/{pk}')
    
    else:
        return render(request,'player_info/delete_opponent.html',ctx)
    
    
    
