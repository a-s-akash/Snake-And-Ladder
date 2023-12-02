from PIL import Image, ImageDraw, ImageFont
def certi(nnm):
    input_image_path = 'certi.png'
    output_image_path = 'output.png'
    new_name = nnm
    image = Image.open(input_image_path)
    font = ImageFont.truetype("arial.ttf", 140)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textbbox((0, 0), new_name, font=font)[2:4]
    image_width, image_height = image.size
    x = (image_width - text_width) // 2
    y = 600
    text_color = '#c09539'
    draw.text((x, y), new_name, font=font, fill=text_color)
    image.save(output_image_path)