# 변수 선언
frame = 1
score = [[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "," "]]
total = [" "," "," "," "," "," "," "," "," "," "]
validData = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
terminate = False

# 1~9 프레임 처리
def normalFrame(frame):
      print("{:^72}".format(str("Frame " + str(frame))))
      while score[frame - 1][0] not in validData:
            score[frame - 1][0] = input("Roll 1: ")
            if score[frame - 1][0] not in validData: 
                  print("잘못된 출력입니다.")
      score[frame - 1][0] = int(score[frame - 1][0])
      if score[frame - 1][0] == 10:
            score[frame - 1][0] = "X"
      scoreCheck(frame)
      printScore(0)
      if score[frame - 1][0] != "X":
            while (score [frame - 1][1] not in validData) or ((score[frame - 1][0] + int(score[frame - 1][1]) > 10)): # 값이 유효하지 않다
                  score[frame - 1][1] = input("Roll 2: ")
                  if score[frame - 1][1] not in validData:
                        print("잘못된 출력입니다.") 
                  elif score[frame - 1][0] + int(score[frame - 1][1]) > 10:
                        print("최대 핀의 개수를 초과하였습니다.")
            score[frame - 1][1] = int(score[frame - 1][1])
            if score[frame - 1][0] + score[frame - 1][1] == 10:
                  score[frame - 1][1] = "/"
            scoreCheck(frame)
            printScore(1)
      frame = frame + 1
      return frame
                        
# 10 프레임 처리
def finalFrame(frame):
      # 제 1구
      print("{:^72}".format("FRAME 10"))
      while score[frame-1][0] not in validData:
            score[frame-1][0] = input("Roll 1: ")
            if score[frame-1][0] not in validData:
                  print("잘못된 출력입니다.")
      score[frame - 1][0] = int(score[frame - 1][0])
      
      if total[7] == " ": # 8프레임에서 스트라이크
            total[7] = total[6] + 10 + 10 + score[frame-1][0]
      if total[8] == " ": # 9프레임 스페어 or 스트라이크
            if score[8][1] == "/":
                  total[8] = total[7] + 10 + score[frame-1][0]
      if score[frame-1][0] == 10:
            score[frame - 1][0] = "X"
      printScore(0)

      # 제 2구
      while (score[frame-1][1] not in validData) or (score[frame-1][0] != "X" and int(score[frame-1][1]) + score[frame-1][0] >10):
            score[frame-1][1] = input("Roll 2: ")
            if score[frame-1][1] not in validData:
                  print("잘못된 출력입니다.")
            elif score[frame-1][0] != "X" and int(score[frame-1][1]) + int(score[frame-1][0]) >10:
                  print("최대 핀의 개수를 초과하였습니다.")
      score[frame - 1][1] = int(score[frame - 1][1])
      if total[8] == " ": #스트라이크
            if score[9][0] == "X":
                  total[8] = total[7] + 10 + 10 + score[9][1]
            else:
                  total[8] = total[7] + score[9][0] + score[9][1]
      if score[9][1] == 10:
            score[9][1] = "X"
            print("{:^72}".format("STRIKE"))
            print("-" * 72)
            print("|{0:^7}|{1:^5}|{2:^5}|{3:^5}|{4:^5}|{5:^5}|{6:^5}|{7:^5}|{8:^5}|{9:^5}|{10:^8}|"
                  .format("Frame", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
            print("-" * 72)
            print("|{:^7}|".format("Pin"), end="")
            for f in range(0, len(score)):
                  for i in range(0, len(score[f])):
                        print("{:<2}".format(score[f][i]), end = "|")
            print("")
            print("-" * 72)
            print("|{:^7}".format("Score"), end="|")
            for s in range(0, len(total)-1):
                  print("{:^5}".format(total[s]), end="|")
            print("{:^8}".format(total[len(total)-1]), end="|")
            print("")
            print("-" * 72)
      if score[9][0] != "X" and score[9][0] + score[9][1] == 10:
            score[9][1] = "/"
            print("{:^72}".format("SPARE"))
            print("-" * 72)
            print("|{0:^7}|{1:^5}|{2:^5}|{3:^5}|{4:^5}|{5:^5}|{6:^5}|{7:^5}|{8:^5}|{9:^5}|{10:^8}|"
                  .format("Frame", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
            print("-" * 72)
            print("|{:^7}|".format("Pin"), end="")
            for f in range(0, len(score)):
                  for i in range(0, len(score[f])):
                        print("{:<2}".format(score[f][i]), end = "|")
            print("")
            print("-" * 72)
            print("|{:^7}".format("Score"), end="|")
            for s in range(0, len(total)-1):
                  print("{:^5}".format(total[s]), end="|")
            print("{:^8}".format(total[len(total)-1]), end="|")
            print("")
            print("-" * 72)
      elif score[9][0] == "X" or score[9][1] == "/":
            print("-" * 72)
            print("|{0:^7}|{1:^5}|{2:^5}|{3:^5}|{4:^5}|{5:^5}|{6:^5}|{7:^5}|{8:^5}|{9:^5}|{10:^8}|"
                  .format("Frame", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
            print("-" * 72)
            print("|{:^7}|".format("Pin"), end="")
            for f in range(0, len(score)):
                  for i in range(0, len(score[f])):
                        print("{:<2}".format(score[f][i]), end = "|")
            print("")
            print("-" * 72)
            print("|{:^7}".format("Score"), end="|")
            for s in range(0, len(total)-1):
                  print("{:^5}".format(total[s]), end="|")
            print("{:^8}".format(total[len(total)-1]), end="|")
            print("")
            print("-" * 72)
      if score[9][0] == "X" or score[9][1] == "/":
            while (score[frame-1][2] not in validData) or (score[frame-1][1] not in ["/", "X"] and int(score[frame-1][2]) + score[frame-1][1] >10):
                  score[frame-1][2] = input("Roll 3: ")
                  if score[frame-1][2] not in validData:
                        print("잘못된 출력입니다.")
                  elif score[frame-1][1] not in ["/", "X"] and int(score[frame-1][2]) + int(score[frame-1][1]) >10:
                        print("최대 핀의 개수를 초과하였습니다.")
            score[frame - 1][2] = int(score[frame - 1][2])
            if score[9][0] == "X":
                  if score[9][1] == "X":
                        total[9] = total[8] + 20 + score[9][2]
                        if score[9][2] == 10:
                              score[9][2] = "X"
                              print("{:^72}".format("STRIKE"))
                  else:
                        total[9] = total[8] + 10 + score[9][1] + score[9][2]
                        if score[9][2] + score[9][1] == 10:
                              score[9][2] = "/"
                              print("{:^72}".format("SPARE"))
                        else:
                              print("{:^72}".format("OPEN"))
            elif score[9][1] == "/":
                  total[9] = total[8] + 10 + score[9][2]
                  if score[9][2] == 10:
                        print("{:^72}".format("STRIKE"))
            print("-" * 72)
            print("|{0:^7}|{1:^5}|{2:^5}|{3:^5}|{4:^5}|{5:^5}|{6:^5}|{7:^5}|{8:^5}|{9:^5}|{10:^8}|"
                  .format("Frame", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
            print("-" * 72)
            print("|{:^7}|".format("Pin"), end="")
            for f in range(0, len(score)):
                  for i in range(0, len(score[f])):
                        print("{:<2}".format(score[f][i]), end = "|")
            print("")
            print("-" * 72)
            print("|{:^7}".format("Score"), end="|")
            for s in range(0, len(total)-1):
                  print("{:^5}".format(total[s]), end="|")
            print("{:^8}".format(total[len(total)-1]), end="|")
            print("")
            
      else: # 세번째 투구 던지지 않고 끝
            total[9] = total[8] + score[9][0] + score[9][1]
            print("{:^72}".format("OPEN"))
            print("-" * 72)
            print("|{0:^7}|{1:^5}|{2:^5}|{3:^5}|{4:^5}|{5:^5}|{6:^5}|{7:^5}|{8:^5}|{9:^5}|{10:^8}|"
                  .format("Frame", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
            print("-" * 72)
            print("|{:^7}|".format("Pin"), end="")
            for f in range(0, len(score)):
                  for i in range(0, len(score[f])):
                        print("{:<2}".format(score[f][i]), end = "|")
            print("")
            print("-" * 72)
            print("|{:^7}".format("Score"), end="|")
            for s in range(0, len(total)-1):
                  print("{:^5}".format(total[s]), end="|")
            print("{:^8}".format(total[len(total)-1]), end="|")
            print("")
      frame = frame +1
      return frame
            

# 점수 처리
def scoreCheck(frame):
      for i in range (0, frame):
            if total[i] == " ":
                  if i == 0:
                        if score[i][0] == "X":
                              if score[i+1][0] == "X":
                                    if score[i+2][0] == "X":
                                          total[i] = 30
                                    elif score[i+2][0] != " ":
                                          total[i] = 10 + 10 + score[i+2][0]
                                    else:
                                          total[i] = " "
                                          break
                              elif score[i+1][0] != " ":
                                    if score[i+1][1] == "/":
                                          total[i] = 10 + 10
                                    elif score[i+1][1] != " ":
                                          total[i] = 10 + score[i+1][1] + score[i+1][0]
                                    else:
                                          total[i] = " "
                                          break
                              else:
                                    total[i] = " "
                                    break
                        elif score[i][1] != " ":
                              if score[i][1] == "/":
                                    if score[i+1][0] != " ":
                                          if score[i+1][0] == "X":
                                                total[i] = 10 + 10
                                          else:
                                                total[i] = 10 + score[i+1][0]
                                    else:
                                          total[i] = " "
                                          break
                              else:
                                    total[i] = score[i][0] + score[i][1]
                        else:
                              total[i] = " "
                              break
                  elif i == frame - 1:
                        if score[i][0] == "X":
                              total[i] = " "
                              break
                        elif score[i][1] == "/":
                              total[i] = " "
                              break
                        else:
                              if score[i][1] == " ":
                                    break
                              else:
                                    total[i] = total[i-1] + score[i][0] + score[i][1]
                  else: #프레임 값이 가운데 일때
                        if score[i][0] == "X":
                              if score[i+1][0] == "X":
                                    if score[i+2][0] == "X":
                                          total[i] = total[i-1] + 30
                                    elif score[i+2][0] != " ":
                                          total[i] = total[i-1] + 10 + 10 + score[i+2][0]
                                    else:
                                          total[i] = " "
                                          break
                              elif score[i+1][0] != " ":
                                    if score[i+1][1] == "/":
                                          total[i] = total[i-1] + 10 + 10
                                    elif score[i+1][1] != " ":
                                          total[i] = total[i-1] + 10 + score[i+1][1] + score[i+1][0]
                                    else:
                                          total[i] = " "
                                          break
                              else:
                                    total[i] = " "
                                    break
                        elif score[i][1] != " ":
                              if score[i][1] == "/":
                                    if score[i+1][0] != " ":
                                          if score[i+1][0] == "X":
                                                total[i] = total[i-1] + 10 + 10
                                          else:
                                                total[i] = total[i-1] + 10 + score[i+1][0]
                                    else:
                                          total[i] = " "
                                          break
                              else:
                                    total[i] = total[i-1] + score[i][0] + score[i][1]
                        else:
                              total[i] = " "
                              break

# 표시 처리
def printScore(attempt):
      if (score[frame-1][attempt] == "X"):
            print("{:^72}".format("STRIKE"))
      elif (attempt == 1) and (score[frame-1][attempt] == "/"):
            print("{:^72}".format("SPARE"))
      elif (attempt == 1):
            print("{:^72}".format("OPEN"))
      print("-" * 72)
      print("|{0:^7}|{1:^5}|{2:^5}|{3:^5}|{4:^5}|{5:^5}|{6:^5}|{7:^5}|{8:^5}|{9:^5}|{10:^8}|"
            .format("Frame", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
      print("-" * 72)
      print("|{:^7}|".format("Pin"), end="")
      for f in range(0, len(score)):
            for i in range(0, len(score[f])):
                  print("{:<2}".format(score[f][i]), end = "|")
      print("")
      print("-" * 72)
      print("|{:^7}".format("Score"), end="|")
      for s in range(0, len(total)-1):
            print("{:^5}".format(total[s]), end="|")
      print("{:^8}".format(total[len(total)-1]), end="|")
      print("")
      print("-" * 72)

# 실제 실행
while not terminate:
      print("-" * 72)
      while frame <= 10:
            if frame < 10:
                  frame = normalFrame(frame)
            elif frame == 10:
                  frame = finalFrame(frame)
      print("-" * 72)
      terminate = input("Quit?(Q/N): ")
      if terminate == "Q":
            terminate == True
      else:
            terminate = False
            frame = 1
            score = [[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "],[" "," "," "]]
            total = [" "," "," "," "," "," "," "," "," "," "]
            validData = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
