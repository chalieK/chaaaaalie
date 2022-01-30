# 이중 for 문 탈출 버그


balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("balls :", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons :", weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print("공과 무기가 충돌")
            break
    else:
        continue # if의 조건과 비슷함 / 아래 for문 내에 값이 없으면 위 for문 으로 돌아감
    print("바깥 for문 break")
    break

# 3이 똑같은 val 이라 break 되어 ball_val[3]이 출력이 안되어야함. 그러나 됨.
# break가 아래 for 문만 탈출되어 4번째 값이 출력되는 버그

    # for 바깥조건: 
    #     바깥동작
    #     for 안쪽 조건:
    #         안쪽 동작
    #         if 충돌하면:
    #             break
    #     else:
    #         continue
    #     break