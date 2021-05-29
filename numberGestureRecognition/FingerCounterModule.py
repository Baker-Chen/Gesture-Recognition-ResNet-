import cv2
import time
import os
import HandTrackingModule as htm


startTime = time.time()
cnt = [0,0,0,0,0,0,0,0,0,0,0,0]
global batch_cnt
global flag
batch_cnt = 0
flag = True




def handrecongnition(fingerlist,cnt):
    global batch_cnt
    global flag
    batchsize = 500

    if(batch_cnt >= batchsize):
        print("collect stop!")
        flag = False
        

    else:
        batch_cnt += 1
        print("batch_cnt = ")
        print(batch_cnt)
        if(fingerlist == [0,1,0,0,0]):
            #print("1!")
            subfolder = "1"
            cnt[1] += 1
            imagName = "one_" + str(cnt[1])
            print(imagName)
            
        elif(fingerlist == [0,1,1,0,0]):
            #print("2!")
            subfolder = "2"
            cnt[2] += 1            
            imagName = "two_" + str(cnt[2])
            print(imagName)
            
        elif(fingerlist == [0,1,1,1,0]):
            #print("3!")
            subfolder = "3"
            cnt[3] += 1
            imagName = "three_" + str(cnt[3])
            print(imagName)
            
        elif(fingerlist == [0,1,1,1,1]):
            #print("4!")
            subfolder = "4"
            cnt[4] += 1
            imagName = "four_" + str(cnt[4])
            print(imagName)
            
        elif(fingerlist == [1,1,1,1,1]):
            #print("5!")
            subfolder = "5"
            cnt[5] += 1
            imagName = "five_" + str(cnt[5])
            print(imagName)
            
        elif(fingerlist == [1,0,0,0,1]):
            #print("6!")
            subfolder = "6"
            cnt[6] += 1
            imagName = "six_" + str(cnt[6])
            print(imagName)
            
        elif(fingerlist == [1,1,0,0,0]):
            #print("7!")
            subfolder = "7"
            cnt[7] += 1
            imagName = "seven_" + str(cnt[7])
            print(imagName)
            
        elif(fingerlist == [1,1,1,0,0]):
            #print("8!")
            subfolder = "8"
            cnt[8] += 1
            imagName = "eight_" + str(cnt[8])
            print(imagName)
            
        elif(fingerlist == [1,1,1,1,0]):
            #print("9!")
            subfolder = "9"
            cnt[9] += 1
            imagName = "nine_" + str(cnt[9])
            print(imagName)
            
        elif(fingerlist == [0,0,0,0,0]):
            #print("0!")
            subfolder = "0"
            cnt[0] += 1
            imagName = "zero_" + str(cnt[0])
            print(imagName)
            
        elif(fingerlist == [0,0,1,1,1]):
            #print("ok!")
            subfolder = "11"
            cnt[10] += 1
            imagName = "ok_" + str(cnt[10])
            print(imagName)
            
        else:
            #print("x")
            subfolder = "unknow"
            cnt[11] += 1
            imagName = "unknow_" + str(cnt[11])
            print(imagName)

        selectfolder(cnt, subfolder, imagName)
        return imagName
        
        
    


def selectfolder(cnt, subfolder, imagName):
    filePath = "E:\\School\\2021_Synopsys_ARC_AIoT\\ARC_project\\handTraining3\\" + subfolder + "\\" +  imagName + ".jpg"
    with open(filePath, 'w') as f:
        cv2.imwrite(filePath, gray)
    # data = str(f.read())
    # #print('data',data)
    # data_list = data.split(",")
    # #print(data_list)
    # for i in range(0,len(data_list),2):
    #     j = i + 1
    #     data_dict[data_list[i]] = int(data_list[j])
    # print(data_dict)
    # op = Operation(data_dict)

wCam, hCam = 640, 480
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
 
# folderPath = "FingerImages"
# myList = os.listdir(folderPath)
# print(myList)
'''
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)
 
print(len(overlayList))
'''
pTime = 0
 
detector = htm.handDetector(detectionCon=0.75)
 
tipIds = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
 
    if len(lmList) != 0:
        fingers = []
 
        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
 
        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
 
        #print(fingers)
        handrecongnition(fingers, cnt)


        totalFingers = fingers.count(1)
        #print(totalFingers)

        #h, w, c = overlayList[totalFingers - 1].shape
        #img[0:h, 0:w] = overlayList[totalFingers - 1]

        #cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        #cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
        #            10, (255, 0, 0), 25)
        cv2.putText(img, str(handrecongnition(fingers, cnt)), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)
 
    #cTime = time.time()
    #fps = 1 / (cTime - pTime)
    #pTime = cTime
 
    #cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
    #            3, (255, 0, 0), 3)
 
    #cv2.imshow("Image", img)
    
    cv2.imshow("Gray", gray)
    cv2.waitKey(1)
    
    if flag == False:
        endTime = time.time()
        totalTime = endTime - startTime
        print(totalTime)
        break

