import cv2

# Kamerayı başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare alınamadı. Çıkılıyor...")
        break

    # Çerçeveyi göster
    frame = cv2.flip(frame, 1)
    cv2.imshow("webcam", frame)


    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
