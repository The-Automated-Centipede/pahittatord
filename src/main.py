# -*- coding: utf-8 -*-
import PIL, random, tweepy
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def main():
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    randomly_generated_word = generate_random_word(random.randrange(4, 11))

    api.update_status(status="Dagens påhittade ord är %s." % randomly_generated_word)

    generate_image(randomly_generated_word, "images/profile_picture.jpg")
    api.update_profile_image("images/profile_picture.jpg")

def generate_random_word(length):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    word = ''

    for a in xrange(length):
        word += random.choice(consonants if a&1 else vowels)

    return word

def generate_image(msg, save_path):
    font_size = 1
    img_fraction = 0.50
    msg = msg.decode("utf8")

    font = ImageFont.truetype("fonts/OpenSans-Light.ttf", font_size)

    W, H = (400, 400)

    img = Image.new("RGBA", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    while font.getsize(msg)[0] < img_fraction * img.size[0]:
        font_size += 1
        font = ImageFont.truetype("fonts/OpenSans-Light.ttf", font_size)

    font_size -= 1
    font = ImageFont.truetype("fonts/OpenSans-Light.ttf", font_size)

    w, h = draw.textsize(msg, font)

    draw.text(((W - w) / 2, (H - h) / 2), msg, fill="black", font=font)
    draw = ImageDraw.Draw(img)

    img.save(save_path)

if __name__ == '__main__':
    main()