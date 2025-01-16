import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from random import random as rd 

def lucky_draw_upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('file') 

        if not uploaded_file:
            return render(request, 'lucky_draw.html', {'error': 'No file uploaded!'})
        try:
            data = pd.read_excel(uploaded_file)
            # print(data)
            if "Name" not in data.columns or "Department" not in data.columns:
                return render(request, 'lucky_draw.html', {'error': 'Invalid file format. Columns "Name" and "Department" are required!'})
            records = data.to_dict(orient='records')
            return render(request, 'lucky_draw.html', {'records': records})
        except Exception as e:
            return render(request, 'lucky_draw.html', {'error': f"Error processing file: {str(e)}"})
    return render(request, 'lucky_draw.html')


    
    
    
    
    # function startDraw() {
    #         let interval = setInterval(() => {
    #             let randomIndex = Math.floor(Math.random() * records.length);
    #             let record = records[randomIndex];
    #             display.textContent = `${record.Name} - ${record.Department}`;
    #         }, 50);

    #         setInterval(() =>{
    #             clearInterval(interval);

    #         }, 1000 )