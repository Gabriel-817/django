from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

cursor = connection.cursor()

# Create your views here.
@csrf_exempt
def join(request):
    if request.method == 'GET':
        return render(request, 'vesCindy/join.html')

    elif request.method =='POST':
        id = request.POST['id']
        na = request.POST['name']
        ag = request.POST['age']
        pw = request.POST['pw']

        ar = [id, na, ag, pw]
        print(ar)

        sql = """
            INSERT INTO vesCindy(ID, NAME, AGE, PW, JOINDATE)
            VALUES (%s, %s, %s, %s, SYSDATE)
            """
        cursor.execute(sql, ar)

        return redirect('/vesCindy/index')

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'vesCindy/login.html')
    if request.method == 'POST':
        ar = [request.POST['id'], request.POST['pw']]
        sql = """
            SELECT ID, NAME
            FROM vesCindy
            WHERE ID=%s AND PW=%s
        """

        cursor.execute(sql, ar)
        data = cursor.fetchone()
        print(type(data))

        if data:
            request.session['userid'] = data[0]
            request.session['username'] = data[1]
            return redirect('/vesCindy/index')

        return redirect('/vesCindy/index')

@csrf_exempt
def vescindy(request):
    if request.method=="GET":
        return render(request, "vesCindy/vescindy.html")
