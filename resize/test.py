from PIL import Image
import torchvision.transforms as transforms

img=Image.open('C:/Users/JungYeonHee/Downloads/00006.jpg');
tf=transforms.ToTensor()
img_t=tf(img)
print(img)
print(img_t)
print(img_t.size())
print(type(img_t))
