from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("Image_1.jpeg") as img:
        # Print image size and format
        print("Image size:", img.size)
        print("Image format:", img.format)
        
        # Rotate the image
        rotated_img = img.rotate(180)
        rotated_img=rotated_img.filter(ImageFilter.BLUR)
        rotated_img=rotated_img.filter(ImageFilter.FIND_EDGES)
        rotated_img.show()  # Display the rotated image
        # Save the rotated image
        #rotated_img.save("Rotated_Image.jpeg")

main()
