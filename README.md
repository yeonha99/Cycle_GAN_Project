# Cycle_GAN_Project
2021학년도 1학기 인하대학교 정보통신공학과 인공지능응용시스템과목 기말 설계 프로젝트입니다.<br><br>
Cycle_GAN을 이용한 사람얼굴<->애니얼굴 변환 모델 학습을 목표로 개발중입니다.
<br>
<br>

# 출력결과
![Imgur](https://i.imgur.com/Qy8aACr.png)

<br>
<br>

# 실행

~~~
!python3 '/content/pytorch-CycleGAN/train.py' \
   --mode 'train' \
   --batch_size 4 \
   --data_dir '/content/real2pocketmon' \
   --ckpt_dir '/content/drive/MyDrive/checkpoint' \
   --log_dir '/content/drive/MyDrive/log' \
    --result_dir '/content/drive/MyDrive/result'
~~~
