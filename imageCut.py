import cv2,os
from multiprocessing import Process,Pool


#img = cv2.imread(r"d:\Document\wenxian.png")
#print(img.shape)

foot_long=int(input('设置取样步长：'))                   # 获取输入的值并转换成int类型
range_of = int((640/foot_long)*(480/foot_long))
print(range_of)
print(640//foot_long)


def image_cut(path_of_img):                      # 对每张图片进行分割,相当于一个二维数组
    img = cv2.imread(path_of_img)
    number_m = 1                                 # 设置迭代开始的行数
    for i in range(480//foot_long):

        for j in range(640//foot_long):

            cropped = img[0 + 8*i:8 + 8*i, 0+8 * j:8 + 8 * j]
            cv2.imwrite(r'd:\Document\biwi\{number}.png'.format(number=number_m), cropped)
            number_m += 1

    print("Finish!")


def test(path_of_img):                           # 分步骤测试上面的函数
    img = cv2.imread(path_of_img)
    number_m = 0
    '''for i in range(range_of):
        if (1 + i) % (640 //foot_long) == 0 and i < 4799:
            #print("change")
            number_m = number_m + foot_long
            print(number_m)'''
        # cropped = img[(0+number_m):(8+number_m),0+8*i:20+8*i]
        # cv2.imwrite(r'd:\Document\biwi\{number}.png'.format(number=i), cropped)
    cropped = img[230:238,330:338]
    cv2.imwrite(r'd:\Document\osbasd.png',cropped)
    print("转换完成！")



if __name__ == '__main__':

    path_img = r'd:\BaiduNetdiskDownload\Biwi Kinect Head Pose Database\head_pose_masks\01\frame_00004_depth_mask.png'
    image_cut(path_img)
    # test(path_img)
'''
    print(os.getpid())   # 打印父进程ID
    poolpool = Pool(6)   # 设置进程池的大小为6，因为电脑CPU是6核12线程，所以会检测到12个核心
    for i in range(6):
        poolpool.apply_async(image_cut(),args=())
    print('等待所有子进程结束')
    poolpool.close()
    poolpool.join()
    print('任务结束')'''