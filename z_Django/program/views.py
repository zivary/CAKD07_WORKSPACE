from django.shortcuts import render

# Create your views here.
def inputdata(request):
    return render(
        request,
        'program/program_inputdata.html'
    )

def result(request):
    a = request.GET['a']
    b = request.GET['b']
    lis=[]
    lis.append(a)
    lis.append(b)

    sum = 0
    for i in lis:
        sum += int(i)
    ans = sum

    return render(
        request,
        'program/program_result.html',
        {
            'a' : a,
            'b' : b,
            'ans' : ans,
            'lis' : lis,
            }
    )