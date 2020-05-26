from xdts_wechat_base import StyleTransformer, CVManager

if __name__ == '__main__':
    transformer = StyleTransformer(model=0)  # 创建一个转换器，用来对图片进行风格迁移
    manager = CVManager(transformer)  # 创建一个管理器，用来对进行一些基本操作
    while True:
        manager.read_camera()  # 读取摄像头图像
        frame = manager.get_image()  # 获得之前读取到的图像
        key = manager.render(1)  # 对图像进行处理并显示

        if key == ord('q'):
            break
        elif ord('0') <= key <= ord('9'):
            transformer.set_model(key - ord('0'))  # 切换模型
