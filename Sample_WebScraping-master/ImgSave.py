import requests

# paste url from ImgGrab program
image_link = requests.get("https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg")
# print(image_link.content)

f = open('Endgame_poster.jpg', 'wb')
f.write(image_link.content)
f.close()
