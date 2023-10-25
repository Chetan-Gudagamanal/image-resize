# from PIL import Image
# import pathlib
# maxsize = (600, 480)
# for input_img_path in pathlib.Path("input").iterdir():
#     output_img_path = str(input_img_path).replace("input","output")
#     with Image.open(input_img_path) as im:
#         im.thumbnail(maxsize)
#         im.save(output_img_path, "JPEG", dpi=(300,300))
#         print(f"processing file {input_img_path} done...")

# from pathlib import Path
# p = Path('input_dir')
# output=[x for x in p.iterdir() ]
# print(output)

from PIL import Image
import pathlib
maxsize = (600, 480)
for input_img in pathlib.Path("input_dir").iterdir():
    output_img = str(input_img).replace("input_dir","output_dir")
    with Image.open(input_img) as img:
        img.thumbnail(maxsize)
        img.save(output_img, "JPEG")