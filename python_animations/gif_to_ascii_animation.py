from PIL import Image, ImageSequence
import os, time

def gif_to_ascii(gif_path):
    img = Image.open(gif_path)

    for frame in ImageSequence.Iterator(img):
        os.system('cls')
        frame = frame.convert("L").resize((60, 30))  # grayscale & size
        ascii_frame = ""

        for y in range(frame.size[1]):
            for x in range(frame.size[0]):
                brightness = frame.getpixel((x, y))
                ascii_char = "@#*+=-:. "[brightness // 32]  # 8 levels
                ascii_frame += ascii_char
            ascii_frame += "\n"

        print(ascii_frame)
        time.sleep(0.1)

gif_to_ascii("E:\projects system\CMD_ASCII_Animations\python_animations\gif.gif")
