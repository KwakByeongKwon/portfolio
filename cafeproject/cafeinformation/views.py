from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import CsvFile,SeoulCafeList
from .forms import FileSelectForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'cafeinformation/index.html')


class FileList(generic.ListView):
    model = CsvFile
    template_name='cafeinformation/list.html'


def detail(request):
    form = FileSelectForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        selected_file_id = form.cleaned_data['file']
        detail_data = CsvFile.objects.get(id=selected_file_id)   
        
        if len(detail_data.file_name) == 15:
            detail_data_name = detail_data.file_name[9:11]
        elif len(detail_data.file_name) == 16:
            detail_data_name = detail_data.file_name[9:12]
        elif len(detail_data.file_name) == 17:
            detail_data_name = detail_data.file_name[9:13]

        return render(request, 'cafeinformation/detail_download.html', {'detail_data': detail_data,'detail_data_name':detail_data_name})
    
    return render(request, 'cafeinformation/detail.html', {'form': form})

def seoul(request):
    seoul_data = CsvFile.objects.get(id=15)
    return render(request,'cafeinformation/seoul.html',{'seoul_data':seoul_data})

def preview(request,id):
    detail_data = CsvFile.objects.get(id=id)
    detail_data_name = detail_data.file_name
    if id == 1:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='강남구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
            
        print(preview_menu)
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data,'preview_menu':preview_menu})
    elif id == 2:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='강동구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 3:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='강북구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 4:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='강서구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 5:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='관악구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 6:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='광진구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 7:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='구로구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 8:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='금천구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 9:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='노원구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 10:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='도봉구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 11:
        detail_data_name = detail_data_name[9:13]
        previews = SeoulCafeList.objects.filter(gu='동대문구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 12:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='동작구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 13:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='마포구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 14:
        detail_data_name = detail_data_name[9:13]
        previews = SeoulCafeList.objects.filter(gu='서대문구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 16:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='서초구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 17:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='성동구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 18:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='성북구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 19:
        detail_data_name = detail_data_name[9:13]
        previews = SeoulCafeList.objects.filter(gu='송파구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 20:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='양천구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 21:
        detail_data_name = detail_data_name[9:13]
        previews = SeoulCafeList.objects.filter(gu='영등포')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 22:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='용산구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 23:
        detail_data_name = detail_data_name[9:13]
        previews = SeoulCafeList.objects.filter(gu='은평구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 24:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='종로구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 25:
        detail_data_name = detail_data_name[9:11]
        previews = SeoulCafeList.objects.filter(gu='중구 ')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 26:
        detail_data_name = detail_data_name[9:12]
        previews = SeoulCafeList.objects.filter(gu='중랑구')
        preview_menu = [preview.cafe_menu.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]

        # previews의 각 객체의 cafe_menu 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_menu):
            preview.cafe_menu = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        
        preview_review_top3 = [preview.review_top3.replace('[','').replace(']','').replace('\'','').replace(',',' / ') for preview in previews]
        # previews의 각 객체의 review_top3 필드를 가공된 값으로 변경
        for preview, formatted_menu in zip(previews, preview_review_top3):
            preview.review_top3 = formatted_menu

        # 변경된 값을 저장
        for preview in previews:
            preview.save()
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
    elif id == 15:
        detail_data_name = '서울전체데이터'
        previews = SeoulCafeList.objects.all()[0::300]
        return render(request,'cafeinformation/preview.html',{'previews':previews,'detail_data_name':detail_data_name,'detail_data':detail_data})
        