from cv2 import cv2
import random

userInput = ""
letterList = ["a", "ka", "sa"]
letterAnswerList = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so"]
answerOptions = []
i = 0
while(i<10):
    # def showPicture:
    correctAnswer = ""
    showPic_prefix = letterList[random.randint(0,len(letterList)-1)] #sa  a
    showPic_suffix = random.randint(1,5) #3
    showPic = '{}-{}.png'.format(showPic_prefix,showPic_suffix)
    # print(showPic)
    # print(showPic_prefix)
    # print(letterList.index(showPic_prefix))
    correctAnswer = '{}'.format(letterAnswerList[((letterList.index(showPic_prefix))*5) + showPic_suffix - 1])
    # print(correctAnswer)
    answerOptions = random.sample(letterAnswerList, 3)
    answerOptions.append(correctAnswer)
    random.shuffle(answerOptions)
    # print(answerOptions)
    img = cv2.imread(showPic)
    # img = cv2.imread("Image 2.jpeg")
    # print(img)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # print("Choose one of following {} or press x to EXIT".format(answerOptions))
    print("Type answer or press x to EXIT")
    userInput = input()
    if(userInput == "x"):
        break
    elif(userInput == correctAnswer):
        print("Correct Answer")
    else:
        print("Wrong Answer")
    i = i+1