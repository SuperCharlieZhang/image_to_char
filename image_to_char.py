from tkinter import *
import tkinter.filedialog
from PIL import Image

codeChar='''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,"^'.'''
count=len(codeChar)
def transform1(image_file):
    image_file=image_file.convert("L")#将图片转换为黑白图片，参数L设置黑白
    code=''
    for h in range(0,image_file.size[1]): #size[1]表示img的高像素值，size[0]表示img宽像素值
        for w in range(0,image_file.size[0]):
            gray = image_file.getpixel((w,h))#返回位于w，h位置的像素
            code=code+codeChar[int(((count-1)*gray)/256)]#建立字符集和灰度之间的映射
        code=code+'\r\n'#在行末加入换行符
    return code
def openImg():
    open_name = tkinter.filedialog.askopenfilename()
    fp = open(open_name, 'rb')
    image_file = Image.open(fp)
    width, height = image_file.size
    ratio = width / height#计算长宽比例，新高度为120
    new_width = int(120 * ratio * 2)
    image_file = image_file.resize((new_width, 120))
    lb.config(text="请保存为txt文件")
    save_name = tkinter.filedialog.asksaveasfilename()
    tmp = open(save_name, 'w')
    tmp.write(transform1(image_file))
    tmp.close()
    lb.config(text="完成")
root=Tk()
root.title('图片转换成字符图')
root.minsize(300,75)
lb=Label(root,text='请选择图片文件')
lb.pack()
btn=Button(root,text="选择图片文件",command=openImg)
btn.pack()
root.mainloop()

