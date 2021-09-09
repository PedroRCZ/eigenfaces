from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse, HttpResponseServerError
from django.views.decorators import gzip
import cv2
import time
import os

# Create your views here.

def index(request):
    return render(request, 'index.html') 


def get_video():
    return ""


def get_frame():


    dataPath = 'App/static/test' 
    imagePaths = os.listdir(dataPath)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()


    # Leyendo el modelo
    face_recognizer.read('App/static/modeloEigenFace.xml')

    camera =cv2.VideoCapture(0,cv2.CAP_DSHOW) 

    faceClassif = cv2.CascadeClassifier('App/static/haarcascade_frontalface_default.xml')

    while True:

        _, img = camera.read()
        if _ == False: break
        
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            cv2.putText(img,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
           
            
            # EigenFaces
            if result[1] < 5700:
                cv2.putText(img,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
                print("es: "+'{}'.format(imagePaths[result[0]]))
            else:
                cv2.putText(img,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)
        

       # cv2.imshow('img',img)
        k = cv2.waitKey(1)
        if k == 27:
            break   


       # _, img = camera.read()
        imgencode=cv2.imencode('.jpg',img)[1]
        stringData=imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
       
    camera.release()
    #cv2.destroyAllWindows()
    
    del(camera)
    



def indexscreen(request): 
    
    template = "stream_video.html"
    return render(request,template)
    

@gzip.gzip_page
def dynamic_stream(request,stream_path="video"):
    try :
        return StreamingHttpResponse(get_frame(),content_type="multipart/x-mixed-replace;boundary=frame")
    except :
        return "error"