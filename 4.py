import cv2

# Videoyu başlat
cap = cv2.VideoCapture("cicekler.mp4")
dosyaAdi="C:/video/1.mp4"
codec=cv2.VideoWriter_fourcc(*'mp4v')
framerate=30
resolution=(640,480)
output=cv2.VideoWriter(dosyaAdi,codec,framerate,resolution)
while True:
    ret, frame = cap.read()
    if ret==0:
        break
    # Çerçeveyi göster
    frame = cv2.flip(frame, 1)
    output.write(frame)
    cv2.imshow("webcam", frame)


    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Kaynakları serbest bırak
output.release()
cap.release()
cv2.destroyAllWindows()
